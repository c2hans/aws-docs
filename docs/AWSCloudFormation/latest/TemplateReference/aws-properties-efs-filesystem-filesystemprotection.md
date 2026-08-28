---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-efs-filesystem-filesystemprotection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EFS::FileSystem FileSystemProtection
<a name="aws-properties-efs-filesystem-filesystemprotection"></a>

Describes the protection on the file system.

## Syntax
<a name="aws-properties-efs-filesystem-filesystemprotection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-efs-filesystem-filesystemprotection-syntax.json"></a>

```
{
  "[ReplicationOverwriteProtection](#cfn-efs-filesystem-filesystemprotection-replicationoverwriteprotection)" : {{String}}
}
```

### YAML
<a name="aws-properties-efs-filesystem-filesystemprotection-syntax.yaml"></a>

```
  [ReplicationOverwriteProtection](#cfn-efs-filesystem-filesystemprotection-replicationoverwriteprotection): {{String}}
```

## Properties
<a name="aws-properties-efs-filesystem-filesystemprotection-properties"></a>

`ReplicationOverwriteProtection`  <a name="cfn-efs-filesystem-filesystemprotection-replicationoverwriteprotection"></a>
The status of the file system's replication overwrite protection.
+ `ENABLED` – The file system cannot be used as the destination file system in a replication configuration. The file system is writeable. Replication overwrite protection is `ENABLED` by default.
+ `DISABLED` – The file system can be used as the destination file system in a replication configuration. The file system is read-only and can only be modified by EFS replication.
+ `REPLICATING` – The file system is being used as the destination file system in a replication configuration. The file system is read-only and is modified only by EFS replication.
If the replication configuration is deleted, the file system's replication overwrite protection is re-enabled, the file system becomes writeable.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
