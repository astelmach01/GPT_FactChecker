import logging
import os

from dotenv import load_dotenv
import ast
import openai
import json
from functions import available_functions

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

MODEL = "gpt-3.5-turbo"


def _handle_function_call(messages, response_message):
    function_name = response_message["function_call"]["name"]
    function_to_call = available_functions[function_name]
    function_args = json.loads(response_message["function_call"]["arguments"])
    function_response = function_to_call(**function_args)

    messages.append(response_message)  # extend conversation with assistant's reply
    messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_response["output"],
        }
    )

    second_response = _create_response(messages)
    return second_response["choices"][0]["message"]


def _create_response(messages: list, functions=None, function_call=None):
    print("Getting chat response...")
    if functions is None:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
        )
        return response

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        functions=functions,
        function_call=function_call,
    )
    return response


class ChatGPT:
    def __init__(self, function_file_name: os.PathLike | None):
        self.function_file_name = function_file_name

    def get_response(self, prompt: str) -> str:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful and expert assistant that writes code in Python only."
                "In your code, write some test cases where the output of running the code"
                "results in either True or False if they all passed. You can achieve this"
                "by using assert statements. For example, if the user asked to write a "
                "function to reverse a string, you would respond with: \n"
                "def reverse_string(string): return string[::-1] \n\n "
                "print(reverse_string('Hello, World!') == '!dlroW ,olleH')"
                "\nMake sure that the program results in some output if it were run with"
                "python main.py, and as a reminder, include test cases in your code."
            },
            {"role": "user", "content": prompt},
        ]

        response = _create_response(
            messages, self._get_functions_info(), {"name": "execute_and_capture_output"}
        )
        response_message = response["choices"][0]["message"]

        if not response_message.get("function_call"):
            print("Not a function call")
            return response_message["content"]

        return _handle_function_call(messages, response_message)

    def _get_functions_info(self):
        if not self.function_file_name:
            return None

        # Initialize the list to store function information
        functions_info = []

        # Parse the Python code in the given file into an AST
        with open(self.function_file_name, "r") as file:
            code = file.read()
        tree = ast.parse(code)

        # Define a function to extract function information from the AST
        def extract_function_info(node):
            if isinstance(node, ast.FunctionDef):
                function_name = node.name
                function_description = ast.get_docstring(node)
                function_parameters = []

                for arg in node.args.args:
                    parameter = {"name": arg.arg, "type": "string"}
                    function_parameters.append(parameter)

                functions_info.append(
                    {
                        "name": function_name,
                        "description": function_description,
                        "parameters": {
                            "type": "object",
                            "properties": {
                                param["name"]: param for param in function_parameters
                            },
                            "required": [
                                param["name"] for param in function_parameters
                            ],
                        },
                    }
                )

        # Traverse the AST to extract function information
        for node in ast.walk(tree):
            extract_function_info(node)

        return functions_info
