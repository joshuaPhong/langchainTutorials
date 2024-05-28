from dotenv import load_dotenv

load_dotenv()

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# set up the model. You can use the model name or the model id
# class will automatically look for the key in the .env file
model = ChatAnthropic(model="claude-3-sonnet-20240229",
                      temperature=0.5,
                      max_tokens=100,
                      verbose=True)

# set up the messages
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

# invoke the model
# output = model.invoke(messages)
# we can pass a message straight to the model
# output = model.invoke(HumanMessage(content="hi!")),
# or a string output = model.invoke("hi!").
# # print the output as an AI message
# print(output)

# or use an output parser to get the output as a string
# set up the output parser
parser = StrOutputParser()
# Invoke the model.
output = model.invoke(messages)
# print the output
print(parser.invoke(output))
# We can use batch processing by passing a list of messages
# And stream processing by passing a single message
