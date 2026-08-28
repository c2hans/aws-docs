---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AppImageConfig KernelGatewayImageConfig
<a name="aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig"></a>

The configuration for the file system and kernels in a SageMaker AI image running as a KernelGateway app.

## Syntax
<a name="aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig-syntax.json"></a>

```
{
  "[FileSystemConfig](#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-filesystemconfig)" : {{FileSystemConfig}},
  "[KernelSpecs](#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-kernelspecs)" : {{[ KernelSpec, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig-syntax.yaml"></a>

```
  [FileSystemConfig](#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-filesystemconfig): {{
    FileSystemConfig}}
  [KernelSpecs](#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-kernelspecs): {{
    - KernelSpec}}
```

## Properties
<a name="aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig-properties"></a>

`FileSystemConfig`  <a name="cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-filesystemconfig"></a>
The Amazon Elastic File System storage configuration for a SageMaker AI image.
*Required*: No
*Type*: [FileSystemConfig](aws-properties-sagemaker-appimageconfig-filesystemconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KernelSpecs`  <a name="cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-kernelspecs"></a>
The specification of the Jupyter kernels in the image.
*Required*: Yes
*Type*: Array of [KernelSpec](aws-properties-sagemaker-appimageconfig-kernelspec.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
