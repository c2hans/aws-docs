---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-selfmanagedactivedirectoryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem SelfManagedActiveDirectoryConfiguration
<a name="aws-properties-fsx-filesystem-selfmanagedactivedirectoryconfiguration"></a>

The configuration that Amazon FSx uses to join a FSx for Windows File Server file system or an FSx for ONTAP storage virtual machine (SVM) to a self-managed (including on-premises) Microsoft Active Directory (AD) directory. For more information, see [ Using Amazon FSx for Windows with your self-managed Microsoft Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html) or [Managing FSx for ONTAP SVMs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html).

## Syntax
<a name="aws-properties-fsx-filesystem-selfmanagedactivedirectoryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-selfmanagedactivedirectoryconfiguration-syntax.json"></a>

```
{
  "[DnsIps](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-dnsips)" : {{[ String, ... ]}},
  "[DomainJoinServiceAccountSecret](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-domainjoinserviceaccountsecret)" : {{String}},
  "[DomainName](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-domainname)" : {{String}},
  "[FileSystemAdministratorsGroup](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-filesystemadministratorsgroup)" : {{String}},
  "[OrganizationalUnitDistinguishedName](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-organizationalunitdistinguishedname)" : {{String}},
  "[Password](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-password)" : {{String}},
  "[UserName](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-selfmanagedactivedirectoryconfiguration-syntax.yaml"></a>

```
  [DnsIps](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-dnsips): {{
    - String}}
  [DomainJoinServiceAccountSecret](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-domainjoinserviceaccountsecret): {{String}}
  [DomainName](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-domainname): {{String}}
  [FileSystemAdministratorsGroup](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-filesystemadministratorsgroup): {{String}}
  [OrganizationalUnitDistinguishedName](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-organizationalunitdistinguishedname): {{String}}
  [Password](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-password): {{String}}
  [UserName](#cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-username): {{String}}
```

## Properties
<a name="aws-properties-fsx-filesystem-selfmanagedactivedirectoryconfiguration-properties"></a>

`DnsIps`  <a name="cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-dnsips"></a>
A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.
*Required*: Conditional
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainJoinServiceAccountSecret`  <a name="cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-domainjoinserviceaccountsecret"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the self-managed Active Directory domain join service account credentials. When provided, Amazon FSx uses the credentials stored in this secret to join the file system to your self-managed Active Directory domain.
The secret must contain two key-value pairs:
+ `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME` - The username for the service account
+ `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD` - The password for the service account
For more information, see [ Using Amazon FSx for Windows with your self-managed Microsoft Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-manage-prereqs.html) or [ Using Amazon FSx for ONTAP with your self-managed Microsoft Active Directory](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/self-manage-prereqs.html).
*Required*: No
*Type*: String
*Pattern*: `^arn:[^:]{1,63}:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+-[a-zA-Z0-9]{6}$`
*Minimum*: `64`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-domainname"></a>
The fully qualified domain name of the self-managed AD directory, such as `corp.example.com`.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemAdministratorsGroup`  <a name="cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-filesystemadministratorsgroup"></a>
(Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don't provide one, your AD domain's Domain Admins group is used.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OrganizationalUnitDistinguishedName`  <a name="cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-organizationalunitdistinguishedname"></a>
(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory. Amazon FSx only accepts OU as the direct parent of the file system. An example is `OU=FSx,DC=yourdomain,DC=corp,DC=com`. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253). If none is provided, the FSx file system is created in the default location of your self-managed AD directory.
Only Organizational Unit (OU) objects can be the direct parent of the file system that you're creating.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,2000}$`
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Password`  <a name="cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-password"></a>
The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
*Required*: No
*Type*: String
*Pattern*: `^.{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserName`  <a name="cfn-fsx-filesystem-selfmanagedactivedirectoryconfiguration-username"></a>
The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in `OrganizationalUnitDistinguishedName`, or in the default location of your AD domain.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
