---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/bedrock-converse.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use Converse
<a name="bedrock-converse"></a>

Converse is the portable conversation API for Amazon Bedrock Runtime. A conversation is a list of *messages*, each with a role and a list of typed *content blocks*. Use it when you want one request format that works across supported models, so you can switch models without rewriting request code.

The following example runs a complete two-turn conversation. For request and response details, see the [converse()](clients/bedrock-runtime/operations/converse/) API reference.

 **Imports**

```
import asyncio

from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import AsyncBedrockRuntimeConfig
from aws_sdk_bedrock_runtime.models import (
    ContentBlockText,
    ConverseInput,
    ConverseOutputMessage,
    InferenceConfiguration,
    Message,
)
```

The generated `output` member is a union. Narrow it to `ConverseOutputMessage` before using `.value`. Each message content block is also a union, so narrow text blocks before reading their values. The following helper functions fail when the response carries no message and when it contains no text content.

```
def narrow_message(response: object) -> Message:
    """Narrow a Converse output union and return its message."""
    output = getattr(response, "output", None)
    if not isinstance(output, ConverseOutputMessage):
        raise RuntimeError(f"Unexpected Converse output: {type(output).__name__}")
    return output.value

def message_text(message: Message) -> str:
    """Collect text only after narrowing every content-block union."""
    text = "".join(
        block.value for block in message.content if isinstance(block, ContentBlockText)
    )
    if not text:
        raise RuntimeError("The model returned no text content")
    return text
```

Create a user `Message` with a text content-block union and pass it to `converse`. Common generation settings belong in `InferenceConfiguration`. Bedrock Runtime does not retain conversation history between calls, so for the second turn the code appends the narrowed assistant message and the next user message, then sends the complete history.

The code also prints the response's `stop_reason` and `usage` fields. The `stop_reason` field reports why the model stopped generating. For example, `end_turn` means the model finished its reply normally, and `max_tokens` means the reply was cut off at the `max_tokens` limit. The `usage` field reports the input and output token counts that inference is billed on.

 **Code**

```
async def converse(client: AsyncBedrockRuntimeClient) -> tuple[str, str]:
    """Run a complete two-turn conversation and return both assistant replies."""
    model_id = "global.amazon.nova-2-lite-v1:0"
    prompt = "Name one moon of Saturn."

    messages = [Message(role="user", content=[ContentBlockText(value=prompt)])]
    response = await client.converse(
        ConverseInput(
            model_id=model_id,
            messages=messages,
            inference_config=InferenceConfiguration(
                max_tokens=100,
                temperature=0.2,
                top_p=0.9,
            ),
        )
    )

    assistant_message = narrow_message(response)
    first_text = message_text(assistant_message)
    print(first_text)
    print(f"stop reason: {response.stop_reason}")
    print(
        f"tokens: {response.usage.input_tokens} input, "
        f"{response.usage.output_tokens} output"
    )

    # Bedrock does not retain history, so include every preceding message.
    follow_up_prompt = "Name another one."

    messages.extend(
        [
            assistant_message,
            Message(
                role="user",
                content=[ContentBlockText(value=follow_up_prompt)],
            ),
        ]
    )
    second_response = await client.converse(
        ConverseInput(model_id=model_id, messages=messages)
    )
    second_text = message_text(narrow_message(second_response))
    print(second_text)
    return first_text, second_text
```

The entry point creates the client and runs the conversation. Run the program with `python converse.py`.

```
async def main() -> None:
    """Create a client in a Region that offers the model and run the example."""
    config = await AsyncBedrockRuntimeConfig.resolve(region="us-east-1")
    async with AsyncBedrockRuntimeClient(config=config) as client:
        await converse(client)

if __name__ == "__main__":
    asyncio.run(main())
```

## More information
<a name="bedrock-converse-more-info"></a>
+ [Use the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html) in the Amazon Bedrock User Guide
+ [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) in the Amazon Bedrock API Reference
