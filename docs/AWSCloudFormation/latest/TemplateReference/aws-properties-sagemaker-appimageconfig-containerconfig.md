---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-appimageconfig-containerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AppImageConfig ContainerConfig
<a name="aws-properties-sagemaker-appimageconfig-containerconfig"></a>

The configuration used to run the application image container.

## Syntax
<a name="aws-properties-sagemaker-appimageconfig-containerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-appimageconfig-containerconfig-syntax.json"></a>

```
{
  "[ContainerArguments](#cfn-sagemaker-appimageconfig-containerconfig-containerarguments)" : {{[ String, ... ]}},
  "[ContainerEntrypoint](#cfn-sagemaker-appimageconfig-containerconfig-containerentrypoint)" : {{[ String, ... ]}},
  "[ContainerEnvironmentVariables](#cfn-sagemaker-appimageconfig-containerconfig-containerenvironmentvariables)" : {{[ CustomImageContainerEnvironmentVariable, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-appimageconfig-containerconfig-syntax.yaml"></a>

```
  [ContainerArguments](#cfn-sagemaker-appimageconfig-containerconfig-containerarguments): {{
    - String}}
  [ContainerEntrypoint](#cfn-sagemaker-appimageconfig-containerconfig-containerentrypoint): {{
    - String}}
  [ContainerEnvironmentVariables](#cfn-sagemaker-appimageconfig-containerconfig-containerenvironmentvariables): {{
    - CustomImageContainerEnvironmentVariable}}
```

## Properties
<a name="aws-properties-sagemaker-appimageconfig-containerconfig-properties"></a>

`ContainerArguments`  <a name="cfn-sagemaker-appimageconfig-containerconfig-containerarguments"></a>
The arguments for the container when you're running the application.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerEntrypoint`  <a name="cfn-sagemaker-appimageconfig-containerconfig-containerentrypoint"></a>
The entrypoint used to run the application in the container.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerEnvironmentVariables`  <a name="cfn-sagemaker-appimageconfig-containerconfig-containerenvironmentvariables"></a>
The environment variables to set in the container
*Required*: No
*Type*: Array of [CustomImageContainerEnvironmentVariable](aws-properties-sagemaker-appimageconfig-customimagecontainerenvironmentvariable.md)
*Minimum*: `0`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
