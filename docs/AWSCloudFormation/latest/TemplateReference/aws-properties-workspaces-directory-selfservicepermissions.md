---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-selfservicepermissions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory SelfservicePermissions
<a name="aws-properties-workspaces-directory-selfservicepermissions"></a>

Describes the self-service permissions for a directory. For more information, see [Enable Self-Service WorkSpace Management Capabilities for Your Users](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html).

## Syntax
<a name="aws-properties-workspaces-directory-selfservicepermissions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-selfservicepermissions-syntax.json"></a>

```
{
  "[ChangeComputeType](#cfn-workspaces-directory-selfservicepermissions-changecomputetype)" : {{String}},
  "[IncreaseVolumeSize](#cfn-workspaces-directory-selfservicepermissions-increasevolumesize)" : {{String}},
  "[RebuildWorkspace](#cfn-workspaces-directory-selfservicepermissions-rebuildworkspace)" : {{String}},
  "[RestartWorkspace](#cfn-workspaces-directory-selfservicepermissions-restartworkspace)" : {{String}},
  "[SwitchRunningMode](#cfn-workspaces-directory-selfservicepermissions-switchrunningmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-selfservicepermissions-syntax.yaml"></a>

```
  [ChangeComputeType](#cfn-workspaces-directory-selfservicepermissions-changecomputetype): {{String}}
  [IncreaseVolumeSize](#cfn-workspaces-directory-selfservicepermissions-increasevolumesize): {{String}}
  [RebuildWorkspace](#cfn-workspaces-directory-selfservicepermissions-rebuildworkspace): {{String}}
  [RestartWorkspace](#cfn-workspaces-directory-selfservicepermissions-restartworkspace): {{String}}
  [SwitchRunningMode](#cfn-workspaces-directory-selfservicepermissions-switchrunningmode): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-selfservicepermissions-properties"></a>

`ChangeComputeType`  <a name="cfn-workspaces-directory-selfservicepermissions-changecomputetype"></a>
Specifies whether users can change the compute type (bundle) for their WorkSpace.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncreaseVolumeSize`  <a name="cfn-workspaces-directory-selfservicepermissions-increasevolumesize"></a>
Specifies whether users can increase the volume size of the drives on their WorkSpace.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RebuildWorkspace`  <a name="cfn-workspaces-directory-selfservicepermissions-rebuildworkspace"></a>
Specifies whether users can rebuild the operating system of a WorkSpace to its original state.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestartWorkspace`  <a name="cfn-workspaces-directory-selfservicepermissions-restartworkspace"></a>
Specifies whether users can restart their WorkSpace.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SwitchRunningMode`  <a name="cfn-workspaces-directory-selfservicepermissions-switchrunningmode"></a>
Specifies whether users can switch the running mode of their WorkSpace.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
