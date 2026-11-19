---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/services-sns.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Amazon SNS

[Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) (Amazon SNS) delivers each message that you publish to a topic to the endpoints subscribed to that topic. The examples on this page create and list topics, subscribe an endpoint, publish a message with message attributes, and remove subscriptions and topics.

Install the Amazon SNS client before you run the examples on this page.

```
python -m pip install aws-sdk-sns
```

## Set up the examples
<a name="sns-shared-setup"></a>

The examples on this page use the `client` that the following `create_client` function returns. Use the client in a `with` statement, or call `client.close()` after the last operation, as described in [Creating a service client](using-requests.md#using-requests-client).

Configure an AWS Region and credentials before you run the examples. For more information, see [Configuration variables](configuration-variables.md) and [Credential providers](credential-providers.md).

The identity that runs the examples needs the `sns:CreateTopic`, `sns:ListTopics`, `sns:Subscribe`, `sns:Publish`, `sns:Unsubscribe`, and `sns:DeleteTopic` permissions.

 **Imports**

```
from aws_sdk_sns import SNSClient, SNSConfig
```

 **Code**

```
def create_client() -> SNSClient:
    config = SNSConfig.resolve()
    return SNSClient(config=config)
```

## Create a topic
<a name="sns-create-topic"></a>

For request and response details, see the [create\_topic()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sns/operations/create_topic/) API reference.

A *topic* groups the endpoints that receive a message, for example an AWS Lambda function and an HTTP webhook. When you publish a message to a topic, Amazon SNS delivers it to each endpoint subscribed to the topic.

Create a topic with `create_topic` and keep the returned ARN. Later operations identify the topic by this ARN.

 **Imports**

```
from aws_sdk_sns import SNSClient
```

 **Code**

```
def create_topic(client: SNSClient, topic_name: str) -> str:
    """Create a topic and return its ARN."""
    response = client.create_topic(name=topic_name)
    if not response.topic_arn:
        raise RuntimeError("SNS did not return a topic ARN")
    return response.topic_arn
```

## List topics
<a name="sns-list-topics"></a>

For request and response details, see the [list\_topics()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sns/operations/list_topics/) API reference.

Each `list_topics` response can contain a partial result. Pass the returned `next_token` to the next call until the response has no token.

 **Imports**

```
from aws_sdk_sns import SNSClient
```

 **Code**

```
def list_topics(client: SNSClient) -> list[str]:
    """Return all topic ARNs, following pagination tokens."""
    topic_arns: list[str] = []
    next_token: str | None = None
    while True:
        page = client.list_topics(next_token=next_token)
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

For request and response details, see the [subscribe()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sns/operations/subscribe/) API reference.

Subscribe an endpoint by specifying its protocol and address. This example subscribes an email address that you control. An email subscription doesn't receive messages until the recipient confirms the subscription.

 **Imports**

```
from aws_sdk_sns import SNSClient
```

 **Code**

```
def subscribe_email(client: SNSClient, topic_arn: str, email: str) -> str:
    """Request an email subscription and return its ARN."""
    response = client.subscribe(
        topic_arn=topic_arn,
        protocol="email",
        endpoint=email,
        return_subscription_arn=True,
    )
    if not response.subscription_arn:
        raise RuntimeError("SNS did not return a subscription ARN")
    return response.subscription_arn
```

Each protocol has its own endpoint format and confirmation behavior. Don't publish sensitive data until the intended endpoint confirms the subscription.

## Publish a message to a topic
<a name="sns-publish-message"></a>

For request and response details, see the [publish()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sns/operations/publish/) API reference.

Publish a message to a topic by its ARN after the topic's endpoints confirm their subscriptions. Message attributes carry typed metadata separately from the message body.

 **Imports**

```
from aws_sdk_sns import SNSClient
```

 **Code**

```
def publish_to_topic(client: SNSClient, topic_arn: str, message: str) -> str:
    """Publish a message and return its message ID."""
    response = client.publish(
        topic_arn=topic_arn,
        message=message,
        message_attributes={
            "event_type": {
                "data_type": "String",
                "string_value": "order-created",
            }
        },
    )
    if not response.message_id:
        raise RuntimeError("SNS did not return a message ID")
    return response.message_id
```

## Unsubscribe an endpoint from a topic
<a name="sns-unsubscribe-endpoint"></a>

For request and response details, see the [unsubscribe()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sns/operations/unsubscribe/) API reference.

Unsubscribing removes one endpoint from a topic. The topic still exists and keeps delivering messages to its other subscriptions.

Call `unsubscribe` with the subscription ARN that `subscribe` returned. Because the subscribe example sets `return_subscription_arn=True`, `subscribe` returns an ARN even before the endpoint confirms. The endpoint must confirm the subscription before you unsubscribe it. If the subscription is still pending confirmation, `unsubscribe` raises the modeled `InvalidParameterException`.

 **Imports**

```
from aws_sdk_sns import SNSClient
```

 **Code**

```
def unsubscribe(client: SNSClient, subscription_arn: str) -> None:
    """Unsubscribe an endpoint identified by its subscription ARN."""
    client.unsubscribe(subscription_arn=subscription_arn)
```

## Delete a topic
<a name="sns-delete-topic"></a>

For request and response details, see the [delete\_topic()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sns/operations/delete_topic/) API reference.

Delete a topic when you no longer need it. Deleting a topic also deletes its subscriptions.

 **Imports**

```
from aws_sdk_sns import SNSClient
```

 **Code**

```
def delete_topic(client: SNSClient, topic_arn: str) -> None:
    """Delete the topic identified by its ARN."""
    client.delete_topic(topic_arn=topic_arn)
```

## More information
<a name="sns-more-info"></a>
+ [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
+ [CreateTopic](https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html) in the Amazon Simple Notification Service API Reference
+ [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) in the Amazon Simple Notification Service API Reference
+ [Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html) in the Amazon Simple Notification Service API Reference
+ [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) in the Amazon Simple Notification Service API Reference
+ [Unsubscribe](https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html) in the Amazon Simple Notification Service API Reference
+ [DeleteTopic](https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html) in the Amazon Simple Notification Service API Reference
