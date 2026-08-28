---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-m2-environment-efsstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::M2::Environment EfsStorageConfiguration
<a name="aws-properties-m2-environment-efsstorageconfiguration"></a>

**Important**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Defines the storage configuration for an Amazon EFS file system.

## Syntax
<a name="aws-properties-m2-environment-efsstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-m2-environment-efsstorageconfiguration-syntax.json"></a>

```
{
  "[FileSystemId](#cfn-m2-environment-efsstorageconfiguration-filesystemid)" : {{String}},
  "[MountPoint](#cfn-m2-environment-efsstorageconfiguration-mountpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-m2-environment-efsstorageconfiguration-syntax.yaml"></a>

```
  [FileSystemId](#cfn-m2-environment-efsstorageconfiguration-filesystemid): {{String}}
  [MountPoint](#cfn-m2-environment-efsstorageconfiguration-mountpoint): {{String}}
```

## Properties
<a name="aws-properties-m2-environment-efsstorageconfiguration-properties"></a>

`FileSystemId`  <a name="cfn-m2-environment-efsstorageconfiguration-filesystemid"></a>
The file system identifier.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,200}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MountPoint`  <a name="cfn-m2-environment-efsstorageconfiguration-mountpoint"></a>
The mount point for the file system.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,200}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
