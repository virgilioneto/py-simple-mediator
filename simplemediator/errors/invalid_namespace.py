__all__ = ['InvalidNamespaceError']

class InvalidNamespaceError(Exception):
    def __init__(self, message=None):
        if (message == None):
            message = 'Invalid Namespace: Namespace MUST BE an string'
        super(InvalidNamespaceError, self).__init__(message)