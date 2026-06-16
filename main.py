"""
AI quiz generator
"""

from pdfreader import SimplePDFViewer
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

# creating object for groq interface
client=Groq()

# reading pdf data
with open("sample.pdf","rb") as fd:
    obj = SimplePDFViewer(fd)
    text = ""
    while True:
        try:
            obj.render()
            text += " ".join(obj.canvas.strings) + "\n"
            obj.next()
        except Exception as e:
            break
# print(text)   


# model calling
response=client.chat.completions.create(
    messages = [
        {
            "role":"system",
            "content":f"you are a professor in a college and give me 10 mcqs based on {text} without answers"
        }
    ],
    model="llama-3.3-70b-versatile"
)      

# displaying response
print(response.choices[0].message.content)