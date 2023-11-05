from functools import wraps

# Decorator definition
def logged_in(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.bearer_token:
            raise ValueError("Client must be logged in to perform this action.")
        return method(self, *args, **kwargs)
    return wrapper
