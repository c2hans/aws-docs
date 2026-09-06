---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/services-bedrock.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Amazon Bedrock Runtime
<a name="services-bedrock"></a>

This chapter provides runnable examples for common [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) Runtime inference patterns — sending conversational messages, streaming model output as it generates, invoking models with native request formats, and exchanging real-time bidirectional events. Each example uses the SDK's asynchronous Bedrock Runtime client with typed inputs and outputs, so you can adapt them to your application without constructing model-specific JSON payloads by hand. Start here to install the client package, configure shared setup, and choose the right inference operation for your use case.

## Set up the examples
<a name="bedrock-setup"></a>

Install the Bedrock Runtime client package.

```
python -m pip install aws-sdk-bedrock-runtime
```

Each example in this chapter is a complete program: its Imports, helper functions, operation code, and `main` entry point together form the full example file. Each program pins the AWS Region to `us-east-1` when it resolves the client configuration, because that Region offers the models that these examples use. Model availability varies by Region, so if you switch to a different model, also set the Region to one that offers that model. The SDK reads credentials from standard AWS settings, such as environment variables and shared AWS configuration files. Configure credentials before running the examples. If none are configured, requests fail when the SDK signs them. For how the SDK finds credentials, see [Credential providers](credential-providers.md).

Running the examples sends inference requests that incur charges. For details, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

## Choose an inference operation
<a name="bedrock-choose-operation"></a>

Choose an API family first, then choose whether the application needs a complete response or incremental output.
+ **Portable conversation format:** Use `converse` to get the model's complete reply in a single response. Use `converse_stream` to receive that reply as a stream of events while the model is still generating it, so your application can display text as it arrives. Both use Bedrock message and content-block models.
+ **Model-native format:** Use `invoke_model` to get the model's complete native response in a single call. Use `invoke_model_with_response_stream` to receive that native output as a stream of events while the model is still generating it. The request, response, and event schemas depend on the selected model.
+ **Real-time bidirectional format:** Use `invoke_model_with_bidirectional_stream` with a compatible model when the application must continue sending input while it receives output. The event protocol depends on the selected model.

Operation support varies by model. For each model's supported operations and capabilities, see [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) in the Amazon Bedrock User Guide and select a model to view its details.

**Topics**
+ [Set up the examples](#bedrock-setup)
+ [Choose an inference operation](#bedrock-choose-operation)
+ [Use Converse](bedrock-converse.md)
+ [Use ConverseStream](bedrock-output-streaming.md)
+ [Use InvokeModel](bedrock-native-invoke.md)
+ [Use InvokeModelWithResponseStream](bedrock-invoke-model-stream.md)
+ [Use bidirectional streaming](bedrock-bidirectional-streaming.md)
