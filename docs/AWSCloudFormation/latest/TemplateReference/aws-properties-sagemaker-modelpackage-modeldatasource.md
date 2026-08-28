---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-modeldatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage ModelDataSource
<a name="aws-properties-sagemaker-modelpackage-modeldatasource"></a>

Specifies the location of ML model data to deploy. If specified, you must specify one and only one of the available data sources.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-modeldatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-modeldatasource-syntax.json"></a>

```
{
  "[S3DataSource](#cfn-sagemaker-modelpackage-modeldatasource-s3datasource)" : {{S3ModelDataSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-modeldatasource-syntax.yaml"></a>

```
  [S3DataSource](#cfn-sagemaker-modelpackage-modeldatasource-s3datasource): {{
    S3ModelDataSource}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-modeldatasource-properties"></a>

`S3DataSource`  <a name="cfn-sagemaker-modelpackage-modeldatasource-s3datasource"></a>
Specifies the S3 location of ML model data to deploy.
*Required*: No
*Type*: [S3ModelDataSource](aws-properties-sagemaker-modelpackage-s3modeldatasource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
