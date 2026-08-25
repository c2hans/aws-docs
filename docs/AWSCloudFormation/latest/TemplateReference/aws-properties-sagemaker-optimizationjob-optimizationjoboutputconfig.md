---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-optimizationjob-optimizationjoboutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::OptimizationJob OptimizationJobOutputConfig
<a name="aws-properties-sagemaker-optimizationjob-optimizationjoboutputconfig"></a>

Details for where to store the optimized model that you create with the optimization job.

## Syntax
<a name="aws-properties-sagemaker-optimizationjob-optimizationjoboutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-optimizationjob-optimizationjoboutputconfig-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-sagemaker-optimizationjob-optimizationjoboutputconfig-kmskeyid)" : {{String}},
  "[S3OutputLocation](#cfn-sagemaker-optimizationjob-optimizationjoboutputconfig-s3outputlocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-optimizationjob-optimizationjoboutputconfig-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-sagemaker-optimizationjob-optimizationjoboutputconfig-kmskeyid): {{String}}
  [S3OutputLocation](#cfn-sagemaker-optimizationjob-optimizationjoboutputconfig-s3outputlocation): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-optimizationjob-optimizationjoboutputconfig-properties"></a>

`KmsKeyId`  <a name="cfn-sagemaker-optimizationjob-optimizationjoboutputconfig-kmskeyid"></a>
The Amazon Resource Name (ARN) of a key in AWS KMS. SageMaker uses they key to encrypt the artifacts of the optimized model when SageMaker uploads the model to Amazon S3.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3OutputLocation`  <a name="cfn-sagemaker-optimizationjob-optimizationjoboutputconfig-s3outputlocation"></a>
The Amazon S3 URI for where to store the optimized model that you create with an optimization job.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
