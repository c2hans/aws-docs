---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspaces-workspace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Workspace
<a name="aws-resource-workspaces-workspace"></a>

The `AWS::WorkSpaces::Workspace` resource specifies a WorkSpace.

Updates are not supported for the `BundleId`, `RootVolumeEncryptionEnabled`, `UserVolumeEncryptionEnabled`, or `VolumeEncryptionKey` properties. To update these properties, you must also update a property that triggers a replacement, such as the `UserName` property.

## Syntax
<a name="aws-resource-workspaces-workspace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspaces-workspace-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpaces::Workspace",
  "Properties" : {
      "[BundleId](#cfn-workspaces-workspace-bundleid)" : {{String}},
      "[DirectoryId](#cfn-workspaces-workspace-directoryid)" : {{String}},
      "[RootVolumeEncryptionEnabled](#cfn-workspaces-workspace-rootvolumeencryptionenabled)" : {{Boolean}},
      "[Tags](#cfn-workspaces-workspace-tags)" : {{[ Tag, ... ]}},
      "[UserName](#cfn-workspaces-workspace-username)" : {{String}},
      "[UserVolumeEncryptionEnabled](#cfn-workspaces-workspace-uservolumeencryptionenabled)" : {{Boolean}},
      "[VolumeEncryptionKey](#cfn-workspaces-workspace-volumeencryptionkey)" : {{String}},
      "[WorkspaceProperties](#cfn-workspaces-workspace-workspaceproperties)" : {{WorkspaceProperties}}
    }
}
```

### YAML
<a name="aws-resource-workspaces-workspace-syntax.yaml"></a>

```
Type: AWS::WorkSpaces::Workspace
Properties:
  [BundleId](#cfn-workspaces-workspace-bundleid): {{String}}
  [DirectoryId](#cfn-workspaces-workspace-directoryid): {{String}}
  [RootVolumeEncryptionEnabled](#cfn-workspaces-workspace-rootvolumeencryptionenabled): {{Boolean}}
  [Tags](#cfn-workspaces-workspace-tags): {{
    - Tag}}
  [UserName](#cfn-workspaces-workspace-username): {{String}}
  [UserVolumeEncryptionEnabled](#cfn-workspaces-workspace-uservolumeencryptionenabled): {{Boolean}}
  [VolumeEncryptionKey](#cfn-workspaces-workspace-volumeencryptionkey): {{String}}
  [WorkspaceProperties](#cfn-workspaces-workspace-workspaceproperties): {{
    WorkspaceProperties}}
```

## Properties
<a name="aws-resource-workspaces-workspace-properties"></a>

`BundleId`  <a name="cfn-workspaces-workspace-bundleid"></a>
The identifier of the bundle for the WorkSpace.
*Required*: Yes
*Type*: String
*Pattern*: `^wsb-[0-9a-z]{8,63}$`
*Update requires*: Updates are not supported.

`DirectoryId`  <a name="cfn-workspaces-workspace-directoryid"></a>
The identifier of the Directory Service directory for the WorkSpace.
*Required*: Yes
*Type*: String
*Pattern*: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
*Minimum*: `10`
*Maximum*: `65`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RootVolumeEncryptionEnabled`  <a name="cfn-workspaces-workspace-rootvolumeencryptionenabled"></a>
Indicates whether the data stored on the root volume is encrypted.
*Required*: No
*Type*: Boolean
*Update requires*: Updates are not supported.

`Tags`  <a name="cfn-workspaces-workspace-tags"></a>
The tags for the WorkSpace.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspaces-workspace-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserName`  <a name="cfn-workspaces-workspace-username"></a>
The user name of the user for the WorkSpace. This user name must exist in the Directory Service directory for the WorkSpace.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserVolumeEncryptionEnabled`  <a name="cfn-workspaces-workspace-uservolumeencryptionenabled"></a>
Indicates whether the data stored on the user volume is encrypted.
*Required*: No
*Type*: Boolean
*Update requires*: Updates are not supported.

`VolumeEncryptionKey`  <a name="cfn-workspaces-workspace-volumeencryptionkey"></a>
The symmetric AWS KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.
*Required*: No
*Type*: String
*Update requires*: Updates are not supported.

`WorkspaceProperties`  <a name="cfn-workspaces-workspace-workspaceproperties"></a>
The WorkSpace properties.
*Required*: No
*Type*: [WorkspaceProperties](aws-properties-workspaces-workspace-workspaceproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspaces-workspace-return-values"></a>

### Ref
<a name="aws-resource-workspaces-workspace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-workspaces-workspace-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-workspaces-workspace-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the WorkSpace, returned as a string.

`WorkspaceId`  <a name="WorkspaceId-fn::getatt"></a>
The identifier of the WorkSpace.

## See also
<a name="aws-resource-workspaces-workspace--seealso"></a>
+ [CreateWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaces.html) in the *Amazon WorkSpaces API Reference*
+ [Launch a Virtual Desktop Using Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspaces-tutorials.html) in the *Amazon WorkSpaces Administration Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
