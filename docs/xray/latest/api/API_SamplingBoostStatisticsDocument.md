---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_SamplingBoostStatisticsDocument.html
---

# SamplingBoostStatisticsDocument
<a name="API_SamplingBoostStatisticsDocument"></a>

Request anomaly stats for a single rule from a service. Results are for the last 10 seconds unless the service has been assigned a longer reporting interval after a previous call to [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html).

## Contents
<a name="API_SamplingBoostStatisticsDocument_Contents"></a>

 ** AnomalyCount **   <a name="xray-Type-SamplingBoostStatisticsDocument-AnomalyCount"></a>
The number of requests with anomaly.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** RuleName **   <a name="xray-Type-SamplingBoostStatisticsDocument-RuleName"></a>
The name of the sampling rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** SampledAnomalyCount **   <a name="xray-Type-SamplingBoostStatisticsDocument-SampledAnomalyCount"></a>
The number of requests with anomaly recorded.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** ServiceName **   <a name="xray-Type-SamplingBoostStatisticsDocument-ServiceName"></a>
Matches the `name` that the service uses to identify itself in segments.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

 ** Timestamp **   <a name="xray-Type-SamplingBoostStatisticsDocument-Timestamp"></a>
The current time, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss).
Type: Timestamp
Required: Yes

 ** TotalCount **   <a name="xray-Type-SamplingBoostStatisticsDocument-TotalCount"></a>
The number of requests that associated to the rule.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_SamplingBoostStatisticsDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/SamplingBoostStatisticsDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/SamplingBoostStatisticsDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/SamplingBoostStatisticsDocument)
