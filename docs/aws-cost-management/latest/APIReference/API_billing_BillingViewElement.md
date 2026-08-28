---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingViewElement.html
---

# BillingViewElement
<a name="API_billing_BillingViewElement"></a>

The metadata associated to the billing view.

## Contents
<a name="API_billing_BillingViewElement_Contents"></a>

 ** arn **   <a name="awscostmanagement-Type-billing_BillingViewElement-arn"></a>
 The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view.
Type: String
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`
Required: No

 ** billingViewType **   <a name="awscostmanagement-Type-billing_BillingViewElement-billingViewType"></a>
The type of billing group.
Type: String
Valid Values: `PRIMARY | BILLING_GROUP | CUSTOM | BILLING_TRANSFER | BILLING_TRANSFER_SHOWBACK`
Required: No

 ** createdAt **   <a name="awscostmanagement-Type-billing_BillingViewElement-createdAt"></a>
The time when the billing view was created.
Type: Timestamp
Required: No

 ** dataFilterExpression **   <a name="awscostmanagement-Type-billing_BillingViewElement-dataFilterExpression"></a>
 See [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html). Billing view only supports `LINKED_ACCOUNT`, `Tags`, and `CostCategories`.
Type: [Expression](API_billing_Expression.md) object
Required: No

 ** derivedViewCount **   <a name="awscostmanagement-Type-billing_BillingViewElement-derivedViewCount"></a>
 The number of billing views that use this billing view as a source.
Type: Integer
Required: No

 ** description **   <a name="awscostmanagement-Type-billing_BillingViewElement-description"></a>
 The description of the billing view.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `([ a-zA-Z0-9_\+=\.\-@]+)?`
Required: No

 ** healthStatus **   <a name="awscostmanagement-Type-billing_BillingViewElement-healthStatus"></a>
 The current health status of the billing view.
Type: [BillingViewHealthStatus](API_billing_BillingViewHealthStatus.md) object
Required: No

 ** name **   <a name="awscostmanagement-Type-billing_BillingViewElement-name"></a>
 The account name of the billing view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[ a-zA-Z0-9_\+=\.\-@]+`
Required: No

 ** ownerAccountId **   <a name="awscostmanagement-Type-billing_BillingViewElement-ownerAccountId"></a>
The account owner of the billing view.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** sourceAccountId **   <a name="awscostmanagement-Type-billing_BillingViewElement-sourceAccountId"></a>
 The AWS account ID that owns the source billing view, if this is a derived billing view.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** sourceViewCount **   <a name="awscostmanagement-Type-billing_BillingViewElement-sourceViewCount"></a>
 The number of source views associated with this billing view.
Type: Integer
Required: No

 ** updatedAt **   <a name="awscostmanagement-Type-billing_BillingViewElement-updatedAt"></a>
The time when the billing view was last updated.
Type: Timestamp
Required: No

 ** viewDefinitionLastUpdatedAt **   <a name="awscostmanagement-Type-billing_BillingViewElement-viewDefinitionLastUpdatedAt"></a>
 The timestamp of when the billing view definition was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_billing_BillingViewElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BillingViewElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BillingViewElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BillingViewElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
