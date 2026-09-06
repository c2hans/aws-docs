---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-appimageconfig-codeeditorappimageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AppImageConfig CodeEditorAppImageConfig
<a name="aws-properties-sagemaker-appimageconfig-codeeditorappimageconfig"></a>

The configuration for the file system and kernels in a SageMaker image running as a Code Editor app. The `FileSystemConfig` object is not supported.

## Syntax
<a name="aws-properties-sagemaker-appimageconfig-codeeditorappimageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-appimageconfig-codeeditorappimageconfig-syntax.json"></a>

```
{
  "[ContainerConfig](#cfn-sagemaker-appimageconfig-codeeditorappimageconfig-containerconfig)" : {{ContainerConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-appimageconfig-codeeditorappimageconfig-syntax.yaml"></a>

```
  [ContainerConfig](#cfn-sagemaker-appimageconfig-codeeditorappimageconfig-containerconfig): {{
    ContainerConfig}}
```

## Properties
<a name="aws-properties-sagemaker-appimageconfig-codeeditorappimageconfig-properties"></a>

`ContainerConfig`  <a name="cfn-sagemaker-appimageconfig-codeeditorappimageconfig-containerconfig"></a>
The container configuration for the Code Editor application image.
*Required*: No
*Type*: [ContainerConfig](aws-properties-sagemaker-appimageconfig-containerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
