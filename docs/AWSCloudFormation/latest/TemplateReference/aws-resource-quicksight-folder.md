---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-folder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Folder
<a name="aws-resource-quicksight-folder"></a>

Creates an empty shared folder.

## Syntax
<a name="aws-resource-quicksight-folder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-folder-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Folder",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-folder-awsaccountid)" : {{String}},
      "[FolderId](#cfn-quicksight-folder-folderid)" : {{String}},
      "[FolderType](#cfn-quicksight-folder-foldertype)" : {{String}},
      "[Name](#cfn-quicksight-folder-name)" : {{String}},
      "[ParentFolderArn](#cfn-quicksight-folder-parentfolderarn)" : {{String}},
      "[Permissions](#cfn-quicksight-folder-permissions)" : {{[ ResourcePermission, ... ]}},
      "[SharingModel](#cfn-quicksight-folder-sharingmodel)" : {{String}},
      "[Tags](#cfn-quicksight-folder-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-folder-syntax.yaml"></a>

```
Type: AWS::QuickSight::Folder
Properties:
  [AwsAccountId](#cfn-quicksight-folder-awsaccountid): {{String}}
  [FolderId](#cfn-quicksight-folder-folderid): {{String}}
  [FolderType](#cfn-quicksight-folder-foldertype): {{String}}
  [Name](#cfn-quicksight-folder-name): {{String}}
  [ParentFolderArn](#cfn-quicksight-folder-parentfolderarn): {{String}}
  [Permissions](#cfn-quicksight-folder-permissions): {{
    - ResourcePermission}}
  [SharingModel](#cfn-quicksight-folder-sharingmodel): {{String}}
  [Tags](#cfn-quicksight-folder-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-quicksight-folder-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-folder-awsaccountid"></a>
The ID for the AWS account where you want to create the folder.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FolderId`  <a name="cfn-quicksight-folder-folderid"></a>
The ID of the folder.
*Required*: No
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FolderType`  <a name="cfn-quicksight-folder-foldertype"></a>
The type of folder it is.
*Required*: No
*Type*: String
*Allowed values*: `SHARED | RESTRICTED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-quicksight-folder-name"></a>
A display name for the folder.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParentFolderArn`  <a name="cfn-quicksight-folder-parentfolderarn"></a>
The Amazon Resource Name (ARN) for the folder.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Permissions`  <a name="cfn-quicksight-folder-permissions"></a>
A structure that describes the principals and the resource-level permissions of a folder.
To specify no permissions, omit `Permissions`.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-folder-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharingModel`  <a name="cfn-quicksight-folder-sharingmodel"></a>
The sharing scope of the folder.
*Required*: No
*Type*: String
*Allowed values*: `ACCOUNT | NAMESPACE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-quicksight-folder-tags"></a>
A list of tags for the folders that you want to apply overrides to.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-folder-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-folder-return-values"></a>

### Ref
<a name="aws-resource-quicksight-folder-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-folder-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-folder-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the folder.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time that the folder was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The time that the folder was last updated.
