from functools import wraps


def validate_response(func):
    """
    Decorates functions that return a response
    and returns the JSON data if the response is valid
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code == 200:
            return response.json()
        is_json = response.headers.get('Content-Type') == 'application/json'
        response_info = response.json() if is_json else response.text
        raise Exception(
            f'Request failed with code {response.status_code},'
            f' data: {response_info}'
        )

    return wrapper
