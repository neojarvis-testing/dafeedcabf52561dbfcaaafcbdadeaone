# test_crewai.py
# Smoke test: import CrewAI and construct Agent/Task/Crew objects (no kickoff to avoid LLM calls).

try:
    from crewai import Agent, Task, Crew, Process
except Exception as e:
    raise SystemExit(f"[CrewAI] Import failed: {e}")

def main():
    try:
        # Keep it offline-safe: just instantiate without calling kickoff()
        greeter = Agent(
            role="Greeter",
            goal="Say a friendly hello",
            backstory="You are a simple greeter agent.",
            allow_delegation=False,
            verbose=False,
        )
        hello_task = Task(
            description="Compose a brief greeting to the user.",
            agent=greeter,
        )
        crew = Crew(agents=[greeter], tasks=[hello_task], process=Process.sequential)
        print("[CrewAI] OK: Agent/Task/Crew instantiated.")
    except Exception as e:
        print("[CrewAI] Runtime error:", e)

if __name__ == "__main__":
    main()
