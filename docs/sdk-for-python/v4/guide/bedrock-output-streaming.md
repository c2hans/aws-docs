---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/bedrock-output-streaming.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use ConverseStream

ConverseStream accepts the same request format as Converse but returns the response as a stream of events. Your application can process output as the model generates it instead of waiting for the complete response. Use it for interactive applications, such as chat, where users should start seeing text as soon as the model begins its reply.

The following example uses the asynchronous client to send one request, print the reply as the model generates it, and then verify that the stream completed. For request and response details, see the [converse\_stream()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/bedrock-runtime/operations/converse_stream/) API reference.

 **Imports**

```
import asyncio
from typing import Any

from aws_sdk_bedrock_runtime import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.models import (
    ContentBlockDeltaText,
    ConverseStreamOutputContentBlockDelta,
    ConverseStreamOutputContentBlockStart,
    ConverseStreamOutputContentBlockStop,
    ConverseStreamOutputMessageStart,
    ConverseStreamOutputMessageStop,
    ConverseStreamOutputMetadata,
    ConverseStreamOutputUnknown,
    TokenUsage,
)
```

`converse_stream` returns the response as a stream of events over an open network connection. The following function reads the events inside an `async with` block, which closes the connection when the stream ends or an error interrupts it. It narrows every generated event union, collects the text deltas, and raises an error for an unknown variant instead of accepting partial output. If the service sends a modeled error event, the `async for` loop raises the generated exception, such as `ThrottlingException` from `aws_sdk_bedrock_runtime.models`. The message-stop event carries the stop reason. The metadata event carries the token usage. The function requires both events before it accepts the accumulated text as complete.

```
async def consume_stream(response: Any) -> tuple[str, str, TokenUsage]:
    """Consume a Converse stream and reject errors or incomplete output."""
    text_parts: list[str] = []
    stop_reason: str | None = None
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
            elif isinstance(event, ConverseStreamOutputUnknown):
                raise RuntimeError(f"Unknown stream event: {event.tag}")
            else:
                raise RuntimeError(f"Unexpected stream event: {type(event).__name__}")

    if not text_parts or stop_reason is None or usage is None:
        raise RuntimeError("The stream ended without all expected events")
    return "".join(text_parts), stop_reason, usage
```

The following function calls `converse_stream` with the same keyword arguments that `converse` takes, then reads the returned stream with `consume_stream`.

 **Code**

```
async def converse_stream(
    client: AsyncBedrockRuntimeClient,
) -> tuple[str, str, TokenUsage]:
    """Send a ConverseStream request and consume its complete response."""
    model_id = "global.amazon.nova-2-lite-v1:0"
    prompt = "Name one moon of Saturn."

    response = await client.converse_stream(
        model_id=model_id,
        messages=[{"role": "user", "content": [{"text": prompt}]}],
    )
    text, stop_reason, usage = await consume_stream(response)
    print(f"\nstop reason: {stop_reason}")
    print(f"tokens: {usage.input_tokens} input, {usage.output_tokens} output")
    return text, stop_reason, usage
```

The entry point creates an asynchronous client with `create_async_client` and runs the streaming request. Run the program with `python converse_stream.py`.

```
async def main() -> None:
    """Create an asynchronous client and run the example."""
    client = await create_async_client()
    async with client:
        await converse_stream(client)

if __name__ == "__main__":
    asyncio.run(main())
```

## More information
<a name="bedrock-output-streaming-more-info"></a>
+ [Use the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html) in the Amazon Bedrock User Guide
+ [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) in the Amazon Bedrock API Reference
