import os
import time

from crewai import Agent, Task, Crew, Process
from crewai_tools import FileReadTool
from langchain_openai import ChatOpenAI

# set this key just to avoid errors initializing the ChatOpenAI client
os.environ["OPENAI_API_KEY"] = "EXAMPLE-KEY"
podcast_topic = "Jellyfish"

start_time = time.time()


llm_llama = ChatOpenAI(
    model="llama3.2:latest",
    base_url="http://localhost:11434/v1",
)


host_agent = Agent(
    role="Podcast host",
    goal=f"You are able to introduce guest and ask interesting questions about {podcast_topic}",
    backstory="You are star podcaster with about 1Million followers on youtube",
    verbose=True,
    llm=llm_llama,
)

sme_agent = Agent(
    role=f"Subject Matter Expert on {podcast_topic}",
    goal=f"You are able to answer questions about {podcast_topic}",
    backstory=f"Your made your career about {podcast_topic}",
    verbose=True,
    llm=llm_llama,
)

scripting_agent = Agent(
    role=f"Script writer agent",
    goal=f"You are able to record the conversation between host and subject matter expert and produce it in written form conversation style",
    backstory=f"Your made record all the conversations as transcripts for producing subtitles",
    verbose=True,
    llm=llm_llama,
)

task_podcasting_host = Task(
    description="""Introduce the topic for podcast: {podcast_topic} 
    and ask interesting questions about the same topic,
     pass the questions and answers from expert to scripting_task""",
    expected_output=f"""Introduce the topic for podcast: {podcast_topic} 
    and ask interesting questions about the same topic,
     pass the questions and answers from expert to scripting_task""",
    agent=host_agent,
    #output_file=f"markdown/{podcast_topic}.md",
)

task_scripter = Task(
    description="""Record the conversation between host and subject matter expert""",
    expected_output="markdown file with conversation written in format of question from host and response from expert",
    agent=scripting_agent,
    output_file=f"markdown/{podcast_topic}.md",
)

crew = Crew(
    agents=[host_agent, sme_agent],
    tasks=[task_podcasting_host, task_scripter],
    process=Process.hierarchical,
    verbose = 2,
    max_execution_time=1500,
    manager_agent= scripting_agent
)

result = crew.kickoff()
print("############")
print(result)
print("Done")
print("--- %s seconds ---" % (time.time() - start_time))