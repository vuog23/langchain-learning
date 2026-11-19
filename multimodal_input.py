from base64 import b64encode
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

load_dotenv()

model = init_chat_model(model="gpt-5-nano")

# message = {
#     'role': 'user',
#     'content': [
#         {'type': 'text', 'text': 'Describe the content of the image.'},
#         {'type': 'image', 'url': 'https://umusic.co.nz/wp-content/uploads/sites/44/2019/02/GH009.jpg'},
#     ]
# }

message = HumanMessage(
    content=[
        {'type': 'text', 'text': 'Describe the content of the image.'},
        {
            'type': 'image',
            'base64': b64encode(open('meme.jpg', 'rb').read()).decode(),
            'mime_type': 'image/jpg' 
        },
    ]
)


response = model.invoke([message])

print(response.content)