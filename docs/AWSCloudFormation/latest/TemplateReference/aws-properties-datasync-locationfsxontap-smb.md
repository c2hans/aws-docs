---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationfsxontap-smb.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationFSxONTAP SMB
<a name="aws-properties-datasync-locationfsxontap-smb"></a>

Specifies the Server Message Block (SMB) protocol configuration that AWS DataSync uses to access a storage virtual machine (SVM) on your Amazon FSx for NetApp ONTAP file system. For more information, see [Accessing FSx for ONTAP file systems](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-access).

## Syntax
<a name="aws-properties-datasync-locationfsxontap-smb-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationfsxontap-smb-syntax.json"></a>

```
{
  "[CmkSecretConfig](#cfn-datasync-locationfsxontap-smb-cmksecretconfig)" : {{CmkSecretConfig}},
  "[CustomSecretConfig](#cfn-datasync-locationfsxontap-smb-customsecretconfig)" : {{CustomSecretConfig}},
  "[Domain](#cfn-datasync-locationfsxontap-smb-domain)" : {{String}},
  "[ManagedSecretConfig](#cfn-datasync-locationfsxontap-smb-managedsecretconfig)" : {{ManagedSecretConfig}},
  "[MountOptions](#cfn-datasync-locationfsxontap-smb-mountoptions)" : {{SmbMountOptions}},
  "[Password](#cfn-datasync-locationfsxontap-smb-password)" : {{String}},
  "[User](#cfn-datasync-locationfsxontap-smb-user)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationfsxontap-smb-syntax.yaml"></a>

```
  [CmkSecretConfig](#cfn-datasync-locationfsxontap-smb-cmksecretconfig): {{
    CmkSecretConfig}}
  [CustomSecretConfig](#cfn-datasync-locationfsxontap-smb-customsecretconfig): {{
    CustomSecretConfig}}
  [Domain](#cfn-datasync-locationfsxontap-smb-domain): {{String}}
  [ManagedSecretConfig](#cfn-datasync-locationfsxontap-smb-managedsecretconfig): {{
    ManagedSecretConfig}}
  [MountOptions](#cfn-datasync-locationfsxontap-smb-mountoptions): {{
    SmbMountOptions}}
  [Password](#cfn-datasync-locationfsxontap-smb-password): {{String}}
  [User](#cfn-datasync-locationfsxontap-smb-user): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationfsxontap-smb-properties"></a>

`CmkSecretConfig`  <a name="cfn-datasync-locationfsxontap-smb-cmksecretconfig"></a>
Property description not available.
*Required*: No
*Type*: [CmkSecretConfig](aws-properties-datasync-locationfsxontap-cmksecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomSecretConfig`  <a name="cfn-datasync-locationfsxontap-smb-customsecretconfig"></a>
Property description not available.
*Required*: No
*Type*: [CustomSecretConfig](aws-properties-datasync-locationfsxontap-customsecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-datasync-locationfsxontap-smb-domain"></a>
Specifies the name of the Windows domain that your storage virtual machine (SVM) belongs to.
If you have multiple domains in your environment, configuring this setting makes sure that DataSync connects to the right SVM.
If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right SVM.
*Required*: No
*Type*: String
*Pattern*: `^([A-Za-z0-9]+[A-Za-z0-9-.]*)*[A-Za-z0-9-]*[A-Za-z0-9]$`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedSecretConfig`  <a name="cfn-datasync-locationfsxontap-smb-managedsecretconfig"></a>
Property description not available.
*Required*: No
*Type*: [ManagedSecretConfig](aws-properties-datasync-locationfsxontap-managedsecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountOptions`  <a name="cfn-datasync-locationfsxontap-smb-mountoptions"></a>
Specifies how DataSync can access a location using the SMB protocol.
*Required*: Yes
*Type*: [SmbMountOptions](aws-properties-datasync-locationfsxontap-smbmountoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Password`  <a name="cfn-datasync-locationfsxontap-smb-password"></a>
Specifies the password of a user who has permission to access your SVM.
*Required*: No
*Type*: String
*Pattern*: `^.{0,104}$`
*Maximum*: `104`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-datasync-locationfsxontap-smb-user"></a>
Specifies a user name that can mount the location and access the files, folders, and metadata that you need in the SVM.
If you provide a user in your Active Directory, note the following:
+ If you're using AWS Directory Service for Microsoft Active Directory, the user must be a member of the AWS Delegated FSx Administrators group.
+  If you're using a self-managed Active Directory, the user must be a member of either the Domain Admins group or a custom group that you specified for file system administration when you created your file system.
Make sure that the user has the permissions it needs to copy the data you want:
+ `SE_TCB_NAME`: Required to set object ownership and file metadata. With this privilege, you also can copy NTFS discretionary access lists (DACLs).
+ `SE_SECURITY_NAME`: May be needed to copy NTFS system access control lists (SACLs). This operation specifically requires the Windows privilege, which is granted to members of the Domain Admins group. If you configure your task to copy SACLs, make sure that the user has the required privileges. For information about copying SACLs, see [Ownership and permissions-related options](https://docs.aws.amazon.com/datasync/latest/userguide/create-task.html#configure-ownership-and-permissions).
*Required*: Yes
*Type*: String
*Pattern*: `^[^\x5B\x5D\\/:;|=,+*?]{1,104}$`
*Maximum*: `104`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
