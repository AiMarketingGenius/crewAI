from crewai import Crew, Agent, Task
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

# Define an agent
agent = Agent(
    role='Senior Research Analyst',
    goal='Extract and summarize key business findings from documents',
    backstory='You are a top analyst trained to extract critical insights from dense information.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define a task
task = Task(
    description='Summarize the business implications from a document passed via environment or input.',
    agent=agent
)

# Define the Crew
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=2
)

crew.kickoff()
