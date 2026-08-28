---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billingconductor-customlineitem-lineitemfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BillingConductor::CustomLineItem LineItemFilter
<a name="aws-properties-billingconductor-customlineitem-lineitemfilter"></a>

A representation of the line item filter for your custom line item. You can use line item filters to include or exclude specific resource values from the billing group's total cost. For example, if you create a custom line item and you want to filter out a value, such as Savings Plans discounts, you can update `LineItemFilter` to exclude it.

## Syntax
<a name="aws-properties-billingconductor-customlineitem-lineitemfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billingconductor-customlineitem-lineitemfilter-syntax.json"></a>

```
{
  "[Attribute](#cfn-billingconductor-customlineitem-lineitemfilter-attribute)" : {{String}},
  "[AttributeValues](#cfn-billingconductor-customlineitem-lineitemfilter-attributevalues)" : {{[ String, ... ]}},
  "[MatchOption](#cfn-billingconductor-customlineitem-lineitemfilter-matchoption)" : {{String}},
  "[Values](#cfn-billingconductor-customlineitem-lineitemfilter-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-billingconductor-customlineitem-lineitemfilter-syntax.yaml"></a>

```
  [Attribute](#cfn-billingconductor-customlineitem-lineitemfilter-attribute): {{String}}
  [AttributeValues](#cfn-billingconductor-customlineitem-lineitemfilter-attributevalues): {{
    - String}}
  [MatchOption](#cfn-billingconductor-customlineitem-lineitemfilter-matchoption): {{String}}
  [Values](#cfn-billingconductor-customlineitem-lineitemfilter-values): {{
    - String}}
```

## Properties
<a name="aws-properties-billingconductor-customlineitem-lineitemfilter-properties"></a>

`Attribute`  <a name="cfn-billingconductor-customlineitem-lineitemfilter-attribute"></a>
The attribute of the line item filter. This specifies what attribute that you can filter on.
*Required*: Yes
*Type*: String
*Allowed values*: `LINE_ITEM_TYPE | SERVICE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AttributeValues`  <a name="cfn-billingconductor-customlineitem-lineitemfilter-attributevalues"></a>
The values of the line item filter. This specifies the values to filter on.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchOption`  <a name="cfn-billingconductor-customlineitem-lineitemfilter-matchoption"></a>
The match criteria of the line item filter. This parameter specifies whether not to include the resource value from the billing group total cost.
*Required*: Yes
*Type*: String
*Allowed values*: `NOT_EQUAL | EQUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-billingconductor-customlineitem-lineitemfilter-values"></a>
The values of the line item filter. This specifies the values to filter on. Currently, you can only exclude Savings Plans discounts.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
