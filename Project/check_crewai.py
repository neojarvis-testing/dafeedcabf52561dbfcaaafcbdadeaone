# check_crewai.py
import sys
try:
    import crewai
    from crewai import Agent, Task, Crew, Process
    print("CREWAI VERSION:", getattr(crewai, "__version__", "unknown"))

    # Safe: construct objects without calling any model
    analyst = Agent(
        role="Analyst",
        goal="Sanity check imports only",
        backstory="No LLM call here.",
        allow_delegation=False,
        verbose=False,
        tools=[],   # keep empty to avoid any network/tooling
    )
    t = Task(description="Dry-run: nothing to do", agent=analyst, expected_output="OK")
    crew = Crew(agents=[analyst], tasks=[t], process=Process.sequential)
    print("CREWAI OK: agents & task instantiated")
    sys.exit(0)
except Exception as e:
    print("CREWAI CHECK FAILED:", repr(e))
    sys.exit(1)
