import re

rules=[
    (r"\b(hi|hey|hello)\b", "Hello! How can I assist you today?"),
    (r"your name|who are you", "I am Kimi a simple rule-based chatbot."),
    (r"how are you", "I am just a program, but I'm functioning as expected!"),
    (r"thanks", "You're welcome!"),
]

def reply(message):
    msg=message.lower().strip()
    for pattern,response in rules:
        if re.search(pattern,msg):
            return response

    return "Sorry! Currently I am not trained to answer that. Please try again later."

while True:
    user=input("You: ")

    if user.lower().strip()=="bye":
        print("Kimi: Goodbye! Have a great day!")
        break

    print("Kimi: ",reply(user))