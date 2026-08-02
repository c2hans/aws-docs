---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-snsaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet SnsAction
<a name="aws-properties-ses-mailmanagerruleset-snsaction"></a>

The action to publish the email content to an Amazon SNS topic. When executed, this action will send the email as a notification to the specified SNS topic.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-snsaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-snsaction-syntax.json"></a>

```
{
  "[ActionFailurePolicy](#cfn-ses-mailmanagerruleset-snsaction-actionfailurepolicy)" : {{String}},
  "[Encoding](#cfn-ses-mailmanagerruleset-snsaction-encoding)" : {{String}},
  "[PayloadType](#cfn-ses-mailmanagerruleset-snsaction-payloadtype)" : {{String}},
  "[RoleArn](#cfn-ses-mailmanagerruleset-snsaction-rolearn)" : {{String}},
  "[TopicArn](#cfn-ses-mailmanagerruleset-snsaction-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-snsaction-syntax.yaml"></a>

```
  [ActionFailurePolicy](#cfn-ses-mailmanagerruleset-snsaction-actionfailurepolicy): {{String}}
  [Encoding](#cfn-ses-mailmanagerruleset-snsaction-encoding): {{String}}
  [PayloadType](#cfn-ses-mailmanagerruleset-snsaction-payloadtype): {{String}}
  [RoleArn](#cfn-ses-mailmanagerruleset-snsaction-rolearn): {{String}}
  [TopicArn](#cfn-ses-mailmanagerruleset-snsaction-topicarn): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-snsaction-properties"></a>

`ActionFailurePolicy`  <a name="cfn-ses-mailmanagerruleset-snsaction-actionfailurepolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, specified SNS topic has been deleted or the role lacks necessary permissions to call the `sns:Publish` API.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Encoding`  <a name="cfn-ses-mailmanagerruleset-snsaction-encoding"></a>
The encoding to use for the email within the Amazon SNS notification. The default value is `UTF-8`. Use `BASE64` if you need to preserve all special characters, especially when the original message uses a different encoding format.
*Required*: No
*Type*: String
*Allowed values*: `UTF-8 | BASE64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PayloadType`  <a name="cfn-ses-mailmanagerruleset-snsaction-payloadtype"></a>
The expected payload type within the Amazon SNS notification. `CONTENT` attempts to publish the full email content with 20KB of headers content. `HEADERS` extracts up to 100KB of header content to include in the notification, email content will not be included to the notification. The default value is `CONTENT`.
*Required*: No
*Type*: String
*Allowed values*: `CONTENT | HEADERS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ses-mailmanagerruleset-snsaction-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM Role to use while writing to Amazon SNS. This role must have access to the `sns:Publish` API for the given topic.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicArn`  <a name="cfn-ses-mailmanagerruleset-snsaction-topicarn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS Topic to which notification for the email received will be published.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc):sns:[a-z]{2}-([a-z]+-)+\d{1}:\d{12}:[\w\-]{1,256}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
