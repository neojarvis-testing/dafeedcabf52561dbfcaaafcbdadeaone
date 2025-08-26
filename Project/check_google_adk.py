# adk_smoke.py
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

def main():
    agent = Agent(name="sanity_agent")
    session = InMemorySessionService()
    runner = Runner(
        agent=agent,
        session_service=session,
        app_name="adk_smoke_test"   # required kwarg
    )
    print("ADK OK:", isinstance(runner, Runner))

if __name__ == "__main__":
    main()
