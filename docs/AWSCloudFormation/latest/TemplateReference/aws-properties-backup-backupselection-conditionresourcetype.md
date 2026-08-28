---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-backupselection-conditionresourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupSelection ConditionResourceType
<a name="aws-properties-backup-backupselection-conditionresourcetype"></a>

Specifies an object that contains an array of triplets made up of a condition type (such as `STRINGEQUALS`), a key, and a value. Conditions are used to filter resources in a selection that is assigned to a backup plan.

## Syntax
<a name="aws-properties-backup-backupselection-conditionresourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-backupselection-conditionresourcetype-syntax.json"></a>

```
{
  "[ConditionKey](#cfn-backup-backupselection-conditionresourcetype-conditionkey)" : {{String}},
  "[ConditionType](#cfn-backup-backupselection-conditionresourcetype-conditiontype)" : {{String}},
  "[ConditionValue](#cfn-backup-backupselection-conditionresourcetype-conditionvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-backupselection-conditionresourcetype-syntax.yaml"></a>

```
  [ConditionKey](#cfn-backup-backupselection-conditionresourcetype-conditionkey): {{String}}
  [ConditionType](#cfn-backup-backupselection-conditionresourcetype-conditiontype): {{String}}
  [ConditionValue](#cfn-backup-backupselection-conditionresourcetype-conditionvalue): {{String}}
```

## Properties
<a name="aws-properties-backup-backupselection-conditionresourcetype-properties"></a>

`ConditionKey`  <a name="cfn-backup-backupselection-conditionresourcetype-conditionkey"></a>
The key in a key-value pair. For example, in `"Department": "accounting"`, `"Department"` is the key.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConditionType`  <a name="cfn-backup-backupselection-conditionresourcetype-conditiontype"></a>
An operation, such as `STRINGEQUALS`, that is applied to a key-value pair used to filter resources in a selection.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConditionValue`  <a name="cfn-backup-backupselection-conditionresourcetype-conditionvalue"></a>
The value in a key-value pair. For example, in `"Department": "accounting"`, `"accounting"` is the value.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
