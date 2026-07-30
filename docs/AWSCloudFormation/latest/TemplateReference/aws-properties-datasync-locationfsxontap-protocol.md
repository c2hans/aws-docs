---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationfsxontap-protocol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationFSxONTAP Protocol
<a name="aws-properties-datasync-locationfsxontap-protocol"></a>

Specifies the data transfer protocol that AWS DataSync uses to access your Amazon FSx file system.

## Syntax
<a name="aws-properties-datasync-locationfsxontap-protocol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationfsxontap-protocol-syntax.json"></a>

```
{
  "[NFS](#cfn-datasync-locationfsxontap-protocol-nfs)" : {{NFS}},
  "[SMB](#cfn-datasync-locationfsxontap-protocol-smb)" : {{SMB}}
}
```

### YAML
<a name="aws-properties-datasync-locationfsxontap-protocol-syntax.yaml"></a>

```
  [NFS](#cfn-datasync-locationfsxontap-protocol-nfs): {{
    NFS}}
  [SMB](#cfn-datasync-locationfsxontap-protocol-smb): {{
    SMB}}
```

## Properties
<a name="aws-properties-datasync-locationfsxontap-protocol-properties"></a>

`NFS`  <a name="cfn-datasync-locationfsxontap-protocol-nfs"></a>
Specifies the Network File System (NFS) protocol configuration that DataSync uses to access your FSx for ONTAP file system's storage virtual machine (SVM).
*Required*: No
*Type*: [NFS](aws-properties-datasync-locationfsxontap-nfs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SMB`  <a name="cfn-datasync-locationfsxontap-protocol-smb"></a>
Specifies the Server Message Block (SMB) protocol configuration that DataSync uses to access your FSx for ONTAP file system's SVM.
*Required*: No
*Type*: [SMB](aws-properties-datasync-locationfsxontap-smb.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
