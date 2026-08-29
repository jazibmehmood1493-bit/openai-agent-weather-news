import os
from swarm import Swarm,Agent
client=Swarm()
def get_weather(location: str):
    return f"The weather in {location} is sunny with a temperature of 25C."
    def get_news(topic: str):
        return f"The latest news on '{topic}':openAI announces new updates!"
        my_agent=Agent(
            name="weather and News Agent",
            instructions="You are a helpful assistant.Use the available tools to provide weather updates or news.",
            functions=[get_weather,get_news],
        )
        if __name__=="__main__":
            response=client.run(
                agent=my_agent,
                messages=[{"role":"user","content":"What is the weather in Tokyo and tell me news about AI?"}],
            )
            print(response.messages[-1]["content"])