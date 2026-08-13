---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-harvestjob-harvesterscheduleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::HarvestJob HarvesterScheduleConfiguration
<a name="aws-properties-mediapackagev2-harvestjob-harvesterscheduleconfiguration"></a>

Defines the schedule configuration for a harvest job.

## Syntax
<a name="aws-properties-mediapackagev2-harvestjob-harvesterscheduleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-harvestjob-harvesterscheduleconfiguration-syntax.json"></a>

```
{
  "[EndTime](#cfn-mediapackagev2-harvestjob-harvesterscheduleconfiguration-endtime)" : {{String}},
  "[StartTime](#cfn-mediapackagev2-harvestjob-harvesterscheduleconfiguration-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-harvestjob-harvesterscheduleconfiguration-syntax.yaml"></a>

```
  [EndTime](#cfn-mediapackagev2-harvestjob-harvesterscheduleconfiguration-endtime): {{String}}
  [StartTime](#cfn-mediapackagev2-harvestjob-harvesterscheduleconfiguration-starttime): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-harvestjob-harvesterscheduleconfiguration-properties"></a>

`EndTime`  <a name="cfn-mediapackagev2-harvestjob-harvesterscheduleconfiguration-endtime"></a>
The end time for the harvest job.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTime`  <a name="cfn-mediapackagev2-harvestjob-harvesterscheduleconfiguration-starttime"></a>
The start time for the harvest job.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
