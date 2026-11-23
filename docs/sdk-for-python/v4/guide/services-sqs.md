---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/services-sqs.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Amazon SQS

[Amazon Simple Queue Service](https://docs.aws.amazon.com/sqs/) (Amazon SQS) is a message queuing service. The examples in this section create and manage queues, send and receive messages, and configure long polling to reduce empty responses.

Install the Amazon SQS client before you run the examples in this section.

```bash
python -m pip install aws-sdk-sqs
```

## Set up the examples
<a name="sqs-shared-setup"></a>

The examples in this section use the `client` that the following `create_client` function returns. Use the client in a `with` statement, or call `client.close()` after the last operation, as described in [Creating a service client](using-requests.md#using-requests-client).

Configure an AWS Region and credentials before you run the examples. For more information, see [Configuration variables](configuration-variables.md) and [Credential providers](credential-providers.md).

 **Imports**

```python
from aws_sdk_sqs import SQSClient, SQSConfig
```

 **Code**

```python
def create_client() -> SQSClient:
    config = SQSConfig.resolve()
    return SQSClient(config=config)
```

**Topics**
+ [Set up the examples](#sqs-shared-setup)
+ [Work with Amazon SQS queues](sqs-queue-operations.md)
+ [Work with Amazon SQS messages](sqs-message-operations.md)
+ [Configure long polling for Amazon SQS](sqs-long-polling.md)
