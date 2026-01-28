import os
import sys
from pathlib import Path

# Setup paths
PROJECT_ROOT = Path("/Users/leokampen/Desktop/ai-android-project/")
sys.path.append(str(PROJECT_ROOT))

from langchain_ollama import ChatOllama
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools import ShellTool
from langgraph.prebuilt import create_react_agent # <--- This is the new, stable way

def main():
    if len(sys.argv) < 2:
        print("Usage: python codex.py \"<your instruction>\"")
        sys.exit(1)
    
    task = " ".join(sys.argv[1:])
    print(f"🤖 Agent starting on task: {task}")

    # 1. Initialize Ollama
    llm = ChatOllama(model="deepseek-coder", temperature=0)

    # 2. Setup Tools
    file_toolkit = FileManagementToolkit(root_dir=str(PROJECT_ROOT))
    tools = file_toolkit.get_tools() + [ShellTool()]

    # 3. Create the Agent (No complicated prompts or executors needed)
    # This creates a "Graph" agent that handles the loop for you
    agent_executor = create_react_agent(llm, tools)

    try:
        # 4. Run (the input format is slightly different for LangGraph)
        print("--- Thinking ---")
        for event in agent_executor.stream(
            {"messages": [("user", task)]},
            config={"configurable": {"thread_id": "1"}}
        ):
            for value in event.values():
                # This prints the AI's thoughts and actions as they happen
                if "messages" in value:
                    last_msg = value["messages"][-1]
                    if hasattr(last_msg, 'content') and last_msg.content:
                        print(f"\n📝 {last_msg.content}")
                    if hasattr(last_msg, 'tool_calls') and last_msg.tool_calls:
                        print(f"🛠  Tool Call: {last_msg.tool_calls[0]['name']}")

        print("\n✅ Task completed.")
    except Exception as e:
        print(f"\n❌ Execution Error: {e}")

if __name__ == "__main__":
    main()
