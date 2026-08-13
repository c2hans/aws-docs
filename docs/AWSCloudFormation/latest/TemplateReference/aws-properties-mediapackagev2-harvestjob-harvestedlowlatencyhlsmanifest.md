---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::HarvestJob HarvestedLowLatencyHlsManifest
<a name="aws-properties-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest"></a>

Information about a harvested Low-Latency HLS manifest.

## Syntax
<a name="aws-properties-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest-syntax.json"></a>

```
{
  "[ManifestName](#cfn-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest-manifestname)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest-syntax.yaml"></a>

```
  [ManifestName](#cfn-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest-manifestname): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest-properties"></a>

`ManifestName`  <a name="cfn-mediapackagev2-harvestjob-harvestedlowlatencyhlsmanifest-manifestname"></a>
The name of the harvested Low-Latency HLS manifest.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
