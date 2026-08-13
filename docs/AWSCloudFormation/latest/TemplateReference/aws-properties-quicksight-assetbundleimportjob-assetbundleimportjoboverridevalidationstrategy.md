---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::AssetBundleImportJob AssetBundleImportJobOverrideValidationStrategy
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy"></a>

An optional parameter that overrides the validation strategy for all analyses and dashboards before the resource is imported.

## Syntax
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy-syntax.json"></a>

```
{
  "[StrictModeForAllResources](#cfn-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy-strictmodeforallresources)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy-syntax.yaml"></a>

```
  [StrictModeForAllResources](#cfn-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy-strictmodeforallresources): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy-properties"></a>

`StrictModeForAllResources`  <a name="cfn-quicksight-assetbundleimportjob-assetbundleimportjoboverridevalidationstrategy-strictmodeforallresources"></a>
A Boolean value that indicates whether to import all analyses and dashboards under strict or lenient mode.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
