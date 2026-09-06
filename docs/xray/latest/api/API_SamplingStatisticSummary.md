---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_SamplingStatisticSummary.html
---

# SamplingStatisticSummary
<a name="API_SamplingStatisticSummary"></a>

Aggregated request sampling data for a sampling rule across all services for a 10-second window.

## Contents
<a name="API_SamplingStatisticSummary_Contents"></a>

 ** BorrowCount **   <a name="xray-Type-SamplingStatisticSummary-BorrowCount"></a>
The number of requests recorded with borrowed reservoir quota.
Type: Integer
Required: No

 ** RequestCount **   <a name="xray-Type-SamplingStatisticSummary-RequestCount"></a>
The number of requests that matched the rule.
Type: Integer
Required: No

 ** RuleName **   <a name="xray-Type-SamplingStatisticSummary-RuleName"></a>
The name of the sampling rule.
Type: String
Required: No

 ** SampledCount **   <a name="xray-Type-SamplingStatisticSummary-SampledCount"></a>
The number of requests recorded.
Type: Integer
Required: No

 ** Timestamp **   <a name="xray-Type-SamplingStatisticSummary-Timestamp"></a>
The start time of the reporting window, in Unix time seconds.
Type: Timestamp
Required: No

## See Also
<a name="API_SamplingStatisticSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/SamplingStatisticSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/SamplingStatisticSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/SamplingStatisticSummary)
