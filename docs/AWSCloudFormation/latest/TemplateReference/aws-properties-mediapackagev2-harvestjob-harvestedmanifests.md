---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-harvestjob-harvestedmanifests.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::HarvestJob HarvestedManifests
<a name="aws-properties-mediapackagev2-harvestjob-harvestedmanifests"></a>

A collection of harvested manifests of different types.

## Syntax
<a name="aws-properties-mediapackagev2-harvestjob-harvestedmanifests-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-harvestjob-harvestedmanifests-syntax.json"></a>

```
{
  "[DashManifests](#cfn-mediapackagev2-harvestjob-harvestedmanifests-dashmanifests)" : {{[ HarvestedDashManifest, ... ]}},
  "[HlsManifests](#cfn-mediapackagev2-harvestjob-harvestedmanifests-hlsmanifests)" : {{[ HarvestedHlsManifest, ... ]}},
  "[LowLatencyHlsManifests](#cfn-mediapackagev2-harvestjob-harvestedmanifests-lowlatencyhlsmanifests)" : {{[ HarvestedLowLatencyHlsManifest, ... ]}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-harvestjob-harvestedmanifests-syntax.yaml"></a>

```
  [DashManifests](#cfn-mediapackagev2-harvestjob-harvestedmanifests-dashmanifests): {{
    - HarvestedDashManifest}}
  [HlsManifests](#cfn-mediapackagev2-harvestjob-harvestedmanifests-hlsmanifests): {{
    - HarvestedHlsManifest}}
  [LowLatencyHlsManifests](#cfn-mediapackagev2-harvestjob-harvestedmanifests-lowlatencyhlsmanifests): {{
    - HarvestedLowLatencyHlsManifest}}
```

## Properties
<a name="aws-properties-mediapackagev2-harvestjob-harvestedmanifests-properties"></a>

`DashManifests`  <a name="cfn-mediapackagev2-harvestjob-harvestedmanifests-dashmanifests"></a>
A list of harvested DASH manifests.
*Required*: No
*Type*: Array of [HarvestedDashManifest](aws-properties-mediapackagev2-harvestjob-harvesteddashmanifest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HlsManifests`  <a name="cfn-mediapackagev2-harvestjob-harvestedmanifests-hlsmanifests"></a>
A list of harvested HLS manifests.
*Required*: No
*Type*: Array of [HarvestedHlsManifest](aws-properties-mediapackagev2-harvestjob-harvestedhlsmanifest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LowLatencyHlsManifests`  <a name="cfn-mediapackagev2-harvestjob-harvestedmanifests-lowlatencyhlsmanifests"></a>
A list of harvested Low-Latency HLS manifests.
*Required*: No
*Type*: Array of [HarvestedLowLatencyHlsManifest](aws-properties-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
