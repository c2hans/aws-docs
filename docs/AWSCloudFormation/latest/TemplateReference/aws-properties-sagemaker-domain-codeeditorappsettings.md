---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-codeeditorappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain CodeEditorAppSettings
<a name="aws-properties-sagemaker-domain-codeeditorappsettings"></a>

The Code Editor application settings.

For more information about Code Editor, see [Get started with Code Editor in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor.html).

## Syntax
<a name="aws-properties-sagemaker-domain-codeeditorappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-codeeditorappsettings-syntax.json"></a>

```
{
  "[AppLifecycleManagement](#cfn-sagemaker-domain-codeeditorappsettings-applifecyclemanagement)" : {{AppLifecycleManagement}},
  "[BuiltInLifecycleConfigArn](#cfn-sagemaker-domain-codeeditorappsettings-builtinlifecycleconfigarn)" : {{String}},
  "[CustomImages](#cfn-sagemaker-domain-codeeditorappsettings-customimages)" : {{[ CustomImage, ... ]}},
  "[DefaultResourceSpec](#cfn-sagemaker-domain-codeeditorappsettings-defaultresourcespec)" : {{ResourceSpec}},
  "[LifecycleConfigArns](#cfn-sagemaker-domain-codeeditorappsettings-lifecycleconfigarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-codeeditorappsettings-syntax.yaml"></a>

```
  [AppLifecycleManagement](#cfn-sagemaker-domain-codeeditorappsettings-applifecyclemanagement): {{
    AppLifecycleManagement}}
  [BuiltInLifecycleConfigArn](#cfn-sagemaker-domain-codeeditorappsettings-builtinlifecycleconfigarn): {{String}}
  [CustomImages](#cfn-sagemaker-domain-codeeditorappsettings-customimages): {{
    - CustomImage}}
  [DefaultResourceSpec](#cfn-sagemaker-domain-codeeditorappsettings-defaultresourcespec): {{
    ResourceSpec}}
  [LifecycleConfigArns](#cfn-sagemaker-domain-codeeditorappsettings-lifecycleconfigarns): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-codeeditorappsettings-properties"></a>

`AppLifecycleManagement`  <a name="cfn-sagemaker-domain-codeeditorappsettings-applifecyclemanagement"></a>
Settings that are used to configure and manage the lifecycle of CodeEditor applications.
*Required*: No
*Type*: [AppLifecycleManagement](aws-properties-sagemaker-domain-applifecyclemanagement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuiltInLifecycleConfigArn`  <a name="cfn-sagemaker-domain-codeeditorappsettings-builtinlifecycleconfigarn"></a>
The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomImages`  <a name="cfn-sagemaker-domain-codeeditorappsettings-customimages"></a>
A list of custom SageMaker images that are configured to run as a Code Editor app.
*Required*: No
*Type*: Array of [CustomImage](aws-properties-sagemaker-domain-customimage.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResourceSpec`  <a name="cfn-sagemaker-domain-codeeditorappsettings-defaultresourcespec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker image used by the Code Editor app.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-domain-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfigArns`  <a name="cfn-sagemaker-domain-codeeditorappsettings-lifecycleconfigarns"></a>
The Amazon Resource Name (ARN) of the Code Editor application lifecycle configuration.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
