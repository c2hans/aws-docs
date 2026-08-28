---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-staticfiles3sourceoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis StaticFileS3SourceOptions
<a name="aws-properties-quicksight-analysis-staticfiles3sourceoptions"></a>

The structure that contains the Amazon S3 location to download the static file from.

## Syntax
<a name="aws-properties-quicksight-analysis-staticfiles3sourceoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-staticfiles3sourceoptions-syntax.json"></a>

```
{
  "[BucketName](#cfn-quicksight-analysis-staticfiles3sourceoptions-bucketname)" : {{String}},
  "[ObjectKey](#cfn-quicksight-analysis-staticfiles3sourceoptions-objectkey)" : {{String}},
  "[Region](#cfn-quicksight-analysis-staticfiles3sourceoptions-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-staticfiles3sourceoptions-syntax.yaml"></a>

```
  [BucketName](#cfn-quicksight-analysis-staticfiles3sourceoptions-bucketname): {{String}}
  [ObjectKey](#cfn-quicksight-analysis-staticfiles3sourceoptions-objectkey): {{String}}
  [Region](#cfn-quicksight-analysis-staticfiles3sourceoptions-region): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-staticfiles3sourceoptions-properties"></a>

`BucketName`  <a name="cfn-quicksight-analysis-staticfiles3sourceoptions-bucketname"></a>
The name of the Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectKey`  <a name="cfn-quicksight-analysis-staticfiles3sourceoptions-objectkey"></a>
The identifier of the static file in the Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-quicksight-analysis-staticfiles3sourceoptions-region"></a>
The Region of the Amazon S3 account that contains the bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
