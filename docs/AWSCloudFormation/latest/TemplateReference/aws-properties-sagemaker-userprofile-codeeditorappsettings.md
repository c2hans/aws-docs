---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-codeeditorappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile CodeEditorAppSettings
<a name="aws-properties-sagemaker-userprofile-codeeditorappsettings"></a>

The Code Editor application settings.

For more information about Code Editor, see [Get started with Code Editor in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor.html).

## Syntax
<a name="aws-properties-sagemaker-userprofile-codeeditorappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-codeeditorappsettings-syntax.json"></a>

```
{
  "[AppLifecycleManagement](#cfn-sagemaker-userprofile-codeeditorappsettings-applifecyclemanagement)" : {{AppLifecycleManagement}},
  "[BuiltInLifecycleConfigArn](#cfn-sagemaker-userprofile-codeeditorappsettings-builtinlifecycleconfigarn)" : {{String}},
  "[CustomImages](#cfn-sagemaker-userprofile-codeeditorappsettings-customimages)" : {{[ CustomImage, ... ]}},
  "[DefaultResourceSpec](#cfn-sagemaker-userprofile-codeeditorappsettings-defaultresourcespec)" : {{ResourceSpec}},
  "[LifecycleConfigArns](#cfn-sagemaker-userprofile-codeeditorappsettings-lifecycleconfigarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-codeeditorappsettings-syntax.yaml"></a>

```
  [AppLifecycleManagement](#cfn-sagemaker-userprofile-codeeditorappsettings-applifecyclemanagement): {{
    AppLifecycleManagement}}
  [BuiltInLifecycleConfigArn](#cfn-sagemaker-userprofile-codeeditorappsettings-builtinlifecycleconfigarn): {{String}}
  [CustomImages](#cfn-sagemaker-userprofile-codeeditorappsettings-customimages): {{
    - CustomImage}}
  [DefaultResourceSpec](#cfn-sagemaker-userprofile-codeeditorappsettings-defaultresourcespec): {{
    ResourceSpec}}
  [LifecycleConfigArns](#cfn-sagemaker-userprofile-codeeditorappsettings-lifecycleconfigarns): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-codeeditorappsettings-properties"></a>

`AppLifecycleManagement`  <a name="cfn-sagemaker-userprofile-codeeditorappsettings-applifecyclemanagement"></a>
Settings that are used to configure and manage the lifecycle of CodeEditor applications.
*Required*: No
*Type*: [AppLifecycleManagement](aws-properties-sagemaker-userprofile-applifecyclemanagement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuiltInLifecycleConfigArn`  <a name="cfn-sagemaker-userprofile-codeeditorappsettings-builtinlifecycleconfigarn"></a>
The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomImages`  <a name="cfn-sagemaker-userprofile-codeeditorappsettings-customimages"></a>
A list of custom SageMaker images that are configured to run as a Code Editor app.
*Required*: No
*Type*: Array of [CustomImage](aws-properties-sagemaker-userprofile-customimage.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResourceSpec`  <a name="cfn-sagemaker-userprofile-codeeditorappsettings-defaultresourcespec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker image used by the Code Editor app.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-userprofile-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfigArns`  <a name="cfn-sagemaker-userprofile-codeeditorappsettings-lifecycleconfigarns"></a>
The Amazon Resource Name (ARN) of the Code Editor application lifecycle configuration.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
