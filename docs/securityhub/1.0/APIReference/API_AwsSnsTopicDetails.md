---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSnsTopicDetails.html
---

# AwsSnsTopicDetails
<a name="API_AwsSnsTopicDetails"></a>

Provides information about an Amazon SNS topic to which notifications can be published.

## Contents
<a name="API_AwsSnsTopicDetails_Contents"></a>

 ** ApplicationSuccessFeedbackRoleArn **   <a name="securityhub-Type-AwsSnsTopicDetails-ApplicationSuccessFeedbackRoleArn"></a>
Indicates failed message delivery status for an Amazon SNS topic that is subscribed to a platform application endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FirehoseFailureFeedbackRoleArn **   <a name="securityhub-Type-AwsSnsTopicDetails-FirehoseFailureFeedbackRoleArn"></a>
Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon Kinesis Data Firehose endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FirehoseSuccessFeedbackRoleArn **   <a name="securityhub-Type-AwsSnsTopicDetails-FirehoseSuccessFeedbackRoleArn"></a>
Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon Kinesis Data Firehose endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HttpFailureFeedbackRoleArn **   <a name="securityhub-Type-AwsSnsTopicDetails-HttpFailureFeedbackRoleArn"></a>
Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HttpSuccessFeedbackRoleArn **   <a name="securityhub-Type-AwsSnsTopicDetails-HttpSuccessFeedbackRoleArn"></a>
Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KmsMasterKeyId **   <a name="securityhub-Type-AwsSnsTopicDetails-KmsMasterKeyId"></a>
The ID of an AWS managed key for Amazon SNS or a customer managed key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Owner **   <a name="securityhub-Type-AwsSnsTopicDetails-Owner"></a>
The subscription's owner.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SqsFailureFeedbackRoleArn **   <a name="securityhub-Type-AwsSnsTopicDetails-SqsFailureFeedbackRoleArn"></a>
Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SqsSuccessFeedbackRoleArn **   <a name="securityhub-Type-AwsSnsTopicDetails-SqsSuccessFeedbackRoleArn"></a>
Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Subscription **   <a name="securityhub-Type-AwsSnsTopicDetails-Subscription"></a>
Subscription is an embedded property that describes the subscription endpoints of an Amazon SNS topic.
Type: Array of [AwsSnsTopicSubscription](API_AwsSnsTopicSubscription.md) objects
Required: No

 ** TopicName **   <a name="securityhub-Type-AwsSnsTopicDetails-TopicName"></a>
The name of the Amazon SNS topic.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsSnsTopicDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsSnsTopicDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsSnsTopicDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsSnsTopicDetails)
