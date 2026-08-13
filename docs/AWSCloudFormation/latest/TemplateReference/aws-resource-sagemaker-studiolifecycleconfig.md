---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-studiolifecycleconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::StudioLifecycleConfig
<a name="aws-resource-sagemaker-studiolifecycleconfig"></a>

Creates a new Amazon SageMaker AI Studio Lifecycle Configuration.

## Syntax
<a name="aws-resource-sagemaker-studiolifecycleconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-studiolifecycleconfig-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::StudioLifecycleConfig",
  "Properties" : {
      "[StudioLifecycleConfigAppType](#cfn-sagemaker-studiolifecycleconfig-studiolifecycleconfigapptype)" : {{String}},
      "[StudioLifecycleConfigContent](#cfn-sagemaker-studiolifecycleconfig-studiolifecycleconfigcontent)" : {{String}},
      "[StudioLifecycleConfigName](#cfn-sagemaker-studiolifecycleconfig-studiolifecycleconfigname)" : {{String}},
      "[Tags](#cfn-sagemaker-studiolifecycleconfig-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-studiolifecycleconfig-syntax.yaml"></a>

```
Type: AWS::SageMaker::StudioLifecycleConfig
Properties:
  [StudioLifecycleConfigAppType](#cfn-sagemaker-studiolifecycleconfig-studiolifecycleconfigapptype): {{String}}
  [StudioLifecycleConfigContent](#cfn-sagemaker-studiolifecycleconfig-studiolifecycleconfigcontent): {{String}}
  [StudioLifecycleConfigName](#cfn-sagemaker-studiolifecycleconfig-studiolifecycleconfigname): {{String}}
  [Tags](#cfn-sagemaker-studiolifecycleconfig-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-studiolifecycleconfig-properties"></a>

`StudioLifecycleConfigAppType`  <a name="cfn-sagemaker-studiolifecycleconfig-studiolifecycleconfigapptype"></a>
The App type to which the Lifecycle Configuration is attached.
*Required*: Yes
*Type*: String
*Allowed values*: `JupyterServer | KernelGateway | CodeEditor | JupyterLab`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StudioLifecycleConfigContent`  <a name="cfn-sagemaker-studiolifecycleconfig-studiolifecycleconfigcontent"></a>
The content of your Amazon SageMaker AI Studio Lifecycle Configuration script. This content must be base64 encoded.
*Required*: Yes
*Type*: String
*Pattern*: `[\S\s]+`
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StudioLifecycleConfigName`  <a name="cfn-sagemaker-studiolifecycleconfig-studiolifecycleconfigname"></a>
The name of the Amazon SageMaker AI Studio Lifecycle Configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-studiolifecycleconfig-tags"></a>
Tags to be associated with the Lifecycle Configuration. Each tag consists of a key and an optional value. Tag keys must be unique per resource. Tags are searchable using the Search API.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-studiolifecycleconfig-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-studiolifecycleconfig-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-studiolifecycleconfig-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-studiolifecycleconfig-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-studiolifecycleconfig-return-values-fn--getatt-fn--getatt"></a>

`StudioLifecycleConfigArn`  <a name="StudioLifecycleConfigArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configuration.
