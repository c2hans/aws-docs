---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_FreeTrialPricingTerm.html
---

# FreeTrialPricingTerm
<a name="API_marketplace-agreements_FreeTrialPricingTerm"></a>

Defines a short-term free pricing model where the buyers aren’t charged anything within a specified limit.

## Contents
<a name="API_marketplace-agreements_FreeTrialPricingTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** duration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FreeTrialPricingTerm-duration"></a>
Duration of the free trial period (5–31 days).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** grants **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FreeTrialPricingTerm-grants"></a>
Entitlements granted to the acceptor of a free trial as part of an agreement execution.
Type: Array of [GrantItem](API_marketplace-agreements_GrantItem.md) objects
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FreeTrialPricingTerm-id"></a>
The unique identifier for the terms.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FreeTrialPricingTerm-type"></a>
Category of the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_FreeTrialPricingTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/FreeTrialPricingTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/FreeTrialPricingTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/FreeTrialPricingTerm)
