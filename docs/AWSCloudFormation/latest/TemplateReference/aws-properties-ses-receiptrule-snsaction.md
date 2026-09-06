---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-receiptrule-snsaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ReceiptRule SNSAction
<a name="aws-properties-ses-receiptrule-snsaction"></a>

The action to publish the email content to an Amazon SNS topic. When executed, this action will send the email as a notification to the specified SNS topic.

## Syntax
<a name="aws-properties-ses-receiptrule-snsaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-receiptrule-snsaction-syntax.json"></a>

```
{
  "[Encoding](#cfn-ses-receiptrule-snsaction-encoding)" : {{String}},
  "[TopicArn](#cfn-ses-receiptrule-snsaction-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-receiptrule-snsaction-syntax.yaml"></a>

```
  [Encoding](#cfn-ses-receiptrule-snsaction-encoding): {{String}}
  [TopicArn](#cfn-ses-receiptrule-snsaction-topicarn): {{String}}
```

## Properties
<a name="aws-properties-ses-receiptrule-snsaction-properties"></a>

`Encoding`  <a name="cfn-ses-receiptrule-snsaction-encoding"></a>
The encoding to use for the email within the Amazon SNS notification. The default value is `UTF-8`. Use `BASE64` if you need to preserve all special characters, especially when the original message uses a different encoding format.
*Required*: No
*Type*: String
*Allowed values*: `UTF-8 | Base64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicArn`  <a name="cfn-ses-receiptrule-snsaction-topicarn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS Topic to which notification for the email received will be published.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
