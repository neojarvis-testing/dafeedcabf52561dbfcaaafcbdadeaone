from agno.agent import Agent

def main():
    a = Agent(name="sanity", instructions="Just echo input.", markdown=False)
    print("AGNO OK:", isinstance(a, Agent))

if __name__ == "__main__":
    main()