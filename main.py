from postClient.PostApplicationClient import PostApplicationClient
from views.login_view_gui import show_login_screen
from views.main_screen import show_main_screen


def func(username, password):
    client = PostApplicationClient(username.get(), password.get())
    show_main_screen(client)


show_login_screen(func)
