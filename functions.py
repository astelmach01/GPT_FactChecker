import io
import sys


def execute_and_capture_output(code: str) -> dict[str, str | bool]:
    """
    This function executes the given code and returns the output, or exception, if any
    Use this to check your code.
    """
    print(f"Executing code {code}")

    # Create a string buffer to capture stdout
    output_buffer = io.StringIO()

    # Save the current stdout so we can restore it later
    original_stdout = sys.stdout

    try:
        # Redirect stdout to the buffer
        sys.stdout = output_buffer

        # Execute the provided code
        exec(code)

        # Get the captured output
        captured_output = output_buffer.getvalue()

        print(f"Got output {captured_output}")
        if not captured_output:
            captured_output = "There was no output to this Python code"

        return {"success": True, "output": captured_output}

    except Exception as e:
        # Get the error message
        error_message = str(e)

        print(f"Got error {error_message}")
        return {"success": False, "output": error_message}

    finally:
        # Restore the original stdout
        sys.stdout = original_stdout


available_functions = {"execute_and_capture_output": execute_and_capture_output}
