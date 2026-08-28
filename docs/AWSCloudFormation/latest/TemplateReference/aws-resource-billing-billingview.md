---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-billing-billingview.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Billing::BillingView
<a name="aws-resource-billing-billingview"></a>

 Creates a billing view with the specified billing view attributes.

## Syntax
<a name="aws-resource-billing-billingview-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-billing-billingview-syntax.json"></a>

```
{
  "Type" : "AWS::Billing::BillingView",
  "Properties" : {
      "[DataFilterExpression](#cfn-billing-billingview-datafilterexpression)" : {{DataFilterExpression}},
      "[Description](#cfn-billing-billingview-description)" : {{String}},
      "[Name](#cfn-billing-billingview-name)" : {{String}},
      "[SourceViews](#cfn-billing-billingview-sourceviews)" : {{[ String, ... ]}},
      "[Tags](#cfn-billing-billingview-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-billing-billingview-syntax.yaml"></a>

```
Type: AWS::Billing::BillingView
Properties:
  [DataFilterExpression](#cfn-billing-billingview-datafilterexpression): {{
    DataFilterExpression}}
  [Description](#cfn-billing-billingview-description): {{String}}
  [Name](#cfn-billing-billingview-name): {{String}}
  [SourceViews](#cfn-billing-billingview-sourceviews): {{
    - String}}
  [Tags](#cfn-billing-billingview-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-billing-billingview-properties"></a>

`DataFilterExpression`  <a name="cfn-billing-billingview-datafilterexpression"></a>
 See [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html). Billing view only supports `LINKED_ACCOUNT`, `Tags`, and `CostCategories`.
*Required*: No
*Type*: [DataFilterExpression](aws-properties-billing-billingview-datafilterexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-billing-billingview-description"></a>
 The description of the billing view.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-billing-billingview-name"></a>
The name of the billing view.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_\+=\.\-@]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceViews`  <a name="cfn-billing-billingview-sourceviews"></a>
A list of billing views used as the data source for the custom billing view.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-billing-billingview-tags"></a>
A list of key value map specifying tags associated to the billing view being created.
*Required*: No
*Type*: [Array](aws-properties-billing-billingview-tags.md) of [Tag](aws-properties-billing-billingview-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-billing-billingview-return-values"></a>

### Ref
<a name="aws-resource-billing-billingview-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-billing-billingview-return-values-fn--getatt"></a>

####
<a name="aws-resource-billing-billingview-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view.

`BillingViewType`  <a name="BillingViewType-fn::getatt"></a>
The type of billing group.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time when the billing view was created.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
The account owner of the billing view.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time when the billing view was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
