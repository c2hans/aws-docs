---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-fleet-scalingconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Fleet ScalingConfigurationInput
<a name="aws-properties-codebuild-fleet-scalingconfigurationinput"></a>

The scaling configuration input of a compute fleet.

## Syntax
<a name="aws-properties-codebuild-fleet-scalingconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-fleet-scalingconfigurationinput-syntax.json"></a>

```
{
  "[MaxCapacity](#cfn-codebuild-fleet-scalingconfigurationinput-maxcapacity)" : {{Integer}},
  "[ScalingType](#cfn-codebuild-fleet-scalingconfigurationinput-scalingtype)" : {{String}},
  "[TargetTrackingScalingConfigs](#cfn-codebuild-fleet-scalingconfigurationinput-targettrackingscalingconfigs)" : {{[ TargetTrackingScalingConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-codebuild-fleet-scalingconfigurationinput-syntax.yaml"></a>

```
  [MaxCapacity](#cfn-codebuild-fleet-scalingconfigurationinput-maxcapacity): {{Integer}}
  [ScalingType](#cfn-codebuild-fleet-scalingconfigurationinput-scalingtype): {{String}}
  [TargetTrackingScalingConfigs](#cfn-codebuild-fleet-scalingconfigurationinput-targettrackingscalingconfigs): {{
    - TargetTrackingScalingConfiguration}}
```

## Properties
<a name="aws-properties-codebuild-fleet-scalingconfigurationinput-properties"></a>

`MaxCapacity`  <a name="cfn-codebuild-fleet-scalingconfigurationinput-maxcapacity"></a>
The maximum number of instances in the ﬂeet when auto-scaling.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingType`  <a name="cfn-codebuild-fleet-scalingconfigurationinput-scalingtype"></a>
The scaling type for a compute fleet.
*Required*: No
*Type*: String
*Allowed values*: `TARGET_TRACKING_SCALING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetTrackingScalingConfigs`  <a name="cfn-codebuild-fleet-scalingconfigurationinput-targettrackingscalingconfigs"></a>
A list of `TargetTrackingScalingConfiguration` objects.
*Required*: No
*Type*: Array of [TargetTrackingScalingConfiguration](aws-properties-codebuild-fleet-targettrackingscalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
