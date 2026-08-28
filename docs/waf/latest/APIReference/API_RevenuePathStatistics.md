---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RevenuePathStatistics.html
---

# RevenuePathStatistics
<a name="API_RevenuePathStatistics"></a>

Revenue statistics for a single content path, including the path, revenue amount, and request count.

## Contents
<a name="API_RevenuePathStatistics_Contents"></a>

 ** Amount **   <a name="WAF-Type-RevenuePathStatistics-Amount"></a>
The total revenue amount from this path in the specified currency.
Type: String
Required: Yes

 ** Path **   <a name="WAF-Type-RevenuePathStatistics-Path"></a>
The URI path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** Percentage **   <a name="WAF-Type-RevenuePathStatistics-Percentage"></a>
The percentage of total revenue from this path.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 100.0.
Required: Yes

 ** RequestCount **   <a name="WAF-Type-RevenuePathStatistics-RequestCount"></a>
The number of monetized requests to this path.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_RevenuePathStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RevenuePathStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RevenuePathStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RevenuePathStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
