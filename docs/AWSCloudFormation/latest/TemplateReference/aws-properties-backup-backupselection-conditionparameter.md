---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-backupselection-conditionparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupSelection ConditionParameter
<a name="aws-properties-backup-backupselection-conditionparameter"></a>

Includes information about tags you define to assign tagged resources to a backup plan.

Include the prefix `aws:ResourceTag` in your tags. For example, `"aws:ResourceTag/TagKey1": "Value1"`.

## Syntax
<a name="aws-properties-backup-backupselection-conditionparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-backupselection-conditionparameter-syntax.json"></a>

```
{
  "[ConditionKey](#cfn-backup-backupselection-conditionparameter-conditionkey)" : {{String}},
  "[ConditionValue](#cfn-backup-backupselection-conditionparameter-conditionvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-backupselection-conditionparameter-syntax.yaml"></a>

```
  [ConditionKey](#cfn-backup-backupselection-conditionparameter-conditionkey): {{String}}
  [ConditionValue](#cfn-backup-backupselection-conditionparameter-conditionvalue): {{String}}
```

## Properties
<a name="aws-properties-backup-backupselection-conditionparameter-properties"></a>

`ConditionKey`  <a name="cfn-backup-backupselection-conditionparameter-conditionkey"></a>
The key in a key-value pair. For example, in the tag `Department: Accounting`, `Department` is the key.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConditionValue`  <a name="cfn-backup-backupselection-conditionparameter-conditionvalue"></a>
The value in a key-value pair. For example, in the tag `Department: Accounting`, `Accounting` is the value.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
