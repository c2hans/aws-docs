---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanageraddresslist-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerAddressList Tag
<a name="aws-properties-ses-mailmanageraddresslist-tag"></a>

The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.

## Syntax
<a name="aws-properties-ses-mailmanageraddresslist-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanageraddresslist-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ses-mailmanageraddresslist-tag-key)" : {{String}},
  "[Value](#cfn-ses-mailmanageraddresslist-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanageraddresslist-tag-syntax.yaml"></a>

```
  [Key](#cfn-ses-mailmanageraddresslist-tag-key): {{String}}
  [Value](#cfn-ses-mailmanageraddresslist-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanageraddresslist-tag-properties"></a>

`Key`  <a name="cfn-ses-mailmanageraddresslist-tag-key"></a>
The key of the key-value tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ses-mailmanageraddresslist-tag-value"></a>
The value of the key-value tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
