---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition FSxWindowsFileServerVolumeConfiguration
<a name="aws-properties-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration"></a>

This parameter is specified when you're using [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) file system for task storage.

For more information and the input format, see [Amazon FSx for Windows File Server volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/wfsx-volumes.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-syntax.json"></a>

```
{
  "[AuthorizationConfig](#cfn-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-authorizationconfig)" : {{FSxAuthorizationConfig}},
  "[FileSystemId](#cfn-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-filesystemid)" : {{String}},
  "[RootDirectory](#cfn-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-rootdirectory)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-syntax.yaml"></a>

```
  [AuthorizationConfig](#cfn-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-authorizationconfig): {{
    FSxAuthorizationConfig}}
  [FileSystemId](#cfn-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-filesystemid): {{String}}
  [RootDirectory](#cfn-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-rootdirectory): {{String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-properties"></a>

`AuthorizationConfig`  <a name="cfn-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-authorizationconfig"></a>
The authorization configuration details for the Amazon FSx for Windows File Server file system.
*Required*: No
*Type*: [FSxAuthorizationConfig](aws-properties-ecs-taskdefinition-fsxauthorizationconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemId`  <a name="cfn-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-filesystemid"></a>
The Amazon FSx for Windows File Server file system ID to use.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RootDirectory`  <a name="cfn-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration-rootdirectory"></a>
The directory within the Amazon FSx for Windows File Server file system to mount as the root directory inside the host.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
