import sys
sys.path.append('./src')
from crewai.main import crew
if __name__ == "__main__":
    crew.kickoff()
