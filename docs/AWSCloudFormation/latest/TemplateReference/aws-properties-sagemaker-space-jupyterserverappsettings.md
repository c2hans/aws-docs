---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-jupyterserverappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space JupyterServerAppSettings
<a name="aws-properties-sagemaker-space-jupyterserverappsettings"></a>

The JupyterServer app settings.

## Syntax
<a name="aws-properties-sagemaker-space-jupyterserverappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-jupyterserverappsettings-syntax.json"></a>

```
{
  "[DefaultResourceSpec](#cfn-sagemaker-space-jupyterserverappsettings-defaultresourcespec)" : {{ResourceSpec}},
  "[LifecycleConfigArns](#cfn-sagemaker-space-jupyterserverappsettings-lifecycleconfigarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-jupyterserverappsettings-syntax.yaml"></a>

```
  [DefaultResourceSpec](#cfn-sagemaker-space-jupyterserverappsettings-defaultresourcespec): {{
    ResourceSpec}}
  [LifecycleConfigArns](#cfn-sagemaker-space-jupyterserverappsettings-lifecycleconfigarns): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-space-jupyterserverappsettings-properties"></a>

`DefaultResourceSpec`  <a name="cfn-sagemaker-space-jupyterserverappsettings-defaultresourcespec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker AI image used by the JupyterServer app. If you use the `LifecycleConfigArns` parameter, then this parameter is also required.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-space-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfigArns`  <a name="cfn-sagemaker-space-jupyterserverappsettings-lifecycleconfigarns"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the JupyterServerApp. If you use this parameter, the `DefaultResourceSpec` parameter is also required.
To remove a Lifecycle Config, you must set `LifecycleConfigArns` to an empty list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
