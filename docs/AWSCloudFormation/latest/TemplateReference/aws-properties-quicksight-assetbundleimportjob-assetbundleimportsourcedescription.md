---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-assetbundleimportjob-assetbundleimportsourcedescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::AssetBundleImportJob AssetBundleImportSourceDescription
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportsourcedescription"></a>

A description of the import source that you provide at the start of an import job. This value is set to either `Body` or `S3Uri`, depending on how the `StartAssetBundleImportJobRequest` is configured.

## Syntax
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportsourcedescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportsourcedescription-syntax.json"></a>

```
{
  "[S3Uri](#cfn-quicksight-assetbundleimportjob-assetbundleimportsourcedescription-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportsourcedescription-syntax.yaml"></a>

```
  [S3Uri](#cfn-quicksight-assetbundleimportjob-assetbundleimportsourcedescription-s3uri): {{String}}
```

## Properties
<a name="aws-properties-quicksight-assetbundleimportjob-assetbundleimportsourcedescription-properties"></a>

`S3Uri`  <a name="cfn-quicksight-assetbundleimportjob-assetbundleimportsourcedescription-s3uri"></a>
The Amazon S3 URI that you provided at the start of the import job.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
