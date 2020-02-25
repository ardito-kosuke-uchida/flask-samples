import functools
from flask import request


def auth_impl(api, func, *args, **kwargs):
    if request.headers.get('x-company-id') is None:
        api.abort(400, 'X-Company-ID が未指定')
    else:
        return func(*args, **kwargs)

def auth(api):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return auth_impl(api, func, *args, **kwargs)

        return wrapper

    return decorator
