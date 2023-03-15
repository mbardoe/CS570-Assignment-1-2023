# Name:

# Complete the code for ConversationStarter
# Every Conversationalist should have a GreetingMaker and a QuestionAsker.
# In the __init__ method you will need to instantiate a GreetingMaker and a QuestionAsker.
# You will need to import those classes in from the other files
# Use those instantiated classes to create a conversation in  start_conversation method.
# Use the QuestionAsker to determine who you are speaking with. A QuestionAsker has pose_question()
# method that returns a string with the name of the person you are conversing with.
# give that string to GreetingMaker's greeting_generator method to have your program produce a
# greeting to start your conversation.


class Conversationalist:

    def __init__(self):
        pass

    def start_conversation(self):
        pass


if __name__ == '__main__':
    talker = Conversationalist()
    talker.start_conversation()
