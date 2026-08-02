---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-monitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service MonitoringConfiguration
<a name="aws-properties-ecs-service-monitoringconfiguration"></a>

The optional monitoring configuration for a service, which defines the resolution for the service-level `CPUUtilization` and `MemoryUtilization` Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of `60` seconds.

## Syntax
<a name="aws-properties-ecs-service-monitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-monitoringconfiguration-syntax.json"></a>

```
{
  "[MetricConfigurations](#cfn-ecs-service-monitoringconfiguration-metricconfigurations)" : {{[ MetricConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-service-monitoringconfiguration-syntax.yaml"></a>

```
  [MetricConfigurations](#cfn-ecs-service-monitoringconfiguration-metricconfigurations): {{
    - MetricConfiguration}}
```

## Properties
<a name="aws-properties-ecs-service-monitoringconfiguration-properties"></a>

`MetricConfigurations`  <a name="cfn-ecs-service-monitoringconfiguration-metricconfigurations"></a>
The list of metric configurations for the service monitoring.
*Required*: Yes
*Type*: Array of [MetricConfiguration](aws-properties-ecs-service-metricconfiguration.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
