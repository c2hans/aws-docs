---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/configuring.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Configuration
<a name="configuring"></a>

The AWS SDK for Python uses a configuration system that automatically discovers and resolves your AWS settings from multiple sources. When you create a client (`client = AsyncBedrockRuntimeClient()`), the SDK automatically resolves configuration values from your environment variables and AWS config files the first time an operation is called.

## Prerequisites
<a name="config-prerequisites"></a>

Before using the SDK, make sure you have the following configured:
+ An AWS Region, either set via the `AWS_REGION` environment variable, in your `~/.aws/config` file, or passed directly in code. Region is required and has no default.
+ AWS credentials available through a supported credential source (see [Credential providers](credential-providers.md)).

## Quick start
<a name="quick-start"></a>

The following example shows the simplest way to create a client and make a request. You do not need explicit configuration. The SDK resolves all configuration values automatically from your environment when the first operation is called:

```
import asyncio
from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.models import Message, ContentBlockText, ConverseInput

async def main():

    async with AsyncBedrockRuntimeClient() as client:

        response = await client.converse(
            ConverseInput(
                model_id="global.amazon.nova-2-lite-v1:0",
                messages=[Message(role="user", content=[ContentBlockText(value="What is 2 + 2?")])],
            )
        )

        print(response.output.value.content[0].value)

asyncio.run(main())
```

This example assumes that `AWS_REGION` is set (or `region` is defined in your config file) and that credentials are available through the credential chain. When you run this, the SDK creates a client, resolves configuration on the first operation call, sends a request to Amazon Bedrock Runtime, and prints the response.

## Explicit configuration
<a name="explicit-configuration"></a>

You can either let the SDK resolve configuration automatically (as shown in [Quick start](#quick-start)), or explicitly resolve it for more control. Explicit resolution lets you override specific values and validate configuration upfront before any operation is called. See [Configuration resolution](config-resolution.md) for details.

## Next steps
<a name="config-next-steps"></a>
+ To understand how the SDK resolves configuration values, see [Configuration resolution](config-resolution.md).
+ To look up a specific configuration setting, see [Configuration variables](configuration-variables.md).
+ To set up profiles for different environments, see [Config files and named profiles](config-files.md).
+ To learn how the SDK finds credentials, see [Credential providers](credential-providers.md).
+ To configure or replace the HTTP client, see [HTTP configuration](http-configuration.md).
+ To understand how retries work and how to configure them, see [Retries](config-retries.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
