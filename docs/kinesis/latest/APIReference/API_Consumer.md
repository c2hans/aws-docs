---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Consumer.html
---

# Consumer
<a name="API_Consumer"></a>

An object that represents the details of the consumer you registered. This type of object is returned by [RegisterStreamConsumer](API_RegisterStreamConsumer.md).

## Contents
<a name="API_Consumer_Contents"></a>

 ** ConsumerARN **   <a name="Streams-Type-Consumer-ConsumerARN"></a>
When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this ARN to be able to call [SubscribeToShard](API_SubscribeToShard.md).
If you delete a consumer and then create a new one with the same name, it won't have the same ARN. That's because consumer ARNs contain the creation timestamp. This is important to keep in mind if you have IAM policies that reference consumer ARNs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(arn):aws.*:kinesis:.*:\d{12}:.*stream\/[a-zA-Z0-9_.-]+\/consumer\/[a-zA-Z0-9_.-]+:[0-9]+`
Required: Yes

 ** ConsumerCreationTimestamp **   <a name="Streams-Type-Consumer-ConsumerCreationTimestamp"></a>

Type: Timestamp
Required: Yes

 ** ConsumerName **   <a name="Streams-Type-Consumer-ConsumerName"></a>
The name of the consumer is something you choose when you register the consumer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** ConsumerStatus **   <a name="Streams-Type-Consumer-ConsumerStatus"></a>
A consumer can't read data while in the `CREATING` or `DELETING` states.
Type: String
Valid Values: `CREATING | DELETING | ACTIVE`
Required: Yes

## See Also
<a name="API_Consumer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/Consumer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/Consumer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/Consumer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
