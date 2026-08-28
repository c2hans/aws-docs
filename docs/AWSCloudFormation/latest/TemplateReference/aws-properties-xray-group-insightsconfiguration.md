---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-xray-group-insightsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::XRay::Group InsightsConfiguration
<a name="aws-properties-xray-group-insightsconfiguration"></a>

The structure containing configurations related to insights.

## Syntax
<a name="aws-properties-xray-group-insightsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-xray-group-insightsconfiguration-syntax.json"></a>

```
{
  "[InsightsEnabled](#cfn-xray-group-insightsconfiguration-insightsenabled)" : {{Boolean}},
  "[NotificationsEnabled](#cfn-xray-group-insightsconfiguration-notificationsenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-xray-group-insightsconfiguration-syntax.yaml"></a>

```
  [InsightsEnabled](#cfn-xray-group-insightsconfiguration-insightsenabled): {{Boolean}}
  [NotificationsEnabled](#cfn-xray-group-insightsconfiguration-notificationsenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-xray-group-insightsconfiguration-properties"></a>

`InsightsEnabled`  <a name="cfn-xray-group-insightsconfiguration-insightsenabled"></a>
Set the InsightsEnabled value to true to enable insights or false to disable insights.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationsEnabled`  <a name="cfn-xray-group-insightsconfiguration-notificationsenabled"></a>
Set the NotificationsEnabled value to true to enable insights notifications. Notifications can only be enabled on a group with InsightsEnabled set to true.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
