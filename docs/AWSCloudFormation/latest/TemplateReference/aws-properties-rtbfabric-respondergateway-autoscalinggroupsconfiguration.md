---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::ResponderGateway AutoScalingGroupsConfiguration
<a name="aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration"></a>

Describes the configuration of an auto scaling group.

## Syntax
<a name="aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration-syntax.json"></a>

```
{
  "[AutoScalingGroupNameList](#cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-autoscalinggroupnamelist)" : {{[ String, ... ]}},
  "[HealthCheckConfig](#cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-healthcheckconfig)" : {{HealthCheckConfig}},
  "[RoleArn](#cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration-syntax.yaml"></a>

```
  [AutoScalingGroupNameList](#cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-autoscalinggroupnamelist): {{
    - String}}
  [HealthCheckConfig](#cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-healthcheckconfig): {{
    HealthCheckConfig}}
  [RoleArn](#cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration-properties"></a>

`AutoScalingGroupNameList`  <a name="cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-autoscalinggroupnamelist"></a>
The names of the auto scaling group.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`HealthCheckConfig`  <a name="cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-healthcheckconfig"></a>
Property description not available.
*Required*: No
*Type*: [HealthCheckConfig](aws-properties-rtbfabric-respondergateway-healthcheckconfig.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`RoleArn`  <a name="cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-rolearn"></a>
The role ARN of the auto scaling group.
*Required*: Yes
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
