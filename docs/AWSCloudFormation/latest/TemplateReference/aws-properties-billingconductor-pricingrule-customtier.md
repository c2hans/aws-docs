---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billingconductor-pricingrule-customtier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BillingConductor::PricingRule CustomTier
<a name="aws-properties-billingconductor-pricingrule-customtier"></a>

 A custom tier for the pricing rule. Each custom tier applies a rate to the usage that falls within the tier's range.

## Syntax
<a name="aws-properties-billingconductor-pricingrule-customtier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billingconductor-pricingrule-customtier-syntax.json"></a>

```
{
  "[BeginRangeInclusive](#cfn-billingconductor-pricingrule-customtier-beginrangeinclusive)" : {{Number}},
  "[EndRangeExclusive](#cfn-billingconductor-pricingrule-customtier-endrangeexclusive)" : {{Number}},
  "[RateValue](#cfn-billingconductor-pricingrule-customtier-ratevalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-billingconductor-pricingrule-customtier-syntax.yaml"></a>

```
  [BeginRangeInclusive](#cfn-billingconductor-pricingrule-customtier-beginrangeinclusive): {{Number}}
  [EndRangeExclusive](#cfn-billingconductor-pricingrule-customtier-endrangeexclusive): {{Number}}
  [RateValue](#cfn-billingconductor-pricingrule-customtier-ratevalue): {{Number}}
```

## Properties
<a name="aws-properties-billingconductor-pricingrule-customtier-properties"></a>

`BeginRangeInclusive`  <a name="cfn-billingconductor-pricingrule-customtier-beginrangeinclusive"></a>
 The inclusive start of the usage range that this tier applies to.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndRangeExclusive`  <a name="cfn-billingconductor-pricingrule-customtier-endrangeexclusive"></a>
 The exclusive end of the usage range that this tier applies to. If you don't specify a value, this tier applies to all usage that is greater than or equal to `BeginRangeInclusive`.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RateValue`  <a name="cfn-billingconductor-pricingrule-customtier-ratevalue"></a>
 The rate that's applied to the usage that falls within this tier.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
