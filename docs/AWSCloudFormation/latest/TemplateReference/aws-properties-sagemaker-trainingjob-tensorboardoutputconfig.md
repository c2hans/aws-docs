---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-tensorboardoutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob TensorBoardOutputConfig
<a name="aws-properties-sagemaker-trainingjob-tensorboardoutputconfig"></a>

Configuration of storage locations for the Amazon SageMaker Debugger TensorBoard output data.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-tensorboardoutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-tensorboardoutputconfig-syntax.json"></a>

```
{
  "[LocalPath](#cfn-sagemaker-trainingjob-tensorboardoutputconfig-localpath)" : {{String}},
  "[S3OutputPath](#cfn-sagemaker-trainingjob-tensorboardoutputconfig-s3outputpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-tensorboardoutputconfig-syntax.yaml"></a>

```
  [LocalPath](#cfn-sagemaker-trainingjob-tensorboardoutputconfig-localpath): {{String}}
  [S3OutputPath](#cfn-sagemaker-trainingjob-tensorboardoutputconfig-s3outputpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-tensorboardoutputconfig-properties"></a>

`LocalPath`  <a name="cfn-sagemaker-trainingjob-tensorboardoutputconfig-localpath"></a>
Path to local storage location for tensorBoard output. Defaults to `/opt/ml/output/tensorboard`.
*Required*: No
*Type*: String
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3OutputPath`  <a name="cfn-sagemaker-trainingjob-tensorboardoutputconfig-s3outputpath"></a>
Path to Amazon S3 storage location for TensorBoard output.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
