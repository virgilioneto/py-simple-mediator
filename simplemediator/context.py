import asyncio

__all__ = ['Context']


class Context ():
    def __init__(self, namespace):
        self.namespace = namespace
        self.event_handlers = {}
        self.enabled = True

    def is_enabled(self):
        return self.enabled

    def get_namespace(self):
        return self.namespace

    def on(self, event_name, fn):
        if (self.event_handlers.get(event_name) is None):
            self.event_handlers[event_name] = {
                'listeners': [],
                'once': False
            }
        self.event_handlers[event_name]['listeners'].append(fn)

    def once(self, event_name, fn):
        if (self.event_handlers.get(event_name) is None):
            self.event_handlers[event_name] = {
                'listeners': [],
                'once': True
            }
        self.event_handlers[event_name]['listeners'].append(fn)

    def off(self, event_name, fn):
        event = self.event_handlers.get(event_name)
        if (event is not None):
            event['listeners'].remove(fn)

    def remove_all_listeners(self, event_name):
        self.event_handlers.__delitem__(event_name)

    def remove_all(self):
        pass

    async def emit(self, event_name, data):
        event = self.event_handlers.get(event_name)
        if (event and type(event['listeners']) == list):
            if (event['once'] is True):
                self.remove_all_listeners(event_name)
            await asyncio.wait([next(data) for next in event['listeners']])

    def get_event_list(self):
        return list(self.event_handlers.keys())

    def get_listeners(self, event_name):
        event = self.event_handlers.get(event_name, {'listeners': []})
        return event['listeners']

    def get_listeners_count(self, event_name):
        return len(self.get_listeners(event_name))

    def enable(self):
        self.event_handlers['enabled'] = True

    def disable(self):
        self.event_handlers['enabled'] = False
