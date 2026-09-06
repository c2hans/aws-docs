---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-ipset-tagitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::IPSet TagItem
<a name="aws-properties-guardduty-ipset-tagitem"></a>

Describes a tag.

## Syntax
<a name="aws-properties-guardduty-ipset-tagitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-guardduty-ipset-tagitem-syntax.json"></a>

```
{
  "[Key](#cfn-guardduty-ipset-tagitem-key)" : {{String}},
  "[Value](#cfn-guardduty-ipset-tagitem-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-guardduty-ipset-tagitem-syntax.yaml"></a>

```
  [Key](#cfn-guardduty-ipset-tagitem-key): {{String}}
  [Value](#cfn-guardduty-ipset-tagitem-value): {{String}}
```

## Properties
<a name="aws-properties-guardduty-ipset-tagitem-properties"></a>

`Key`  <a name="cfn-guardduty-ipset-tagitem-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-guardduty-ipset-tagitem-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
