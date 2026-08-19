---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-optimizationjob-optimizationjobmodelsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::OptimizationJob OptimizationJobModelSource
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsource"></a>

The location of the source model to optimize with an optimization job.

## Syntax
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsource-syntax.json"></a>

```
{
  "[S3](#cfn-sagemaker-optimizationjob-optimizationjobmodelsource-s3)" : {{OptimizationJobModelSourceS3}}
}
```

### YAML
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsource-syntax.yaml"></a>

```
  [S3](#cfn-sagemaker-optimizationjob-optimizationjobmodelsource-s3): {{
    OptimizationJobModelSourceS3}}
```

## Properties
<a name="aws-properties-sagemaker-optimizationjob-optimizationjobmodelsource-properties"></a>

`S3`  <a name="cfn-sagemaker-optimizationjob-optimizationjobmodelsource-s3"></a>
The Amazon S3 location of a source model to optimize with an optimization job.
*Required*: No
*Type*: [OptimizationJobModelSourceS3](aws-properties-sagemaker-optimizationjob-optimizationjobmodelsources3.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
