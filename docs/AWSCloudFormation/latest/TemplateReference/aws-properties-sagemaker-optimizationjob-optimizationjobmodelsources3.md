---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-optimizationjob-optimizationjobmodelsources3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::OptimizationJob OptimizationJobModelSourceS3
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsources3"></a>

The Amazon S3 location of a source model to optimize with an optimization job.

## Syntax
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsources3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsources3-syntax.json"></a>

```
{
  "[S3Uri](#cfn-sagemaker-optimizationjob-optimizationjobmodelsources3-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsources3-syntax.yaml"></a>

```
  [S3Uri](#cfn-sagemaker-optimizationjob-optimizationjobmodelsources3-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsources3-properties"></a>

`S3Uri`  <a name="cfn-sagemaker-optimizationjob-optimizationjobmodelsources3-s3uri"></a>
An Amazon S3 URI that locates a source model to optimize with an optimization job.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
