import os
import time

from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool
from langchain_openai import ChatOpenAI

# set this key just to avoid errors initializing the ChatOpenAI client
os.environ["OPENAI_API_KEY"] = "EXAMPLE-KEY"

start_time = time.time()


llm_llama = ChatOpenAI(
    model="llama3.2:latest",
    base_url="http://localhost:11434/v1",
)

file_read_tool = FileReadTool(file_path='manifestos/bjp-manifesto.txt')

summarizer_agent = Agent(
    role="Political Reporter",
    goal="You are able to evaluate a political party manifesto for upcoming election",
    backstory="Journalist with background in maharashtra politics",
    verbose=True,
    llm=llm_llama,
    tools = [file_read_tool]
)

task_report = Task(
    description="""Read the document and make it read""",
    expected_output="Extract key insights so a voter can read this document to gain insights",
    agent=summarizer_agent,
    output_file="markdown/mva2.md",
)



consolidation_agent = Agent(
    role="Senior Political Editor",
    goal="Extract key insights from summary report",
    backstory="""You are a renowned Political Analyst and have a background covering maharashtra politics """,
    verbose=True,
    llm = llm_llama,
    #tools = [file_read_tool]
)

task_consolidate = Task(
    description="""Create a summary table with Categories like Governance, Economic Development, Social Welfare 
    along with any other social political issues mentioned""",
    expected_output="Extract key insights so a voter can read this document to gain insights",
    agent=consolidation_agent,
    output_file="markdown/bjp3.md",
)



# crew = Crew(
#     agents=[summarizer_agent, consolidation_agent],
#     tasks=[task_report, task_consolidate],
#     process=Process.sequential,
#     verbose = 2,
#     max_execution_time=1500
# )

# crew = Crew(
#     agents = [consolidation_agent],
#     tasks = [task_consolidate],
#     verbose = 2
# )

crew = Crew(
    agents = [summarizer_agent, consolidation_agent],
    tasks = [task_consolidate],
    verbose = 2
)

result = crew.kickoff()
print("############")
print(result)
print("Done")
print("--- %s seconds ---" % (time.time() - start_time))