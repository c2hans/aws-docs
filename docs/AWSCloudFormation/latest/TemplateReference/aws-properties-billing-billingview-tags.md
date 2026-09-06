---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billing-billingview-tags.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Billing::BillingView Tags
<a name="aws-properties-billing-billingview-tags"></a>

Tags associated with the billing view resource.

## Syntax
<a name="aws-properties-billing-billingview-tags-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billing-billingview-tags-syntax.json"></a>

```
{
  "[Key](#cfn-billing-billingview-tags-key)" : {{String}},
  "[Values](#cfn-billing-billingview-tags-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-billing-billingview-tags-syntax.yaml"></a>

```
  [Key](#cfn-billing-billingview-tags-key): {{String}}
  [Values](#cfn-billing-billingview-tags-values): {{
    - String}}
```

## Properties
<a name="aws-properties-billing-billingview-tags-properties"></a>

`Key`  <a name="cfn-billing-billingview-tags-key"></a>
 A list of tag key value pairs that are associated with the resource.
*Required*: No
*Type*: String
*Pattern*: `[\S\s]*`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-billing-billingview-tags-values"></a>
 The metadata values that you can use to filter and group your results.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024 | 200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
