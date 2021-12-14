#!/bin/env python3
"""
My understanding of how observer pattern works
      ------------------                  ---------------------------
      |                 |                 |     Observers            |
      |                 |                 |                          |
      |  Skype channel  |    event        |  ---------- ------------ |
      |                 |  -------------->|  | Is PTO  || Is Article||    
      |  (subject)      |                 |  |_________||___________||
      |                 |                 |  ------------------      |
      |                 |                 |  |  Is Question    |     |
      |                 |                 |  |_________________|     |
      |_________________|                 |__________________________|

Note: I could be completely wrong about how I am implementing observer pattern
"""

class Subject():
    """
    Skype chats
    """
    def __init__(self):
        "Initialize subject"
        self._subscribers = []

    def add_subscribers(self, observer):
        "Add new subscibers/observers"
        self._subscribers.append(observer)
        print(f"Adding new subscirber - {observer}")

    def remove_subscribers(self, observer):
        "Remove existing subsciber/observers"
        self._subscribers.remove(observer)
        print(f"Removing  subscirber - {observer}")

    def notify_event(self):
        "Notify the observers in case of event"
        for obs in self._subscribers:
            obs.update("New chat")

class Observer():
    """
    Subscribers for Skype chat
    """
    def update(self, msg: str):
        "Update message"
        pass

class Is_pto(Observer):
    """
    Is PTO object
    """
    def update(self, msg: str):
        "Update observer notification"
        print(f"{msg} received by the is PTO observer")

class Is_article(Observer):
    """
    Is Article object
    """
    def update(self, msg:str):
        "Update observer notification"
        print(f"{msg} received by the is Article observer")

class Is_question(Observer):
    """
    Is Question object
    """
    def update(self, msg:str):
        "Update observer notification"
        print(f"{msg} received by the is Question observer")

if __name__ == "__main__":
    subject = Subject()

    pto = Is_pto()
    article = Is_article()
    question = Is_question()

    # Add IS_PTO & IS_Question observers
    subject.add_subscribers(pto)
    subject.add_subscribers(question)
    
    # Notify the observers about an event
    subject.notify_event()
