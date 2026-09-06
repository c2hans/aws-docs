---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BillingConductor::CustomLineItem CustomLineItemFlatChargeDetails
<a name="aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails"></a>

The charge details of a custom line item. It should contain only one of `Flat` or `Percentage`.

## Syntax
<a name="aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails-syntax.json"></a>

```
{
  "[ChargeValue](#cfn-billingconductor-customlineitem-customlineitemflatchargedetails-chargevalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails-syntax.yaml"></a>

```
  [ChargeValue](#cfn-billingconductor-customlineitem-customlineitemflatchargedetails-chargevalue): {{Number}}
```

## Properties
<a name="aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails-properties"></a>

`ChargeValue`  <a name="cfn-billingconductor-customlineitem-customlineitemflatchargedetails-chargevalue"></a>
The custom line item's fixed charge value in USD.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
