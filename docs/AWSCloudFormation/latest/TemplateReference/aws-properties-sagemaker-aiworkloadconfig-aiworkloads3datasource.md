---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-aiworkloadconfig-aiworkloads3datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AIWorkloadConfig AIWorkloadS3DataSource
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloads3datasource"></a>

The Amazon S3 data source for an AI workload.

## Syntax
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloads3datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloads3datasource-syntax.json"></a>

```
{
  "[S3Uri](#cfn-sagemaker-aiworkloadconfig-aiworkloads3datasource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloads3datasource-syntax.yaml"></a>

```
  [S3Uri](#cfn-sagemaker-aiworkloadconfig-aiworkloads3datasource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloads3datasource-properties"></a>

`S3Uri`  <a name="cfn-sagemaker-aiworkloadconfig-aiworkloads3datasource-s3uri"></a>
The Amazon S3 URI of the data.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
