---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_FaultStatistics.html
---

# FaultStatistics
<a name="API_FaultStatistics"></a>

Information about requests that failed with a 5xx Server Error status code.

## Contents
<a name="API_FaultStatistics_Contents"></a>

 ** OtherCount **   <a name="xray-Type-FaultStatistics-OtherCount"></a>
The number of requests that failed with untracked 5xx Server Error status codes.
Type: Long
Required: No

 ** TotalCount **   <a name="xray-Type-FaultStatistics-TotalCount"></a>
The total number of requests that failed with a 5xx Server Error status code.
Type: Long
Required: No

## See Also
<a name="API_FaultStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/FaultStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/FaultStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/FaultStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
