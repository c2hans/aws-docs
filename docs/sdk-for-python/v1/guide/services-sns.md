---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/services-sns.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Amazon SNS
<a name="services-sns"></a>

This page provides runnable examples for common [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) (Amazon SNS) workflows — creating topics, subscribing endpoints across protocols, publishing messages with metadata attributes, and managing subscription and topic lifecycle. Each example uses the SDK's asynchronous SNS client with typed inputs and outputs, so you can adapt them to your application without assembling raw request parameters. Start below to install the client package and configure shared setup that the remaining examples build on.

Install the SNS client before running the asynchronous examples on this page:

```
python -m pip install aws-sdk-sns
```

## Set up the examples
<a name="sns-shared-setup"></a>

The `client` that is used in the following examples can be created from the following snippet by calling `client = await create_client()` from your asynchronous code. Use the client as an asynchronous context manager, or call `await client.close()` after the last operation, as described in [Creating a service client](using-requests.md#using-requests-client). When you resolve the generated asynchronous configuration with `resolve()`, the SDK reads the AWS Region from standard AWS settings, such as environment variables and shared AWS configuration files. The SDK also reads credentials from the same settings. Configure both before running the examples: if no Region is configured, `resolve()` fails before the client is created, and if no credentials are configured, requests fail when the SDK signs them. For more information about the Region and other settings, see [Configuration variables](configuration-variables.md). For how the SDK finds credentials, see [Credential providers](credential-providers.md).

 **Imports**

```
from aws_sdk_sns.client import AsyncSNSClient
from aws_sdk_sns.config import AsyncSNSConfig
```

 **Code**

```
async def create_client() -> AsyncSNSClient:
    config = await AsyncSNSConfig.resolve()
    return AsyncSNSClient(config=config)
```

## Create a topic
<a name="sns-create-topic"></a>

For request and response details, see the [create\_topic()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sns/operations/create_topic/) API reference.

A *topic* is a logical grouping of communication channels that defines which systems to send a message to, for example, fanning out a message to AWS Lambda and an HTTP webhook. You send messages to Amazon SNS, then they're distributed to the channels defined in the topic. This makes the messages available to subscribers.

Create a topic with `create_topic` and retain the returned ARN. Later operations identify the topic by this ARN.

 **Imports**

```
from aws_sdk_sns.client import AsyncSNSClient
from aws_sdk_sns.models import CreateTopicInput
```

 **Code**

```
async def create_topic(client: AsyncSNSClient, topic_name: str) -> str:
    """Create a topic and return its ARN."""
    response = await client.create_topic(
        input=CreateTopicInput(name=topic_name)
    )
    if not response.topic_arn:
        raise RuntimeError("SNS did not return a topic ARN")
    return response.topic_arn
```

## List topics
<a name="sns-list-topics"></a>

For request and response details, see the [list\_topics()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sns/operations/list_topics/) API reference.

`list_topics` can return a partial result. Continue with `next_token` until Amazon SNS returns no continuation token.

 **Imports**

```
from aws_sdk_sns.client import AsyncSNSClient
from aws_sdk_sns.models import ListTopicsInput
```

 **Code**

```
async def list_topics(client: AsyncSNSClient) -> list[str]:
    """Return all topic ARNs, following pagination tokens."""
    topic_arns: list[str] = []
    next_token: str | None = None
    while True:
        page = await client.list_topics(
            input=ListTopicsInput(next_token=next_token)
        )
        topic_arns.extend(
            topic.topic_arn
            for topic in page.topics or []
            if topic.topic_arn
        )
        next_token = page.next_token
        if not next_token:
            return topic_arns
```

## Subscribe an endpoint to a topic
<a name="sns-subscribe-endpoint"></a>

For request and response details, see the [subscribe()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sns/operations/subscribe/) API reference.

After you create a topic, you can configure which communication channels will be endpoints for that topic. Messages are distributed to these endpoints after Amazon SNS receives them.

Subscribe an endpoint by specifying its protocol and address. This example subscribes an email address that you control. Email subscriptions do not receive publications until the recipient confirms the subscription.

 **Imports**

```
from aws_sdk_sns.client import AsyncSNSClient
from aws_sdk_sns.models import SubscribeInput
```

 **Code**

```
async def subscribe_email(
    client: AsyncSNSClient, topic_arn: str, email: str
) -> str:
    """Request an email subscription and return its ARN or status."""
    response = await client.subscribe(
        input=SubscribeInput(
            topic_arn=topic_arn,
            protocol="email",
            endpoint=email,
            return_subscription_arn=True,
        )
    )
    if not response.subscription_arn:
        raise RuntimeError("SNS did not return a subscription status")
    return response.subscription_arn
```

Different protocols have different endpoint formats and confirmation behavior. Do not publish sensitive data until the intended endpoint has confirmed the subscription.

## Publish a message to a topic
<a name="sns-publish-message"></a>

For request and response details, see the [publish()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sns/operations/publish/) API reference.

After you have a topic and one or more endpoints configured for it, you can publish a message to it.

Publish to a topic ARN after its intended endpoints are confirmed. Message attributes carry typed metadata separately from the body.

 **Imports**

```
from aws_sdk_sns.client import AsyncSNSClient
from aws_sdk_sns.models import MessageAttributeValue, PublishInput
```

 **Code**

```
async def publish_to_topic(
    client: AsyncSNSClient, topic_arn: str, message: str
) -> str:
    """Publish a message and return its message ID."""
    response = await client.publish(
        input=PublishInput(
            topic_arn=topic_arn,
            message=message,
            message_attributes={
                "event_type": MessageAttributeValue(
                    data_type="String",
                    string_value="order-created",
                )
            },
        )
    )
    if not response.message_id:
        raise RuntimeError("SNS did not return a message ID")
    return response.message_id
```

## Unsubscribe an endpoint from a topic
<a name="sns-unsubscribe-endpoint"></a>

For request and response details, see the [unsubscribe()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sns/operations/unsubscribe/) API reference.

You can remove the communication channels configured as endpoints for a topic. After doing that, the topic itself continues to exist and distributes messages to any other endpoints configured for that topic.

Use `unsubscribe` with the subscription ARN returned by `subscribe`. The subscription must be confirmed first: because the examples request `return_subscription_arn=True`, `subscribe` returns a real ARN even before the endpoint confirms, but unsubscribing a subscription that is still pending confirmation fails with the modeled `InvalidParameterException`.

 **Imports**

```
from aws_sdk_sns.client import AsyncSNSClient
from aws_sdk_sns.models import UnsubscribeInput
```

 **Code**

```
async def unsubscribe(client: AsyncSNSClient, subscription_arn: str) -> None:
    """Unsubscribe an endpoint identified by its subscription ARN."""
    await client.unsubscribe(
        input=UnsubscribeInput(subscription_arn=subscription_arn)
    )
```

## Delete a topic
<a name="sns-delete-topic"></a>

For request and response details, see the [delete\_topic()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sns/operations/delete_topic/) API reference.

Delete a temporary topic when it is no longer needed. Deleting a topic also deletes its subscriptions.

 **Imports**

```
from aws_sdk_sns.client import AsyncSNSClient
from aws_sdk_sns.models import DeleteTopicInput
```

 **Code**

```
async def delete_topic(client: AsyncSNSClient, topic_arn: str) -> None:
    """Delete the topic identified by its ARN."""
    await client.delete_topic(input=DeleteTopicInput(topic_arn=topic_arn))
```

## More information
<a name="sns-more-info"></a>
+ [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
+ [CreateTopic](https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html) in the Amazon Simple Notification Service API Reference
+ [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) in the Amazon Simple Notification Service API Reference
+ [Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html) in the Amazon Simple Notification Service API Reference
+ [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) in the Amazon Simple Notification Service API Reference
+ [Unsubscribe](https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html) in the Amazon Simple Notification Service API Reference
+ [DeleteTopic](https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html) in the Amazon Simple Notification Service API Reference
