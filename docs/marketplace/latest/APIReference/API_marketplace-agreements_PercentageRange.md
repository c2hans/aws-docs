---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_PercentageRange.html
---

# PercentageRange
<a name="API_marketplace-agreements_PercentageRange"></a>

A range of price increase percentages that the proposer can choose from before the adjustment deadline of the agreement.

 `MinValue` will be less than `MaxValue`, and `DefaultValue` will fall within the range. When the proposer authorizes a single percentage instead of a range, `PriceIncrease` is a `FixedPercentage` rather than a `PercentageRange`.

## Contents
<a name="API_marketplace-agreements_PercentageRange_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** defaultValue **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PercentageRange-defaultValue"></a>
The percentage that is applied if the proposer doesn't choose a value before the adjustment deadline. Valid values range from `0.00` to `100.00`, with up to two decimal places.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `(100(\.0{1,2})?|[1-9]\d?(\.\d{1,2})?|0(\.\d{1,2})?)`
Required: No

 ** maxValue **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PercentageRange-maxValue"></a>
The highest percentage that the proposer can choose, from `0.00` to `100.00` with up to two decimal places.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `(100(\.0{1,2})?|[1-9]\d?(\.\d{1,2})?|0(\.\d{1,2})?)`
Required: No

 ** minValue **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PercentageRange-minValue"></a>
The lowest percentage that the proposer can choose, from `0.00` to `100.00` with up to two decimal places.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `(100(\.0{1,2})?|[1-9]\d?(\.\d{1,2})?|0(\.\d{1,2})?)`
Required: No

## See Also
<a name="API_marketplace-agreements_PercentageRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/PercentageRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/PercentageRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/PercentageRange)
