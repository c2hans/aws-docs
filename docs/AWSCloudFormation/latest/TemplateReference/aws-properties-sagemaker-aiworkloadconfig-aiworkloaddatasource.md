---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-aiworkloadconfig-aiworkloaddatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AIWorkloadConfig AIWorkloadDataSource
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloaddatasource"></a>

The data source for an AI workload input data channel.

## Syntax
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloaddatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloaddatasource-syntax.json"></a>

```
{
  "[S3DataSource](#cfn-sagemaker-aiworkloadconfig-aiworkloaddatasource-s3datasource)" : {{AIWorkloadS3DataSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloaddatasource-syntax.yaml"></a>

```
  [S3DataSource](#cfn-sagemaker-aiworkloadconfig-aiworkloaddatasource-s3datasource): {{
    AIWorkloadS3DataSource}}
```

## Properties
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloaddatasource-properties"></a>

`S3DataSource`  <a name="cfn-sagemaker-aiworkloadconfig-aiworkloaddatasource-s3datasource"></a>
The Amazon S3 data source configuration.
*Required*: No
*Type*: [AIWorkloadS3DataSource](aws-properties-sagemaker-aiworkloadconfig-aiworkloads3datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
