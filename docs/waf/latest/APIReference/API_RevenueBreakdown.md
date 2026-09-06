---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RevenueBreakdown.html
---

# RevenueBreakdown
<a name="API_RevenueBreakdown"></a>

A summary of AI bot monetization revenue, including total revenue, revenue by verification tier, and request counts.

## Contents
<a name="API_RevenueBreakdown_Contents"></a>

 ** Currency **   <a name="WAF-Type-RevenueBreakdown-Currency"></a>
The currency of the revenue amounts.
Type: String
Valid Values: `USDC`
Required: No

 ** TotalAmount **   <a name="WAF-Type-RevenueBreakdown-TotalAmount"></a>
The total revenue amount in the specified currency.
Type: String
Required: No

 ** TotalMonetizeServed **   <a name="WAF-Type-RevenueBreakdown-TotalMonetizeServed"></a>
The total number of HTTP 402 Payment Required responses served to AI agents.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** TotalSettled **   <a name="WAF-Type-RevenueBreakdown-TotalSettled"></a>
The total number of successfully settled payment transactions.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** UnverifiedAmount **   <a name="WAF-Type-RevenueBreakdown-UnverifiedAmount"></a>
The revenue amount from unverified AI bots.
Type: String
Required: No

 ** VerifiedAmount **   <a name="WAF-Type-RevenueBreakdown-VerifiedAmount"></a>
The revenue amount from verified AI bots.
Type: String
Required: No

## See Also
<a name="API_RevenueBreakdown_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RevenueBreakdown)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RevenueBreakdown)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RevenueBreakdown)
