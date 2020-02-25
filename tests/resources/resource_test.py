import unittest
from unittest import mock
from app.app import create_app
import functools

def dummy_auth_impl(api, func, *args, **kwargs):
    return func(*args, **kwargs)

def skip_auth(func):
    @functools.wraps(func)
    def test_wrapper(*args, **kwargs):
        with mock.patch('app.utils.auth.auth_impl', dummy_auth_impl):
            return func(*args, **kwargs)

    return test_wrapper

class ResourceTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        app = create_app()
        app.testing = True
        self.client = app.test_client()
