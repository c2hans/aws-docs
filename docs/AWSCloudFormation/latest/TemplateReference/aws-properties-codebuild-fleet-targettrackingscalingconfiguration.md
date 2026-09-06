---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-fleet-targettrackingscalingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Fleet TargetTrackingScalingConfiguration
<a name="aws-properties-codebuild-fleet-targettrackingscalingconfiguration"></a>

Defines when a new instance is auto-scaled into the compute fleet.

## Syntax
<a name="aws-properties-codebuild-fleet-targettrackingscalingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-fleet-targettrackingscalingconfiguration-syntax.json"></a>

```
{
  "[MetricType](#cfn-codebuild-fleet-targettrackingscalingconfiguration-metrictype)" : {{String}},
  "[TargetValue](#cfn-codebuild-fleet-targettrackingscalingconfiguration-targetvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-codebuild-fleet-targettrackingscalingconfiguration-syntax.yaml"></a>

```
  [MetricType](#cfn-codebuild-fleet-targettrackingscalingconfiguration-metrictype): {{String}}
  [TargetValue](#cfn-codebuild-fleet-targettrackingscalingconfiguration-targetvalue): {{Number}}
```

## Properties
<a name="aws-properties-codebuild-fleet-targettrackingscalingconfiguration-properties"></a>

`MetricType`  <a name="cfn-codebuild-fleet-targettrackingscalingconfiguration-metrictype"></a>
The metric type to determine auto-scaling.
*Required*: No
*Type*: String
*Allowed values*: `FLEET_UTILIZATION_RATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetValue`  <a name="cfn-codebuild-fleet-targettrackingscalingconfiguration-targetvalue"></a>
The value of `metricType` when to start scaling.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
