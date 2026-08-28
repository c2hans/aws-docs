---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-backupplan-indexactionsresourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupPlan IndexActionsResourceType
<a name="aws-properties-backup-backupplan-indexactionsresourcetype"></a>

Specifies index actions.

## Syntax
<a name="aws-properties-backup-backupplan-indexactionsresourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-backupplan-indexactionsresourcetype-syntax.json"></a>

```
{
  "[ResourceTypes](#cfn-backup-backupplan-indexactionsresourcetype-resourcetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-backup-backupplan-indexactionsresourcetype-syntax.yaml"></a>

```
  [ResourceTypes](#cfn-backup-backupplan-indexactionsresourcetype-resourcetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-backup-backupplan-indexactionsresourcetype-properties"></a>

`ResourceTypes`  <a name="cfn-backup-backupplan-indexactionsresourcetype-resourcetypes"></a>
0 or 1 index action will be accepted for each BackupRule.
Valid values:
+ `EBS` for Amazon Elastic Block Store
+ `S3` for Amazon Simple Storage Service (Amazon S3)
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
