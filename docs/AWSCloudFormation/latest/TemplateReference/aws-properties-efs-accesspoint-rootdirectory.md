---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-efs-accesspoint-rootdirectory.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EFS::AccessPoint RootDirectory
<a name="aws-properties-efs-accesspoint-rootdirectory"></a>

Specifies the directory on the Amazon EFS file system that the access point provides access to. The access point exposes the specified file system path as the root directory of your file system to applications using the access point. NFS clients using the access point can only access data in the access point's `RootDirectory` and its subdirectories.

## Syntax
<a name="aws-properties-efs-accesspoint-rootdirectory-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-efs-accesspoint-rootdirectory-syntax.json"></a>

```
{
  "[CreationInfo](#cfn-efs-accesspoint-rootdirectory-creationinfo)" : {{CreationInfo}},
  "[Path](#cfn-efs-accesspoint-rootdirectory-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-efs-accesspoint-rootdirectory-syntax.yaml"></a>

```
  [CreationInfo](#cfn-efs-accesspoint-rootdirectory-creationinfo): {{
    CreationInfo}}
  [Path](#cfn-efs-accesspoint-rootdirectory-path): {{String}}
```

## Properties
<a name="aws-properties-efs-accesspoint-rootdirectory-properties"></a>

`CreationInfo`  <a name="cfn-efs-accesspoint-rootdirectory-creationinfo"></a>
(Optional) Specifies the POSIX IDs and permissions to apply to the access point's `RootDirectory`. If the `RootDirectory` > `Path` specified does not exist, EFS creates the root directory using the `CreationInfo` settings when a client connects to an access point. When specifying the `CreationInfo`, you must provide values for all properties.
If you do not provide `CreationInfo` and the specified `RootDirectory` > `Path` does not exist, attempts to mount the file system using the access point will fail.
*Required*: No
*Type*: [CreationInfo](aws-properties-efs-accesspoint-creationinfo.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Path`  <a name="cfn-efs-accesspoint-rootdirectory-path"></a>
Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the `CreationInfo`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
