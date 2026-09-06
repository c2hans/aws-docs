---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy Tag
<a name="aws-properties-ses-mailmanagertrafficpolicy-tag"></a>

A key-value pair (the value is optional), that you can define and assign to AWS resources.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ses-mailmanagertrafficpolicy-tag-key)" : {{String}},
  "[Value](#cfn-ses-mailmanagertrafficpolicy-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-tag-syntax.yaml"></a>

```
  [Key](#cfn-ses-mailmanagertrafficpolicy-tag-key): {{String}}
  [Value](#cfn-ses-mailmanagertrafficpolicy-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-tag-properties"></a>

`Key`  <a name="cfn-ses-mailmanagertrafficpolicy-tag-key"></a>
The key of the key-value tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9/_\+=\.:@\-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ses-mailmanagertrafficpolicy-tag-value"></a>
The value of the key-value tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9/_\+=\.:@\-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
