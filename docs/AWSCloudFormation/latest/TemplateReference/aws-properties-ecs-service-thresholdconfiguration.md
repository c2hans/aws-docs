---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-thresholdconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ThresholdConfiguration
<a name="aws-properties-ecs-service-thresholdconfiguration"></a>

Defines the failure threshold that the deployment circuit breaker uses to monitor a deployment. The `type` and `value` together determine the number of task failures that are tolerated before the circuit breaker triggers.

By default, the threshold configuration uses a `type` of `BOUNDED_PERCENT` with a `value` of `50`.

## Syntax
<a name="aws-properties-ecs-service-thresholdconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-thresholdconfiguration-syntax.json"></a>

```
{
  "[Type](#cfn-ecs-service-thresholdconfiguration-type)" : {{String}},
  "[Value](#cfn-ecs-service-thresholdconfiguration-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-service-thresholdconfiguration-syntax.yaml"></a>

```
  [Type](#cfn-ecs-service-thresholdconfiguration-type): {{String}}
  [Value](#cfn-ecs-service-thresholdconfiguration-value): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-service-thresholdconfiguration-properties"></a>

`Type`  <a name="cfn-ecs-service-thresholdconfiguration-type"></a>
Determines how Amazon ECS uses `value` to calculate the failure threshold. For the percentage types (`BOUNDED_PERCENT` and `UNBOUNDED_PERCENT`), Amazon ECS multiplies `value` by the latest service desired count. For `COUNT`, Amazon ECS uses `value` directly as the threshold. The default is `BOUNDED_PERCENT`.
*Required*: Yes
*Type*: String
*Allowed values*: `COUNT | BOUNDED_PERCENT | UNBOUNDED_PERCENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ecs-service-thresholdconfiguration-value"></a>
Specifies the integer that Amazon ECS uses to calculate the failure threshold. When `type` is `COUNT`, this value is the failure threshold itself. When `type` is a percentage type, Amazon ECS multiplies this value by the latest service desired count to produce the failure threshold. The default is `50`.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
