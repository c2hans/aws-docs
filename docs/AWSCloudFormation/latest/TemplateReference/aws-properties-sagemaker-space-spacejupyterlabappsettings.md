---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-spacejupyterlabappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space SpaceJupyterLabAppSettings
<a name="aws-properties-sagemaker-space-spacejupyterlabappsettings"></a>

The settings for the JupyterLab application within a space.

## Syntax
<a name="aws-properties-sagemaker-space-spacejupyterlabappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-spacejupyterlabappsettings-syntax.json"></a>

```
{
  "[AppLifecycleManagement](#cfn-sagemaker-space-spacejupyterlabappsettings-applifecyclemanagement)" : {{SpaceAppLifecycleManagement}},
  "[CodeRepositories](#cfn-sagemaker-space-spacejupyterlabappsettings-coderepositories)" : {{[ CodeRepository, ... ]}},
  "[DefaultResourceSpec](#cfn-sagemaker-space-spacejupyterlabappsettings-defaultresourcespec)" : {{ResourceSpec}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-spacejupyterlabappsettings-syntax.yaml"></a>

```
  [AppLifecycleManagement](#cfn-sagemaker-space-spacejupyterlabappsettings-applifecyclemanagement): {{
    SpaceAppLifecycleManagement}}
  [CodeRepositories](#cfn-sagemaker-space-spacejupyterlabappsettings-coderepositories): {{
    - CodeRepository}}
  [DefaultResourceSpec](#cfn-sagemaker-space-spacejupyterlabappsettings-defaultresourcespec): {{
    ResourceSpec}}
```

## Properties
<a name="aws-properties-sagemaker-space-spacejupyterlabappsettings-properties"></a>

`AppLifecycleManagement`  <a name="cfn-sagemaker-space-spacejupyterlabappsettings-applifecyclemanagement"></a>
Settings that are used to configure and manage the lifecycle of JupyterLab applications in a space.
*Required*: No
*Type*: [SpaceAppLifecycleManagement](aws-properties-sagemaker-space-spaceapplifecyclemanagement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeRepositories`  <a name="cfn-sagemaker-space-spacejupyterlabappsettings-coderepositories"></a>
A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.
*Required*: No
*Type*: Array of [CodeRepository](aws-properties-sagemaker-space-coderepository.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResourceSpec`  <a name="cfn-sagemaker-space-spacejupyterlabappsettings-defaultresourcespec"></a>
Specifies the ARNs of a SageMaker image and SageMaker image version, and the instance type that the version runs on.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-space-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
