---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-notificationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup NotificationConfiguration
<a name="aws-properties-autoscaling-autoscalinggroup-notificationconfiguration"></a>

A structure that specifies an Amazon SNS notification configuration for the `NotificationConfigurations` property of the [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html) resource.

For an example template snippet, see [Configure Amazon EC2 Auto Scaling resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2-auto-scaling.html).

For more information, see [Get Amazon SNS notifications when your Auto Scaling group scales](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-notificationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-notificationconfiguration-syntax.json"></a>

```
{
  "[NotificationTypes](#cfn-autoscaling-autoscalinggroup-notificationconfiguration-notificationtypes)" : {{[ String, ... ]}},
  "[TopicARN](#cfn-autoscaling-autoscalinggroup-notificationconfiguration-topicarn)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-notificationconfiguration-syntax.yaml"></a>

```
  [NotificationTypes](#cfn-autoscaling-autoscalinggroup-notificationconfiguration-notificationtypes): {{
    - String}}
  [TopicARN](#cfn-autoscaling-autoscalinggroup-notificationconfiguration-topicarn): {{
    - String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-notificationconfiguration-properties"></a>

`NotificationTypes`  <a name="cfn-autoscaling-autoscalinggroup-notificationconfiguration-notificationtypes"></a>
A list of event types that send a notification. Event types can include any of the following types.
*Allowed values*:
+  `autoscaling:EC2_INSTANCE_LAUNCH`
+  `autoscaling:EC2_INSTANCE_LAUNCH_ERROR`
+  `autoscaling:EC2_INSTANCE_TERMINATE`
+  `autoscaling:EC2_INSTANCE_TERMINATE_ERROR`
+  `autoscaling:TEST_NOTIFICATION`
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicARN`  <a name="cfn-autoscaling-autoscalinggroup-notificationconfiguration-topicarn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS topic.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
