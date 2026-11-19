---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/services-bedrock.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Amazon Bedrock Runtime

Amazon Bedrock Runtime runs inference on the foundation models in [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html). This section has runnable examples for common inference patterns. The examples send conversational messages, stream model output as the model generates it, invoke models with native request formats, and exchange real-time bidirectional events. This page shows how to install the client package, create the clients, and choose an inference operation and the client type that it needs.

## Set up the examples
<a name="bedrock-setup"></a>

Install the Bedrock Runtime client package.

```
python -m pip install aws-sdk-bedrock-runtime
```

Each example in this section is a complete program when you add the setup code for its client type to the same file. The Converse and InvokeModel examples call `create_client`. The ConverseStream and InvokeModelWithResponseStream examples call `create_async_client`. The bidirectional streaming example creates its own client, because it needs a different HTTP client. Each `main` function uses the client in a `with` or `async with` block, which closes the client when the block exits.

The examples pin the AWS Region to `us-east-1` when they resolve the client configuration, because that Region offers the models that these examples use. Model availability varies by Region, so if you switch to a different model, also set the Region to one that offers that model. Configure credentials before you run the examples, as described in [Credential providers](credential-providers.md).

The identity that runs the examples needs access to the models that they use and the following permissions. The `converse` and `invoke_model` examples need `bedrock:InvokeModel`. The `converse_stream` and `invoke_model_with_response_stream` examples need `bedrock:InvokeModelWithResponseStream`. The bidirectional streaming example needs `bedrock:InvokeModelWithBidirectionalStream`.

------
#### [ Synchronous client ]

```
from aws_sdk_bedrock_runtime import BedrockRuntimeClient, BedrockRuntimeConfig

def create_client() -> BedrockRuntimeClient:
    """Create a synchronous client in a Region that offers the models."""
    config = BedrockRuntimeConfig.resolve(region="us-east-1")
    return BedrockRuntimeClient(config=config)
```

------
#### [ Asynchronous client ]

```
from aws_sdk_bedrock_runtime import AsyncBedrockRuntimeClient, AsyncBedrockRuntimeConfig

async def create_async_client() -> AsyncBedrockRuntimeClient:
    """Create an asynchronous client in a Region that offers the models."""
    config = await AsyncBedrockRuntimeConfig.resolve(region="us-east-1")
    return AsyncBedrockRuntimeClient(config=config)
```

------

Running the examples sends inference requests that incur charges. For details, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

## Choose an inference operation
<a name="bedrock-choose-operation"></a>

First choose a request format. The Converse operations use Bedrock message and content-block models. The same request works across supported models. The InvokeModel operations use the selected model's native format, so the request, response, and event schemas depend on the model. Then choose whether your application needs the complete response or output as the model generates it.

| Operation | Request format | Response | Client type |
| --- | --- | --- | --- |
| converse | Converse messages | The complete reply in one response | Synchronous or asynchronous |
| converse\_stream | Converse messages | A stream of events while the model generates the reply | Asynchronous only |
| invoke\_model | Model-native JSON | The complete native response | Synchronous or asynchronous |
| invoke\_model\_with\_response\_stream | Model-native JSON | A stream of model-native events while the model generates the reply | Asynchronous only |
| invoke\_model\_with\_bidirectional\_stream | Model-native JSON events | A stream of output events while the application keeps sending input events | Asynchronous only, with the CRT HTTP client |

Operation support varies by model. For each model's supported operations and capabilities, see [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) in the Amazon Bedrock User Guide and select a model to view its details.

**Topics**
+ [Set up the examples](#bedrock-setup)
+ [Choose an inference operation](#bedrock-choose-operation)
+ [Use Converse](bedrock-converse.md)
+ [Use ConverseStream](bedrock-output-streaming.md)
+ [Use InvokeModel](bedrock-native-invoke.md)
+ [Use InvokeModelWithResponseStream](bedrock-invoke-model-stream.md)
+ [Use bidirectional streaming](bedrock-bidirectional-streaming.md)
