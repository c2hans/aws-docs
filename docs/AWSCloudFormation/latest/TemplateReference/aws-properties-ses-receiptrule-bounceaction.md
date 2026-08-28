---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-receiptrule-bounceaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ReceiptRule BounceAction
<a name="aws-properties-ses-receiptrule-bounceaction"></a>

The action to send a bounce response for the email. When executed, this action generates a non-delivery report (bounce) back to the sender.

## Syntax
<a name="aws-properties-ses-receiptrule-bounceaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-receiptrule-bounceaction-syntax.json"></a>

```
{
  "[Message](#cfn-ses-receiptrule-bounceaction-message)" : {{String}},
  "[Sender](#cfn-ses-receiptrule-bounceaction-sender)" : {{String}},
  "[SmtpReplyCode](#cfn-ses-receiptrule-bounceaction-smtpreplycode)" : {{String}},
  "[StatusCode](#cfn-ses-receiptrule-bounceaction-statuscode)" : {{String}},
  "[TopicArn](#cfn-ses-receiptrule-bounceaction-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-receiptrule-bounceaction-syntax.yaml"></a>

```
  [Message](#cfn-ses-receiptrule-bounceaction-message): {{String}}
  [Sender](#cfn-ses-receiptrule-bounceaction-sender): {{String}}
  [SmtpReplyCode](#cfn-ses-receiptrule-bounceaction-smtpreplycode): {{String}}
  [StatusCode](#cfn-ses-receiptrule-bounceaction-statuscode): {{String}}
  [TopicArn](#cfn-ses-receiptrule-bounceaction-topicarn): {{String}}
```

## Properties
<a name="aws-properties-ses-receiptrule-bounceaction-properties"></a>

`Message`  <a name="cfn-ses-receiptrule-bounceaction-message"></a>
The human-readable text to include in the bounce message.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sender`  <a name="cfn-ses-receiptrule-bounceaction-sender"></a>
The sender email address of the bounce message.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmtpReplyCode`  <a name="cfn-ses-receiptrule-bounceaction-smtpreplycode"></a>
The SMTP reply code for the bounce, as defined by RFC 5321.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusCode`  <a name="cfn-ses-receiptrule-bounceaction-statuscode"></a>
The enhanced status code for the bounce, in the format of x.y.z (e.g. 5.1.1).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicArn`  <a name="cfn-ses-receiptrule-bounceaction-topicarn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) operation in Amazon SNS.
For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
