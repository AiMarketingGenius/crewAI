from crewai import Agent, Task, Crew

# Define an agent
agent = Agent(
    role="Senior Technical Writer",
    goal="Turn complex research into plain English",
    backstory="Has 15 years of experience translating dense technical documentation into readable summaries.",
    verbose=True
)

# Define a task — THIS was missing expected_output
task = Task(
    description="Summarize the following research paper in plain English for a general audience.",
    expected_output="A one-paragraph summary that is simple, clear, and avoids jargon.",
    agent=agent
)

# Crew setup
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)
