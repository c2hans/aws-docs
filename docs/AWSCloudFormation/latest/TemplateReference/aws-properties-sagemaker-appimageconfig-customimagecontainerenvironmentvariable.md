---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-appimageconfig-customimagecontainerenvironmentvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AppImageConfig CustomImageContainerEnvironmentVariable
<a name="aws-properties-sagemaker-appimageconfig-customimagecontainerenvironmentvariable"></a>

The environment variables to set in the container

## Syntax
<a name="aws-properties-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-syntax.json"></a>

```
{
  "[Key](#cfn-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-key)" : {{String}},
  "[Value](#cfn-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-syntax.yaml"></a>

```
  [Key](#cfn-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-key): {{String}}
  [Value](#cfn-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-value): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-properties"></a>

`Key`  <a name="cfn-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-key"></a>
The key that identifies a container environment variable.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-appimageconfig-customimagecontainerenvironmentvariable-value"></a>
The value of the container environment variable.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
