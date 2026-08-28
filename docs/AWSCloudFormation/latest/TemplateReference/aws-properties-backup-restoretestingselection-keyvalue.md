---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-restoretestingselection-keyvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::RestoreTestingSelection KeyValue
<a name="aws-properties-backup-restoretestingselection-keyvalue"></a>

Pair of two related strings. Allowed characters are letters, white space, and numbers that can be represented in UTF-8 and the following characters: ` + - = . _ : /`

## Syntax
<a name="aws-properties-backup-restoretestingselection-keyvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-restoretestingselection-keyvalue-syntax.json"></a>

```
{
  "[Key](#cfn-backup-restoretestingselection-keyvalue-key)" : {{String}},
  "[Value](#cfn-backup-restoretestingselection-keyvalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-restoretestingselection-keyvalue-syntax.yaml"></a>

```
  [Key](#cfn-backup-restoretestingselection-keyvalue-key): {{String}}
  [Value](#cfn-backup-restoretestingselection-keyvalue-value): {{String}}
```

## Properties
<a name="aws-properties-backup-restoretestingselection-keyvalue-properties"></a>

`Key`  <a name="cfn-backup-restoretestingselection-keyvalue-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-backup-restoretestingselection-keyvalue-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
