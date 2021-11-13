"""
    Module to manage the events in the application. 
    Part of the Observer design pattern. 

"""
 subscrbers = dict()

 def subscribe(event_type: str, fn):
     """ Map the events and handler functions they should trigger""" 
    if not event_type in subscrbers:
         subscrbers[event_type] = []
    subscrbers[event_type].append(fn)


def post_event(event_type: str, **data):
    """ Trigger the handler function mapped """
    if not event_type in subscrbers:
        return 
    for fn in subscrbers[event_type]:
        fn(**data)
