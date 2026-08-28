---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationseteventdestination-snsdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSetEventDestination SnsDestination
<a name="aws-properties-ses-configurationseteventdestination-snsdestination"></a>

Contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.

Event destinations, such as Amazon SNS, are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html).

## Syntax
<a name="aws-properties-ses-configurationseteventdestination-snsdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationseteventdestination-snsdestination-syntax.json"></a>

```
{
  "[TopicARN](#cfn-ses-configurationseteventdestination-snsdestination-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-configurationseteventdestination-snsdestination-syntax.yaml"></a>

```
  [TopicARN](#cfn-ses-configurationseteventdestination-snsdestination-topicarn): {{String}}
```

## Properties
<a name="aws-properties-ses-configurationseteventdestination-snsdestination-properties"></a>

`TopicARN`  <a name="cfn-ses-configurationseteventdestination-snsdestination-topicarn"></a>
The ARN of the Amazon SNS topic for email sending events. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) Amazon SNS operation.
For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z0-9-]*:sns:[a-z0-9-]+:\d{12}:[^:]+$`
*Minimum*: `36`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
