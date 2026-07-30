---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billingconductor-customlineitem-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BillingConductor::CustomLineItem Tag
<a name="aws-properties-billingconductor-customlineitem-tag"></a>

A custom key-value pair associated with a Billing Conductor resource.

## Syntax
<a name="aws-properties-billingconductor-customlineitem-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billingconductor-customlineitem-tag-syntax.json"></a>

```
{
  "[Key](#cfn-billingconductor-customlineitem-tag-key)" : {{String}},
  "[Value](#cfn-billingconductor-customlineitem-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-billingconductor-customlineitem-tag-syntax.yaml"></a>

```
  [Key](#cfn-billingconductor-customlineitem-tag-key): {{String}}
  [Value](#cfn-billingconductor-customlineitem-tag-value): {{String}}
```

## Properties
<a name="aws-properties-billingconductor-customlineitem-tag-properties"></a>

`Key`  <a name="cfn-billingconductor-customlineitem-tag-key"></a>
The key in a key-value pair.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-billingconductor-customlineitem-tag-value"></a>
The value in a key-value pair of a tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
