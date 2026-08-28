---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-metricconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service MetricConfiguration
<a name="aws-properties-ecs-service-metricconfiguration"></a>

The configuration for a specific set of metrics to collect for a service.

## Syntax
<a name="aws-properties-ecs-service-metricconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-metricconfiguration-syntax.json"></a>

```
{
  "[MetricNames](#cfn-ecs-service-metricconfiguration-metricnames)" : {{[ String, ... ]}},
  "[ResolutionSeconds](#cfn-ecs-service-metricconfiguration-resolutionseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-service-metricconfiguration-syntax.yaml"></a>

```
  [MetricNames](#cfn-ecs-service-metricconfiguration-metricnames): {{
    - String}}
  [ResolutionSeconds](#cfn-ecs-service-metricconfiguration-resolutionseconds): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-service-metricconfiguration-properties"></a>

`MetricNames`  <a name="cfn-ecs-service-metricconfiguration-metricnames"></a>
The list of metric names to configure. The supported metric names are `CPUUtilization` and `MemoryUtilization`.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `CPUUtilization | MemoryUtilization`
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResolutionSeconds`  <a name="cfn-ecs-service-metricconfiguration-resolutionseconds"></a>
The resolution, in seconds, at which to collect the metrics. The valid values are `20` and `60`.
*Required*: Yes
*Type*: Integer
*Allowed values*: `20 | 60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
