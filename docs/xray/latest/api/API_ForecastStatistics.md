---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ForecastStatistics.html
---

# ForecastStatistics
<a name="API_ForecastStatistics"></a>

The predicted high and low fault count. This is used to determine if a service has become anomalous and if an insight should be created.

## Contents
<a name="API_ForecastStatistics_Contents"></a>

 ** FaultCountHigh **   <a name="xray-Type-ForecastStatistics-FaultCountHigh"></a>
The upper limit of fault counts for a service.
Type: Long
Required: No

 ** FaultCountLow **   <a name="xray-Type-ForecastStatistics-FaultCountLow"></a>
The lower limit of fault counts for a service.
Type: Long
Required: No

## See Also
<a name="API_ForecastStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ForecastStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ForecastStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ForecastStatistics)
