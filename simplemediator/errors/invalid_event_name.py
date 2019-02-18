__all__ = ['InvalidEventNameError']


class InvalidEventNameError(Exception):
    def __init__(self, message=None):
        if (message is None):
            message = 'Invalid Event Name: Event Name MUST BE an string'
        super(InvalidEventNameError, self).__init__(message)
