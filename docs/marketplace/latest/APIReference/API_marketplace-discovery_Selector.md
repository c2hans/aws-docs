---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_Selector.html
---

# Selector
<a name="API_marketplace-discovery_Selector"></a>

A selector used to choose a specific configuration within a configurable upfront rate card.

## Contents
<a name="API_marketplace-discovery_Selector_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Selector-type"></a>
The category of the selector, such as `Duration`.
Type: String
Valid Values: `Duration`
Required: Yes

 ** value **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Selector-value"></a>
The value of the selector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

## See Also
<a name="API_marketplace-discovery_Selector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/Selector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/Selector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/Selector)
