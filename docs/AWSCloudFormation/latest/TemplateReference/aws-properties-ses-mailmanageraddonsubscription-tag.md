---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanageraddonsubscription-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerAddonSubscription Tag
<a name="aws-properties-ses-mailmanageraddonsubscription-tag"></a>

A key-value pair (the value is optional), that you can define and assign to AWS resources.

## Syntax
<a name="aws-properties-ses-mailmanageraddonsubscription-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanageraddonsubscription-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ses-mailmanageraddonsubscription-tag-key)" : {{String}},
  "[Value](#cfn-ses-mailmanageraddonsubscription-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanageraddonsubscription-tag-syntax.yaml"></a>

```
  [Key](#cfn-ses-mailmanageraddonsubscription-tag-key): {{String}}
  [Value](#cfn-ses-mailmanageraddonsubscription-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanageraddonsubscription-tag-properties"></a>

`Key`  <a name="cfn-ses-mailmanageraddonsubscription-tag-key"></a>
The key of the key-value tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ses-mailmanageraddonsubscription-tag-value"></a>
The value of the key-value tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
