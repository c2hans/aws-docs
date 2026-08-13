---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automldatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLDataSource
<a name="aws-properties-sagemaker-automljob-automldatasource"></a>

The data source for the Autopilot job.

## Syntax
<a name="aws-properties-sagemaker-automljob-automldatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automldatasource-syntax.json"></a>

```
{
  "[S3DataSource](#cfn-sagemaker-automljob-automldatasource-s3datasource)" : {{AutoMLS3DataSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automldatasource-syntax.yaml"></a>

```
  [S3DataSource](#cfn-sagemaker-automljob-automldatasource-s3datasource): {{
    AutoMLS3DataSource}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automldatasource-properties"></a>

`S3DataSource`  <a name="cfn-sagemaker-automljob-automldatasource-s3datasource"></a>
The Amazon S3 location of the input data.
*Required*: Yes
*Type*: [AutoMLS3DataSource](aws-properties-sagemaker-automljob-automls3datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
