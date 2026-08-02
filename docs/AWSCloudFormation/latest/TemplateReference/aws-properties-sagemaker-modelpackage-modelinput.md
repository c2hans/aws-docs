---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-modelinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage ModelInput
<a name="aws-properties-sagemaker-modelpackage-modelinput"></a>

Input object for the model.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-modelinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-modelinput-syntax.json"></a>

```
{
  "[DataInputConfig](#cfn-sagemaker-modelpackage-modelinput-datainputconfig)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-modelinput-syntax.yaml"></a>

```
  [DataInputConfig](#cfn-sagemaker-modelpackage-modelinput-datainputconfig): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-modelinput-properties"></a>

`DataInputConfig`  <a name="cfn-sagemaker-modelpackage-modelinput-datainputconfig"></a>
The input configuration object for the model.
*Required*: Yes
*Type*: String
*Pattern*: `[\S\s]+`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
