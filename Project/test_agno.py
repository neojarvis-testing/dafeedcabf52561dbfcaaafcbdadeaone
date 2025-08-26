# test_agno.py
# Smoke test: try a few common Agno imports; report which one is present.
# (Different distributions use different module paths. This keeps it safe.)

def try_imports():
    candidates = [
        ("agno", "import agno"),
        ("agno.agent", "from agno.agent import Agent"),
        ("agno_sdk", "import agno_sdk"),
        ("agnostudio", "import agnostudio"),
    ]
    available = []
    for name, stmt in candidates:
        try:
            exec(stmt, {})
            available.append(name)
        except Exception:
            pass
    return available

def main():
    available = try_imports()
    if not available:
        print("[Agno] Not found. Try: pip install agno")
    else:
        print(f"[Agno] OK: found modules -> {', '.join(available)}")

if __name__ == "__main__":
    main()
