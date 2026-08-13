---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob DataSource
<a name="aws-properties-sagemaker-trainingjob-datasource"></a>

Describes the location of the channel data.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-datasource-syntax.json"></a>

```
{
  "[FileSystemDataSource](#cfn-sagemaker-trainingjob-datasource-filesystemdatasource)" : {{FileSystemDataSource}},
  "[S3DataSource](#cfn-sagemaker-trainingjob-datasource-s3datasource)" : {{S3DataSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-datasource-syntax.yaml"></a>

```
  [FileSystemDataSource](#cfn-sagemaker-trainingjob-datasource-filesystemdatasource): {{
    FileSystemDataSource}}
  [S3DataSource](#cfn-sagemaker-trainingjob-datasource-s3datasource): {{
    S3DataSource}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-datasource-properties"></a>

`FileSystemDataSource`  <a name="cfn-sagemaker-trainingjob-datasource-filesystemdatasource"></a>
The file system that is associated with a channel.
*Required*: No
*Type*: [FileSystemDataSource](aws-properties-sagemaker-trainingjob-filesystemdatasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3DataSource`  <a name="cfn-sagemaker-trainingjob-datasource-s3datasource"></a>
The S3 location of the data source that is associated with a channel.
*Required*: No
*Type*: [S3DataSource](aws-properties-sagemaker-trainingjob-s3datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
