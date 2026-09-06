---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/bedrock-native-invoke.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use InvokeModel
<a name="bedrock-native-invoke"></a>

InvokeModel sends a request in the selected model's native JSON format and returns the model's complete native response. Use it when you need model-specific request or response features that the portable Converse format doesn't expose. The request and response schemas depend on the selected model.

The following example sends one Amazon Nova 2 Messages API request and prints the reply text. For request and response details, see the [invoke\_model()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/bedrock-runtime/operations/invoke_model/) API reference.

 **Imports**

```
import asyncio
import json
from typing import Any

from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import AsyncBedrockRuntimeConfig
from aws_sdk_bedrock_runtime.models import InvokeModelInput
```

The following helper functions build the model-native request and validate the model-native response.

```
def build_native_request(prompt: str) -> dict[str, Any]:
    """Build an Amazon Nova 2 Messages API request."""
    return {
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "inferenceConfig": {
            "maxTokens": 100,
            "temperature": 0.2,
            "topP": 0.9,
        },
    }

def parse_native_text(body: bytes) -> str:
    """Validate an Amazon Nova 2 response and collect its text blocks."""
    payload: Any = json.loads(body.decode("utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError("The model returned a malformed native response")
    output = payload.get("output")
    message = output.get("message") if isinstance(output, dict) else None
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, list):
        raise RuntimeError("The model returned no native text content")
    text = "".join(
        block["text"]
        for block in content
        if isinstance(block, dict)
        and isinstance(block.get("text"), str)
        and block["text"]
    )
    if not text:
        raise RuntimeError("The model returned no native text content")
    return text
```

Serialize the native request to UTF-8 JSON bytes, set both media types, and decode the response according to the selected model's response schema.

 **Code**

```
async def invoke_model(client: AsyncBedrockRuntimeClient) -> str:
    """Invoke a Nova model and print its validated native text response."""
    # Model-native request and response schemas vary by model provider.
    model_id = "global.amazon.nova-2-lite-v1:0"
    prompt = "Name one moon of Saturn."

    response = await client.invoke_model(
        InvokeModelInput(
            model_id=model_id,
            content_type="application/json",
            accept="application/json",
            body=json.dumps(build_native_request(prompt)).encode("utf-8"),
        )
    )
    text = parse_native_text(response.body)
    print(text)
    return text
```

The entry point creates the client and runs the request. Run the program with `python invoke_model.py`.

```
async def main() -> None:
    """Create a client in a Region that offers the model and run the example."""
    config = await AsyncBedrockRuntimeConfig.resolve(region="us-east-1")
    async with AsyncBedrockRuntimeClient(config=config) as client:
        await invoke_model(client)

if __name__ == "__main__":
    asyncio.run(main())
```

## More information
<a name="bedrock-native-invoke-more-info"></a>
+ [Use the Invoke API with Amazon Nova 2](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-invoke-api.html) in the Amazon Nova User Guide
+ [Inference request parameters and response fields](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html) in the Amazon Bedrock User Guide
+ [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) in the Amazon Bedrock API Reference
