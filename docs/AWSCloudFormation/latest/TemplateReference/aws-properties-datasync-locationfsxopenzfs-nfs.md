---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationfsxopenzfs-nfs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationFSxOpenZFS NFS
<a name="aws-properties-datasync-locationfsxopenzfs-nfs"></a>

Represents the Network File System (NFS) protocol that AWS DataSync uses to access your Amazon FSx for OpenZFS file system.

## Syntax
<a name="aws-properties-datasync-locationfsxopenzfs-nfs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationfsxopenzfs-nfs-syntax.json"></a>

```
{
  "[MountOptions](#cfn-datasync-locationfsxopenzfs-nfs-mountoptions)" : {{MountOptions}}
}
```

### YAML
<a name="aws-properties-datasync-locationfsxopenzfs-nfs-syntax.yaml"></a>

```
  [MountOptions](#cfn-datasync-locationfsxopenzfs-nfs-mountoptions): {{
    MountOptions}}
```

## Properties
<a name="aws-properties-datasync-locationfsxopenzfs-nfs-properties"></a>

`MountOptions`  <a name="cfn-datasync-locationfsxopenzfs-nfs-mountoptions"></a>
Represents the mount options that are available for DataSync to access an NFS location.
*Required*: Yes
*Type*: [MountOptions](aws-properties-datasync-locationfsxopenzfs-mountoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
