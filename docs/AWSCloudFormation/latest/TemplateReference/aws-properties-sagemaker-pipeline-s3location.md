---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-pipeline-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Pipeline S3Location
<a name="aws-properties-sagemaker-pipeline-s3location"></a>

The location of the pipeline definition stored in Amazon S3. If specified, SageMaker will retrieve the pipeline definition from this location.

## Syntax
<a name="aws-properties-sagemaker-pipeline-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-pipeline-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-sagemaker-pipeline-s3location-bucket)" : {{String}},
  "[ETag](#cfn-sagemaker-pipeline-s3location-etag)" : {{String}},
  "[Key](#cfn-sagemaker-pipeline-s3location-key)" : {{String}},
  "[Version](#cfn-sagemaker-pipeline-s3location-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-pipeline-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-sagemaker-pipeline-s3location-bucket): {{String}}
  [ETag](#cfn-sagemaker-pipeline-s3location-etag): {{String}}
  [Key](#cfn-sagemaker-pipeline-s3location-key): {{String}}
  [Version](#cfn-sagemaker-pipeline-s3location-version): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-pipeline-s3location-properties"></a>

`Bucket`  <a name="cfn-sagemaker-pipeline-s3location-bucket"></a>
The name of the S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ETag`  <a name="cfn-sagemaker-pipeline-s3location-etag"></a>
A file checksum of the pipeline definition file.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-sagemaker-pipeline-s3location-key"></a>
The object key (or key name) which uniquely identifies the object in an S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-sagemaker-pipeline-s3location-version"></a>
The version ID of the pipeline definition file. If not specified, Amazon SageMaker will retrieve the latest version.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
