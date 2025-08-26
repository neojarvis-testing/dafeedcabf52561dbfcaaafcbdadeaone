# check_langgraph.py
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class S(TypedDict):
    msg: str

def step1(state: S) -> S:
    return {"msg": state["msg"] + " -> step1"}

def step2(state: S) -> S:
    return {"msg": state["msg"] + " -> step2"}

def main():
    g = StateGraph(S)
    g.add_node("step1", step1)
    g.add_node("step2", step2)
    g.add_edge(START, "step1")
    g.add_edge("step1", "step2")
    g.add_edge("step2", END)
    app = g.compile()
    out = app.invoke({"msg": "ok"})
    print("LANGGRAPH OK:", out["msg"])

if __name__ == "__main__":
    main()
