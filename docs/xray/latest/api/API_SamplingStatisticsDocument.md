---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_SamplingStatisticsDocument.html
---

# SamplingStatisticsDocument
<a name="API_SamplingStatisticsDocument"></a>

Request sampling results for a single rule from a service. Results are for the last 10 seconds unless the service has been assigned a longer reporting interval after a previous call to [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html).

## Contents
<a name="API_SamplingStatisticsDocument_Contents"></a>

 ** ClientID **   <a name="xray-Type-SamplingStatisticsDocument-ClientID"></a>
A unique identifier for the service in hexadecimal.
Type: String
Length Constraints: Fixed length of 24.
Required: Yes

 ** RequestCount **   <a name="xray-Type-SamplingStatisticsDocument-RequestCount"></a>
The number of requests that matched the rule.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** RuleName **   <a name="xray-Type-SamplingStatisticsDocument-RuleName"></a>
The name of the sampling rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** SampledCount **   <a name="xray-Type-SamplingStatisticsDocument-SampledCount"></a>
The number of requests recorded.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Timestamp **   <a name="xray-Type-SamplingStatisticsDocument-Timestamp"></a>
The current time, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss).
Type: Timestamp
Required: Yes

 ** BorrowCount **   <a name="xray-Type-SamplingStatisticsDocument-BorrowCount"></a>
The number of requests recorded with borrowed reservoir quota.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_SamplingStatisticsDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/SamplingStatisticsDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/SamplingStatisticsDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/SamplingStatisticsDocument)
