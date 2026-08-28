---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/bedrock-output-streaming.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use ConverseStream
<a name="bedrock-output-streaming"></a>

ConverseStream accepts the same request format as Converse but returns the response as a stream of events, so your application can process output as the model generates it instead of waiting for the complete response. Use it for interactive applications, such as chat, where users should start seeing text as soon as the model begins its reply.

The following example sends one request, prints the reply as the model generates it, and then verifies that the stream completed. For request and response details, see the [converse\_stream()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/bedrock-runtime/operations/converse_stream/) API reference.

 **Imports**

```
import asyncio
from typing import Any

from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import AsyncBedrockRuntimeConfig
from aws_sdk_bedrock_runtime.models import (
    ContentBlockDeltaText,
    ContentBlockText,
    ConverseStreamInput,
    ConverseStreamOutputContentBlockDelta,
    ConverseStreamOutputContentBlockStart,
    ConverseStreamOutputContentBlockStop,
    ConverseStreamOutputInternalServerException,
    ConverseStreamOutputMessageStart,
    ConverseStreamOutputMessageStop,
    ConverseStreamOutputMetadata,
    ConverseStreamOutputModelStreamErrorException,
    ConverseStreamOutputServiceUnavailableException,
    ConverseStreamOutputThrottlingException,
    ConverseStreamOutputUnknown,
    ConverseStreamOutputValidationException,
    Message,
    StopReason,
    TokenUsage,
)
```

Group the modeled stream-error events so that the event loop can treat every failure variant the same way.

```
STREAM_ERRORS = (
    ConverseStreamOutputInternalServerException,
    ConverseStreamOutputModelStreamErrorException,
    ConverseStreamOutputServiceUnavailableException,
    ConverseStreamOutputThrottlingException,
    ConverseStreamOutputValidationException,
)
```

`converse_stream` returns the response as a stream of events over an open network connection. The following function reads the events inside an `async with` block, which closes the connection when the stream ends or an error interrupts it. It narrows every generated event union, collects the text deltas, and raises on `STREAM_ERRORS` events and unknown variants instead of accepting partial output. The message-stop event carries the stop reason, and the metadata event carries the token usage. The function requires both events before it accepts the accumulated text as complete.

```
async def consume_stream(response: Any) -> tuple[str, StopReason, TokenUsage]:
    """Consume a Converse stream and reject errors or incomplete output."""
    text_parts: list[str] = []
    stop_reason: StopReason | None = None
    usage: TokenUsage | None = None

    async with response as stream:
        async for event in stream.output_stream:
            if isinstance(event, ConverseStreamOutputMessageStart):
                print(f"assistant role: {event.value.role}")
            elif isinstance(event, ConverseStreamOutputContentBlockStart):
                print(f"content block {event.value.content_block_index} started")
            elif isinstance(event, ConverseStreamOutputContentBlockDelta):
                delta = event.value.delta
                if isinstance(delta, ContentBlockDeltaText):
                    text_parts.append(delta.value)
                    print(delta.value, end="", flush=True)
            elif isinstance(event, ConverseStreamOutputContentBlockStop):
                print(f"\ncontent block {event.value.content_block_index} stopped")
            elif isinstance(event, ConverseStreamOutputMessageStop):
                stop_reason = event.value.stop_reason
            elif isinstance(event, ConverseStreamOutputMetadata):
                usage = event.value.usage
            elif isinstance(event, STREAM_ERRORS):
                raise RuntimeError(event.value.message or type(event).__name__)
            elif isinstance(event, ConverseStreamOutputUnknown):
                raise RuntimeError(f"Unknown stream event: {event.tag}")
            else:
                raise RuntimeError(f"Unexpected stream event: {type(event).__name__}")

    if not text_parts or stop_reason is None or usage is None:
        raise RuntimeError("The stream ended without all expected events")
    return "".join(text_parts), stop_reason, usage
```

The following function sends one complete Converse request and hands the response to `consume_stream`.

 **Code**

```
async def converse_stream(
    client: AsyncBedrockRuntimeClient,
) -> tuple[str, StopReason, TokenUsage]:
    """Send a ConverseStream request and consume its complete response."""
    model_id = "global.amazon.nova-2-lite-v1:0"
    prompt = "Name one moon of Saturn."

    response = await client.converse_stream(
        ConverseStreamInput(
            model_id=model_id,
            messages=[
                Message(
                    role="user",
                    content=[ContentBlockText(value=prompt)],
                )
            ],
        )
    )
    text, stop_reason, usage = await consume_stream(response)
    print(f"\nstop reason: {stop_reason}")
    print(f"tokens: {usage.input_tokens} input, {usage.output_tokens} output")
    return text, stop_reason, usage
```

The entry point creates the client and runs the streaming request. Run the program with `python converse_stream.py`.

```
async def main() -> None:
    """Create a client in a Region that offers the model and run the example."""
    config = await AsyncBedrockRuntimeConfig.resolve(region="us-east-1")
    async with AsyncBedrockRuntimeClient(config=config) as client:
        await converse_stream(client)

if __name__ == "__main__":
    asyncio.run(main())
```

## More information
<a name="bedrock-output-streaming-more-info"></a>
+ [Use the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html) in the Amazon Bedrock User Guide
+ [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) in the Amazon Bedrock API Reference

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
