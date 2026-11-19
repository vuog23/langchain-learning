import os
import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

@tool('get_weather', description='Return weather information for a given city', return_direct=False)
def get_weather(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

agent = create_agent(
    model="gpt-5-nano",
    tools=[get_weather],
    system_prompt="Your are a helpful weather assistant, who always crack jokes and it humorous while remaining helpful."
)


response = agent.invoke({
    'messages':[
        {"role": "user", "content": "What is the weather like in Vienna?"}
    ]
})


print(response)
print(response["messages"][-1].content)

