---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-instanceplacementconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob InstancePlacementConfig
<a name="aws-properties-sagemaker-hyperparametertuningjob-instanceplacementconfig"></a>

Configuration for how instances are placed and allocated within UltraServers. This is only applicable for UltraServer capacity.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-instanceplacementconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-instanceplacementconfig-syntax.json"></a>

```
{
  "[EnableMultipleJobs](#cfn-sagemaker-hyperparametertuningjob-instanceplacementconfig-enablemultiplejobs)" : {{Boolean}},
  "[PlacementSpecifications](#cfn-sagemaker-hyperparametertuningjob-instanceplacementconfig-placementspecifications)" : {{[ PlacementSpecificationsItems, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-instanceplacementconfig-syntax.yaml"></a>

```
  [EnableMultipleJobs](#cfn-sagemaker-hyperparametertuningjob-instanceplacementconfig-enablemultiplejobs): {{Boolean}}
  [PlacementSpecifications](#cfn-sagemaker-hyperparametertuningjob-instanceplacementconfig-placementspecifications): {{
    - PlacementSpecificationsItems}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-instanceplacementconfig-properties"></a>

`EnableMultipleJobs`  <a name="cfn-sagemaker-hyperparametertuningjob-instanceplacementconfig-enablemultiplejobs"></a>
If set to true, allows multiple jobs to share the same UltraServer instances. If set to false, ensures this job's instances are placed on an UltraServer exclusively, with no other jobs sharing the same UltraServer. Default is false.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlacementSpecifications`  <a name="cfn-sagemaker-hyperparametertuningjob-instanceplacementconfig-placementspecifications"></a>
A list of specifications for how instances should be placed on specific UltraServers. Maximum of 10 items is supported.
*Required*: No
*Type*: Array of [PlacementSpecificationsItems](aws-properties-sagemaker-hyperparametertuningjob-placementspecificationsitems.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
