---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-spacecodeeditorappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space SpaceCodeEditorAppSettings
<a name="aws-properties-sagemaker-space-spacecodeeditorappsettings"></a>

The application settings for a Code Editor space.

## Syntax
<a name="aws-properties-sagemaker-space-spacecodeeditorappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-spacecodeeditorappsettings-syntax.json"></a>

```
{
  "[AppLifecycleManagement](#cfn-sagemaker-space-spacecodeeditorappsettings-applifecyclemanagement)" : {{SpaceAppLifecycleManagement}},
  "[DefaultResourceSpec](#cfn-sagemaker-space-spacecodeeditorappsettings-defaultresourcespec)" : {{ResourceSpec}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-spacecodeeditorappsettings-syntax.yaml"></a>

```
  [AppLifecycleManagement](#cfn-sagemaker-space-spacecodeeditorappsettings-applifecyclemanagement): {{
    SpaceAppLifecycleManagement}}
  [DefaultResourceSpec](#cfn-sagemaker-space-spacecodeeditorappsettings-defaultresourcespec): {{
    ResourceSpec}}
```

## Properties
<a name="aws-properties-sagemaker-space-spacecodeeditorappsettings-properties"></a>

`AppLifecycleManagement`  <a name="cfn-sagemaker-space-spacecodeeditorappsettings-applifecyclemanagement"></a>
Settings that are used to configure and manage the lifecycle of CodeEditor applications in a space.
*Required*: No
*Type*: [SpaceAppLifecycleManagement](aws-properties-sagemaker-space-spaceapplifecyclemanagement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResourceSpec`  <a name="cfn-sagemaker-space-spacecodeeditorappsettings-defaultresourcespec"></a>
Specifies the ARNs of a SageMaker image and SageMaker image version, and the instance type that the version runs on.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-space-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
