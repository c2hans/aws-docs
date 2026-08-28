---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-appimageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AppImageConfig
<a name="aws-resource-sagemaker-appimageconfig"></a>

Creates a configuration for running a SageMaker AI image as a KernelGateway app. The configuration specifies the Amazon Elastic File System storage volume on the image, and a list of the kernels in the image.

## Syntax
<a name="aws-resource-sagemaker-appimageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-appimageconfig-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::AppImageConfig",
  "Properties" : {
      "[AppImageConfigName](#cfn-sagemaker-appimageconfig-appimageconfigname)" : {{String}},
      "[CodeEditorAppImageConfig](#cfn-sagemaker-appimageconfig-codeeditorappimageconfig)" : {{CodeEditorAppImageConfig}},
      "[JupyterLabAppImageConfig](#cfn-sagemaker-appimageconfig-jupyterlabappimageconfig)" : {{JupyterLabAppImageConfig}},
      "[KernelGatewayImageConfig](#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig)" : {{KernelGatewayImageConfig}},
      "[Tags](#cfn-sagemaker-appimageconfig-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-appimageconfig-syntax.yaml"></a>

```
Type: AWS::SageMaker::AppImageConfig
Properties:
  [AppImageConfigName](#cfn-sagemaker-appimageconfig-appimageconfigname): {{String}}
  [CodeEditorAppImageConfig](#cfn-sagemaker-appimageconfig-codeeditorappimageconfig): {{
    CodeEditorAppImageConfig}}
  [JupyterLabAppImageConfig](#cfn-sagemaker-appimageconfig-jupyterlabappimageconfig): {{
    JupyterLabAppImageConfig}}
  [KernelGatewayImageConfig](#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig): {{
    KernelGatewayImageConfig}}
  [Tags](#cfn-sagemaker-appimageconfig-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-appimageconfig-properties"></a>

`AppImageConfigName`  <a name="cfn-sagemaker-appimageconfig-appimageconfigname"></a>
The name of the AppImageConfig. Must be unique to your account.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CodeEditorAppImageConfig`  <a name="cfn-sagemaker-appimageconfig-codeeditorappimageconfig"></a>
The configuration for the file system and the runtime, such as the environment variables and entry point.
*Required*: No
*Type*: [CodeEditorAppImageConfig](aws-properties-sagemaker-appimageconfig-codeeditorappimageconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JupyterLabAppImageConfig`  <a name="cfn-sagemaker-appimageconfig-jupyterlabappimageconfig"></a>
The configuration for the file system and the runtime, such as the environment variables and entry point.
*Required*: No
*Type*: [JupyterLabAppImageConfig](aws-properties-sagemaker-appimageconfig-jupyterlabappimageconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KernelGatewayImageConfig`  <a name="cfn-sagemaker-appimageconfig-kernelgatewayimageconfig"></a>
The configuration for the file system and kernels in the SageMaker AI image.
*Required*: No
*Type*: [KernelGatewayImageConfig](aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-appimageconfig-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-appimageconfig-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-appimageconfig-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-appimageconfig-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the AppImageConfig.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-appimageconfig-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-appimageconfig-return-values-fn--getatt-fn--getatt"></a>

`AppImageConfigArn`  <a name="AppImageConfigArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AppImageConfig, such as `arn:aws:sagemaker:us-west-2:account-id:app-image-config/my-app-image-config-name`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
