---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BillingConductor::CustomLineItem CustomLineItemChargeDetails
<a name="aws-properties-billingconductor-customlineitem-customlineitemchargedetails"></a>

The charge details of a custom line item. It should contain only one of `Flat` or `Percentage`.

## Syntax
<a name="aws-properties-billingconductor-customlineitem-customlineitemchargedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billingconductor-customlineitem-customlineitemchargedetails-syntax.json"></a>

```
{
  "[Flat](#cfn-billingconductor-customlineitem-customlineitemchargedetails-flat)" : {{CustomLineItemFlatChargeDetails}},
  "[LineItemFilters](#cfn-billingconductor-customlineitem-customlineitemchargedetails-lineitemfilters)" : {{[ LineItemFilter, ... ]}},
  "[Percentage](#cfn-billingconductor-customlineitem-customlineitemchargedetails-percentage)" : {{CustomLineItemPercentageChargeDetails}},
  "[Type](#cfn-billingconductor-customlineitem-customlineitemchargedetails-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-billingconductor-customlineitem-customlineitemchargedetails-syntax.yaml"></a>

```
  [Flat](#cfn-billingconductor-customlineitem-customlineitemchargedetails-flat): {{
    CustomLineItemFlatChargeDetails}}
  [LineItemFilters](#cfn-billingconductor-customlineitem-customlineitemchargedetails-lineitemfilters): {{
    - LineItemFilter}}
  [Percentage](#cfn-billingconductor-customlineitem-customlineitemchargedetails-percentage): {{
    CustomLineItemPercentageChargeDetails}}
  [Type](#cfn-billingconductor-customlineitem-customlineitemchargedetails-type): {{String}}
```

## Properties
<a name="aws-properties-billingconductor-customlineitem-customlineitemchargedetails-properties"></a>

`Flat`  <a name="cfn-billingconductor-customlineitem-customlineitemchargedetails-flat"></a>
A `CustomLineItemFlatChargeDetails` that describes the charge details of a flat custom line item.
*Required*: No
*Type*: [CustomLineItemFlatChargeDetails](aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineItemFilters`  <a name="cfn-billingconductor-customlineitem-customlineitemchargedetails-lineitemfilters"></a>
A representation of the line item filter.
*Required*: No
*Type*: Array of [LineItemFilter](aws-properties-billingconductor-customlineitem-lineitemfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Percentage`  <a name="cfn-billingconductor-customlineitem-customlineitemchargedetails-percentage"></a>
A `CustomLineItemPercentageChargeDetails` that describes the charge details of a percentage custom line item.
*Required*: No
*Type*: [CustomLineItemPercentageChargeDetails](aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-billingconductor-customlineitem-customlineitemchargedetails-type"></a>
The type of the custom line item that indicates whether the charge is a fee or credit.
*Required*: Yes
*Type*: String
*Allowed values*: `FEE | CREDIT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
