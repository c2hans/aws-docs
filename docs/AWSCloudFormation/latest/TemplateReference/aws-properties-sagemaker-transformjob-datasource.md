---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-transformjob-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TransformJob DataSource
<a name="aws-properties-sagemaker-transformjob-datasource"></a>

Describes the location of the channel data.

## Syntax
<a name="aws-properties-sagemaker-transformjob-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-transformjob-datasource-syntax.json"></a>

```
{
  "[S3DataSource](#cfn-sagemaker-transformjob-datasource-s3datasource)" : {{S3DataSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-transformjob-datasource-syntax.yaml"></a>

```
  [S3DataSource](#cfn-sagemaker-transformjob-datasource-s3datasource): {{
    S3DataSource}}
```

## Properties
<a name="aws-properties-sagemaker-transformjob-datasource-properties"></a>

`S3DataSource`  <a name="cfn-sagemaker-transformjob-datasource-s3datasource"></a>
The S3 location of the data source that is associated with a channel.
*Required*: Yes
*Type*: [S3DataSource](aws-properties-sagemaker-transformjob-s3datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
