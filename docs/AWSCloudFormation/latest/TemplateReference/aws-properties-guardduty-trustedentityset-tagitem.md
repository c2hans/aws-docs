---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-trustedentityset-tagitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::TrustedEntitySet TagItem
<a name="aws-properties-guardduty-trustedentityset-tagitem"></a>

Describes a tag. For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-guardduty-trustedentityset-tagitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-guardduty-trustedentityset-tagitem-syntax.json"></a>

```
{
  "[Key](#cfn-guardduty-trustedentityset-tagitem-key)" : {{String}},
  "[Value](#cfn-guardduty-trustedentityset-tagitem-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-guardduty-trustedentityset-tagitem-syntax.yaml"></a>

```
  [Key](#cfn-guardduty-trustedentityset-tagitem-key): {{String}}
  [Value](#cfn-guardduty-trustedentityset-tagitem-value): {{String}}
```

## Properties
<a name="aws-properties-guardduty-trustedentityset-tagitem-properties"></a>

`Key`  <a name="cfn-guardduty-trustedentityset-tagitem-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-guardduty-trustedentityset-tagitem-value"></a>
The tag value. This is optional.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
