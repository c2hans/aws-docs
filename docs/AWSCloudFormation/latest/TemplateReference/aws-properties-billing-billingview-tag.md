---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billing-billingview-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Billing::BillingView Tag
<a name="aws-properties-billing-billingview-tag"></a>

<a name="aws-properties-billing-billingview-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Billing::BillingView](aws-resource-billing-billingview.md).

## Syntax
<a name="aws-properties-billing-billingview-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billing-billingview-tag-syntax.json"></a>

```
{
  "[Key](#cfn-billing-billingview-tag-key)" : {{String}},
  "[Value](#cfn-billing-billingview-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-billing-billingview-tag-syntax.yaml"></a>

```
  [Key](#cfn-billing-billingview-tag-key): {{String}}
  [Value](#cfn-billing-billingview-tag-value): {{String}}
```

## Properties
<a name="aws-properties-billing-billingview-tag-properties"></a>

`Key`  <a name="cfn-billing-billingview-tag-key"></a>
 A list of tag key value pairs that are associated with the resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-billing-billingview-tag-value"></a>
 The metadata that you can use to filter and group your results.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
