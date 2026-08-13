---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-harvestjob-destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::HarvestJob Destination
<a name="aws-properties-mediapackagev2-harvestjob-destination"></a>

The configuration for the destination where the harvested content will be exported.

## Syntax
<a name="aws-properties-mediapackagev2-harvestjob-destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-harvestjob-destination-syntax.json"></a>

```
{
  "[S3Destination](#cfn-mediapackagev2-harvestjob-destination-s3destination)" : {{S3DestinationConfig}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-harvestjob-destination-syntax.yaml"></a>

```
  [S3Destination](#cfn-mediapackagev2-harvestjob-destination-s3destination): {{
    S3DestinationConfig}}
```

## Properties
<a name="aws-properties-mediapackagev2-harvestjob-destination-properties"></a>

`S3Destination`  <a name="cfn-mediapackagev2-harvestjob-destination-s3destination"></a>
The configuration for exporting harvested content to an S3 bucket. This includes details such as the bucket name and destination path within the bucket.
*Required*: Yes
*Type*: [S3DestinationConfig](aws-properties-mediapackagev2-harvestjob-s3destinationconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
