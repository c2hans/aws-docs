---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-optimizationjob-modelquantizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::OptimizationJob ModelQuantizationConfig
<a name="aws-properties-sagemaker-optimizationjob-modelquantizationconfig"></a>

Settings for the model quantization technique that's applied by a model optimization job.

## Syntax
<a name="aws-properties-sagemaker-optimizationjob-modelquantizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-optimizationjob-modelquantizationconfig-syntax.json"></a>

```
{
  "[Image](#cfn-sagemaker-optimizationjob-modelquantizationconfig-image)" : {{String}},
  "[OverrideEnvironment](#cfn-sagemaker-optimizationjob-modelquantizationconfig-overrideenvironment)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-sagemaker-optimizationjob-modelquantizationconfig-syntax.yaml"></a>

```
  [Image](#cfn-sagemaker-optimizationjob-modelquantizationconfig-image): {{String}}
  [OverrideEnvironment](#cfn-sagemaker-optimizationjob-modelquantizationconfig-overrideenvironment): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-sagemaker-optimizationjob-modelquantizationconfig-properties"></a>

`Image`  <a name="cfn-sagemaker-optimizationjob-modelquantizationconfig-image"></a>
The URI of an LMI DLC in Amazon ECR. SageMaker uses this image to run the optimization.
*Required*: No
*Type*: String
*Pattern*: `[\S]+`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OverrideEnvironment`  <a name="cfn-sagemaker-optimizationjob-modelquantizationconfig-overrideenvironment"></a>
Environment variables that override the default ones in the model container.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
