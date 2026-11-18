---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/configuring.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Configuration
<a name="configuring"></a>

The AWS SDK for Python v4 resolves client configuration from values that you pass in code, environment variables, and the shared AWS config files. If you create a client without a configuration (`client = BedrockRuntimeClient()`), the client resolves its configuration from your environment the first time you call an operation.

## Prerequisites
<a name="config-prerequisites"></a>

Before you use the SDK, configure the following:
+ An AWS Region. Set it with the `AWS_REGION` environment variable, in your `~/.aws/config` file, or in code. The Region is required and has no default.
+ AWS credentials from a supported credential source. For more information, see [Credential providers](credential-providers.md).

## Quick start
<a name="quick-start"></a>

The following example creates a client without a configuration and sends a request.

```
from aws_sdk_bedrock_runtime import BedrockRuntimeClient
from aws_sdk_bedrock_runtime.models import (
    ContentBlockText,
    ConverseOutputMessage,
)

def main() -> None:
    with BedrockRuntimeClient() as client:
        response = client.converse(
            model_id="global.amazon.nova-2-lite-v1:0",
            messages=[
                {"role": "user", "content": [{"text": "What is 2 + 2?"}]}
            ],
        )
        if isinstance(response.output, ConverseOutputMessage):
            for block in response.output.value.content:
                if isinstance(block, ContentBlockText):
                    print(block.value)

if __name__ == "__main__":
    main()
```

This example assumes that you set the Region with `AWS_REGION` or the `region` setting in your config file, and that the default credential resolver chain can find credentials. The `with` statement closes the client when the block ends.

## Explicit configuration
<a name="explicit-configuration"></a>

Instead of letting the client resolve its configuration on the first call, you can resolve the configuration yourself and pass it to the client. Explicit resolution lets you override specific values and validate the configuration before you call an operation. Call `resolve()` on the config class for the service. For an asynchronous client, use the `Async` config class and await `resolve()`.

------
#### [ Synchronous client ]

```
from aws_sdk_bedrock_runtime import BedrockRuntimeClient, BedrockRuntimeConfig

def create_client() -> BedrockRuntimeClient:
    config = BedrockRuntimeConfig.resolve(region="us-west-2", max_attempts=5)
    return BedrockRuntimeClient(config=config)
```

------
#### [ Asynchronous client ]

```
from aws_sdk_bedrock_runtime import AsyncBedrockRuntimeClient, AsyncBedrockRuntimeConfig

async def create_client() -> AsyncBedrockRuntimeClient:
    config = await AsyncBedrockRuntimeConfig.resolve(
        region="us-west-2", max_attempts=5
    )
    return AsyncBedrockRuntimeClient(config=config)
```

------

The synchronous and asynchronous config classes have the same fields and resolve them the same way. For fields that take a component, such as an HTTP client or a credential resolver, use components that match the client mode. The rest of this chapter uses synchronous examples. For more information about the two client types, see [Synchronous and asynchronous clients](using-sync-async.md). For details about resolution, see [Configuration resolution](config-resolution.md).

## Next steps
<a name="config-next-steps"></a>
+ To understand how the SDK resolves configuration values, see [Configuration resolution](config-resolution.md).
+ To look up a specific configuration setting, see [Configuration variables](configuration-variables.md).
+ To set up profiles for different environments, see [Config files and named profiles](config-files.md).
+ To learn how the SDK finds credentials, see [Credential providers](credential-providers.md).
+ To configure or replace the HTTP client, see [HTTP configuration](http-configuration.md).
+ To use Federal Information Processing Standard (FIPS) endpoints, dual-stack endpoints, or custom endpoints, see [Endpoint configuration](config-endpoints.md).
+ To understand how retries work and how to configure them, see [Retries](config-retries.md).
