# test_google_adk.py
# Smoke test: Detect likely Google Agent/ADK packages without calling cloud APIs.
# (Names are evolving; this only verifies local install presence.)

def try_candidates():
    candidates = [
        ("google_ai_agent_sdk", "import google_ai_agent_sdk"),
        ("google_agents", "import google_agents"),
        ("google.generativeai", "import google.generativeai as genai"),  # fallback: Gemini client
        ("vertexai", "import vertexai"),  # Vertex AI Python SDK
    ]
    found = []
    for name, stmt in candidates:
        try:
            ns = {}
            exec(stmt, ns)
            found.append(name)
        except Exception:
            pass
    return found

def main():
    found = try_candidates()
    if found:
        print(f"[Google ADK] OK: detected -> {', '.join(found)}")
    else:
        print("[Google ADK] Not found. Install the relevant SDK (e.g., vertexai or google.generativeai) or your ADK package.")

if __name__ == "__main__":
    main()
