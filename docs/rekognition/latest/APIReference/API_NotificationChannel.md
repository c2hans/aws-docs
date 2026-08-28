---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_NotificationChannel.html
---

# NotificationChannel
<a name="API_NotificationChannel"></a>

The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the completion status of a video analysis operation. For more information, see [Calling Amazon Rekognition Video operations](https://docs.aws.amazon.com/rekognition/latest/dg/api-video.html). Note that the Amazon SNS topic must have a topic name that begins with *AmazonRekognition* if you are using the AmazonRekognitionServiceRole permissions policy to access the topic. For more information, see [Giving access to multiple Amazon SNS topics](https://docs.aws.amazon.com/rekognition/latest/dg/api-video-roles.html#api-video-roles-all-topics).

## Contents
<a name="API_NotificationChannel_Contents"></a>

 ** RoleArn **   <a name="rekognition-Type-NotificationChannel-RoleArn"></a>
The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.
Type: String
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** SNSTopicArn **   <a name="rekognition-Type-NotificationChannel-SNSTopicArn"></a>
The Amazon SNS topic to which Amazon Rekognition posts the completion status.
Type: String
Pattern: `(^arn:aws:sns:.*:\w{12}:.+$)`
Required: Yes

## See Also
<a name="API_NotificationChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/NotificationChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/NotificationChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/NotificationChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
