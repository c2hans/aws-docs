---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/bedrock-converse.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use Converse
<a name="bedrock-converse"></a>

Converse is the portable conversation API for Amazon Bedrock Runtime. A conversation is a list of *messages*, each with a role and a list of typed *content blocks*. Use it when you want one request format that works across supported models, so you can switch models without rewriting request code.

The following example uses the synchronous client to run a complete two-turn conversation. For request and response details, see the [converse()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/bedrock-runtime/operations/converse/) API reference.

 **Imports**

```
from aws_sdk_bedrock_runtime import BedrockRuntimeClient
from aws_sdk_bedrock_runtime.models import (
    ContentBlockText,
    ConverseOutputMessage,
    Message,
    MessageDict,
)
```

The generated `output` member is a union. Narrow it to `ConverseOutputMessage` before using `.value`. Each message content block is also a union, so narrow text blocks before reading their values. The following helper functions raise an error when the response has no message or the message has no text content.

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

Pass the model ID and the conversation to `converse` as the `model_id` and `messages` keyword arguments. Each message is a dictionary with a role and a list of content blocks. A text content block is a dictionary with a single `"text"` key. To set common generation settings, such as the token limit and temperature, pass a dictionary as `inference_config`. Bedrock Runtime doesn't keep conversation history between calls. For the second turn, the code appends the narrowed assistant message and the next user message, then sends the complete history. The assistant message is the generated `Message` object from the response, so the `messages` list is annotated as `list[Message | MessageDict]`.

The code also prints the response's `stop_reason` and `usage` fields. The `stop_reason` field reports why the model stopped generating. For example, `end_turn` means the model finished its reply normally. A value of `max_tokens` means the reply was cut off at the `max_tokens` limit. The `usage` field reports the input and output token counts that inference is billed on.

 **Code**

```
def converse(client: BedrockRuntimeClient) -> tuple[str, str]:
    """Run a complete two-turn conversation and return both assistant replies."""
    model_id = "global.amazon.nova-2-lite-v1:0"
    prompt = "Name one moon of Saturn."

    messages: list[Message | MessageDict] = [
        {"role": "user", "content": [{"text": prompt}]}
    ]
    response = client.converse(
        model_id=model_id,
        messages=messages,
        inference_config={
            "max_tokens": 100,
            "temperature": 0.2,
            "top_p": 0.9,
        },
    )

    assistant_message = narrow_message(response)
    first_text = message_text(assistant_message)
    print(first_text)
    print(f"stop reason: {response.stop_reason}")
    print(
        f"tokens: {response.usage.input_tokens} input, "
        f"{response.usage.output_tokens} output"
    )

    # Bedrock doesn't keep history, so include every preceding message.
    follow_up_prompt = "Name another one."

    messages.extend(
        [
            assistant_message,
            {"role": "user", "content": [{"text": follow_up_prompt}]},
        ]
    )
    second_response = client.converse(model_id=model_id, messages=messages)
    second_text = message_text(narrow_message(second_response))
    print(second_text)
    return first_text, second_text
```

The entry point creates a synchronous client with `create_client` and runs the conversation. Run the program with `python converse.py`.

```
def main() -> None:
    """Create a synchronous client and run the example."""
    with create_client() as client:
        converse(client)

if __name__ == "__main__":
    main()
```

## More information
<a name="bedrock-converse-more-info"></a>
+ [Use the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html) in the Amazon Bedrock User Guide
+ [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) in the Amazon Bedrock API Reference
