---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/services-sqs.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Amazon SQS
<a name="services-sqs"></a>

This chapter provides runnable examples for common [Amazon Simple Queue Service](https://docs.aws.amazon.com/sqs/) (Amazon SQS) workflows — creating and managing queues, sending and receiving messages, and configuring long polling to reduce empty responses and lower costs. Each example uses the SDK's asynchronous SQS client with typed inputs and outputs, so you can adapt them to your application without assembling raw request parameters. Start here to install the client package and configure shared setup that the remaining pages build on.

Install the SQS client before running the asynchronous examples on this page:

```
python -m pip install aws-sdk-sqs
```

## Set up the examples
<a name="sqs-shared-setup"></a>

The `client` that is used in the following examples can be created from the following snippet by calling `client = await create_client()` from your asynchronous code. Use the client as an asynchronous context manager, or call `await client.close()` after the last operation, as described in [Creating a service client](using-requests.md#using-requests-client). When you resolve the generated asynchronous configuration with `resolve()`, the SDK reads the AWS Region from standard AWS settings, such as environment variables and shared AWS configuration files. The SDK also reads credentials from the same settings. Configure both before running the examples: if no Region is configured, `resolve()` fails before the client is created, and if no credentials are configured, requests fail when the SDK signs them. For more information about the Region and other settings, see [Configuration variables](configuration-variables.md). For how the SDK finds credentials, see [Credential providers](credential-providers.md).

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.config import AsyncSQSConfig
```

 **Code**

```
async def create_client() -> AsyncSQSClient:
    config = await AsyncSQSConfig.resolve()
    return AsyncSQSClient(config=config)
```

**Topics**
+ [Set up the examples](#sqs-shared-setup)
+ [Work with Amazon SQS queues](sqs-queue-operations.md)
+ [Work with Amazon SQS messages](sqs-message-operations.md)
+ [Configure long polling for Amazon SQS](sqs-long-polling.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
