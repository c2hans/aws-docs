---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_UnprocessedStatistics.html
---

# UnprocessedStatistics
<a name="API_UnprocessedStatistics"></a>

Sampling statistics from a call to [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html) that X-Ray could not process.

## Contents
<a name="API_UnprocessedStatistics_Contents"></a>

 ** ErrorCode **   <a name="xray-Type-UnprocessedStatistics-ErrorCode"></a>
The error code.
Type: String
Required: No

 ** Message **   <a name="xray-Type-UnprocessedStatistics-Message"></a>
The error message.
Type: String
Required: No

 ** RuleName **   <a name="xray-Type-UnprocessedStatistics-RuleName"></a>
The name of the sampling rule.
Type: String
Required: No

## See Also
<a name="API_UnprocessedStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/UnprocessedStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/UnprocessedStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/UnprocessedStatistics)
