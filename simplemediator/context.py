import asyncio

__all__ = ['Context']


class Context ():
    def __init__(self, namespace):
        self.namespace = namespace
        self.eventHandlers = {}
        self.enabled = True

    def isEnabled(self):
        return self.enabled

    def getNamespace(self):
        return self.namespace

    def on(self, event_name, fn):
        if (self.eventHandlers.get(event_name) is None):
            self.eventHandlers[event_name] = {
                'listeners': [],
                'once': False
            }
        self.eventHandlers[event_name]['listeners'].append(fn)

    def once(self, event_name, fn):
        if (self.eventHandlers.get(event_name) is None):
            self.eventHandlers[event_name] = {
                'listeners': [],
                'once': True
            }
        self.eventHandlers[event_name]['listeners'].append(fn)

    def off(self, event_name, fn):
        event = self.eventHandlers.get(event_name)
        if (event is not None):
            event['listeners'].remove(fn)

    def removeAllListeners(self, event_name):
        self.eventHandlers.__delitem__(event_name)

    def removeAll(self):
        pass

    async def emit(self, event_name, data):
        event = self.eventHandlers.get(event_name)
        if (event and type(event['listeners']) == list):
            if (event['once'] is True):
                self.removeAllListeners(event_name)
            await asyncio.wait([next(data) for next in event['listeners']])

    def getEventList(self):
        return list(self.eventHandlers.keys())

    def getListeners(self, event_name):
        event = self.eventHandlers.get(event_name, {'listeners': []})
        return event['listeners']

    def getListenersCount(self, event_name):
        return len(self.getListenersCount(event_name))

    def enable(self):
        self.eventHandlers['enabled'] = True

    def disable(self):
        self.eventHandlers['enabled'] = False
