# check_google_adk.py
import sys
try:
    import google_adk  # module name on PyPI installs as google_adk
    from google.adk.agents import Agent  # public API per docs
    from google.adk.sessions import InMemorySessionService
    from google.adk.runners import Runner

    print("GOOGLE ADK VERSION:", getattr(google_adk, "__version__", "unknown"))

    # Construct minimal in-memory plumbing without running an LLM
    agent = Agent(name="sanity-agent")  # no tools/models attached
    session = InMemorySessionService()
    runner = Runner(agent=agent, session_service=session)
    print("GOOGLE ADK OK: core classes instantiated")
    sys.exit(0)
except Exception as e:
    print("GOOGLE ADK CHECK FAILED:", repr(e))
    print("Hint: `pip show google-adk` to verify install.")
    sys.exit(1)
