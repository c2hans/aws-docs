---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PercentageRange.html
---

# PercentageRange
<a name="API_marketplace-discovery_PercentageRange"></a>

A price increase percentage range with minimum, maximum, and default values.

## Contents
<a name="API_marketplace-discovery_PercentageRange_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** defaultValue **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PercentageRange-defaultValue"></a>
The percentage increase applied by default when no other value is finalized before the adjustment deadline. Falls between `minimumValue` and `maximumValue`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** maximumValue **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PercentageRange-maximumValue"></a>
The maximum percentage by which the price can increase at each renewal cycle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** minimumValue **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PercentageRange-minimumValue"></a>
The minimum percentage by which the price can increase at each renewal cycle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

## See Also
<a name="API_marketplace-discovery_PercentageRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PercentageRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PercentageRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PercentageRange)
