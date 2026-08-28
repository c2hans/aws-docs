---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingViewListElement.html
---

# BillingViewListElement
<a name="API_billing_BillingViewListElement"></a>

A representation of a billing view.

## Contents
<a name="API_billing_BillingViewListElement_Contents"></a>

 ** arn **   <a name="awscostmanagement-Type-billing_BillingViewListElement-arn"></a>
The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view.
Type: String
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`
Required: No

 ** billingViewType **   <a name="awscostmanagement-Type-billing_BillingViewListElement-billingViewType"></a>
The type of billing view.
Type: String
Valid Values: `PRIMARY | BILLING_GROUP | CUSTOM | BILLING_TRANSFER | BILLING_TRANSFER_SHOWBACK`
Required: No

 ** description **   <a name="awscostmanagement-Type-billing_BillingViewListElement-description"></a>
 The description of the billing view.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `([ a-zA-Z0-9_\+=\.\-@]+)?`
Required: No

 ** healthStatus **   <a name="awscostmanagement-Type-billing_BillingViewListElement-healthStatus"></a>
 The current health status of the billing view.
Type: [BillingViewHealthStatus](API_billing_BillingViewHealthStatus.md) object
Required: No

 ** name **   <a name="awscostmanagement-Type-billing_BillingViewListElement-name"></a>
 A list of names of the Billing view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[ a-zA-Z0-9_\+=\.\-@]+`
Required: No

 ** ownerAccountId **   <a name="awscostmanagement-Type-billing_BillingViewListElement-ownerAccountId"></a>
 The list of owners of the Billing view.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** sourceAccountId **   <a name="awscostmanagement-Type-billing_BillingViewListElement-sourceAccountId"></a>
 The AWS account ID that owns the source billing view, if this is a derived billing view.
Type: String
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_billing_BillingViewListElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BillingViewListElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BillingViewListElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BillingViewListElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
