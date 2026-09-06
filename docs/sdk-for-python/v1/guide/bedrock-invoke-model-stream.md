---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/bedrock-invoke-model-stream.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use InvokeModelWithResponseStream
<a name="bedrock-invoke-model-stream"></a>

InvokeModelWithResponseStream accepts the same model-native request format as InvokeModel but returns the response as a stream of model-native events, so your application can process output as the model generates it instead of waiting for the complete response. Use it for interactive applications that work in a model's native format. The request and event schemas depend on the selected model.

The following example sends one Amazon Nova 2 Messages API request, prints the reply as the model generates it, and then verifies that the stream completed. For request and response details, see the [invoke\_model\_with\_response\_stream()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/bedrock-runtime/operations/invoke_model_with_response_stream/) API reference.

 **Imports**

```
import asyncio
import json
from typing import Any

from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import AsyncBedrockRuntimeConfig
from aws_sdk_bedrock_runtime.models import (
    InvokeModelWithResponseStreamInput,
    ResponseStreamChunk,
    ResponseStreamInternalServerException,
    ResponseStreamModelStreamErrorException,
    ResponseStreamModelTimeoutException,
    ResponseStreamServiceUnavailableException,
    ResponseStreamThrottlingException,
    ResponseStreamUnknown,
    ResponseStreamValidationException,
)
```

The constants name the expected Amazon Nova 2 event types and the modeled stream-error events.

```
NOVA_EVENT_NAMES = {
    "messageStart",
    "contentBlockStart",
    "contentBlockDelta",
    "contentBlockStop",
    "messageStop",
    "metadata",
}
NATIVE_STREAM_ERRORS = (
    ResponseStreamInternalServerException,
    ResponseStreamModelStreamErrorException,
    ResponseStreamModelTimeoutException,
    ResponseStreamServiceUnavailableException,
    ResponseStreamThrottlingException,
    ResponseStreamValidationException,
)
```

The following helper builds the model-native request.

```
def build_native_request(prompt: str) -> dict[str, Any]:
    """Build an Amazon Nova 2 Messages API request."""
    return {
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "inferenceConfig": {"maxTokens": 100, "temperature": 0.2, "topP": 0.9},
    }
```

`invoke_model_with_response_stream` returns model-native JSON events over an open network connection. The following function reads the events inside an `async with` block, which closes the connection when the stream ends or an error interrupts it. It narrows every generated event union, validates every model-native JSON payload, collects the text deltas, and accepts output only if the model signaled a complete message and the stream finished without a modeled error.

```
async def consume_stream(response: Any) -> str:
    """Consume Nova JSON events and reject errors or incomplete output."""
    text_parts: list[str] = []
    saw_message_stop = False

    async with response as stream:
        async for event in stream.output_stream:
            if isinstance(event, ResponseStreamChunk):
                payload = event.value.bytes_
                if not payload:
                    continue
                chunk: Any = json.loads(payload.decode("utf-8"))
                if not isinstance(chunk, dict):
                    raise RuntimeError("The model returned a malformed native event")
                event_names = NOVA_EVENT_NAMES.intersection(chunk)
                if len(event_names) != 1:
                    raise RuntimeError("The model returned an unexpected native event")
                event_name = event_names.pop()
                if event_name == "messageStop":
                    saw_message_stop = True
                elif event_name == "contentBlockDelta":
                    block_delta = chunk[event_name]
                    delta = (
                        block_delta.get("delta")
                        if isinstance(block_delta, dict)
                        else None
                    )
                    if not isinstance(delta, dict):
                        raise RuntimeError("The model returned a malformed text delta")
                    text = delta.get("text")
                    if text is not None and not isinstance(text, str):
                        raise RuntimeError("The model returned a malformed text delta")
                    if text:
                        text_parts.append(text)
                        print(text, end="", flush=True)
            elif isinstance(event, NATIVE_STREAM_ERRORS):
                raise RuntimeError(event.value.message or type(event).__name__)
            elif isinstance(event, ResponseStreamUnknown):
                raise RuntimeError(f"Unknown native stream event: {event.tag}")
            else:
                raise RuntimeError(
                    f"Unexpected native stream event: {type(event).__name__}"
                )

    if not text_parts or not saw_message_stop:
        raise RuntimeError("The native stream ended without a complete text response")
    return "".join(text_parts)
```

Serialize the native request to UTF-8 JSON bytes, set both media types, and consume the validated stream.

 **Code**

```
async def invoke_model_with_response_stream(client: AsyncBedrockRuntimeClient) -> str:
    """Send a native streaming request and consume its validated output."""
    # Model-native request and event schemas vary by model provider.
    model_id = "global.amazon.nova-2-lite-v1:0"
    prompt = "Name one moon of Saturn."

    response = await client.invoke_model_with_response_stream(
        InvokeModelWithResponseStreamInput(
            model_id=model_id,
            content_type="application/json",
            accept="application/json",
            body=json.dumps(build_native_request(prompt)).encode("utf-8"),
        )
    )
    text = await consume_stream(response)
    print()
    return text
```

The entry point creates the client and runs the streaming request. Run the program with `python invoke_model_with_response_stream.py`.

```
async def main() -> None:
    """Create a client in a Region that offers the model and run the example."""
    config = await AsyncBedrockRuntimeConfig.resolve(region="us-east-1")
    async with AsyncBedrockRuntimeClient(config=config) as client:
        await invoke_model_with_response_stream(client)

if __name__ == "__main__":
    asyncio.run(main())
```

## More information
<a name="bedrock-invoke-model-stream-more-info"></a>
+ [Stream Amazon Nova 2 responses](https://docs.aws.amazon.com/nova/latest/nova2-userguide/streaming-responses.html) in the Amazon Nova User Guide
+ [Inference request parameters and response fields](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html) in the Amazon Bedrock User Guide
+ [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) in the Amazon Bedrock API Reference
