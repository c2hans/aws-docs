---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-snapshotschedule-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::SnapshotSchedule Tag
<a name="aws-properties-redshift-snapshotschedule-tag"></a>

A tag consisting of a name/value pair for a resource.

## Syntax
<a name="aws-properties-redshift-snapshotschedule-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-snapshotschedule-tag-syntax.json"></a>

```
{
  "[Key](#cfn-redshift-snapshotschedule-tag-key)" : {{String}},
  "[Value](#cfn-redshift-snapshotschedule-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-snapshotschedule-tag-syntax.yaml"></a>

```
  [Key](#cfn-redshift-snapshotschedule-tag-key): {{String}}
  [Value](#cfn-redshift-snapshotschedule-tag-value): {{String}}
```

## Properties
<a name="aws-properties-redshift-snapshotschedule-tag-properties"></a>

`Key`  <a name="cfn-redshift-snapshotschedule-tag-key"></a>
The key, or name, for the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-redshift-snapshotschedule-tag-value"></a>
The value for the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
