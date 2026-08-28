---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-componentversion-lambdaeventsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::ComponentVersion LambdaEventSource
<a name="aws-properties-greengrassv2-componentversion-lambdaeventsource"></a>

Contains information about an event source for an AWS Lambda function. The event source defines the topics on which this Lambda function subscribes to receive messages that run the function.

## Syntax
<a name="aws-properties-greengrassv2-componentversion-lambdaeventsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-componentversion-lambdaeventsource-syntax.json"></a>

```
{
  "[Topic](#cfn-greengrassv2-componentversion-lambdaeventsource-topic)" : {{String}},
  "[Type](#cfn-greengrassv2-componentversion-lambdaeventsource-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrassv2-componentversion-lambdaeventsource-syntax.yaml"></a>

```
  [Topic](#cfn-greengrassv2-componentversion-lambdaeventsource-topic): {{String}}
  [Type](#cfn-greengrassv2-componentversion-lambdaeventsource-type): {{String}}
```

## Properties
<a name="aws-properties-greengrassv2-componentversion-lambdaeventsource-properties"></a>

`Topic`  <a name="cfn-greengrassv2-componentversion-lambdaeventsource-topic"></a>
The topic to which to subscribe to receive event messages.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-greengrassv2-componentversion-lambdaeventsource-type"></a>
The type of event source. Choose from the following options:
+ `PUB_SUB` – Subscribe to local publish/subscribe messages. This event source type doesn't support MQTT wildcards (`+` and `#`) in the event source topic.
+ `IOT_CORE` – Subscribe to AWS IoT Core MQTT messages. This event source type supports MQTT wildcards (`+` and `#`) in the event source topic.
*Required*: No
*Type*: String
*Allowed values*: `PUB_SUB | IOT_CORE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
