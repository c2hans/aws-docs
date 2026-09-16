---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-backup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::Backup
<a name="aws-resource-fsx-backup"></a>

A backup of an Amazon FSx for Windows File Server, Amazon FSx for Lustre file system, Amazon FSx for NetApp ONTAP volume, or Amazon FSx for OpenZFS file system.

## Syntax
<a name="aws-resource-fsx-backup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fsx-backup-syntax.json"></a>

```
{
  "Type" : "AWS::FSx::Backup",
  "Properties" : {
      "[FileSystemId](#cfn-fsx-backup-filesystemid)" : {{String}},
      "[Tags](#cfn-fsx-backup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-fsx-backup-syntax.yaml"></a>

```
Type: AWS::FSx::Backup
Properties:
  [FileSystemId](#cfn-fsx-backup-filesystemid): {{String}}
  [Tags](#cfn-fsx-backup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-fsx-backup-properties"></a>

`FileSystemId`  <a name="cfn-fsx-backup-filesystemid"></a>
The ID of the file system to back up.
*Required*: Yes
*Type*: String
*Pattern*: `^(fs-[0-9a-f]{8,})$`
*Minimum*: `11`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-fsx-backup-tags"></a>
The tags associated with a particular file system.
*Required*: No
*Type*: Array of [Tag](aws-properties-fsx-backup-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fsx-backup-return-values"></a>

### Ref
<a name="aws-resource-fsx-backup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fsx-backup-return-values-fn--getatt"></a>

####
<a name="aws-resource-fsx-backup-return-values-fn--getatt-fn--getatt"></a>

`BackupId`  <a name="BackupId-fn::getatt"></a>
The ID of the backup.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time when a particular backup was created.

`Lifecycle`  <a name="Lifecycle-fn::getatt"></a>
The lifecycle status of the backup.
+ `AVAILABLE` - The backup is fully available.
+ `PENDING` - For user-initiated backups on Lustre file systems only; Amazon FSx hasn't started creating the backup.
+ `CREATING` - Amazon FSx is creating the backup.
+ `TRANSFERRING` - For user-initiated backups on Lustre file systems only; Amazon FSx is transferring the backup to Amazon S3.
+ `COPYING` - Amazon FSx is copying the backup.
+ `DELETED` - Amazon FSx deleted the backup and it's no longer available.
+ `FAILED` - Amazon FSx couldn't finish the backup.

`ResourceARN`  <a name="ResourceARN-fn::getatt"></a>
The Amazon Resource Name (ARN) for the backup resource.

`Type`  <a name="Type-fn::getatt"></a>
The type of the file-system backup.
