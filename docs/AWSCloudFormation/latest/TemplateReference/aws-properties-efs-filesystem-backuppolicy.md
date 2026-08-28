---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-efs-filesystem-backuppolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EFS::FileSystem BackupPolicy
<a name="aws-properties-efs-filesystem-backuppolicy"></a>

The backup policy turns automatic backups for the file system on or off.

## Syntax
<a name="aws-properties-efs-filesystem-backuppolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-efs-filesystem-backuppolicy-syntax.json"></a>

```
{
  "[Status](#cfn-efs-filesystem-backuppolicy-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-efs-filesystem-backuppolicy-syntax.yaml"></a>

```
  [Status](#cfn-efs-filesystem-backuppolicy-status): {{String}}
```

## Properties
<a name="aws-properties-efs-filesystem-backuppolicy-properties"></a>

`Status`  <a name="cfn-efs-filesystem-backuppolicy-status"></a>
Set the backup policy status for the file system.
+ ** `ENABLED` ** - Turns automatic backups on for the file system.
+ ** `DISABLED` ** - Turns automatic backups off for the file system.
*Required*: Yes
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
