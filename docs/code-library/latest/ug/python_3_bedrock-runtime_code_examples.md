---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_bedrock-runtime_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Bedrock Runtime examples using SDK for Python (Boto3)
<a name="python_3_bedrock-runtime_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Amazon Bedrock Runtime.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)
+ [Amazon Nova](#amazon_nova)
+ [Amazon Nova Canvas](#amazon_nova_canvas)
+ [Amazon Nova Reel](#amazon_nova_reel)
+ [Amazon Titan Image Generator](#amazon_titan_image_generator)
+ [Amazon Titan Text](#amazon_titan_text)
+ [Amazon Titan Text Embeddings](#amazon_titan_text_embeddings)
+ [Anthropic Claude](#anthropic_claude)
+ [Cohere Command](#cohere_command)
+ [DeepSeek](#deepseek)
+ [Meta Llama](#meta_llama)
+ [Mistral AI](#mistral_ai)
+ [Stable Image Core](#stable_image_core)

## Scenarios
<a name="scenarios"></a>

### Create a playground application to interact with Amazon Bedrock foundation models
<a name="cross_FMPlayground_python_3_topic"></a>

The following code example shows how to create playgrounds to interact with Amazon Bedrock foundation models through different modalities.

**SDK for Python (Boto3)**
 The Python Foundation Model (FM) Playground is a Python/FastAPI sample application that showcases how to use Amazon Bedrock with Python. This example shows how Python developers can use Amazon Bedrock to build generative AI-enabled applications. You can test and interact with Amazon Bedrock foundation models by using the following three playgrounds:
+ A text playground.
+ A chat playground.
+ An image playground.
The example also lists and displays the foundation models you have access to, along with their characteristics. For source code and deployment instructions, see the project in [GitHub](https://github.com/build-on-aws/python-fm-playground).

**Services used in this example**
+ Amazon Bedrock Runtime

### Create and invoke a managed prompt
<a name="bedrock-agent_GettingStartedWithBedrockPrompts_python_3_topic"></a>

The following code example shows how to:
+ Create a managed prompt.
+ Create a version of the prompt.
+ Invoke the prompt using the version.
+ Clean up resources (optional).

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples).
Create and invoke a managed prompt.

```
import argparse
import boto3
import logging
import time

# Now import the modules
from prompt import create_prompt, create_prompt_version, delete_prompt
from run_prompt import invoke_prompt

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

def run_scenario(bedrock_client, bedrock_runtime_client, model_id, cleanup=True):
    """
    Runs the Amazon Bedrock managed prompt scenario.

    Args:
        bedrock_client: The Amazon Bedrock Agent client.
        bedrock_runtime_client: The Amazon Bedrock Runtime client.
        model_id (str): The model ID to use for the prompt.
        cleanup (bool): Whether to clean up resources at the end of the scenario.

    Returns:
        dict: A dictionary containing the created resources.
    """
    prompt_id = None

    try:
        # Step 1: Create a prompt
        print("\n=== Step 1: Creating a prompt ===")
        prompt_name = f"PlaylistGenerator-{int(time.time())}"
        prompt_description = "Playlist generator"
        prompt_template = """
          Make me a {{genre}} playlist consisting of the following number of songs: {{number}}."""

        create_response = create_prompt(
            bedrock_client,
            prompt_name,
            prompt_description,
            prompt_template,
            model_id
        )

        prompt_id = create_response['id']
        print(f"Created prompt: {prompt_name} with ID: {prompt_id}")

        # Create a version of the prompt
        print("\n=== Creating a version of the prompt ===")
        version_response = create_prompt_version(
            bedrock_client,
            prompt_id,
            description="Initial version of the product description generator"
        )

        prompt_version_arn = version_response['arn']
        prompt_version = version_response['version']

        print(f"Created prompt version: {prompt_version}")
        print(f"Prompt version ARN: {prompt_version_arn}")

        # Step 2: Invoke the prompt directly
        print("\n=== Step 2: Invoking the prompt ===")
        input_variables = {
            "genre": "pop",
            "number": "2",
           }

        # Use the ARN from the create_prompt_version response
        result = invoke_prompt(
            bedrock_runtime_client,
            prompt_version_arn,
            input_variables
        )
        # Display the playlist
        print(f"\n{result}")

        # Step 3: Clean up resources (optional)
        if cleanup:
            print("\n=== Step 3: Cleaning up resources ===")

            # Delete the prompt
            print(f"Deleting prompt {prompt_id}...")
            delete_prompt(bedrock_client, prompt_id)

            print("Cleanup complete")
        else:
            print("\n=== Resources were not cleaned up ===")
            print(f"Prompt ID: {prompt_id}")

    except Exception as e:
        logger.exception("Error in scenario: %s", str(e))

        # Attempt to clean up if an error occurred and cleanup was requested
        if cleanup and prompt_id:
            try:
                print("\nCleaning up resources after error...")

                # Delete the prompt
                try:
                    delete_prompt(bedrock_client, prompt_id)
                    print("Cleanup after error complete")
                except Exception as cleanup_error:
                    logger.error("Error during cleanup: %s", str(cleanup_error))
            except Exception as final_error:
                logger.error("Final error during cleanup: %s", str(final_error))

        # Re-raise the original exception
        raise

def main():
    """
    Entry point for the Amazon Bedrock managed prompt scenario.
    """
    parser = argparse.ArgumentParser(
        description="Run the Amazon Bedrock managed prompt scenario."
    )
    parser.add_argument(
        '--region',
        default='us-east-1',
        help="The AWS Region to use."
    )
    parser.add_argument(
        '--model-id',
        default='anthropic.claude-v2',
        help="The model ID to use for the prompt."
    )
    parser.add_argument(
        '--cleanup',
        action='store_true',
        default=True,
        help="Clean up resources at the end of the scenario."
    )
    parser.add_argument(
        '--no-cleanup',
        action='store_false',
        dest='cleanup',
        help="Don't clean up resources at the end of the scenario."
    )
    args = parser.parse_args()

    bedrock_client = boto3.client('bedrock-agent', region_name=args.region)
    bedrock_runtime_client = boto3.client('bedrock-runtime', region_name=args.region)

    print("=== Amazon Bedrock Managed Prompt Scenario ===")
    print(f"Region: {args.region}")
    print(f"Model ID: {args.model_id}")
    print(f"Cleanup resources: {args.cleanup}")

    try:
        run_scenario(
            bedrock_client,
            bedrock_runtime_client,
            args.model_id,
            args.cleanup
        )

    except Exception as e:
        logger.exception("Error running scenario: %s", str(e))

if __name__ == "__main__":
    main()
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse)
  + [CreatePrompt](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreatePrompt)
  + [CreatePromptVersion](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/CreatePromptVersion)
  + [DeletePrompt](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-12-12/DeletePrompt)

### Orchestrate generative AI applications with Step Functions
<a name="cross_ServerlessPromptChaining_python_3_topic"></a>

The following code example shows how to build and orchestrate generative AI applications with Amazon Bedrock and Step Functions.

**SDK for Python (Boto3)**
 The Amazon Bedrock Serverless Prompt Chaining scenario demonstrates how [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), and [https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) can be used to build and orchestrate complex, serverless, and highly scalable generative AI applications. It contains the following working examples:
+  Write an analysis of a given novel for a literature blog. This example illustrates a simple, sequential chain of prompts.
+  Generate a short story about a given topic. This example illustrates how the AI can iteratively process a list of items that it previously generated.
+  Create an itinerary for a weekend vacation to a given destination. This example illustrates how to parallelize multiple distinct prompts.
+  Pitch movie ideas to a human user acting as a movie producer. This example illustrates how to parallelize the same prompt with different inference parameters, how to backtrack to a previous step in the chain, and how to include human input as part of the workflow.
+  Plan a meal based on ingredients the user has at hand. This example illustrates how prompt chains can incorporate two distinct AI conversations, with two AI personas engaging in a debate with each other to improve the final outcome.
+  Find and summarize today's highest trending GitHub repository. This example illustrates chaining multiple AI agents that interact with external APIs.
 For complete source code and instructions to set up and run, see the full project on [GitHub](https://github.com/aws-samples/amazon-bedrock-serverless-prompt-chaining).

**Services used in this example**
+ Amazon Bedrock
+ Amazon Bedrock Runtime
+ Amazon Bedrock Agents
+ Amazon Bedrock Agents Runtime
+ Step Functions

### Tool use with the Converse API
<a name="bedrock-runtime_Scenario_ToolUse_python_3_topic"></a>

The following code example shows how to build a typical interaction between an application, a generative AI model, and connected tools or APIs to mediate interactions between the AI and the outside world. It uses the example of connecting an external weather API to the AI model so it can provide real-time weather information based on user input.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
The primary execution script of the demo. This script orchestrates the conversation between the user, the Amazon Bedrock Converse API, and a weather tool.

```
"""
This demo illustrates a tool use scenario using Amazon Bedrock's Converse API and a weather tool.
The script interacts with a foundation model on Amazon Bedrock to provide weather information based on user
input. It uses the Open-Meteo API (https://open-meteo.com) to retrieve current weather data for a given location.
"""

import boto3
import logging
from enum import Enum

import utils.tool_use_print_utils as output
import weather_tool

logging.basicConfig(level=logging.INFO, format="%(message)s")

AWS_REGION = "us-east-1"

# For the most recent list of models supported by the Converse API's tool use functionality, visit:
# https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html
class SupportedModels(Enum):
    CLAUDE_OPUS = "anthropic.claude-3-opus-20240229-v1:0"
    CLAUDE_SONNET = "anthropic.claude-3-sonnet-20240229-v1:0"
    CLAUDE_HAIKU = "anthropic.claude-3-haiku-20240307-v1:0"
    COHERE_COMMAND_R = "cohere.command-r-v1:0"
    COHERE_COMMAND_R_PLUS = "cohere.command-r-plus-v1:0"

# Set the model ID, e.g., Claude 3 Haiku.
MODEL_ID = SupportedModels.CLAUDE_HAIKU.value

SYSTEM_PROMPT = """
You are a weather assistant that provides current weather data for user-specified locations using only
the Weather_Tool, which expects latitude and longitude. Infer the coordinates from the location yourself.
If the user provides coordinates, infer the approximate location and refer to it in your response.
To use the tool, you strictly apply the provided tool specification.

- Explain your step-by-step process, and give brief updates before each step.
- Only use the Weather_Tool for data. Never guess or make up information.
- Repeat the tool use for subsequent requests if necessary.
- If the tool errors, apologize, explain weather is unavailable, and suggest other options.
- Report temperatures in °C (°F) and wind in km/h (mph). Keep weather reports concise. Sparingly use
  emojis where appropriate.
- Only respond to weather queries. Remind off-topic users of your purpose.
- Never claim to search online, access external data, or use tools besides Weather_Tool.
- Complete the entire process until you have all required data before sending the complete response.
"""

# The maximum number of recursive calls allowed in the tool_use_demo function.
# This helps prevent infinite loops and potential performance issues.
MAX_RECURSIONS = 5

class ToolUseDemo:
    """
    Demonstrates the tool use feature with the Amazon Bedrock Converse API.
    """

    def __init__(self):
        # Prepare the system prompt
        self.system_prompt = [{"text": SYSTEM_PROMPT}]

        # Prepare the tool configuration with the weather tool's specification
        self.tool_config = {"tools": [weather_tool.get_tool_spec()]}

        # Create a Bedrock Runtime client in the specified AWS Region.
        self.bedrockRuntimeClient = boto3.client(
            "bedrock-runtime", region_name=AWS_REGION
        )

    def run(self):
        """
        Starts the conversation with the user and handles the interaction with Bedrock.
        """
        # Print the greeting and a short user guide
        output.header()

        # Start with an emtpy conversation
        conversation = []

        # Get the first user input
        user_input = self._get_user_input()

        while user_input is not None:
            # Create a new message with the user input and append it to the conversation
            message = {"role": "user", "content": [{"text": user_input}]}
            conversation.append(message)

            # Send the conversation to Amazon Bedrock
            bedrock_response = self._send_conversation_to_bedrock(conversation)

            # Recursively handle the model's response until the model has returned
            # its final response or the recursion counter has reached 0
            self._process_model_response(
                bedrock_response, conversation, max_recursion=MAX_RECURSIONS
            )

            # Repeat the loop until the user decides to exit the application
            user_input = self._get_user_input()

        output.footer()

    def _send_conversation_to_bedrock(self, conversation):
        """
        Sends the conversation, the system prompt, and the tool spec to Amazon Bedrock, and returns the response.

        :param conversation: The conversation history including the next message to send.
        :return: The response from Amazon Bedrock.
        """
        output.call_to_bedrock(conversation)

        # Send the conversation, system prompt, and tool configuration, and return the response
        return self.bedrockRuntimeClient.converse(
            modelId=MODEL_ID,
            messages=conversation,
            system=self.system_prompt,
            toolConfig=self.tool_config,
        )

    def _process_model_response(
        self, model_response, conversation, max_recursion=MAX_RECURSIONS
    ):
        """
        Processes the response received via Amazon Bedrock and performs the necessary actions
        based on the stop reason.

        :param model_response: The model's response returned via Amazon Bedrock.
        :param conversation: The conversation history.
        :param max_recursion: The maximum number of recursive calls allowed.
        """

        if max_recursion <= 0:
            # Stop the process, the number of recursive calls could indicate an infinite loop
            logging.warning(
                "Warning: Maximum number of recursions reached. Please try again."
            )
            exit(1)

        # Append the model's response to the ongoing conversation
        message = model_response["output"]["message"]
        conversation.append(message)

        if model_response["stopReason"] == "tool_use":
            # If the stop reason is "tool_use", forward everything to the tool use handler
            self._handle_tool_use(message, conversation, max_recursion)

        if model_response["stopReason"] == "end_turn":
            # If the stop reason is "end_turn", print the model's response text, and finish the process
            output.model_response(message["content"][0]["text"])
            return

    def _handle_tool_use(
        self, model_response, conversation, max_recursion=MAX_RECURSIONS
    ):
        """
        Handles the tool use case by invoking the specified tool and sending the tool's response back to Bedrock.
        The tool response is appended to the conversation, and the conversation is sent back to Amazon Bedrock for further processing.

        :param model_response: The model's response containing the tool use request.
        :param conversation: The conversation history.
        :param max_recursion: The maximum number of recursive calls allowed.
        """

        # Initialize an empty list of tool results
        tool_results = []

        # The model's response can consist of multiple content blocks
        for content_block in model_response["content"]:
            if "text" in content_block:
                # If the content block contains text, print it to the console
                output.model_response(content_block["text"])

            if "toolUse" in content_block:
                # If the content block is a tool use request, forward it to the tool
                tool_response = self._invoke_tool(content_block["toolUse"])

                # Add the tool use ID and the tool's response to the list of results
                tool_results.append(
                    {
                        "toolResult": {
                            "toolUseId": (tool_response["toolUseId"]),
                            "content": [{"json": tool_response["content"]}],
                        }
                    }
                )

        # Embed the tool results in a new user message
        message = {"role": "user", "content": tool_results}

        # Append the new message to the ongoing conversation
        conversation.append(message)

        # Send the conversation to Amazon Bedrock
        response = self._send_conversation_to_bedrock(conversation)

        # Recursively handle the model's response until the model has returned
        # its final response or the recursion counter has reached 0
        self._process_model_response(response, conversation, max_recursion - 1)

    def _invoke_tool(self, payload):
        """
        Invokes the specified tool with the given payload and returns the tool's response.
        If the requested tool does not exist, an error message is returned.

        :param payload: The payload containing the tool name and input data.
        :return: The tool's response or an error message.
        """
        tool_name = payload["name"]

        if tool_name == "Weather_Tool":
            input_data = payload["input"]
            output.tool_use(tool_name, input_data)

            # Invoke the weather tool with the input data provided by
            response = weather_tool.fetch_weather_data(input_data)
        else:
            error_message = (
                f"The requested tool with name '{tool_name}' does not exist."
            )
            response = {"error": "true", "message": error_message}

        return {"toolUseId": payload["toolUseId"], "content": response}

    @staticmethod
    def _get_user_input(prompt="Your weather info request"):
        """
        Prompts the user for input and returns the user's response.
        Returns None if the user enters 'x' to exit.

        :param prompt: The prompt to display to the user.
        :return: The user's input or None if the user chooses to exit.
        """
        output.separator()
        user_input = input(f"{prompt} (x to exit): ")

        if user_input == "":
            prompt = "Please enter your weather info request, e.g. the name of a city"
            return ToolUseDemo._get_user_input(prompt)

        elif user_input.lower() == "x":
            return None

        else:
            return user_input

if __name__ == "__main__":
    tool_use_demo = ToolUseDemo()
    tool_use_demo.run()
```
The weather tool used by the demo. This script defines the tool specification and implements the logic to retrieve weather data using from the Open-Meteo API.

```
import requests
from requests.exceptions import RequestException

def get_tool_spec():
    """
    Returns the JSON Schema specification for the Weather tool. The tool specification
    defines the input schema and describes the tool's functionality.
    For more information, see https://json-schema.org/understanding-json-schema/reference.

    :return: The tool specification for the Weather tool.
    """
    return {
        "toolSpec": {
            "name": "Weather_Tool",
            "description": "Get the current weather for a given location, based on its WGS84 coordinates.",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "latitude": {
                            "type": "string",
                            "description": "Geographical WGS84 latitude of the location.",
                        },
                        "longitude": {
                            "type": "string",
                            "description": "Geographical WGS84 longitude of the location.",
                        },
                    },
                    "required": ["latitude", "longitude"],
                }
            },
        }
    }

def fetch_weather_data(input_data):
    """
    Fetches weather data for the given latitude and longitude using the Open-Meteo API.
    Returns the weather data or an error message if the request fails.

    :param input_data: The input data containing the latitude and longitude.
    :return: The weather data or an error message.
    """
    endpoint = "https://api.open-meteo.com/v1/forecast"
    latitude = input_data.get("latitude")
    longitude = input_data.get("longitude", "")
    params = {"latitude": latitude, "longitude": longitude, "current_weather": True}

    try:
        response = requests.get(endpoint, params=params)
        weather_data = {"weather_data": response.json()}
        response.raise_for_status()
        return weather_data
    except RequestException as e:
        return e.response.json()
    except Exception as e:
        return {"error": type(e), "message": str(e)}
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

## Amazon Nova
<a name="amazon_nova"></a>

### Converse
<a name="bedrock-runtime_Converse_AmazonNovaText_python_3_topic"></a>

The following code example shows how to send a text message to Amazon Nova, using Bedrock's Converse API.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Amazon Nova, using Bedrock's Converse API.

```
# Use the Conversation API to send a text message to Amazon Nova.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Amazon Nova Lite.
model_id = "amazon.nova-lite-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

### ConverseStream
<a name="bedrock-runtime_ConverseStream_AmazonNovaText_python_3_topic"></a>

The following code example shows how to send a text message to Amazon Nova, using Bedrock's Converse API and process the response stream in real-time.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Amazon Nova, using Bedrock's Converse API and process the response stream in real-time.

```
# Use the Conversation API to send a text message to Amazon Nova Text
# and print the response stream.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Amazon Nova Lite.
model_id = "amazon.nova-lite-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    streaming_response = client.converse_stream(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the streamed response text in real-time.
    for chunk in streaming_response["stream"]:
        if "contentBlockDelta" in chunk:
            text = chunk["contentBlockDelta"]["delta"]["text"]
            print(text, end="")

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [ConverseStream](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/ConverseStream) in *AWS SDK for Python (Boto3) API Reference*.

### Document understanding
<a name="bedrock-runtime_DocumentUnderstanding_AmazonNova_python_3_topic"></a>

The following code example shows how to send and process a document with Amazon Nova on Amazon Bedrock.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send and process a document with Amazon Nova on Amazon Bedrock.

```
# Send and process a document with Amazon Nova on Amazon Bedrock.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g. Amazon Nova Lite.
model_id = "amazon.nova-lite-v1:0"

# Load the document
with open("example-data/amazon-nova-service-cards.pdf", "rb") as file:
    document_bytes = file.read()

# Start a conversation with a user message and the document
conversation = [
    {
        "role": "user",
        "content": [
            {"text": "Briefly compare the models described in this document"},
            {
                "document": {
                    # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                    "format": "pdf",
                    "name": "Amazon Nova Service Cards",
                    "source": {"bytes": document_bytes},
                }
            },
        ],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 500, "temperature": 0.3},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

## Amazon Nova Canvas
<a name="amazon_nova_canvas"></a>

### InvokeModel
<a name="bedrock-runtime_InvokeModel_AmazonNovaImageGeneration_python_3_topic"></a>

The following code example shows how to invoke Amazon Nova Canvas on Amazon Bedrock to generate an image.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Create an image with the Amazon Nova Canvas.

```
# Use the native inference API to create an image with Amazon Nova Canvas

import base64
import json
import os
import random

import boto3

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID.
model_id = "amazon.nova-canvas-v1:0"

# Define the image generation prompt for the model.
prompt = "A stylized picture of a cute old steampunk robot."

# Generate a random seed between 0 and 858,993,459
seed = random.randint(0, 858993460)

# Format the request payload using the model's native structure.
native_request = {
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {"text": prompt},
    "imageGenerationConfig": {
        "seed": seed,
        "quality": "standard",
        "height": 512,
        "width": 512,
        "numberOfImages": 1,
    },
}

# Convert the native request to JSON.
request = json.dumps(native_request)

# Invoke the model with the request.
response = client.invoke_model(modelId=model_id, body=request)

# Decode the response body.
model_response = json.loads(response["body"].read())

# Extract the image data.
base64_image_data = model_response["images"][0]

# Save the generated image to a local folder.
i, output_dir = 1, "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
while os.path.exists(os.path.join(output_dir, f"nova_canvas_{i}.png")):
    i += 1

image_data = base64.b64decode(base64_image_data)

image_path = os.path.join(output_dir, f"nova_canvas_{i}.png")
with open(image_path, "wb") as file:
    file.write(image_data)

print(f"The generated image has been saved to {image_path}")
```
+  For API details, see [InvokeModel](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/InvokeModel) in *AWS SDK for Python (Boto3) API Reference*.

## Amazon Nova Reel
<a name="amazon_nova_reel"></a>

### Text-to-video
<a name="bedrock-runtime_Scenario_AmazonNova_TextToVideo_python_3_topic"></a>

The following code example shows how to use Amazon Nova Reel to generate a video from a text prompt.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Use Amazon Nova Reel to generate a video from a text prompt.

```
"""
This example demonstrates how to use Amazon Nova Reel to generate a video from a text prompt.

It shows how to:
- Set up the Amazon Bedrock runtime client
- Configure a text-to-video request
- Submit an asynchronous job for video generation
- Poll for job completion status
- Access the generated video from S3
"""

import random
import time

import boto3

# Replace with your own S3 bucket to store the generated video
# Format: s3://your-bucket-name
OUTPUT_S3_URI = "s3://REPLACE-WITH-YOUR-S3-BUCKET-NAME"

def start_text_to_video_generation_job(bedrock_runtime, prompt, output_s3_uri):
    """
    Starts an asynchronous text-to-video generation job using Amazon Nova Reel.

    :param bedrock_runtime: The Bedrock runtime client
    :param prompt: The text description of the video to generate
    :param output_s3_uri: S3 URI where the generated video will be stored

    :return: The invocation ARN of the async job
    """
    # Specify the model ID for text-to-video generation
    model_id = "amazon.nova-reel-v1:0"

    # Generate a random seed between 0 and 2,147,483,646
    # This helps ensure unique video generation results
    seed = random.randint(0, 2147483646)

    # Configure the video generation request with additional parameters
    model_input = {
        "taskType": "TEXT_VIDEO",
        "textToVideoParams": {"text": prompt},
        "videoGenerationConfig": {
            "fps": 24,
            "durationSeconds": 6,
            "dimension": "1280x720",
            "seed": seed,
        },
    }

    # Specify the S3 location for the output video
    output_config = {"s3OutputDataConfig": {"s3Uri": output_s3_uri}}

    # Invoke the model asynchronously
    response = bedrock_runtime.start_async_invoke(
        modelId=model_id, modelInput=model_input, outputDataConfig=output_config
    )

    invocation_arn = response["invocationArn"]

    return invocation_arn

def query_job_status(bedrock_runtime, invocation_arn):
    """
    Queries the status of an asynchronous video generation job.

    :param bedrock_runtime: The Bedrock runtime client
    :param invocation_arn: The ARN of the async invocation to check

    :return: The runtime response containing the job status and details
    """
    return bedrock_runtime.get_async_invoke(invocationArn=invocation_arn)

def main():
    """
    Main function that demonstrates the complete workflow for generating
    a video from a text prompt using Amazon Nova Reel.
    """
    # Create a Bedrock Runtime client
    # Note: Credentials will be loaded from the environment or AWS CLI config
    bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

    # Configure the text prompt and output location
    prompt = "Closeup of a cute old steampunk robot. Camera zoom in."

    # Verify the S3 URI has been set to a valid bucket
    if "REPLACE-WITH-YOUR-S3-BUCKET-NAME" in OUTPUT_S3_URI:
        print("ERROR: You must replace the OUTPUT_S3_URI with your own S3 bucket URI")
        return

    print("Submitting video generation job...")
    invocation_arn = start_text_to_video_generation_job(
        bedrock_runtime, prompt, OUTPUT_S3_URI
    )
    print(f"Job started with invocation ARN: {invocation_arn}")

    # Poll for job completion
    while True:
        print("\nPolling job status...")
        job = query_job_status(bedrock_runtime, invocation_arn)
        status = job["status"]

        if status == "Completed":
            bucket_uri = job["outputDataConfig"]["s3OutputDataConfig"]["s3Uri"]
            print(f"\nSuccess! The video is available at: {bucket_uri}/output.mp4")
            break
        elif status == "Failed":
            print(
                f"\nVideo generation failed: {job.get('failureMessage', 'Unknown error')}"
            )
            break
        else:
            print("In progress. Waiting 15 seconds...")
            time.sleep(15)

if __name__ == "__main__":
    main()
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [GetAsyncInvoke](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/GetAsyncInvoke)
  + [StartAsyncInvoke](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/StartAsyncInvoke)

## Amazon Titan Image Generator
<a name="amazon_titan_image_generator"></a>

### InvokeModel
<a name="bedrock-runtime_InvokeModel_TitanImageGenerator_python_3_topic"></a>

The following code example shows how to invoke Amazon Titan Image on Amazon Bedrock to generate an image.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Create an image with the Amazon Titan Image Generator.

```
# Use the native inference API to create an image with Amazon Titan Image Generator

import base64
import boto3
import json
import os
import random

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Titan Image Generator G1.
model_id = "amazon.titan-image-generator-v2:0"

# Define the image generation prompt for the model.
prompt = "A stylized picture of a cute old steampunk robot."

# Generate a random seed.
seed = random.randint(0, 2147483647)

# Format the request payload using the model's native structure.
native_request = {
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {"text": prompt},
    "imageGenerationConfig": {
        "numberOfImages": 1,
        "quality": "standard",
        "cfgScale": 8.0,
        "height": 512,
        "width": 512,
        "seed": seed,
    },
}

# Convert the native request to JSON.
request = json.dumps(native_request)

# Invoke the model with the request.
response = client.invoke_model(modelId=model_id, body=request)

# Decode the response body.
model_response = json.loads(response["body"].read())

# Extract the image data.
base64_image_data = model_response["images"][0]

# Save the generated image to a local folder.
i, output_dir = 1, "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
while os.path.exists(os.path.join(output_dir, f"titan_{i}.png")):
    i += 1

image_data = base64.b64decode(base64_image_data)

image_path = os.path.join(output_dir, f"titan_{i}.png")
with open(image_path, "wb") as file:
    file.write(image_data)

print(f"The generated image has been saved to {image_path}")
```
+  For API details, see [InvokeModel](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/InvokeModel) in *AWS SDK for Python (Boto3) API Reference*.

## Amazon Titan Text
<a name="amazon_titan_text"></a>

### InvokeModel
<a name="bedrock-runtime_InvokeModel_TitanText_python_3_topic"></a>

The following code example shows how to send a text message to Amazon Titan Text, using the Invoke Model API.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Use the Invoke Model API to send a text message.

```
# Use the native inference API to send a text message to Amazon Titan Text.

import boto3
import json

from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Titan Text Premier.
model_id = "amazon.titan-text-premier-v1:0"

# Define the prompt for the model.
prompt = "Describe the purpose of a 'hello world' program in one line."

# Format the request payload using the model's native structure.
native_request = {
    "inputText": prompt,
    "textGenerationConfig": {
        "maxTokenCount": 512,
        "temperature": 0.5,
    },
}

# Convert the native request to JSON.
request = json.dumps(native_request)

try:
    # Invoke the model with the request.
    response = client.invoke_model(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

# Decode the response body.
model_response = json.loads(response["body"].read())

# Extract and print the response text.
response_text = model_response["results"][0]["outputText"]
print(response_text)
```
+  For API details, see [InvokeModel](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/InvokeModel) in *AWS SDK for Python (Boto3) API Reference*.

## Amazon Titan Text Embeddings
<a name="amazon_titan_text_embeddings"></a>

### InvokeModel
<a name="bedrock-runtime_InvokeModelWithResponseStream_TitanTextEmbeddings_python_3_topic"></a>

The following code example shows how to:
+ Get started creating your first embedding.
+ Create embeddings configuring the number of dimensions and normalization (V2 only).

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Create your first embedding with Amazon Titan Text Embeddings.

```
# Generate and print an embedding with Amazon Titan Text Embeddings V2.

import boto3
import json

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Titan Text Embeddings V2.
model_id = "amazon.titan-embed-text-v2:0"

# The text to convert to an embedding.
input_text = "Please recommend books with a theme similar to the movie 'Inception'."

# Create the request for the model.
native_request = {"inputText": input_text}

# Convert the native request to JSON.
request = json.dumps(native_request)

# Invoke the model with the request.
response = client.invoke_model(modelId=model_id, body=request)

# Decode the model's native response body.
model_response = json.loads(response["body"].read())

# Extract and print the generated embedding and the input text token count.
embedding = model_response["embedding"]
input_token_count = model_response["inputTextTokenCount"]

print("\nYour input:")
print(input_text)
print(f"Number of input tokens: {input_token_count}")
print(f"Size of the generated embedding: {len(embedding)}")
print("Embedding:")
print(embedding)
```
+  For API details, see [InvokeModel](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/InvokeModel) in *AWS SDK for Python (Boto3) API Reference*.

## Anthropic Claude
<a name="anthropic_claude"></a>

### Converse
<a name="bedrock-runtime_Converse_AnthropicClaude_python_3_topic"></a>

The following code example shows how to send a text message to Anthropic Claude, using Bedrock's Converse API.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Anthropic Claude, using Bedrock's Converse API.

```
# Use the Conversation API to send a text message to Anthropic Claude.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Claude 3 Haiku.
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

### ConverseStream
<a name="bedrock-runtime_ConverseStream_AnthropicClaude_python_3_topic"></a>

The following code example shows how to send a text message to Anthropic Claude, using Bedrock's Converse API and process the response stream in real-time.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Anthropic Claude, using Bedrock's Converse API and process the response stream in real-time.

```
# Use the Conversation API to send a text message to Anthropic Claude
# and print the response stream.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Claude 3 Haiku.
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    streaming_response = client.converse_stream(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the streamed response text in real-time.
    for chunk in streaming_response["stream"]:
        if "contentBlockDelta" in chunk:
            text = chunk["contentBlockDelta"]["delta"]["text"]
            print(text, end="")

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [ConverseStream](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/ConverseStream) in *AWS SDK for Python (Boto3) API Reference*.

### Document understanding
<a name="bedrock-runtime_DocumentUnderstanding_AnthropicClaude_python_3_topic"></a>

The following code example shows how to send and process a document with Anthropic Claude on Amazon Bedrock.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send and process a document with Anthropic Claude on Amazon Bedrock.

```
# Send and process a document with Anthropic Claude on Amazon Bedrock.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g. Claude 3 Haiku.
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

# Load the document
with open("example-data/amazon-nova-service-cards.pdf", "rb") as file:
    document_bytes = file.read()

# Start a conversation with a user message and the document
conversation = [
    {
        "role": "user",
        "content": [
            {"text": "Briefly compare the models described in this document"},
            {
                "document": {
                    # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                    "format": "pdf",
                    "name": "Amazon Nova Service Cards",
                    "source": {"bytes": document_bytes},
                }
            },
        ],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 500, "temperature": 0.3},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

### Scenario: Tool use with the Converse API
<a name="bedrock-runtime_Scenario_ToolUseDemo_AnthropicClaude_python_3_topic"></a>

The following code example shows how to build a typical interaction between an application, a generative AI model, and connected tools or APIs to mediate interactions between the AI and the outside world. It uses the example of connecting an external weather API to the AI model so it can provide real-time weather information based on user input.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
The primary execution script of the demo. This script orchestrates the conversation between the user, the Amazon Bedrock Converse API, and a weather tool.

```
"""
This demo illustrates a tool use scenario using Amazon Bedrock's Converse API and a weather tool.
The script interacts with a foundation model on Amazon Bedrock to provide weather information based on user
input. It uses the Open-Meteo API (https://open-meteo.com) to retrieve current weather data for a given location.
"""

import boto3
import logging
from enum import Enum

import utils.tool_use_print_utils as output
import weather_tool

logging.basicConfig(level=logging.INFO, format="%(message)s")

AWS_REGION = "us-east-1"

# For the most recent list of models supported by the Converse API's tool use functionality, visit:
# https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html
class SupportedModels(Enum):
    CLAUDE_OPUS = "anthropic.claude-3-opus-20240229-v1:0"
    CLAUDE_SONNET = "anthropic.claude-3-sonnet-20240229-v1:0"
    CLAUDE_HAIKU = "anthropic.claude-3-haiku-20240307-v1:0"
    COHERE_COMMAND_R = "cohere.command-r-v1:0"
    COHERE_COMMAND_R_PLUS = "cohere.command-r-plus-v1:0"

# Set the model ID, e.g., Claude 3 Haiku.
MODEL_ID = SupportedModels.CLAUDE_HAIKU.value

SYSTEM_PROMPT = """
You are a weather assistant that provides current weather data for user-specified locations using only
the Weather_Tool, which expects latitude and longitude. Infer the coordinates from the location yourself.
If the user provides coordinates, infer the approximate location and refer to it in your response.
To use the tool, you strictly apply the provided tool specification.

- Explain your step-by-step process, and give brief updates before each step.
- Only use the Weather_Tool for data. Never guess or make up information.
- Repeat the tool use for subsequent requests if necessary.
- If the tool errors, apologize, explain weather is unavailable, and suggest other options.
- Report temperatures in °C (°F) and wind in km/h (mph). Keep weather reports concise. Sparingly use
  emojis where appropriate.
- Only respond to weather queries. Remind off-topic users of your purpose.
- Never claim to search online, access external data, or use tools besides Weather_Tool.
- Complete the entire process until you have all required data before sending the complete response.
"""

# The maximum number of recursive calls allowed in the tool_use_demo function.
# This helps prevent infinite loops and potential performance issues.
MAX_RECURSIONS = 5

class ToolUseDemo:
    """
    Demonstrates the tool use feature with the Amazon Bedrock Converse API.
    """

    def __init__(self):
        # Prepare the system prompt
        self.system_prompt = [{"text": SYSTEM_PROMPT}]

        # Prepare the tool configuration with the weather tool's specification
        self.tool_config = {"tools": [weather_tool.get_tool_spec()]}

        # Create a Bedrock Runtime client in the specified AWS Region.
        self.bedrockRuntimeClient = boto3.client(
            "bedrock-runtime", region_name=AWS_REGION
        )

    def run(self):
        """
        Starts the conversation with the user and handles the interaction with Bedrock.
        """
        # Print the greeting and a short user guide
        output.header()

        # Start with an emtpy conversation
        conversation = []

        # Get the first user input
        user_input = self._get_user_input()

        while user_input is not None:
            # Create a new message with the user input and append it to the conversation
            message = {"role": "user", "content": [{"text": user_input}]}
            conversation.append(message)

            # Send the conversation to Amazon Bedrock
            bedrock_response = self._send_conversation_to_bedrock(conversation)

            # Recursively handle the model's response until the model has returned
            # its final response or the recursion counter has reached 0
            self._process_model_response(
                bedrock_response, conversation, max_recursion=MAX_RECURSIONS
            )

            # Repeat the loop until the user decides to exit the application
            user_input = self._get_user_input()

        output.footer()

    def _send_conversation_to_bedrock(self, conversation):
        """
        Sends the conversation, the system prompt, and the tool spec to Amazon Bedrock, and returns the response.

        :param conversation: The conversation history including the next message to send.
        :return: The response from Amazon Bedrock.
        """
        output.call_to_bedrock(conversation)

        # Send the conversation, system prompt, and tool configuration, and return the response
        return self.bedrockRuntimeClient.converse(
            modelId=MODEL_ID,
            messages=conversation,
            system=self.system_prompt,
            toolConfig=self.tool_config,
        )

    def _process_model_response(
        self, model_response, conversation, max_recursion=MAX_RECURSIONS
    ):
        """
        Processes the response received via Amazon Bedrock and performs the necessary actions
        based on the stop reason.

        :param model_response: The model's response returned via Amazon Bedrock.
        :param conversation: The conversation history.
        :param max_recursion: The maximum number of recursive calls allowed.
        """

        if max_recursion <= 0:
            # Stop the process, the number of recursive calls could indicate an infinite loop
            logging.warning(
                "Warning: Maximum number of recursions reached. Please try again."
            )
            exit(1)

        # Append the model's response to the ongoing conversation
        message = model_response["output"]["message"]
        conversation.append(message)

        if model_response["stopReason"] == "tool_use":
            # If the stop reason is "tool_use", forward everything to the tool use handler
            self._handle_tool_use(message, conversation, max_recursion)

        if model_response["stopReason"] == "end_turn":
            # If the stop reason is "end_turn", print the model's response text, and finish the process
            output.model_response(message["content"][0]["text"])
            return

    def _handle_tool_use(
        self, model_response, conversation, max_recursion=MAX_RECURSIONS
    ):
        """
        Handles the tool use case by invoking the specified tool and sending the tool's response back to Bedrock.
        The tool response is appended to the conversation, and the conversation is sent back to Amazon Bedrock for further processing.

        :param model_response: The model's response containing the tool use request.
        :param conversation: The conversation history.
        :param max_recursion: The maximum number of recursive calls allowed.
        """

        # Initialize an empty list of tool results
        tool_results = []

        # The model's response can consist of multiple content blocks
        for content_block in model_response["content"]:
            if "text" in content_block:
                # If the content block contains text, print it to the console
                output.model_response(content_block["text"])

            if "toolUse" in content_block:
                # If the content block is a tool use request, forward it to the tool
                tool_response = self._invoke_tool(content_block["toolUse"])

                # Add the tool use ID and the tool's response to the list of results
                tool_results.append(
                    {
                        "toolResult": {
                            "toolUseId": (tool_response["toolUseId"]),
                            "content": [{"json": tool_response["content"]}],
                        }
                    }
                )

        # Embed the tool results in a new user message
        message = {"role": "user", "content": tool_results}

        # Append the new message to the ongoing conversation
        conversation.append(message)

        # Send the conversation to Amazon Bedrock
        response = self._send_conversation_to_bedrock(conversation)

        # Recursively handle the model's response until the model has returned
        # its final response or the recursion counter has reached 0
        self._process_model_response(response, conversation, max_recursion - 1)

    def _invoke_tool(self, payload):
        """
        Invokes the specified tool with the given payload and returns the tool's response.
        If the requested tool does not exist, an error message is returned.

        :param payload: The payload containing the tool name and input data.
        :return: The tool's response or an error message.
        """
        tool_name = payload["name"]

        if tool_name == "Weather_Tool":
            input_data = payload["input"]
            output.tool_use(tool_name, input_data)

            # Invoke the weather tool with the input data provided by
            response = weather_tool.fetch_weather_data(input_data)
        else:
            error_message = (
                f"The requested tool with name '{tool_name}' does not exist."
            )
            response = {"error": "true", "message": error_message}

        return {"toolUseId": payload["toolUseId"], "content": response}

    @staticmethod
    def _get_user_input(prompt="Your weather info request"):
        """
        Prompts the user for input and returns the user's response.
        Returns None if the user enters 'x' to exit.

        :param prompt: The prompt to display to the user.
        :return: The user's input or None if the user chooses to exit.
        """
        output.separator()
        user_input = input(f"{prompt} (x to exit): ")

        if user_input == "":
            prompt = "Please enter your weather info request, e.g. the name of a city"
            return ToolUseDemo._get_user_input(prompt)

        elif user_input.lower() == "x":
            return None

        else:
            return user_input

if __name__ == "__main__":
    tool_use_demo = ToolUseDemo()
    tool_use_demo.run()
```
The weather tool used by the demo. This script defines the tool specification and implements the logic to retrieve weather data using from the Open-Meteo API.

```
import requests
from requests.exceptions import RequestException

def get_tool_spec():
    """
    Returns the JSON Schema specification for the Weather tool. The tool specification
    defines the input schema and describes the tool's functionality.
    For more information, see https://json-schema.org/understanding-json-schema/reference.

    :return: The tool specification for the Weather tool.
    """
    return {
        "toolSpec": {
            "name": "Weather_Tool",
            "description": "Get the current weather for a given location, based on its WGS84 coordinates.",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "latitude": {
                            "type": "string",
                            "description": "Geographical WGS84 latitude of the location.",
                        },
                        "longitude": {
                            "type": "string",
                            "description": "Geographical WGS84 longitude of the location.",
                        },
                    },
                    "required": ["latitude", "longitude"],
                }
            },
        }
    }

def fetch_weather_data(input_data):
    """
    Fetches weather data for the given latitude and longitude using the Open-Meteo API.
    Returns the weather data or an error message if the request fails.

    :param input_data: The input data containing the latitude and longitude.
    :return: The weather data or an error message.
    """
    endpoint = "https://api.open-meteo.com/v1/forecast"
    latitude = input_data.get("latitude")
    longitude = input_data.get("longitude", "")
    params = {"latitude": latitude, "longitude": longitude, "current_weather": True}

    try:
        response = requests.get(endpoint, params=params)
        weather_data = {"weather_data": response.json()}
        response.raise_for_status()
        return weather_data
    except RequestException as e:
        return e.response.json()
    except Exception as e:
        return {"error": type(e), "message": str(e)}
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

## Cohere Command
<a name="cohere_command"></a>

### Converse
<a name="bedrock-runtime_Converse_CohereCommand_python_3_topic"></a>

The following code example shows how to send a text message to Cohere Command, using Bedrock's Converse API.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Cohere Command, using Bedrock's Converse API.

```
# Use the Conversation API to send a text message to Cohere Command.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Command R.
model_id = "cohere.command-r-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

### ConverseStream
<a name="bedrock-runtime_ConverseStream_CohereCommand_python_3_topic"></a>

The following code example shows how to send a text message to Cohere Command, using Bedrock's Converse API and process the response stream in real-time.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Cohere Command, using Bedrock's Converse API and process the response stream in real-time.

```
# Use the Conversation API to send a text message to Cohere Command
# and print the response stream.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Command R.
model_id = "cohere.command-r-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    streaming_response = client.converse_stream(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the streamed response text in real-time.
    for chunk in streaming_response["stream"]:
        if "contentBlockDelta" in chunk:
            text = chunk["contentBlockDelta"]["delta"]["text"]
            print(text, end="")

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [ConverseStream](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/ConverseStream) in *AWS SDK for Python (Boto3) API Reference*.

### Document understanding
<a name="bedrock-runtime_DocumentUnderstanding_CohereCommand_python_3_topic"></a>

The following code example shows how to send and process a document with Cohere Command models on Amazon Bedrock.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send and process a document with Cohere Command models on Amazon Bedrock.

```
# Send and process a document with Cohere Command models on Amazon Bedrock.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g. Command R+.
model_id = "cohere.command-r-plus-v1:0"

# Load the document
with open("example-data/amazon-nova-service-cards.pdf", "rb") as file:
    document_bytes = file.read()

# Start a conversation with a user message and the document
conversation = [
    {
        "role": "user",
        "content": [
            {"text": "Briefly compare the models described in this document"},
            {
                "document": {
                    # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                    "format": "pdf",
                    "name": "Amazon Nova Service Cards",
                    "source": {"bytes": document_bytes},
                }
            },
        ],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 500, "temperature": 0.3},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

### Scenario: Tool use with the Converse API
<a name="bedrock-runtime_Scenario_ToolUseDemo_CohereCommand_python_3_topic"></a>

The following code example shows how to build a typical interaction between an application, a generative AI model, and connected tools or APIs to mediate interactions between the AI and the outside world. It uses the example of connecting an external weather API to the AI model so it can provide real-time weather information based on user input.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
The primary execution script of the demo. This script orchestrates the conversation between the user, the Amazon Bedrock Converse API, and a weather tool.

```
"""
This demo illustrates a tool use scenario using Amazon Bedrock's Converse API and a weather tool.
The script interacts with a foundation model on Amazon Bedrock to provide weather information based on user
input. It uses the Open-Meteo API (https://open-meteo.com) to retrieve current weather data for a given location.
"""

import boto3
import logging
from enum import Enum

import utils.tool_use_print_utils as output
import weather_tool

logging.basicConfig(level=logging.INFO, format="%(message)s")

AWS_REGION = "us-east-1"

# For the most recent list of models supported by the Converse API's tool use functionality, visit:
# https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html
class SupportedModels(Enum):
    CLAUDE_OPUS = "anthropic.claude-3-opus-20240229-v1:0"
    CLAUDE_SONNET = "anthropic.claude-3-sonnet-20240229-v1:0"
    CLAUDE_HAIKU = "anthropic.claude-3-haiku-20240307-v1:0"
    COHERE_COMMAND_R = "cohere.command-r-v1:0"
    COHERE_COMMAND_R_PLUS = "cohere.command-r-plus-v1:0"

# Set the model ID, e.g., Claude 3 Haiku.
MODEL_ID = SupportedModels.CLAUDE_HAIKU.value

SYSTEM_PROMPT = """
You are a weather assistant that provides current weather data for user-specified locations using only
the Weather_Tool, which expects latitude and longitude. Infer the coordinates from the location yourself.
If the user provides coordinates, infer the approximate location and refer to it in your response.
To use the tool, you strictly apply the provided tool specification.

- Explain your step-by-step process, and give brief updates before each step.
- Only use the Weather_Tool for data. Never guess or make up information.
- Repeat the tool use for subsequent requests if necessary.
- If the tool errors, apologize, explain weather is unavailable, and suggest other options.
- Report temperatures in °C (°F) and wind in km/h (mph). Keep weather reports concise. Sparingly use
  emojis where appropriate.
- Only respond to weather queries. Remind off-topic users of your purpose.
- Never claim to search online, access external data, or use tools besides Weather_Tool.
- Complete the entire process until you have all required data before sending the complete response.
"""

# The maximum number of recursive calls allowed in the tool_use_demo function.
# This helps prevent infinite loops and potential performance issues.
MAX_RECURSIONS = 5

class ToolUseDemo:
    """
    Demonstrates the tool use feature with the Amazon Bedrock Converse API.
    """

    def __init__(self):
        # Prepare the system prompt
        self.system_prompt = [{"text": SYSTEM_PROMPT}]

        # Prepare the tool configuration with the weather tool's specification
        self.tool_config = {"tools": [weather_tool.get_tool_spec()]}

        # Create a Bedrock Runtime client in the specified AWS Region.
        self.bedrockRuntimeClient = boto3.client(
            "bedrock-runtime", region_name=AWS_REGION
        )

    def run(self):
        """
        Starts the conversation with the user and handles the interaction with Bedrock.
        """
        # Print the greeting and a short user guide
        output.header()

        # Start with an emtpy conversation
        conversation = []

        # Get the first user input
        user_input = self._get_user_input()

        while user_input is not None:
            # Create a new message with the user input and append it to the conversation
            message = {"role": "user", "content": [{"text": user_input}]}
            conversation.append(message)

            # Send the conversation to Amazon Bedrock
            bedrock_response = self._send_conversation_to_bedrock(conversation)

            # Recursively handle the model's response until the model has returned
            # its final response or the recursion counter has reached 0
            self._process_model_response(
                bedrock_response, conversation, max_recursion=MAX_RECURSIONS
            )

            # Repeat the loop until the user decides to exit the application
            user_input = self._get_user_input()

        output.footer()

    def _send_conversation_to_bedrock(self, conversation):
        """
        Sends the conversation, the system prompt, and the tool spec to Amazon Bedrock, and returns the response.

        :param conversation: The conversation history including the next message to send.
        :return: The response from Amazon Bedrock.
        """
        output.call_to_bedrock(conversation)

        # Send the conversation, system prompt, and tool configuration, and return the response
        return self.bedrockRuntimeClient.converse(
            modelId=MODEL_ID,
            messages=conversation,
            system=self.system_prompt,
            toolConfig=self.tool_config,
        )

    def _process_model_response(
        self, model_response, conversation, max_recursion=MAX_RECURSIONS
    ):
        """
        Processes the response received via Amazon Bedrock and performs the necessary actions
        based on the stop reason.

        :param model_response: The model's response returned via Amazon Bedrock.
        :param conversation: The conversation history.
        :param max_recursion: The maximum number of recursive calls allowed.
        """

        if max_recursion <= 0:
            # Stop the process, the number of recursive calls could indicate an infinite loop
            logging.warning(
                "Warning: Maximum number of recursions reached. Please try again."
            )
            exit(1)

        # Append the model's response to the ongoing conversation
        message = model_response["output"]["message"]
        conversation.append(message)

        if model_response["stopReason"] == "tool_use":
            # If the stop reason is "tool_use", forward everything to the tool use handler
            self._handle_tool_use(message, conversation, max_recursion)

        if model_response["stopReason"] == "end_turn":
            # If the stop reason is "end_turn", print the model's response text, and finish the process
            output.model_response(message["content"][0]["text"])
            return

    def _handle_tool_use(
        self, model_response, conversation, max_recursion=MAX_RECURSIONS
    ):
        """
        Handles the tool use case by invoking the specified tool and sending the tool's response back to Bedrock.
        The tool response is appended to the conversation, and the conversation is sent back to Amazon Bedrock for further processing.

        :param model_response: The model's response containing the tool use request.
        :param conversation: The conversation history.
        :param max_recursion: The maximum number of recursive calls allowed.
        """

        # Initialize an empty list of tool results
        tool_results = []

        # The model's response can consist of multiple content blocks
        for content_block in model_response["content"]:
            if "text" in content_block:
                # If the content block contains text, print it to the console
                output.model_response(content_block["text"])

            if "toolUse" in content_block:
                # If the content block is a tool use request, forward it to the tool
                tool_response = self._invoke_tool(content_block["toolUse"])

                # Add the tool use ID and the tool's response to the list of results
                tool_results.append(
                    {
                        "toolResult": {
                            "toolUseId": (tool_response["toolUseId"]),
                            "content": [{"json": tool_response["content"]}],
                        }
                    }
                )

        # Embed the tool results in a new user message
        message = {"role": "user", "content": tool_results}

        # Append the new message to the ongoing conversation
        conversation.append(message)

        # Send the conversation to Amazon Bedrock
        response = self._send_conversation_to_bedrock(conversation)

        # Recursively handle the model's response until the model has returned
        # its final response or the recursion counter has reached 0
        self._process_model_response(response, conversation, max_recursion - 1)

    def _invoke_tool(self, payload):
        """
        Invokes the specified tool with the given payload and returns the tool's response.
        If the requested tool does not exist, an error message is returned.

        :param payload: The payload containing the tool name and input data.
        :return: The tool's response or an error message.
        """
        tool_name = payload["name"]

        if tool_name == "Weather_Tool":
            input_data = payload["input"]
            output.tool_use(tool_name, input_data)

            # Invoke the weather tool with the input data provided by
            response = weather_tool.fetch_weather_data(input_data)
        else:
            error_message = (
                f"The requested tool with name '{tool_name}' does not exist."
            )
            response = {"error": "true", "message": error_message}

        return {"toolUseId": payload["toolUseId"], "content": response}

    @staticmethod
    def _get_user_input(prompt="Your weather info request"):
        """
        Prompts the user for input and returns the user's response.
        Returns None if the user enters 'x' to exit.

        :param prompt: The prompt to display to the user.
        :return: The user's input or None if the user chooses to exit.
        """
        output.separator()
        user_input = input(f"{prompt} (x to exit): ")

        if user_input == "":
            prompt = "Please enter your weather info request, e.g. the name of a city"
            return ToolUseDemo._get_user_input(prompt)

        elif user_input.lower() == "x":
            return None

        else:
            return user_input

if __name__ == "__main__":
    tool_use_demo = ToolUseDemo()
    tool_use_demo.run()
```
The weather tool used by the demo. This script defines the tool specification and implements the logic to retrieve weather data using from the Open-Meteo API.

```
import requests
from requests.exceptions import RequestException

def get_tool_spec():
    """
    Returns the JSON Schema specification for the Weather tool. The tool specification
    defines the input schema and describes the tool's functionality.
    For more information, see https://json-schema.org/understanding-json-schema/reference.

    :return: The tool specification for the Weather tool.
    """
    return {
        "toolSpec": {
            "name": "Weather_Tool",
            "description": "Get the current weather for a given location, based on its WGS84 coordinates.",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "latitude": {
                            "type": "string",
                            "description": "Geographical WGS84 latitude of the location.",
                        },
                        "longitude": {
                            "type": "string",
                            "description": "Geographical WGS84 longitude of the location.",
                        },
                    },
                    "required": ["latitude", "longitude"],
                }
            },
        }
    }

def fetch_weather_data(input_data):
    """
    Fetches weather data for the given latitude and longitude using the Open-Meteo API.
    Returns the weather data or an error message if the request fails.

    :param input_data: The input data containing the latitude and longitude.
    :return: The weather data or an error message.
    """
    endpoint = "https://api.open-meteo.com/v1/forecast"
    latitude = input_data.get("latitude")
    longitude = input_data.get("longitude", "")
    params = {"latitude": latitude, "longitude": longitude, "current_weather": True}

    try:
        response = requests.get(endpoint, params=params)
        weather_data = {"weather_data": response.json()}
        response.raise_for_status()
        return weather_data
    except RequestException as e:
        return e.response.json()
    except Exception as e:
        return {"error": type(e), "message": str(e)}
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

## DeepSeek
<a name="deepseek"></a>

### Document understanding
<a name="bedrock-runtime_DocumentUnderstanding_DeepSeek_python_3_topic"></a>

The following code example shows how to send and process a document with DeepSeek on Amazon Bedrock.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send and process a document with DeepSeek on Amazon Bedrock.

```
# Send and process a document with DeepSeek on Amazon Bedrock.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g. DeepSeek-R1
model_id = "us.deepseek.r1-v1:0"

# Load the document
with open("example-data/amazon-nova-service-cards.pdf", "rb") as file:
    document_bytes = file.read()

# Start a conversation with a user message and the document
conversation = [
    {
        "role": "user",
        "content": [
            {"text": "Briefly compare the models described in this document"},
            {
                "document": {
                    # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                    "format": "pdf",
                    "name": "Amazon Nova Service Cards",
                    "source": {"bytes": document_bytes},
                }
            },
        ],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 2000, "temperature": 0.3},
    )

    # Extract and print the reasoning and response text.
    reasoning, response_text = "", ""
    for item in response["output"]["message"]["content"]:
        for key, value in item.items():
            if key == "reasoningContent":
                reasoning = value["reasoningText"]["text"]
            elif key == "text":
                response_text = value

    print(f"\nReasoning:\n{reasoning}")
    print(f"\nResponse:\n{response_text}")

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

## Meta Llama
<a name="meta_llama"></a>

### Converse
<a name="bedrock-runtime_Converse_MetaLlama_python_3_topic"></a>

The following code example shows how to send a text message to Meta Llama, using Bedrock's Converse API.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Meta Llama, using Bedrock's Converse API.

```
# Use the Conversation API to send a text message to Meta Llama.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Llama 3 8b Instruct.
model_id = "meta.llama3-8b-instruct-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

### ConverseStream
<a name="bedrock-runtime_ConverseStream_MetaLlama_python_3_topic"></a>

The following code example shows how to send a text message to Meta Llama, using Bedrock's Converse API and process the response stream in real-time.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Meta Llama, using Bedrock's Converse API and process the response stream in real-time.

```
# Use the Conversation API to send a text message to Meta Llama
# and print the response stream.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Llama 3 8b Instruct.
model_id = "meta.llama3-8b-instruct-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    streaming_response = client.converse_stream(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the streamed response text in real-time.
    for chunk in streaming_response["stream"]:
        if "contentBlockDelta" in chunk:
            text = chunk["contentBlockDelta"]["delta"]["text"]
            print(text, end="")

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [ConverseStream](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/ConverseStream) in *AWS SDK for Python (Boto3) API Reference*.

### Document understanding
<a name="bedrock-runtime_DocumentUnderstanding_MetaLlama_python_3_topic"></a>

The following code example shows how to send and process a document with Llama on Amazon Bedrock.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send and process a document with Llama on Amazon Bedrock.

```
# Send and process a document with Llama on Amazon Bedrock.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g. Llama 3.1 8B Instruct.
model_id = "us.meta.llama3-1-8b-instruct-v1:0"

# Load the document
with open("example-data/amazon-nova-service-cards.pdf", "rb") as file:
    document_bytes = file.read()

# Start a conversation with a user message and the document
conversation = [
    {
        "role": "user",
        "content": [
            {"text": "Briefly compare the models described in this document"},
            {
                "document": {
                    # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                    "format": "pdf",
                    "name": "Amazon Nova Service Cards",
                    "source": {"bytes": document_bytes},
                }
            },
        ],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 500, "temperature": 0.3},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

## Mistral AI
<a name="mistral_ai"></a>

### Converse
<a name="bedrock-runtime_Converse_Mistral_python_3_topic"></a>

The following code example shows how to send a text message to Mistral, using Bedrock's Converse API.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Mistral, using Bedrock's Converse API.

```
# Use the Conversation API to send a text message to Mistral.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Mistral Large.
model_id = "mistral.mistral-large-2402-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

### ConverseStream
<a name="bedrock-runtime_ConverseStream_Mistral_python_3_topic"></a>

The following code example shows how to send a text message to Mistral, using Bedrock's Converse API and process the response stream in real-time.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send a text message to Mistral, using Bedrock's Converse API and process the response stream in real-time.

```
# Use the Conversation API to send a text message to Mistral
# and print the response stream.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Mistral Large.
model_id = "mistral.mistral-large-2402-v1:0"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    streaming_response = client.converse_stream(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the streamed response text in real-time.
    for chunk in streaming_response["stream"]:
        if "contentBlockDelta" in chunk:
            text = chunk["contentBlockDelta"]["delta"]["text"]
            print(text, end="")

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [ConverseStream](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/ConverseStream) in *AWS SDK for Python (Boto3) API Reference*.

### Document understanding
<a name="bedrock-runtime_DocumentUnderstanding_Mistral_python_3_topic"></a>

The following code example shows how to send and process a document with Mistral models on Amazon Bedrock.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Send and process a document with Mistral models on Amazon Bedrock.

```
# Send and process a document with Mistral models on Amazon Bedrock.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Mistral Large.
model_id = "mistral.mistral-large-2402-v1:0"

# Load the document
with open("example-data/amazon-nova-service-cards.pdf", "rb") as file:
    document_bytes = file.read()

# Start a conversation with a user message and the document
conversation = [
    {
        "role": "user",
        "content": [
            {"text": "Briefly compare the models described in this document"},
            {
                "document": {
                    # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                    "format": "pdf",
                    "name": "Amazon Nova Service Cards",
                    "source": {"bytes": document_bytes},
                }
            },
        ],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 500, "temperature": 0.3},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for Python (Boto3) API Reference*.

## Stable Image Core
<a name="stable_image_core"></a>

### InvokeModel
<a name="bedrock-runtime_InvokeModel_StableDiffusion_python_3_topic"></a>

The following code example shows how to invoke Stability.ai Stable Image Core on Amazon Bedrock to generate an image.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime#code-examples).
Create an image with Stable Diffusion.

```
# Use the native inference API to create an image with Stability AI Stable Image Core

import base64
import boto3
import json
import os
import random

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-west-2")

# Set the model ID, e.g., Stable Image Core.
model_id = "stability.stable-image-core-v1:1"

# Define the image generation prompt for the model.
prompt = "A stylized picture of a cute old steampunk robot."

# Generate a random seed.
seed = random.randint(0, 4294967295)

# Format the request payload using the model's native structure.
native_request = {
    "prompt": prompt,
    "aspect_ratio": "1:1",
    "seed": seed,
    "output_format": "png",
}

# Convert the native request to JSON.
request = json.dumps(native_request)

# Invoke the model with the request.
response = client.invoke_model(modelId=model_id, body=request)

# Decode the response body.
model_response = json.loads(response["body"].read())

# Extract the image data.
base64_image_data = model_response["images"][0]

# Save the generated image to a local folder.
i, output_dir = 1, "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
while os.path.exists(os.path.join(output_dir, f"stability_{i}.png")):
    i += 1

image_data = base64.b64decode(base64_image_data)

image_path = os.path.join(output_dir, f"stability_{i}.png")
with open(image_path, "wb") as file:
    file.write(image_data)

print(f"The generated image has been saved to {image_path}")
```
+  For API details, see [InvokeModel](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/InvokeModel) in *AWS SDK for Python (Boto3) API Reference*.
