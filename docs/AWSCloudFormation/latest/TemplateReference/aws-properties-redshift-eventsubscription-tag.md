---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-eventsubscription-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::EventSubscription Tag
<a name="aws-properties-redshift-eventsubscription-tag"></a>

A tag consisting of a name/value pair for a resource.

## Syntax
<a name="aws-properties-redshift-eventsubscription-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-eventsubscription-tag-syntax.json"></a>

```
{
  "[Key](#cfn-redshift-eventsubscription-tag-key)" : {{String}},
  "[Value](#cfn-redshift-eventsubscription-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-eventsubscription-tag-syntax.yaml"></a>

```
  [Key](#cfn-redshift-eventsubscription-tag-key): {{String}}
  [Value](#cfn-redshift-eventsubscription-tag-value): {{String}}
```

## Properties
<a name="aws-properties-redshift-eventsubscription-tag-properties"></a>

`Key`  <a name="cfn-redshift-eventsubscription-tag-key"></a>
The key, or name, for the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-redshift-eventsubscription-tag-value"></a>
The value for the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
