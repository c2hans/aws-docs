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
