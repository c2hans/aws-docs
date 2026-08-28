---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_DataPointEntry.html
---

# DataPointEntry
<a name="API_DataPointEntry"></a>

A single data point in a revenue time series, representing aggregated monetization metrics for a specific time interval.

## Contents
<a name="API_DataPointEntry_Contents"></a>

 ** Category **   <a name="WAF-Type-DataPointEntry-Category"></a>
The bot category for this data point, when grouped by category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Date **   <a name="WAF-Type-DataPointEntry-Date"></a>
The timestamp for this data point.
Type: Timestamp
Required: No

 ** GroupByValue **   <a name="WAF-Type-DataPointEntry-GroupByValue"></a>
The group-by dimension value for this data point.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Intent **   <a name="WAF-Type-DataPointEntry-Intent"></a>
The intent classification for this data point, when grouped by intent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** MonetizeServedCount **   <a name="WAF-Type-DataPointEntry-MonetizeServedCount"></a>
The number of HTTP 402 Payment Required responses served during this interval.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** SettledCount **   <a name="WAF-Type-DataPointEntry-SettledCount"></a>
The number of successfully settled payments during this interval.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** TotalAmount **   <a name="WAF-Type-DataPointEntry-TotalAmount"></a>
The total revenue amount during this interval in the specified currency.
Type: String
Required: No

## See Also
<a name="API_DataPointEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DataPointEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DataPointEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DataPointEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
