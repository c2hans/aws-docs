---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-jupyterlabappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain JupyterLabAppSettings
<a name="aws-properties-sagemaker-domain-jupyterlabappsettings"></a>

The settings for the JupyterLab application.

## Syntax
<a name="aws-properties-sagemaker-domain-jupyterlabappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-jupyterlabappsettings-syntax.json"></a>

```
{
  "[AppLifecycleManagement](#cfn-sagemaker-domain-jupyterlabappsettings-applifecyclemanagement)" : {{AppLifecycleManagement}},
  "[BuiltInLifecycleConfigArn](#cfn-sagemaker-domain-jupyterlabappsettings-builtinlifecycleconfigarn)" : {{String}},
  "[CodeRepositories](#cfn-sagemaker-domain-jupyterlabappsettings-coderepositories)" : {{[ CodeRepository, ... ]}},
  "[CustomImages](#cfn-sagemaker-domain-jupyterlabappsettings-customimages)" : {{[ CustomImage, ... ]}},
  "[DefaultResourceSpec](#cfn-sagemaker-domain-jupyterlabappsettings-defaultresourcespec)" : {{ResourceSpec}},
  "[LifecycleConfigArns](#cfn-sagemaker-domain-jupyterlabappsettings-lifecycleconfigarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-jupyterlabappsettings-syntax.yaml"></a>

```
  [AppLifecycleManagement](#cfn-sagemaker-domain-jupyterlabappsettings-applifecyclemanagement): {{
    AppLifecycleManagement}}
  [BuiltInLifecycleConfigArn](#cfn-sagemaker-domain-jupyterlabappsettings-builtinlifecycleconfigarn): {{String}}
  [CodeRepositories](#cfn-sagemaker-domain-jupyterlabappsettings-coderepositories): {{
    - CodeRepository}}
  [CustomImages](#cfn-sagemaker-domain-jupyterlabappsettings-customimages): {{
    - CustomImage}}
  [DefaultResourceSpec](#cfn-sagemaker-domain-jupyterlabappsettings-defaultresourcespec): {{
    ResourceSpec}}
  [LifecycleConfigArns](#cfn-sagemaker-domain-jupyterlabappsettings-lifecycleconfigarns): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-jupyterlabappsettings-properties"></a>

`AppLifecycleManagement`  <a name="cfn-sagemaker-domain-jupyterlabappsettings-applifecyclemanagement"></a>
Indicates whether idle shutdown is activated for JupyterLab applications.
*Required*: No
*Type*: [AppLifecycleManagement](aws-properties-sagemaker-domain-applifecyclemanagement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuiltInLifecycleConfigArn`  <a name="cfn-sagemaker-domain-jupyterlabappsettings-builtinlifecycleconfigarn"></a>
The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeRepositories`  <a name="cfn-sagemaker-domain-jupyterlabappsettings-coderepositories"></a>
A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.
*Required*: No
*Type*: Array of [CodeRepository](aws-properties-sagemaker-domain-coderepository.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomImages`  <a name="cfn-sagemaker-domain-jupyterlabappsettings-customimages"></a>
A list of custom SageMaker images that are configured to run as a JupyterLab app.
*Required*: No
*Type*: Array of [CustomImage](aws-properties-sagemaker-domain-customimage.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResourceSpec`  <a name="cfn-sagemaker-domain-jupyterlabappsettings-defaultresourcespec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker image used by the JupyterLab app.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-domain-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfigArns`  <a name="cfn-sagemaker-domain-jupyterlabappsettings-lifecycleconfigarns"></a>
The Amazon Resource Name (ARN) of the lifecycle configurations attached to the user profile or domain. To remove a lifecycle config, you must set `LifecycleConfigArns` to an empty list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
