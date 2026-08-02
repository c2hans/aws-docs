---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::StorageVirtualMachine ActiveDirectoryConfiguration
<a name="aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration"></a>

Describes the self-managed Microsoft Active Directory to which you want to join the SVM. Joining an Active Directory provides user authentication and access control for SMB clients, including Microsoft Windows and macOS clients accessing the file system.

## Syntax
<a name="aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-syntax.json"></a>

```
{
  "[NetBiosName](#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-netbiosname)" : {{String}},
  "[SelfManagedActiveDirectoryConfiguration](#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration)" : {{SelfManagedActiveDirectoryConfiguration}}
}
```

### YAML
<a name="aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-syntax.yaml"></a>

```
  [NetBiosName](#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-netbiosname): {{String}}
  [SelfManagedActiveDirectoryConfiguration](#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration): {{
    SelfManagedActiveDirectoryConfiguration}}
```

## Properties
<a name="aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-properties"></a>

`NetBiosName`  <a name="cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-netbiosname"></a>
The NetBIOS name of the Active Directory computer object that will be created for your SVM.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfManagedActiveDirectoryConfiguration`  <a name="cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration"></a>
The configuration that Amazon FSx uses to join the ONTAP storage virtual machine (SVM) to your self-managed (including on-premises) Microsoft Active Directory directory.
*Required*: No
*Type*: [SelfManagedActiveDirectoryConfiguration](aws-properties-fsx-storagevirtualmachine-selfmanagedactivedirectoryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
