---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_SetTopicAttributes.html
---

# SetTopicAttributes
<a name="API_SetTopicAttributes"></a>

Allows a topic owner to set an attribute of the topic to a new value.

**Note**
To remove the ability to change topic permissions, you must deny permissions to the `AddPermission`, `RemovePermission`, and `SetTopicAttributes` actions in your IAM policy.

## Request Parameters
<a name="API_SetTopicAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AttributeName **
A map of attributes with their corresponding values.
The following lists the names, descriptions, and values of the special request parameters that the `SetTopicAttributes` action uses:
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
  +  `ApplicationSuccessFeedbackRoleArn` – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an platform application endpoint.
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
The following attribute applies only to [server-side-encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html):
+  `KmsMasterKeyId` – The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms). For more examples, see [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) in the * AWS Key Management Service API Reference*.
+  `SignatureVersion` – The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, `SignatureVersion` is set to `1`.
The following attribute applies only to [FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html):
+  `ArchivePolicy` – The policy that sets the retention period for messages stored in the message archive of an Amazon SNS FIFO topic.
+  `ContentBasedDeduplication` – Enables content-based deduplication for FIFO topics.
  + By default, `ContentBasedDeduplication` is set to `false`. If you create a FIFO topic and this attribute is `false`, you must specify a value for the `MessageDeduplicationId` parameter for the [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) action.
  + When you set `ContentBasedDeduplication` to `true`, Amazon SNS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).

    (Optional) To override the generated value, you can specify a value for the `MessageDeduplicationId` parameter for the `Publish` action.
+  `FifoThroughputScope` – Enables higher throughput for your FIFO topic by adjusting the scope of deduplication. This attribute has two possible values:
  +  `Topic` – The scope of message deduplication is across the entire topic. This is the default value and maintains existing behavior, with a maximum throughput of 3000 messages per second or 20MB per second, whichever comes first.
  +  `MessageGroup` – The scope of deduplication is within each individual message group, which enables higher throughput per topic subject to regional quotas. For more information on quotas or to request an increase, see [Amazon SNS service quotas](https://docs.aws.amazon.com/general/latest/gr/sns.html) in the Amazon Web Services General Reference.
Type: String
Required: Yes

 ** AttributeValue **
The new value for the attribute.
Type: String
Required: No

 ** TopicArn **
The ARN of the topic to modify.
Type: String
Required: Yes

## Errors
<a name="API_SetTopicAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** InvalidSecurity **
The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.
HTTP Status Code: 403

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

## Examples
<a name="API_SetTopicAttributes_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_SetTopicAttributes_Example_1"></a>

The following example sets the `DisplayName` attribute to `MyTopicName`.

#### Sample Request
<a name="API_SetTopicAttributes_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=SetTopicAttributes
&TopicArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic
&AttributeName=DisplayName
&AttributeValue=MyTopicName
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_SetTopicAttributes_Example_1_Response"></a>

```
<SetTopicAttributesResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>a8763b99-33a7-11df-a9b7-05d48da6f042</RequestId>
    </ResponseMetadata>
</SetTopicAttributesResponse>
```

### Example
<a name="API_SetTopicAttributes_Example_2"></a>

The following example sets the delivery policy to 5 retries.

The JSON format for `AttributeValue` is as follows. For more information on the `DeliveryPolicy` topic attribute, see [Creating an HTTP/S delivery policy](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html#creating-delivery-policy).

```
"http": {
    "defaultHealthyRetryPolicy": {
        "minDelayTarget": <int>,
        "maxDelayTarget": <int>,
        "numRetries": <int>,
        "numMaxDelayRetries": <int>,
        "backoffFunction": "<linear|arithmetic|geometric|exponential>"
    },
    "disableSubscriptionOverrides": <boolean>,
    "defaultThrottlePolicy": {
        "maxReceivesPerSecond": <int>
    },
    "defaultRequestPolicy" : {
        "headerContentType" : "<text/plain | application/json | application/xml>"
    }
}
```

## See Also
<a name="API_SetTopicAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/SetTopicAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/SetTopicAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/SetTopicAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/SetTopicAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/SetTopicAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/SetTopicAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/SetTopicAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/SetTopicAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/SetTopicAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/SetTopicAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
