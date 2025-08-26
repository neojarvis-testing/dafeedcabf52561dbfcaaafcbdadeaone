# test_langgraph.py
# Smoke test: import LangGraph, build a 1-node graph, invoke once.

from typing import TypedDict
try:
    from langgraph.graph import StateGraph, END
except Exception as e:
    raise SystemExit(f"[LangGraph] Import failed: {e}")

class State(TypedDict):
    msg: str

def echo(state: State) -> State:
    return {"msg": state["msg"] + " ✅"}

def main():
    try:
        g = StateGraph(State)
        g.add_node("echo", echo)
        g.set_entry_point("echo")
        g.add_edge("echo", END)
        app = g.compile()

        out = app.invoke({"msg": "Hello LangGraph"})
        print("[LangGraph] OK:", out)
    except Exception as e:
        print("[LangGraph] Runtime error:", e)

if __name__ == "__main__":
    main()
