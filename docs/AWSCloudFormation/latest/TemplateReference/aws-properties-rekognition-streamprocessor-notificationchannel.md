---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rekognition-streamprocessor-notificationchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::StreamProcessor NotificationChannel
<a name="aws-properties-rekognition-streamprocessor-notificationchannel"></a>

 The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation. Amazon Rekognition publishes a notification the first time an object of interest or a person is detected in the video stream. Amazon Rekognition also publishes an an end-of-session notification with a summary when the stream processing session is complete. For more information, see [StreamProcessorNotificationChannel](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorNotificationChannel).

## Syntax
<a name="aws-properties-rekognition-streamprocessor-notificationchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rekognition-streamprocessor-notificationchannel-syntax.json"></a>

```
{
  "[Arn](#cfn-rekognition-streamprocessor-notificationchannel-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-rekognition-streamprocessor-notificationchannel-syntax.yaml"></a>

```
  [Arn](#cfn-rekognition-streamprocessor-notificationchannel-arn): {{String}}
```

## Properties
<a name="aws-properties-rekognition-streamprocessor-notificationchannel-properties"></a>

`Arn`  <a name="cfn-rekognition-streamprocessor-notificationchannel-arn"></a>
The ARN of the SNS topic that receives notifications.
*Required*: Yes
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
