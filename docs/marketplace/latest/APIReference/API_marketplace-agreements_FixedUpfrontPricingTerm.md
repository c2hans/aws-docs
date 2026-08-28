---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_FixedUpfrontPricingTerm.html
---

# FixedUpfrontPricingTerm
<a name="API_marketplace-agreements_FixedUpfrontPricingTerm"></a>

Defines a prepaid pricing model where the customers are charged a fixed upfront amount.

## Contents
<a name="API_marketplace-agreements_FixedUpfrontPricingTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FixedUpfrontPricingTerm-currencyCode"></a>
Defines the currency for the prices mentioned in this term.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** duration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FixedUpfrontPricingTerm-duration"></a>
Contract duration for the terms.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** grants **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FixedUpfrontPricingTerm-grants"></a>
Entitlements granted to the acceptor of fixed upfront as part of agreement execution.
Type: Array of [GrantItem](API_marketplace-agreements_GrantItem.md) objects
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FixedUpfrontPricingTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** price **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FixedUpfrontPricingTerm-price"></a>
Fixed amount to be charged to the customer when this term is accepted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FixedUpfrontPricingTerm-type"></a>
Category of the term being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_FixedUpfrontPricingTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/FixedUpfrontPricingTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/FixedUpfrontPricingTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/FixedUpfrontPricingTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
