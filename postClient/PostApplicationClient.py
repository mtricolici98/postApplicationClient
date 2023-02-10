import json
import sys

import requests

from constants.api_constants import API_URL
from postClient.model.Comment import Comment
from postClient.model.Post import Post
from utils.response_utils import validate_response


class PostApplicationClient:

    def __init__(self, username, password):
        self.token = self.login(username, password)

    @staticmethod
    def login(username, password):
        login_response = requests.post(
            f'{API_URL}/user/login',
            data=json.dumps(dict(
                login=username,
                password=password
            ))
        )
        if login_response.status_code == 200:
            login_data = login_response.json()
            return login_data.get('token')
        else:
            print('Could not authenitcate')
            sys.exit()

    @validate_response
    def _do_post_request(self, url, data, params=None):
        return requests.post(
            f'{API_URL}{url}',
            headers={
                'Auth-Token': self.token
            },
            data=json.dumps(data) if not type(data) == str else data,
            params=params
        )

    @validate_response
    def _do_get_request(self, url, params=None):
        return requests.get(
            f'{API_URL}{url}',
            headers={
                'Auth-Token': self.token
            },
            params=params
        )

    def get_my_posts(self):
        data = self._do_get_request('/posts/list/my')
        converted_data = [Post(**info) for info in data]
        return converted_data

    def get_post_comments(self, post_id):
        data = self._do_get_request(f'/posts/comments/{post_id}/')
        converted_data = [Comment(**info) for info in data]
        return converted_data

    def make_new_post(self, title, message):
        return self._do_post_request('/posts/add', data={
            'title': title,
            'message': message,
        })
