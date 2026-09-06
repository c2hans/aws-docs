---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_FixedPercentage.html
---

# FixedPercentage
<a name="API_marketplace-agreements_FixedPercentage"></a>

A fixed price increase that is applied each time the agreement renews.

## Contents
<a name="API_marketplace-agreements_FixedPercentage_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** value **   <a name="AWSMarketplaceService-Type-marketplace-agreements_FixedPercentage-value"></a>
The percentage by which the price increases at each renewal, from `0.00` to `100.00` with up to two decimal places. A value of `0.00` means that the agreement renews at the same price.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `(100(\.0{1,2})?|[1-9]\d?(\.\d{1,2})?|0(\.\d{1,2})?)`
Required: No

## See Also
<a name="API_marketplace-agreements_FixedPercentage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/FixedPercentage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/FixedPercentage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/FixedPercentage)
