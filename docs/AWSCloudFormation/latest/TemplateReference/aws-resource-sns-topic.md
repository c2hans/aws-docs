---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topic.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SNS::Topic
<a name="aws-resource-sns-topic"></a>

The `AWS::SNS::Topic` resource creates a topic to which notifications can be published.

**Note**
One account can create a maximum of 100,000 standard topics and 1,000 FIFO topics. For more information, see [Amazon SNS endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sns.html) in the *AWS General Reference*.

## Syntax
<a name="aws-resource-sns-topic-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sns-topic-syntax.json"></a>

```
{
  "Type" : "AWS::SNS::Topic",
  "Properties" : {
      "[ArchivePolicy](#cfn-sns-topic-archivepolicy)" : {{Json}},
      "[ContentBasedDeduplication](#cfn-sns-topic-contentbaseddeduplication)" : {{Boolean}},
      "[DataProtectionPolicy](#cfn-sns-topic-dataprotectionpolicy)" : {{Json}},
      "[DeliveryStatusLogging](#cfn-sns-topic-deliverystatuslogging)" : {{[ LoggingConfig, ... ]}},
      "[DisplayName](#cfn-sns-topic-displayname)" : {{String}},
      "[FifoThroughputScope](#cfn-sns-topic-fifothroughputscope)" : {{String}},
      "[FifoTopic](#cfn-sns-topic-fifotopic)" : {{Boolean}},
      "[KmsMasterKeyId](#cfn-sns-topic-kmsmasterkeyid)" : {{String}},
      "[SignatureVersion](#cfn-sns-topic-signatureversion)" : {{String}},
      "[Subscription](#cfn-sns-topic-subscription)" : {{[ Subscription, ... ]}},
      "[Tags](#cfn-sns-topic-tags)" : {{[ Tag, ... ]}},
      "[TopicName](#cfn-sns-topic-topicname)" : {{String}},
      "[TracingConfig](#cfn-sns-topic-tracingconfig)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sns-topic-syntax.yaml"></a>

```
Type: AWS::SNS::Topic
Properties:
  [ArchivePolicy](#cfn-sns-topic-archivepolicy): {{Json}}
  [ContentBasedDeduplication](#cfn-sns-topic-contentbaseddeduplication): {{Boolean}}
  [DataProtectionPolicy](#cfn-sns-topic-dataprotectionpolicy): {{Json}}
  [DeliveryStatusLogging](#cfn-sns-topic-deliverystatuslogging): {{
    - LoggingConfig}}
  [DisplayName](#cfn-sns-topic-displayname): {{String}}
  [FifoThroughputScope](#cfn-sns-topic-fifothroughputscope): {{String}}
  [FifoTopic](#cfn-sns-topic-fifotopic): {{Boolean}}
  [KmsMasterKeyId](#cfn-sns-topic-kmsmasterkeyid): {{String}}
  [SignatureVersion](#cfn-sns-topic-signatureversion): {{String}}
  [Subscription](#cfn-sns-topic-subscription): {{
    - Subscription}}
  [Tags](#cfn-sns-topic-tags): {{
    - Tag}}
  [TopicName](#cfn-sns-topic-topicname): {{String}}
  [TracingConfig](#cfn-sns-topic-tracingconfig): {{String}}
```

## Properties
<a name="aws-resource-sns-topic-properties"></a>

`ArchivePolicy`  <a name="cfn-sns-topic-archivepolicy"></a>
The `ArchivePolicy` determines the number of days Amazon SNS retains messages in FIFO topics. You can set a retention period ranging from 1 to 365 days. This property is only applicable to FIFO topics; attempting to use it with standard topics will result in a creation failure.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentBasedDeduplication`  <a name="cfn-sns-topic-contentbaseddeduplication"></a>
`ContentBasedDeduplication` enables deduplication of messages based on their content for FIFO topics. By default, this property is set to false. If you create a FIFO topic with `ContentBasedDeduplication` set to false, you must provide a `MessageDeduplicationId` for each `Publish` action. When set to true, Amazon SNS automatically generates a `MessageDeduplicationId` using a SHA-256 hash of the message body (excluding message attributes). You can optionally override this generated value by specifying a `MessageDeduplicationId` in the `Publish` action. Note that this property only applies to FIFO topics; using it with standard topics will cause the creation to fail.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataProtectionPolicy`  <a name="cfn-sns-topic-dataprotectionpolicy"></a>
The body of the policy document you want to use for this topic.
You can only add one policy per topic.
The policy must be in JSON string format.
Length Constraints: Maximum length of 30,720.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliveryStatusLogging`  <a name="cfn-sns-topic-deliverystatuslogging"></a>
The `DeliveryStatusLogging` configuration enables you to log the delivery status of messages sent from your Amazon SNS topic to subscribed endpoints with the following supported delivery protocols:
+ HTTP
+ Amazon Kinesis Data Firehose
+ AWS Lambda
+ Platform application endpoint
+ Amazon Simple Queue Service
Once configured, log entries are sent to Amazon CloudWatch Logs.
*Required*: No
*Type*: Array of [LoggingConfig](aws-properties-sns-topic-loggingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-sns-topic-displayname"></a>
The display name to use for an Amazon SNS topic with SMS subscriptions. The display name must be maximum 100 characters long, including hyphens (-), underscores (\_), spaces, and tabs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FifoThroughputScope`  <a name="cfn-sns-topic-fifothroughputscope"></a>
Specifies the throughput quota and deduplication behavior to apply for the FIFO topic. Valid values are `Topic` or `MessageGroup`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FifoTopic`  <a name="cfn-sns-topic-fifotopic"></a>
Set to true to create a FIFO topic.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsMasterKeyId`  <a name="cfn-sns-topic-kmsmasterkeyid"></a>
The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms). For more examples, see ` [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) ` in the *AWS Key Management Service API Reference*.
This property applies only to [server-side-encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SignatureVersion`  <a name="cfn-sns-topic-signatureversion"></a>
The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, `SignatureVersion` is set to `1`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subscription`  <a name="cfn-sns-topic-subscription"></a>
The Amazon SNS subscriptions (endpoints) for this topic.
If you specify the `Subscription` property in the `AWS::SNS::Topic` resource and it creates an associated subscription resource, the associated subscription is not deleted when the `AWS::SNS::Topic` resource is deleted.
*Required*: No
*Type*: [Array](aws-properties-sns-topic-subscription.md) of [Subscription](aws-properties-sns-topic-subscription.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sns-topic-tags"></a>
The list of tags to add to a new topic.
To be able to tag a topic on creation, you must have the `sns:CreateTopic` and `sns:TagResource` permissions.
*Required*: No
*Type*: Array of [Tag](aws-properties-sns-topic-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicName`  <a name="cfn-sns-topic-topicname"></a>
The name of the topic you want to create. Topic names must include only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long. FIFO topic names must end with `.fifo`.
If you don't specify a name, CloudFormation generates a unique physical ID and uses that ID for the topic name. For more information, see [Name type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).
If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TracingConfig`  <a name="cfn-sns-topic-tracingconfig"></a>
Tracing mode of an Amazon SNS topic. By default `TracingConfig` is set to `PassThrough`, and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to `Active`, Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sns-topic-return-values"></a>

### Ref
<a name="aws-resource-sns-topic-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the topic ARN, for example: `arn:aws:sns:us-east-1:123456789012:mystack-mytopic-NZJ5JSMVGFIE`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sns-topic-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sns-topic-return-values-fn--getatt-fn--getatt"></a>

`TopicArn`  <a name="TopicArn-fn::getatt"></a>
Returns the ARN of an Amazon SNS topic.

`TopicName`  <a name="TopicName-fn::getatt"></a>
Returns the name of an Amazon SNS topic.

## Examples
<a name="aws-resource-sns-topic--examples"></a>

### An Amazon SNS topic with two Amazon SQS queue subscriptions
<a name="aws-resource-sns-topic--examples--An_Amazon_SNS_topic_with_two_Amazon_SQS_queue_subscriptions"></a>

#### JSON
<a name="aws-resource-sns-topic--examples--An_Amazon_SNS_topic_with_two_Amazon_SQS_queue_subscriptions--json"></a>

```
{
  "MySNSTopic": {
    "Type": "AWS::SNS::Topic",
    "Properties": {
      "Subscription": [
        {
          "Endpoint": {
            "Fn::GetAtt": [
              "MyQueue1",
              "Arn"
            ]
          },
          "Protocol": "sqs"
        },
        {
          "Endpoint": {
            "Fn::GetAtt": [
              "MyQueue2",
              "Arn"
            ]
          },
          "Protocol": "sqs"
        }
      ],
      "TopicName": "SampleTopic",
      "ArchivePolicy": {
      "MessageRetentionPeriod": "7"
      }
    }
  },
  "Outputs": {
    "TopicArn": {
      "Description": "The ARN of the created SNS topic",
      "Value": {
        "Ref": "MySNSTopic"
      }
    },
    "TopicName": {
      "Description": "The name of the created SNS topic",
      "Value": "SampleTopic"
    }
  }
}
```

#### YAML
<a name="aws-resource-sns-topic--examples--An_Amazon_SNS_topic_with_two_Amazon_SQS_queue_subscriptions--yaml"></a>

```
MySNSTopic:
  Type: AWS::SNS::Topic
  Properties:
    Subscription:
      - Endpoint:
          Fn::GetAtt:
            - "MyQueue1"
            - "Arn"
        Protocol: "sqs"
      - Endpoint:
          Fn::GetAtt:
            - "MyQueue2"
            - "Arn"
        Protocol: "sqs"
    TopicName: "SampleTopic"
    ArchivePolicy:
      MessageRetentionPeriod: "7"

Outputs:
  TopicArn:
    Description: The ARN of the created SNS topic
    Value: !Ref MySNSTopic
  TopicName:
    Description: The name of the created SNS topic
    Value: "SampleTopic"
```

## See also
<a name="aws-resource-sns-topic--seealso"></a>
+ [Using an CloudFormation template to create a topic that sends messages to Amazon SQS queues](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToSQS.cloudformation.html) in the *Amazon SNS Developer Guide*
+ The [Using CloudFormation](https://docs.aws.amazon.com/sns/latest/dg/fifo-topic-code-examples.html#fifo-topic-cfn) code example for FIFO topics in the *Amazon SNS Developer Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
