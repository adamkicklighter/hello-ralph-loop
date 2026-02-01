import subprocess
import json
import time

MAX_ITERATIONS = 5

state = {"iterations": []}

for i in range(MAX_ITERATIONS):
    print(f"\n--- Iteration {i+1} ---")

    # Here you manually run Copilot Agent in Agent mode with agent_prompt.md
    input("Run Copilot Agent now with agent_prompt.md. Press Enter when done...")

    # Execute the produced code
    try:
        result = subprocess.run(
            ["python", "workspace/main.py"],
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout.strip()
        success = output == "Hello, Ralph Loop!"
    except Exception as e:
        output = str(e)
        success = False

    iteration_record = {
        "iteration": i+1,
        "output": output,
        "success": success
    }
    state["iterations"].append(iteration_record)

    with open("state.json", "w") as f:
        json.dump(state, f, indent=2)

    if success:
        print("Objective achieved.")
        break
    else:
        print("Objective not met. Looping...")

time.sleep(1)
