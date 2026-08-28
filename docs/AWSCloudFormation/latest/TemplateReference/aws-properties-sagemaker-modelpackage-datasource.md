---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage DataSource
<a name="aws-properties-sagemaker-modelpackage-datasource"></a>

Describes the location of the channel data.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-datasource-syntax.json"></a>

```
{
  "[S3DataSource](#cfn-sagemaker-modelpackage-datasource-s3datasource)" : {{S3DataSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-datasource-syntax.yaml"></a>

```
  [S3DataSource](#cfn-sagemaker-modelpackage-datasource-s3datasource): {{
    S3DataSource}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-datasource-properties"></a>

`S3DataSource`  <a name="cfn-sagemaker-modelpackage-datasource-s3datasource"></a>
The S3 location of the data source that is associated with a channel.
*Required*: Yes
*Type*: [S3DataSource](aws-properties-sagemaker-modelpackage-s3datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
