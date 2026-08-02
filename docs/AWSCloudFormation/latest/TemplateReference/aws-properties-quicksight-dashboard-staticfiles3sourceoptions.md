---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-staticfiles3sourceoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard StaticFileS3SourceOptions
<a name="aws-properties-quicksight-dashboard-staticfiles3sourceoptions"></a>

The structure that contains the Amazon S3 location to download the static file from.

## Syntax
<a name="aws-properties-quicksight-dashboard-staticfiles3sourceoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-staticfiles3sourceoptions-syntax.json"></a>

```
{
  "[BucketName](#cfn-quicksight-dashboard-staticfiles3sourceoptions-bucketname)" : {{String}},
  "[ObjectKey](#cfn-quicksight-dashboard-staticfiles3sourceoptions-objectkey)" : {{String}},
  "[Region](#cfn-quicksight-dashboard-staticfiles3sourceoptions-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-staticfiles3sourceoptions-syntax.yaml"></a>

```
  [BucketName](#cfn-quicksight-dashboard-staticfiles3sourceoptions-bucketname): {{String}}
  [ObjectKey](#cfn-quicksight-dashboard-staticfiles3sourceoptions-objectkey): {{String}}
  [Region](#cfn-quicksight-dashboard-staticfiles3sourceoptions-region): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-staticfiles3sourceoptions-properties"></a>

`BucketName`  <a name="cfn-quicksight-dashboard-staticfiles3sourceoptions-bucketname"></a>
The name of the Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectKey`  <a name="cfn-quicksight-dashboard-staticfiles3sourceoptions-objectkey"></a>
The identifier of the static file in the Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-quicksight-dashboard-staticfiles3sourceoptions-region"></a>
The Region of the Amazon S3 account that contains the bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
