---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-checkpointconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob CheckpointConfig
<a name="aws-properties-sagemaker-trainingjob-checkpointconfig"></a>

Contains information about the output location for managed spot training checkpoint data.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-checkpointconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-checkpointconfig-syntax.json"></a>

```
{
  "[LocalPath](#cfn-sagemaker-trainingjob-checkpointconfig-localpath)" : {{String}},
  "[S3Uri](#cfn-sagemaker-trainingjob-checkpointconfig-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-checkpointconfig-syntax.yaml"></a>

```
  [LocalPath](#cfn-sagemaker-trainingjob-checkpointconfig-localpath): {{String}}
  [S3Uri](#cfn-sagemaker-trainingjob-checkpointconfig-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-checkpointconfig-properties"></a>

`LocalPath`  <a name="cfn-sagemaker-trainingjob-checkpointconfig-localpath"></a>
(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/`.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-sagemaker-trainingjob-checkpointconfig-s3uri"></a>
Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix`.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
