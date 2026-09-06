---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-model-modeldatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Model ModelDataSource
<a name="aws-properties-sagemaker-model-modeldatasource"></a>

Specifies the location of ML model data to deploy. If specified, you must specify one and only one of the available data sources.

## Syntax
<a name="aws-properties-sagemaker-model-modeldatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-model-modeldatasource-syntax.json"></a>

```
{
  "[S3DataSource](#cfn-sagemaker-model-modeldatasource-s3datasource)" : {{S3DataSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-model-modeldatasource-syntax.yaml"></a>

```
  [S3DataSource](#cfn-sagemaker-model-modeldatasource-s3datasource): {{
    S3DataSource}}
```

## Properties
<a name="aws-properties-sagemaker-model-modeldatasource-properties"></a>

`S3DataSource`  <a name="cfn-sagemaker-model-modeldatasource-s3datasource"></a>
Specifies the S3 location of ML model data to deploy.
*Required*: Yes
*Type*: [S3DataSource](aws-properties-sagemaker-model-s3datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
