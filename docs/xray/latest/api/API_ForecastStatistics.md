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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
