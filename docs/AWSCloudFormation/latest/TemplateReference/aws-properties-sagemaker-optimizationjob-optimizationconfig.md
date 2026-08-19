---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-optimizationjob-optimizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::OptimizationJob OptimizationConfig
<a name="aws-properties-sagemaker-optimizationjob-optimizationconfig"></a>

Settings for an optimization technique that you apply with a model optimization job.

## Syntax
<a name="aws-properties-sagemaker-optimizationjob-optimizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-optimizationjob-optimizationconfig-syntax.json"></a>

```
{
  "[ModelCompilationConfig](#cfn-sagemaker-optimizationjob-optimizationconfig-modelcompilationconfig)" : {{ModelCompilationConfig}},
  "[ModelQuantizationConfig](#cfn-sagemaker-optimizationjob-optimizationconfig-modelquantizationconfig)" : {{ModelQuantizationConfig}},
  "[ModelShardingConfig](#cfn-sagemaker-optimizationjob-optimizationconfig-modelshardingconfig)" : {{ModelShardingConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-optimizationjob-optimizationconfig-syntax.yaml"></a>

```
  [ModelCompilationConfig](#cfn-sagemaker-optimizationjob-optimizationconfig-modelcompilationconfig): {{
    ModelCompilationConfig}}
  [ModelQuantizationConfig](#cfn-sagemaker-optimizationjob-optimizationconfig-modelquantizationconfig): {{
    ModelQuantizationConfig}}
  [ModelShardingConfig](#cfn-sagemaker-optimizationjob-optimizationconfig-modelshardingconfig): {{
    ModelShardingConfig}}
```

## Properties
<a name="aws-properties-sagemaker-optimizationjob-optimizationconfig-properties"></a>

`ModelCompilationConfig`  <a name="cfn-sagemaker-optimizationjob-optimizationconfig-modelcompilationconfig"></a>
Settings for the model compilation technique that's applied by a model optimization job.
*Required*: No
*Type*: [ModelCompilationConfig](aws-properties-sagemaker-optimizationjob-modelcompilationconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelQuantizationConfig`  <a name="cfn-sagemaker-optimizationjob-optimizationconfig-modelquantizationconfig"></a>
Settings for the model quantization technique that's applied by a model optimization job.
*Required*: No
*Type*: [ModelQuantizationConfig](aws-properties-sagemaker-optimizationjob-modelquantizationconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelShardingConfig`  <a name="cfn-sagemaker-optimizationjob-optimizationconfig-modelshardingconfig"></a>
Settings for the model sharding technique that's applied by a model optimization job.
*Required*: No
*Type*: [ModelShardingConfig](aws-properties-sagemaker-optimizationjob-modelshardingconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
