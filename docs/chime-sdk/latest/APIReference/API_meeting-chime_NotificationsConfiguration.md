---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_NotificationsConfiguration.html
---

# NotificationsConfiguration
<a name="API_meeting-chime_NotificationsConfiguration"></a>

The configuration for resource targets to receive notifications when meeting and attendee events occur.

## Contents
<a name="API_meeting-chime_NotificationsConfiguration_Contents"></a>

 ** LambdaFunctionArn **   <a name="chimesdk-Type-meeting-chime_NotificationsConfiguration-LambdaFunctionArn"></a>
The ARN of the AWS Lambda function in the notifications configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** SnsTopicArn **   <a name="chimesdk-Type-meeting-chime_NotificationsConfiguration-SnsTopicArn"></a>
The ARN of the SNS topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** SqsQueueArn **   <a name="chimesdk-Type-meeting-chime_NotificationsConfiguration-SqsQueueArn"></a>
The ARN of the SQS queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

## See Also
<a name="API_meeting-chime_NotificationsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/NotificationsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/NotificationsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/NotificationsConfiguration)
