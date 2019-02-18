from .context import Context
from .errors import *

__all__ = ['Mediator']


class Mediator ():
    contexts = {}

    @staticmethod
    def get_context(namespace='default'):
        if type(namespace) != str:
            raise InvalidNamespaceError()

        if (Mediator.contexts.get(namespace)):
            return Mediator.contexts[namespace]
        else:
            Mediator.contexts[namespace] = Context(namespace)
            return Mediator.contexts[namespace]

    @staticmethod
    def get_context_list():
        return list(Mediator.contexts.keys())

    @staticmethod
    def destroy_context(namespace='default'):
        if type(namespace) != str:
            raise InvalidNamespaceError()

        Mediator.contexts.get(namespace).remove_all()
        Mediator.contexts.__delitem__(namespace)

    @staticmethod
    def destroy_all_contexts():
        [
            Mediator.destroy_context(namespace)
            for namespace in Mediator.get_context_list()
        ]

    @staticmethod
    def on_context_event(event_name: str, namespace: str = 'default'):
        if type(event_name) != str:
            raise InvalidEventNameError()
        if type(namespace) != str:
            raise InvalidNamespaceError()

        def decorator(n):
            context = Mediator.get_context(namespace)
            context.on(event_name, n)
        return decorator

    @staticmethod
    async def emit_context_event(event_name, data, namespace: str = 'default'):
        if type(event_name) != str:
            raise InvalidEventNameError()
        if type(namespace) != str:
            raise InvalidNamespaceError()

        context = Mediator.get_context(namespace)
        await context.emit(event_name, data)
