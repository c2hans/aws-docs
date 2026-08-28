---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationfsxontap-nfs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationFSxONTAP NFS
<a name="aws-properties-datasync-locationfsxontap-nfs"></a>

Specifies the Network File System (NFS) protocol configuration that AWS DataSync uses to access a storage virtual machine (SVM) on your Amazon FSx for NetApp ONTAP file system. For more information, see [Accessing FSx for ONTAP file systems](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-access).

## Syntax
<a name="aws-properties-datasync-locationfsxontap-nfs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationfsxontap-nfs-syntax.json"></a>

```
{
  "[MountOptions](#cfn-datasync-locationfsxontap-nfs-mountoptions)" : {{NfsMountOptions}}
}
```

### YAML
<a name="aws-properties-datasync-locationfsxontap-nfs-syntax.yaml"></a>

```
  [MountOptions](#cfn-datasync-locationfsxontap-nfs-mountoptions): {{
    NfsMountOptions}}
```

## Properties
<a name="aws-properties-datasync-locationfsxontap-nfs-properties"></a>

`MountOptions`  <a name="cfn-datasync-locationfsxontap-nfs-mountoptions"></a>
Specifies how DataSync can access a location using the NFS protocol.
*Required*: Yes
*Type*: [NfsMountOptions](aws-properties-datasync-locationfsxontap-nfsmountoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
