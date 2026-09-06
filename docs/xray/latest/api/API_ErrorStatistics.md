---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ErrorStatistics.html
---

# ErrorStatistics
<a name="API_ErrorStatistics"></a>

Information about requests that failed with a 4xx Client Error status code.

## Contents
<a name="API_ErrorStatistics_Contents"></a>

 ** OtherCount **   <a name="xray-Type-ErrorStatistics-OtherCount"></a>
The number of requests that failed with untracked 4xx Client Error status codes.
Type: Long
Required: No

 ** ThrottleCount **   <a name="xray-Type-ErrorStatistics-ThrottleCount"></a>
The number of requests that failed with a 429 throttling status code.
Type: Long
Required: No

 ** TotalCount **   <a name="xray-Type-ErrorStatistics-TotalCount"></a>
The total number of requests that failed with a 4xx Client Error status code.
Type: Long
Required: No

## See Also
<a name="API_ErrorStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ErrorStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ErrorStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ErrorStatistics)
