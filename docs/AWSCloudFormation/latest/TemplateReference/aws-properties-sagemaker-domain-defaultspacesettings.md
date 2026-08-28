---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-defaultspacesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain DefaultSpaceSettings
<a name="aws-properties-sagemaker-domain-defaultspacesettings"></a>

The default settings for shared spaces that users create in the domain.

SageMaker applies these settings only to shared spaces. It doesn't apply them to private spaces.

## Syntax
<a name="aws-properties-sagemaker-domain-defaultspacesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-defaultspacesettings-syntax.json"></a>

```
{
  "[CustomFileSystemConfigs](#cfn-sagemaker-domain-defaultspacesettings-customfilesystemconfigs)" : {{[ CustomFileSystemConfig, ... ]}},
  "[CustomPosixUserConfig](#cfn-sagemaker-domain-defaultspacesettings-customposixuserconfig)" : {{CustomPosixUserConfig}},
  "[ExecutionRole](#cfn-sagemaker-domain-defaultspacesettings-executionrole)" : {{String}},
  "[JupyterLabAppSettings](#cfn-sagemaker-domain-defaultspacesettings-jupyterlabappsettings)" : {{JupyterLabAppSettings}},
  "[JupyterServerAppSettings](#cfn-sagemaker-domain-defaultspacesettings-jupyterserverappsettings)" : {{JupyterServerAppSettings}},
  "[KernelGatewayAppSettings](#cfn-sagemaker-domain-defaultspacesettings-kernelgatewayappsettings)" : {{KernelGatewayAppSettings}},
  "[SecurityGroups](#cfn-sagemaker-domain-defaultspacesettings-securitygroups)" : {{[ String, ... ]}},
  "[SpaceStorageSettings](#cfn-sagemaker-domain-defaultspacesettings-spacestoragesettings)" : {{DefaultSpaceStorageSettings}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-defaultspacesettings-syntax.yaml"></a>

```
  [CustomFileSystemConfigs](#cfn-sagemaker-domain-defaultspacesettings-customfilesystemconfigs): {{
    - CustomFileSystemConfig}}
  [CustomPosixUserConfig](#cfn-sagemaker-domain-defaultspacesettings-customposixuserconfig): {{
    CustomPosixUserConfig}}
  [ExecutionRole](#cfn-sagemaker-domain-defaultspacesettings-executionrole): {{String}}
  [JupyterLabAppSettings](#cfn-sagemaker-domain-defaultspacesettings-jupyterlabappsettings): {{
    JupyterLabAppSettings}}
  [JupyterServerAppSettings](#cfn-sagemaker-domain-defaultspacesettings-jupyterserverappsettings): {{
    JupyterServerAppSettings}}
  [KernelGatewayAppSettings](#cfn-sagemaker-domain-defaultspacesettings-kernelgatewayappsettings): {{
    KernelGatewayAppSettings}}
  [SecurityGroups](#cfn-sagemaker-domain-defaultspacesettings-securitygroups): {{
    - String}}
  [SpaceStorageSettings](#cfn-sagemaker-domain-defaultspacesettings-spacestoragesettings): {{
    DefaultSpaceStorageSettings}}
```

## Properties
<a name="aws-properties-sagemaker-domain-defaultspacesettings-properties"></a>

`CustomFileSystemConfigs`  <a name="cfn-sagemaker-domain-defaultspacesettings-customfilesystemconfigs"></a>
The settings for assigning a custom file system to a domain. Permitted users can access this file system in Amazon SageMaker AI Studio.
*Required*: No
*Type*: Array of [CustomFileSystemConfig](aws-properties-sagemaker-domain-customfilesystemconfig.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomPosixUserConfig`  <a name="cfn-sagemaker-domain-defaultspacesettings-customposixuserconfig"></a>
Property description not available.
*Required*: No
*Type*: [CustomPosixUserConfig](aws-properties-sagemaker-domain-customposixuserconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRole`  <a name="cfn-sagemaker-domain-defaultspacesettings-executionrole"></a>
The ARN of the execution role for the space.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JupyterLabAppSettings`  <a name="cfn-sagemaker-domain-defaultspacesettings-jupyterlabappsettings"></a>
Property description not available.
*Required*: No
*Type*: [JupyterLabAppSettings](aws-properties-sagemaker-domain-jupyterlabappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JupyterServerAppSettings`  <a name="cfn-sagemaker-domain-defaultspacesettings-jupyterserverappsettings"></a>
The JupyterServer app settings.
*Required*: No
*Type*: [JupyterServerAppSettings](aws-properties-sagemaker-domain-jupyterserverappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KernelGatewayAppSettings`  <a name="cfn-sagemaker-domain-defaultspacesettings-kernelgatewayappsettings"></a>
The KernelGateway app settings.
*Required*: No
*Type*: [KernelGatewayAppSettings](aws-properties-sagemaker-domain-kernelgatewayappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroups`  <a name="cfn-sagemaker-domain-defaultspacesettings-securitygroups"></a>
The security group IDs for the Amazon VPC that the space uses for communication.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `32 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceStorageSettings`  <a name="cfn-sagemaker-domain-defaultspacesettings-spacestoragesettings"></a>
Property description not available.
*Required*: No
*Type*: [DefaultSpaceStorageSettings](aws-properties-sagemaker-domain-defaultspacestoragesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
