---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-harvestjob-s3destinationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::HarvestJob S3DestinationConfig
<a name="aws-properties-mediapackagev2-harvestjob-s3destinationconfig"></a>

Configuration parameters for where in an S3 bucket to place the harvested content.

## Syntax
<a name="aws-properties-mediapackagev2-harvestjob-s3destinationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-harvestjob-s3destinationconfig-syntax.json"></a>

```
{
  "[BucketName](#cfn-mediapackagev2-harvestjob-s3destinationconfig-bucketname)" : {{String}},
  "[DestinationPath](#cfn-mediapackagev2-harvestjob-s3destinationconfig-destinationpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-harvestjob-s3destinationconfig-syntax.yaml"></a>

```
  [BucketName](#cfn-mediapackagev2-harvestjob-s3destinationconfig-bucketname): {{String}}
  [DestinationPath](#cfn-mediapackagev2-harvestjob-s3destinationconfig-destinationpath): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-harvestjob-s3destinationconfig-properties"></a>

`BucketName`  <a name="cfn-mediapackagev2-harvestjob-s3destinationconfig-bucketname"></a>
The name of an S3 bucket within which harvested content will be exported.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationPath`  <a name="cfn-mediapackagev2-harvestjob-s3destinationconfig-destinationpath"></a>
The path within the specified S3 bucket where the harvested content will be placed.
*Required*: Yes
*Type*: String
*Pattern*: `^[\S]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
