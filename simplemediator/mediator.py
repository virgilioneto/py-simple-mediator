from .context import Context
from .errors import *

__all__ = ['Mediator']

class Mediator ():
    contexts = {}
    @staticmethod
    def getContext(namespace='default'):
        if type(namespace) != str:
            raise InvalidNamespaceError()
            
        if (Mediator.contexts.get(namespace)):
            return Mediator.contexts[namespace]
        else:
            Mediator.contexts[namespace] = Context(namespace)
            return Mediator.contexts[namespace]

    @staticmethod
    def getContextList():
        return list(Mediator.contexts.keys())

    @staticmethod
    def destroyContext(namespace='default'):
        if type(namespace) != str:
            raise InvalidNamespaceError()

        Mediator.contexts.get(namespace).removeAll()
        Mediator.contexts.__delitem__(namespace)
    
    @staticmethod
    def destroyAllContexts():
        [Mediator.destroyContext(namespace) for namespace in Mediator.getContextList()]
    
    @staticmethod
    def onContextEvent(event_name:str, namespace:str='default'):
        if type(event_name) != str:
            raise InvalidEventNameError()
        if type(namespace) != str:
            raise InvalidNamespaceError()

        def decorator(n):
            context = Mediator.getContext(namespace)
            context.on(event_name, n)
        return decorator

    @staticmethod
    async def emitContextEvent(event_name, data, namespace='default'):
        if type(event_name) != str:
            raise InvalidEventNameError()
        if type(namespace) != str:
            raise InvalidNamespaceError()

        context = Mediator.getContext(namespace)
        await context.emit(event_name, data)