---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html
---

# CreateTopic
<a name="API_CreateTopic"></a>

Creates a topic to which notifications can be published. Users can create at most 100,000 standard topics (at most 1,000 FIFO topics). For more information, see [Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) in the *Amazon SNS Developer Guide*. This action is idempotent, so if the requester already owns a topic with the specified name, that topic's ARN is returned without creating a new topic.

## Request Parameters
<a name="API_CreateTopic_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Attributes** Attributes.entry.N.key (key)Attributes.entry.N.value (value)
A map of attributes with their corresponding values.
The following lists names, descriptions, and values of the special request parameters that the `CreateTopic` action uses:
+  `DeliveryPolicy` – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
+  `DisplayName` – The display name to use for a topic with SMS, `email`, and `email-json` subscriptions. For `email` and `email-json` subscriptions, the display name is used as the sender name for regular notification messages. Subscription confirmation and unsubscribe confirmation emails always use "AWS Notifications" as the sender name.
+  `Policy` – The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.
+  `TracingConfig` – Tracing mode of an Amazon SNS topic. By default `TracingConfig` is set to `PassThrough`, and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to `Active`, Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. This is only supported on standard topics.
+ HTTP
  +  `HTTPSuccessFeedbackRoleArn` – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint.
  +  `HTTPSuccessFeedbackSampleRate` – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an HTTP endpoint.
  +  `HTTPFailureFeedbackRoleArn` – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint.
+ Amazon Data Firehose
  +  `FirehoseSuccessFeedbackRoleArn` – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint.
  +  `FirehoseSuccessFeedbackSampleRate` – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint.
  +  `FirehoseFailureFeedbackRoleArn` – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint.
+  AWS Lambda
  +  `LambdaSuccessFeedbackRoleArn` – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an AWS Lambda endpoint.
  +  `LambdaSuccessFeedbackSampleRate` – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an AWS Lambda endpoint.
  +  `LambdaFailureFeedbackRoleArn` – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an AWS Lambda endpoint.
+ Platform application endpoint
  +  `ApplicationSuccessFeedbackRoleArn` – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to a platform application endpoint.
  +  `ApplicationSuccessFeedbackSampleRate` – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an platform application endpoint.
  +  `ApplicationFailureFeedbackRoleArn` – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an platform application endpoint.
**Note**
In addition to being able to configure topic attributes for message delivery status of notification messages sent to Amazon SNS application endpoints, you can also configure application attributes for the delivery status of push notification messages sent to push notification services.
For example, For more information, see [Using Amazon SNS Application Attributes for Message Delivery Status](https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html).
+ Amazon SQS
  +  `SQSSuccessFeedbackRoleArn` – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint.
  +  `SQSSuccessFeedbackSampleRate` – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint.
  +  `SQSFailureFeedbackRoleArn` – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint.
The <ENDPOINT>SuccessFeedbackRoleArn and <ENDPOINT>FailureFeedbackRoleArn attributes are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The <ENDPOINT>SuccessFeedbackSampleRate attribute is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the <ENDPOINT>FailureFeedbackRoleArn attribute, then all failed message deliveries generate CloudWatch Logs.
The following attribute applies only to [server-side encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html):
+  `KmsMasterKeyId` – The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms). For more examples, see [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) in the * AWS Key Management Service API Reference*.
The following attributes apply only to [FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html):
+  `ArchivePolicy` – The policy that sets the retention period for messages stored in the message archive of an Amazon SNS FIFO topic.
+  `ContentBasedDeduplication` – Enables content-based deduplication for FIFO topics.
  + By default, `ContentBasedDeduplication` is set to `false`. If you create a FIFO topic and this attribute is `false`, you must specify a value for the `MessageDeduplicationId` parameter for the [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) action.
  + When you set `ContentBasedDeduplication` to `true`, Amazon SNS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).

    (Optional) To override the generated value, you can specify a value for the `MessageDeduplicationId` parameter for the `Publish` action.
+  `FifoThroughputScope` – Enables higher throughput for your FIFO topic by adjusting the scope of deduplication. This attribute has two possible values:
  +  `Topic` – The scope of message deduplication is across the entire topic. This is the default value and maintains existing behavior, with a maximum throughput of 3000 messages per second or 20MB per second, whichever comes first.
  +  `MessageGroup` – The scope of deduplication is within each individual message group, which enables higher throughput per topic subject to regional quotas. For more information on quotas or to request an increase, see [Amazon SNS service quotas](https://docs.aws.amazon.com/general/latest/gr/sns.html) in the Amazon Web Services General Reference.
Type: String to string map
Required: No

 ** DataProtectionPolicy **
Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see [Amazon SNS message data protection availability change](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html).
The body of the policy document you want to use for this topic.
You can only add one policy per topic.
The policy must be in JSON string format.
Length Constraints: Maximum length of 30,720.
Type: String
Required: No

 ** Name **
The name of the topic you want to create.
Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.
For a FIFO (first-in-first-out) topic, the name must end with the `.fifo` suffix.
Type: String
Required: Yes

 **Tags.member.N**
The list of tags to add to a new topic.
To be able to tag a topic on creation, you must have the `sns:CreateTopic` and `sns:TagResource` permissions.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CreateTopic_ResponseElements"></a>

The following element is returned by the service.

 ** TopicArn **
The Amazon Resource Name (ARN) assigned to the created topic.
Type: String

## Errors
<a name="API_CreateTopic_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** ConcurrentAccess **
Can't perform multiple operations on a tag simultaneously. Perform the operations sequentially.
HTTP Status Code: 400

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** InvalidSecurity **
The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.
HTTP Status Code: 403

 ** StaleTag **
A tag has been added to a resource with the same ARN as a deleted resource. Wait a short while and then retry the operation.
HTTP Status Code: 400

 ** TagLimitExceeded **
Can't add more than 50 tags to a topic.
HTTP Status Code: 400

 ** TagPolicy **
The request doesn't comply with the IAM tag policy. Correct your request and then retry it.
HTTP Status Code: 400

 ** TopicLimitExceeded **
Indicates that the customer already owns the maximum allowed number of topics.
HTTP Status Code: 403

## Examples
<a name="API_CreateTopic_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_CreateTopic_Example_1"></a>

This example illustrates one usage of CreateTopic.

#### Sample Request
<a name="API_CreateTopic_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=CreateTopic
&Name=My-Topic
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateTopic_Example_1_Response"></a>

```
<CreateTopicResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <CreateTopicResult>
        <TopicArn>arn:aws:sns:us-east-2:123456789012:My-Topic</TopicArn>
    </CreateTopicResult>
    <ResponseMetadata>
        <RequestId>a8dec8b3-33a4-11df-8963-01868b7c937a</RequestId>
    </ResponseMetadata>
</CreateTopicResponse>
```

## See Also
<a name="API_CreateTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/CreateTopic)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/CreateTopic)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/CreateTopic)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/CreateTopic)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/CreateTopic)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/CreateTopic)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/CreateTopic)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/CreateTopic)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/CreateTopic)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/CreateTopic)
