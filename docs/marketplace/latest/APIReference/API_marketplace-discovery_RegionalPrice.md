---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_RegionalPrice.html
---

# RegionalPrice

A price override for a pricing dimension in one AWS Region.

## Contents
<a name="API_marketplace-discovery_RegionalPrice_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RegionalPrice-displayName"></a>
The human-readable display name of the Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** price **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RegionalPrice-price"></a>
The per-unit price for the dimension in this Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** region **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RegionalPrice-region"></a>
The AWS Region the override applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## See Also
<a name="API_marketplace-discovery_RegionalPrice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/RegionalPrice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/RegionalPrice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/RegionalPrice)
