---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billing-billingview-datafilterexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Billing::BillingView DataFilterExpression
<a name="aws-properties-billing-billingview-datafilterexpression"></a>

See [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html). Billing view only supports `LINKED_ACCOUNT` and `Tags`.

## Syntax
<a name="aws-properties-billing-billingview-datafilterexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billing-billingview-datafilterexpression-syntax.json"></a>

```
{
  "[Dimensions](#cfn-billing-billingview-datafilterexpression-dimensions)" : {{Dimensions}},
  "[Tags](#cfn-billing-billingview-datafilterexpression-tags)" : {{Tags}},
  "[TimeRange](#cfn-billing-billingview-datafilterexpression-timerange)" : {{TimeRange}}
}
```

### YAML
<a name="aws-properties-billing-billingview-datafilterexpression-syntax.yaml"></a>

```
  [Dimensions](#cfn-billing-billingview-datafilterexpression-dimensions): {{
    Dimensions}}
  [Tags](#cfn-billing-billingview-datafilterexpression-tags): {{
    Tags}}
  [TimeRange](#cfn-billing-billingview-datafilterexpression-timerange): {{
    TimeRange}}
```

## Properties
<a name="aws-properties-billing-billingview-datafilterexpression-properties"></a>

`Dimensions`  <a name="cfn-billing-billingview-datafilterexpression-dimensions"></a>
 The specific `Dimension` to use for `Expression`.
*Required*: No
*Type*: [Dimensions](aws-properties-billing-billingview-dimensions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-billing-billingview-datafilterexpression-tags"></a>
 The specific `Tag` to use for `Expression`.
*Required*: No
*Type*: [Tags](aws-properties-billing-billingview-tags.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeRange`  <a name="cfn-billing-billingview-datafilterexpression-timerange"></a>
Property description not available.
*Required*: No
*Type*: [TimeRange](aws-properties-billing-billingview-timerange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
