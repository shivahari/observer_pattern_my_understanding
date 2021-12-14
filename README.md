# observer_pattern_my_understanding
This project is an abstraction of my understanding of the observer pattern

I have tried to mimic the example of how Skype chats are passed on to various observers.

The Subject in this example is:
- Skype chat

The observers in this example are:
1. IS PTO observer, verifies if every chat message is a PTO notification
2. IS Article observer, verifies if every chat message is an Article
3. IS Question observer, verifies if every chat message is a question

NOTE: I could be very wrong with my understanding and my abstract implementation, please feel free to raise a PR or an issue if you find something misinterpreted
