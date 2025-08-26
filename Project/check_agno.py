# check_agno.py
import sys
try:
    import agno
    print("AGNO VERSION:", getattr(agno, "__version__", "unknown"))

    # Some Agno versions expose Agent at agno.Agent; others via submodules.
    Agent = getattr(agno, "Agent", None)
    if Agent is not None:
        a = Agent(name="sanity-agent")  # Should not trigger network
        print("AGNO OK: Agent constructed")
    else:
        print("AGNO OK: package imported (Agent symbol not found in this version)")
    sys.exit(0)
except Exception as e:
    print("AGNO CHECK FAILED:", repr(e))
    sys.exit(1)
