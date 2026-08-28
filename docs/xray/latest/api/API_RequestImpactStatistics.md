---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_RequestImpactStatistics.html
---

# RequestImpactStatistics
<a name="API_RequestImpactStatistics"></a>

Statistics that describe how the incident has impacted a service.

## Contents
<a name="API_RequestImpactStatistics_Contents"></a>

 ** FaultCount **   <a name="xray-Type-RequestImpactStatistics-FaultCount"></a>
The number of requests that have resulted in a fault,
Type: Long
Required: No

 ** OkCount **   <a name="xray-Type-RequestImpactStatistics-OkCount"></a>
The number of successful requests.
Type: Long
Required: No

 ** TotalCount **   <a name="xray-Type-RequestImpactStatistics-TotalCount"></a>
The total number of requests to the service.
Type: Long
Required: No

## See Also
<a name="API_RequestImpactStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/RequestImpactStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/RequestImpactStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/RequestImpactStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
