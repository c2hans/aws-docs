---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ByolPricingTerm.html
---

# ByolPricingTerm
<a name="API_marketplace-agreements_ByolPricingTerm"></a>

Enables you and your customers to move your existing agreements to AWS Marketplace. The customer won't be charged for product usage in AWS Marketplace because they already paid for the product outside of AWS Marketplace.

## Contents
<a name="API_marketplace-agreements_ByolPricingTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ByolPricingTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ByolPricingTerm-type"></a>
Type of the term being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_ByolPricingTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ByolPricingTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ByolPricingTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ByolPricingTerm)
