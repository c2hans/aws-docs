---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-spacesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space SpaceSettings
<a name="aws-properties-sagemaker-space-spacesettings"></a>

A collection of space settings.

## Syntax
<a name="aws-properties-sagemaker-space-spacesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-spacesettings-syntax.json"></a>

```
{
  "[AppType](#cfn-sagemaker-space-spacesettings-apptype)" : {{String}},
  "[CodeEditorAppSettings](#cfn-sagemaker-space-spacesettings-codeeditorappsettings)" : {{SpaceCodeEditorAppSettings}},
  "[CustomFileSystems](#cfn-sagemaker-space-spacesettings-customfilesystems)" : {{[ CustomFileSystem, ... ]}},
  "[JupyterLabAppSettings](#cfn-sagemaker-space-spacesettings-jupyterlabappsettings)" : {{SpaceJupyterLabAppSettings}},
  "[JupyterServerAppSettings](#cfn-sagemaker-space-spacesettings-jupyterserverappsettings)" : {{JupyterServerAppSettings}},
  "[KernelGatewayAppSettings](#cfn-sagemaker-space-spacesettings-kernelgatewayappsettings)" : {{KernelGatewayAppSettings}},
  "[RemoteAccess](#cfn-sagemaker-space-spacesettings-remoteaccess)" : {{String}},
  "[SpaceManagedResources](#cfn-sagemaker-space-spacesettings-spacemanagedresources)" : {{String}},
  "[SpaceStorageSettings](#cfn-sagemaker-space-spacesettings-spacestoragesettings)" : {{SpaceStorageSettings}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-spacesettings-syntax.yaml"></a>

```
  [AppType](#cfn-sagemaker-space-spacesettings-apptype): {{String}}
  [CodeEditorAppSettings](#cfn-sagemaker-space-spacesettings-codeeditorappsettings): {{
    SpaceCodeEditorAppSettings}}
  [CustomFileSystems](#cfn-sagemaker-space-spacesettings-customfilesystems): {{
    - CustomFileSystem}}
  [JupyterLabAppSettings](#cfn-sagemaker-space-spacesettings-jupyterlabappsettings): {{
    SpaceJupyterLabAppSettings}}
  [JupyterServerAppSettings](#cfn-sagemaker-space-spacesettings-jupyterserverappsettings): {{
    JupyterServerAppSettings}}
  [KernelGatewayAppSettings](#cfn-sagemaker-space-spacesettings-kernelgatewayappsettings): {{
    KernelGatewayAppSettings}}
  [RemoteAccess](#cfn-sagemaker-space-spacesettings-remoteaccess): {{String}}
  [SpaceManagedResources](#cfn-sagemaker-space-spacesettings-spacemanagedresources): {{String}}
  [SpaceStorageSettings](#cfn-sagemaker-space-spacesettings-spacestoragesettings): {{
    SpaceStorageSettings}}
```

## Properties
<a name="aws-properties-sagemaker-space-spacesettings-properties"></a>

`AppType`  <a name="cfn-sagemaker-space-spacesettings-apptype"></a>
The type of app created within the space.
If using the [ UpdateSpace](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateSpace.html) API, you can't change the app type of your space by specifying a different value for this field.
*Required*: No
*Type*: String
*Allowed values*: `JupyterServer | KernelGateway | TensorBoard | RStudioServerPro | RSessionGateway | JupyterLab | CodeEditor`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeEditorAppSettings`  <a name="cfn-sagemaker-space-spacesettings-codeeditorappsettings"></a>
The Code Editor application settings.
*Required*: No
*Type*: [SpaceCodeEditorAppSettings](aws-properties-sagemaker-space-spacecodeeditorappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomFileSystems`  <a name="cfn-sagemaker-space-spacesettings-customfilesystems"></a>
A file system, created by you, that you assign to a space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.
*Required*: No
*Type*: Array of [CustomFileSystem](aws-properties-sagemaker-space-customfilesystem.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JupyterLabAppSettings`  <a name="cfn-sagemaker-space-spacesettings-jupyterlabappsettings"></a>
The settings for the JupyterLab application.
*Required*: No
*Type*: [SpaceJupyterLabAppSettings](aws-properties-sagemaker-space-spacejupyterlabappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JupyterServerAppSettings`  <a name="cfn-sagemaker-space-spacesettings-jupyterserverappsettings"></a>
The JupyterServer app settings.
*Required*: No
*Type*: [JupyterServerAppSettings](aws-properties-sagemaker-space-jupyterserverappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KernelGatewayAppSettings`  <a name="cfn-sagemaker-space-spacesettings-kernelgatewayappsettings"></a>
The KernelGateway app settings.
*Required*: No
*Type*: [KernelGatewayAppSettings](aws-properties-sagemaker-space-kernelgatewayappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemoteAccess`  <a name="cfn-sagemaker-space-spacesettings-remoteaccess"></a>
A setting that enables or disables remote access for a SageMaker space. When enabled, this allows you to connect to the remote space from your local IDE.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceManagedResources`  <a name="cfn-sagemaker-space-spacesettings-spacemanagedresources"></a>
If you enable this option, SageMaker AI creates the following resources on your behalf when you create the space:
+ The user profile that possesses the space.
+ The app that the space contains.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceStorageSettings`  <a name="cfn-sagemaker-space-spacesettings-spacestoragesettings"></a>
The storage settings for a space.
*Required*: No
*Type*: [SpaceStorageSettings](aws-properties-sagemaker-space-spacestoragesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
