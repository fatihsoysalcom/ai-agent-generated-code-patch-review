
# This script simulates an AI coding agent generating a patch for a simple Python function
# and emphasizes the critical human review process.

# --- 1. Original Code with a Potential Issue ---
# This is the code an AI agent might analyze.
original_code = """
def calculate_average(numbers):
    # This function calculates the average of a list of numbers.
    # AI identifies: Returning 0 for an empty list can be misleading.
    if len(numbers) == 0:
        return 0 
    total = sum(numbers)
    return total / len(numbers)

# Example usage:
data1 = [10, 20, 30, 40, 50]
print(f"Average of {data1}: {calculate_average(data1)}")

data2 = []
print(f"Average of {data2}: {calculate_average(data2)}")
"""

# --- 2. Simulated AI Agent's Analysis ---
ai_analysis = (
    "The `calculate_average` function returns 0 for an empty list, which might be misleading. "
    "It should ideally raise a ValueError or return None to indicate an invalid operation, "
    "rather than a numerical result."
)

# --- 3. Simulated AI Agent's Generated Patch ---
# The AI identifies the problematic line and suggests a replacement.
problematic_snippet = "        return 0 "
ai_generated_fix_snippet = "        raise ValueError('Cannot calculate average of an empty list')"

# --- 4. Function to Simulate Applying and Reviewing the Patch ---
def apply_and_review_patch(original_code_str, problem_snippet, fix_snippet, analysis_desc):
    print("--- Original Code ---")
    print(original_code_str)

    print("\n--- AI Agent Analysis ---")
    print(analysis_desc)

    print("\n--- AI Proposed Patch (Snippet Replacement) ---")
    print(f"Problematic line:\n{problem_snippet.strip()}") # Display without leading spaces
    print(f"Proposed fix:\n{fix_snippet.strip()}") # Display without leading spaces

    # Simulate applying the patch by replacing the problematic snippet.
    # In a real scenario, this would involve more sophisticated diffing and patching tools.
    patched_code_str = original_code_str.replace(problem_snippet, fix_snippet)

    print("\n--- Patched Code (for Human Review) ---")
    print(patched_code_str)

    # --- 5. Emphasize the Human Review Step (Core Concept of the Article) ---
    print("\n--- Human Review Required ---")
    print("An AI agent has generated this patch. Before deploying, a human developer MUST:")
    print("1. Understand the proposed change and its implications.")
    print("2. Verify the correctness of the fix (e.g., does it solve the problem without introducing new ones?).")
    print("3. Check for potential side effects or regressions.")
    print("4. Ensure it aligns with coding standards and architectural principles.")
    print("5. Write or update tests to cover the new behavior.")
    print("\nThis simulated example highlights the *output* of an AI agent and the critical *human step* that follows.")

# --- Run the Simulation ---
apply_and_review_patch(original_code, problematic_snippet, ai_generated_fix_snippet, ai_analysis)
