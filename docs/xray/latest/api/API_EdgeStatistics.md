---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_EdgeStatistics.html
---

# EdgeStatistics
<a name="API_EdgeStatistics"></a>

Response statistics for an edge.

## Contents
<a name="API_EdgeStatistics_Contents"></a>

 ** ErrorStatistics **   <a name="xray-Type-EdgeStatistics-ErrorStatistics"></a>
Information about requests that failed with a 4xx Client Error status code.
Type: [ErrorStatistics](API_ErrorStatistics.md) object
Required: No

 ** FaultStatistics **   <a name="xray-Type-EdgeStatistics-FaultStatistics"></a>
Information about requests that failed with a 5xx Server Error status code.
Type: [FaultStatistics](API_FaultStatistics.md) object
Required: No

 ** OkCount **   <a name="xray-Type-EdgeStatistics-OkCount"></a>
The number of requests that completed with a 2xx Success status code.
Type: Long
Required: No

 ** TotalCount **   <a name="xray-Type-EdgeStatistics-TotalCount"></a>
The total number of completed requests.
Type: Long
Required: No

 ** TotalResponseTime **   <a name="xray-Type-EdgeStatistics-TotalResponseTime"></a>
The aggregate response time of completed requests.
Type: Double
Required: No

## See Also
<a name="API_EdgeStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/EdgeStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/EdgeStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/EdgeStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
