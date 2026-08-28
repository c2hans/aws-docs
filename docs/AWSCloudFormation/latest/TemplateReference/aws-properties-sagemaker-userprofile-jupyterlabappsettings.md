---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-jupyterlabappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile JupyterLabAppSettings
<a name="aws-properties-sagemaker-userprofile-jupyterlabappsettings"></a>

The settings for the JupyterLab application.

## Syntax
<a name="aws-properties-sagemaker-userprofile-jupyterlabappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-jupyterlabappsettings-syntax.json"></a>

```
{
  "[AppLifecycleManagement](#cfn-sagemaker-userprofile-jupyterlabappsettings-applifecyclemanagement)" : {{AppLifecycleManagement}},
  "[BuiltInLifecycleConfigArn](#cfn-sagemaker-userprofile-jupyterlabappsettings-builtinlifecycleconfigarn)" : {{String}},
  "[CodeRepositories](#cfn-sagemaker-userprofile-jupyterlabappsettings-coderepositories)" : {{[ CodeRepository, ... ]}},
  "[CustomImages](#cfn-sagemaker-userprofile-jupyterlabappsettings-customimages)" : {{[ CustomImage, ... ]}},
  "[DefaultResourceSpec](#cfn-sagemaker-userprofile-jupyterlabappsettings-defaultresourcespec)" : {{ResourceSpec}},
  "[EmrSettings](#cfn-sagemaker-userprofile-jupyterlabappsettings-emrsettings)" : {{EmrSettings}},
  "[LifecycleConfigArns](#cfn-sagemaker-userprofile-jupyterlabappsettings-lifecycleconfigarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-jupyterlabappsettings-syntax.yaml"></a>

```
  [AppLifecycleManagement](#cfn-sagemaker-userprofile-jupyterlabappsettings-applifecyclemanagement): {{
    AppLifecycleManagement}}
  [BuiltInLifecycleConfigArn](#cfn-sagemaker-userprofile-jupyterlabappsettings-builtinlifecycleconfigarn): {{String}}
  [CodeRepositories](#cfn-sagemaker-userprofile-jupyterlabappsettings-coderepositories): {{
    - CodeRepository}}
  [CustomImages](#cfn-sagemaker-userprofile-jupyterlabappsettings-customimages): {{
    - CustomImage}}
  [DefaultResourceSpec](#cfn-sagemaker-userprofile-jupyterlabappsettings-defaultresourcespec): {{
    ResourceSpec}}
  [EmrSettings](#cfn-sagemaker-userprofile-jupyterlabappsettings-emrsettings): {{
    EmrSettings}}
  [LifecycleConfigArns](#cfn-sagemaker-userprofile-jupyterlabappsettings-lifecycleconfigarns): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-jupyterlabappsettings-properties"></a>

`AppLifecycleManagement`  <a name="cfn-sagemaker-userprofile-jupyterlabappsettings-applifecyclemanagement"></a>
Indicates whether idle shutdown is activated for JupyterLab applications.
*Required*: No
*Type*: [AppLifecycleManagement](aws-properties-sagemaker-userprofile-applifecyclemanagement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuiltInLifecycleConfigArn`  <a name="cfn-sagemaker-userprofile-jupyterlabappsettings-builtinlifecycleconfigarn"></a>
The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeRepositories`  <a name="cfn-sagemaker-userprofile-jupyterlabappsettings-coderepositories"></a>
A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.
*Required*: No
*Type*: Array of [CodeRepository](aws-properties-sagemaker-userprofile-coderepository.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomImages`  <a name="cfn-sagemaker-userprofile-jupyterlabappsettings-customimages"></a>
A list of custom SageMaker images that are configured to run as a JupyterLab app.
*Required*: No
*Type*: Array of [CustomImage](aws-properties-sagemaker-userprofile-customimage.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResourceSpec`  <a name="cfn-sagemaker-userprofile-jupyterlabappsettings-defaultresourcespec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker image used by the JupyterLab app.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-userprofile-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmrSettings`  <a name="cfn-sagemaker-userprofile-jupyterlabappsettings-emrsettings"></a>
The configuration parameters that specify the IAM roles assumed by the execution role of SageMaker (assumable roles) and the cluster instances or job execution environments (execution roles or runtime roles) to manage and access resources required for running Amazon EMR clusters or Amazon EMR Serverless applications.
*Required*: No
*Type*: [EmrSettings](aws-properties-sagemaker-userprofile-emrsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfigArns`  <a name="cfn-sagemaker-userprofile-jupyterlabappsettings-lifecycleconfigarns"></a>
The Amazon Resource Name (ARN) of the lifecycle configurations attached to the user profile or domain. To remove a lifecycle config, you must set `LifecycleConfigArns` to an empty list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
