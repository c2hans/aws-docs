---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SNS::Subscription
<a name="aws-resource-sns-subscription"></a>

The `AWS::SNS::Subscription` resource subscribes an endpoint to an Amazon SNS topic. For a subscription to be created, the owner of the endpoint must` confirm the subscription.

## Syntax
<a name="aws-resource-sns-subscription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sns-subscription-syntax.json"></a>

```
{
  "Type" : "AWS::SNS::Subscription",
  "Properties" : {
      "[DeliveryPolicy](#cfn-sns-subscription-deliverypolicy)" : {{Json}},
      "[Endpoint](#cfn-sns-subscription-endpoint)" : {{String}},
      "[FilterPolicy](#cfn-sns-subscription-filterpolicy)" : {{Json}},
      "[FilterPolicyScope](#cfn-sns-subscription-filterpolicyscope)" : {{String}},
      "[Protocol](#cfn-sns-subscription-protocol)" : {{String}},
      "[RawMessageDelivery](#cfn-sns-subscription-rawmessagedelivery)" : {{Boolean}},
      "[RedrivePolicy](#cfn-sns-subscription-redrivepolicy)" : {{Json}},
      "[Region](#cfn-sns-subscription-region)" : {{String}},
      "[ReplayPolicy](#cfn-sns-subscription-replaypolicy)" : {{Json}},
      "[SubscriptionRoleArn](#cfn-sns-subscription-subscriptionrolearn)" : {{String}},
      "[TopicArn](#cfn-sns-subscription-topicarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sns-subscription-syntax.yaml"></a>

```
Type: AWS::SNS::Subscription
Properties:
  [DeliveryPolicy](#cfn-sns-subscription-deliverypolicy): {{Json}}
  [Endpoint](#cfn-sns-subscription-endpoint): {{String}}
  [FilterPolicy](#cfn-sns-subscription-filterpolicy): {{Json}}
  [FilterPolicyScope](#cfn-sns-subscription-filterpolicyscope): {{String}}
  [Protocol](#cfn-sns-subscription-protocol): {{String}}
  [RawMessageDelivery](#cfn-sns-subscription-rawmessagedelivery): {{Boolean}}
  [RedrivePolicy](#cfn-sns-subscription-redrivepolicy): {{Json}}
  [Region](#cfn-sns-subscription-region): {{String}}
  [ReplayPolicy](#cfn-sns-subscription-replaypolicy): {{Json}}
  [SubscriptionRoleArn](#cfn-sns-subscription-subscriptionrolearn): {{String}}
  [TopicArn](#cfn-sns-subscription-topicarn): {{String}}
```

## Properties
<a name="aws-resource-sns-subscription-properties"></a>

`DeliveryPolicy`  <a name="cfn-sns-subscription-deliverypolicy"></a>
The delivery policy JSON assigned to the subscription. Enables the subscriber to define the message delivery retry strategy in the case of an HTTP/S endpoint subscribed to the topic. For more information, see ` [GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html) ` in the *Amazon SNS API Reference* and [Message delivery retries](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html) in the *Amazon SNS Developer Guide*.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-sns-subscription-endpoint"></a>
The subscription's endpoint. The endpoint value depends on the protocol that you specify. For more information, see the `Endpoint` parameter of the ` [Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html) ` action in the *Amazon SNS API Reference*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterPolicy`  <a name="cfn-sns-subscription-filterpolicy"></a>
The filter policy JSON assigned to the subscription. Enables the subscriber to filter out unwanted messages. For more information, see ` [GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html) ` in the *Amazon SNS API Reference* and [Message filtering](https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html) in the *Amazon SNS Developer Guide*.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterPolicyScope`  <a name="cfn-sns-subscription-filterpolicyscope"></a>
This attribute lets you choose the filtering scope by using one of the following string value types:
+ `MessageAttributes` (default) - The filter is applied on the message attributes.
+ `MessageBody` - The filter is applied on the message body.
`Null` is not a valid value for `FilterPolicyScope`. To delete a filter policy, delete the `FilterPolicy` property but keep `FilterPolicyScope` property as is.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-sns-subscription-protocol"></a>
The subscription's protocol. For more information, see the `Protocol` parameter of the ` [Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html) ` action in the *Amazon SNS API Reference*.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RawMessageDelivery`  <a name="cfn-sns-subscription-rawmessagedelivery"></a>
When set to `true`, enables raw message delivery. Raw messages don't contain any JSON formatting and can be sent to Amazon SQS and HTTP/S endpoints. For more information, see ` [GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html) ` in the *Amazon SNS API Reference*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedrivePolicy`  <a name="cfn-sns-subscription-redrivepolicy"></a>
When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.
For more information about the redrive policy and dead-letter queues, see [Amazon SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) in the *Amazon SQS Developer Guide*.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-sns-subscription-region"></a>
For cross-region subscriptions, the region in which the topic resides.
If no region is specified, CloudFormation uses the region of the caller as the default.
If you perform an update operation that only updates the `Region` property of a `AWS::SNS::Subscription` resource, that operation will fail unless you are either:
+ Updating the `Region` from `NULL` to the caller region.
+ Updating the `Region` from the caller region to `NULL`.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ReplayPolicy`  <a name="cfn-sns-subscription-replaypolicy"></a>
Specifies whether Amazon SNS resends the notification to the subscription when a message's attribute changes.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriptionRoleArn`  <a name="cfn-sns-subscription-subscriptionrolearn"></a>
This property applies only to Amazon Data Firehose delivery stream subscriptions. Specify the ARN of the IAM role that has the following:
+ Permission to write to the Amazon Data Firehose delivery stream
+ Amazon SNS listed as a trusted entity
Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see [Fanout to Amazon Data Firehose delivery streams](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html) in the *Amazon SNS Developer Guide.*
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicArn`  <a name="cfn-sns-subscription-topicarn"></a>
The ARN of the topic to subscribe to.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sns-subscription-return-values"></a>

### Ref
<a name="aws-resource-sns-subscription-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the subscription's logical name. This attribute allows you to reference the logical name of the subscription resource within the CloudFormation template.

For example, if you have a subscription resource named 'MySubscription', you can use '\!Ref MySubscription' to refer to its logical name in other parts of the CloudFormation template.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sns-subscription-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sns-subscription-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the ARN of the subscription created by the `AWS::SNS::Subscription` resource.

## Examples
<a name="aws-resource-sns-subscription--examples"></a>

**Topics**
+ [Create a subscription with mandatory attributes](#aws-resource-sns-subscription--examples--Create_a_subscription_with_mandatory_attributes)
+ [Create a subscription with optional attributes](#aws-resource-sns-subscription--examples--Create_a_subscription_with_optional_attributes)

### Create a subscription with mandatory attributes
<a name="aws-resource-sns-subscription--examples--Create_a_subscription_with_mandatory_attributes"></a>

The following example creates a subscription with only an endpoint, protocol, and topic ARN.

#### JSON
<a name="aws-resource-sns-subscription--examples--Create_a_subscription_with_mandatory_attributes--json"></a>

```
"MySubscription" : {
  "Type" : "AWS::SNS::Subscription",
  "Properties" : {
    "Endpoint" : "test@example.com",
    "Protocol" : "email",
    "TopicArn" : { "Ref" : "MySNSTopic" }
  }
}
```

#### YAML
<a name="aws-resource-sns-subscription--examples--Create_a_subscription_with_mandatory_attributes--yaml"></a>

```
MySubscription:
  Type: AWS::SNS::Subscription
  Properties:
    Endpoint: test@example.com
    Protocol: email
    TopicArn: !Ref 'MySNSTopic'
```

### Create a subscription with optional attributes
<a name="aws-resource-sns-subscription--examples--Create_a_subscription_with_optional_attributes"></a>

The following example creates a subscription with a filter policy, delivery policy, and raw message delivery enabled.

**Note**
You can set subscription attributes only on standalone Amazon SNS subscriptions (not on subscriptions nested in topics).

#### YAML
<a name="aws-resource-sns-subscription--examples--Create_a_subscription_with_optional_attributes--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  CarSalesTopic:
    Type: 'AWS::SNS::Topic'
  ERPSubscription:
    Type: 'AWS::SNS::Subscription'
    Properties:
      TopicArn: !Ref CarSalesTopic
      Endpoint: !GetAtt
        - ERPIntegrationQueue
        - Arn
      Protocol: sqs
      RawMessageDelivery: 'true'
  CRMSubscription:
    Type: 'AWS::SNS::Subscription'
    Properties:
      TopicArn: !Ref CarSalesTopic
      Endpoint: !GetAtt
        - CRMIntegrationQueue
        - Arn
      Protocol: sqs
      RawMessageDelivery: 'true'
      FilterPolicy:
        buyer-class:
          - vip
  SCMSubscription:
    Type: 'AWS::SNS::Subscription'
    Properties:
      TopicArn: !Ref CarSalesTopic
      Endpoint: !Ref myHttpEndpoint
      Protocol: https
      DeliveryPolicy:
        healthyRetryPolicy:
          numRetries: 20
          minDelayTarget: 10
          maxDelayTarget: 30
          numMinDelayRetries: 3
          numMaxDelayRetries: 17
          numNoDelayRetries: 0
          backoffFunction: exponential
  ERPIntegrationQueue:
    Type: 'AWS::SQS::Queue'
    Properties: {}
  CRMIntegrationQueue:
    Type: 'AWS::SQS::Queue'
    Properties: {}
Parameters:
  myHttpEndpoint:
    Type: String
```

#### JSON
<a name="aws-resource-sns-subscription--examples--Create_a_subscription_with_optional_attributes--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "CarSalesTopic": {
            "Type": "AWS::SNS::Topic"
        },
        "ERPSubscription": {
            "Type": "AWS::SNS::Subscription",
            "Properties": {
                "TopicArn": {
                    "Ref": "CarSalesTopic"
                },
                "Endpoint": {
                    "Fn::GetAtt": ["ERPIntegrationQueue", "Arn"]
                },
                "Protocol": "sqs",
                "RawMessageDelivery": "true"
            }
        },
        "CRMSubscription": {
            "Type": "AWS::SNS::Subscription",
            "Properties": {
                "TopicArn": {
                    "Ref": "CarSalesTopic"
                },
                "Endpoint": {
                    "Fn::GetAtt": ["CRMIntegrationQueue", "Arn"]
                },
                "Protocol": "sqs",
                "RawMessageDelivery": "true",
                "FilterPolicy": {
                    "buyer-class": [
                        "vip"
                    ]
                }
            }
        },
        "SCMSubscription": {
            "Type": "AWS::SNS::Subscription",
            "Properties": {
                "TopicArn": {
                    "Ref": "CarSalesTopic"
                },
                "Endpoint": {
                    "Ref": "myHttpEndpoint"
                },
                "Protocol": "https",
                "DeliveryPolicy": {
                    "healthyRetryPolicy": {
                        "numRetries": 20,
                        "minDelayTarget": 10,
                        "maxDelayTarget": 30,
                        "numMinDelayRetries": 3,
                        "numMaxDelayRetries": 17,
                        "numNoDelayRetries": 0,
                        "backoffFunction": "exponential"
                    }
                }
            }
        },
        "ERPIntegrationQueue": {
            "Type": "AWS::SQS::Queue",
            "Properties": {}
        },
        "CRMIntegrationQueue": {
            "Type": "AWS::SQS::Queue",
            "Properties": {}
        }
    },
    "Parameters": {
        "myHttpEndpoint": {
            "Type": "String"
        }
    }
}
```
