---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-harvestjob-harvestedhlsmanifest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::HarvestJob HarvestedHlsManifest
<a name="aws-properties-mediapackagev2-harvestjob-harvestedhlsmanifest"></a>

Information about a harvested HLS manifest.

## Syntax
<a name="aws-properties-mediapackagev2-harvestjob-harvestedhlsmanifest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-harvestjob-harvestedhlsmanifest-syntax.json"></a>

```
{
  "[ManifestName](#cfn-mediapackagev2-harvestjob-harvestedhlsmanifest-manifestname)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-harvestjob-harvestedhlsmanifest-syntax.yaml"></a>

```
  [ManifestName](#cfn-mediapackagev2-harvestjob-harvestedhlsmanifest-manifestname): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-harvestjob-harvestedhlsmanifest-properties"></a>

`ManifestName`  <a name="cfn-mediapackagev2-harvestjob-harvestedhlsmanifest-manifestname"></a>
The name of the harvested HLS manifest.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
