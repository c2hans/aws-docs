---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-restoretestingselection-protectedresourceconditions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::RestoreTestingSelection ProtectedResourceConditions
<a name="aws-properties-backup-restoretestingselection-protectedresourceconditions"></a>

The conditions that you define for resources in your restore testing plan using tags.

## Syntax
<a name="aws-properties-backup-restoretestingselection-protectedresourceconditions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-restoretestingselection-protectedresourceconditions-syntax.json"></a>

```
{
  "[StringEquals](#cfn-backup-restoretestingselection-protectedresourceconditions-stringequals)" : {{[ KeyValue, ... ]}},
  "[StringNotEquals](#cfn-backup-restoretestingselection-protectedresourceconditions-stringnotequals)" : {{[ KeyValue, ... ]}}
}
```

### YAML
<a name="aws-properties-backup-restoretestingselection-protectedresourceconditions-syntax.yaml"></a>

```
  [StringEquals](#cfn-backup-restoretestingselection-protectedresourceconditions-stringequals): {{
    - KeyValue}}
  [StringNotEquals](#cfn-backup-restoretestingselection-protectedresourceconditions-stringnotequals): {{
    - KeyValue}}
```

## Properties
<a name="aws-properties-backup-restoretestingselection-protectedresourceconditions-properties"></a>

`StringEquals`  <a name="cfn-backup-restoretestingselection-protectedresourceconditions-stringequals"></a>
Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called "exact matching."
*Required*: No
*Type*: Array of [KeyValue](aws-properties-backup-restoretestingselection-keyvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringNotEquals`  <a name="cfn-backup-restoretestingselection-protectedresourceconditions-stringnotequals"></a>
Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called "negated matching."
*Required*: No
*Type*: Array of [KeyValue](aws-properties-backup-restoretestingselection-keyvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
