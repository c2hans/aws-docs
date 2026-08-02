---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketNotificationConfigurationDetail.html
---

# AwsS3BucketNotificationConfigurationDetail
<a name="API_AwsS3BucketNotificationConfigurationDetail"></a>

Details for an S3 bucket notification configuration.

## Contents
<a name="API_AwsS3BucketNotificationConfigurationDetail_Contents"></a>

 ** Destination **   <a name="securityhub-Type-AwsS3BucketNotificationConfigurationDetail-Destination"></a>
The ARN of the Lambda function, Amazon SQS queue, or Amazon SNS topic that generates the notification.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Events **   <a name="securityhub-Type-AwsS3BucketNotificationConfigurationDetail-Events"></a>
The list of events that trigger a notification.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Filter **   <a name="securityhub-Type-AwsS3BucketNotificationConfigurationDetail-Filter"></a>
The filters that determine which S3 buckets generate notifications.
Type: [AwsS3BucketNotificationConfigurationFilter](API_AwsS3BucketNotificationConfigurationFilter.md) object
Required: No

 ** Type **   <a name="securityhub-Type-AwsS3BucketNotificationConfigurationDetail-Type"></a>
Indicates the type of notification. Notifications can be generated using Lambda functions, Amazon SQS queues, or Amazon SNS topics, with corresponding valid values as follows:
+  `LambdaConfiguration`
+  `QueueConfiguration`
+  `TopicConfiguration`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketNotificationConfigurationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketNotificationConfigurationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketNotificationConfigurationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketNotificationConfigurationDetail)
