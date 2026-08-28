---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestReport.html
---

# TestReport
<a name="API_TestReport"></a>

Contains aggregated test-level metrics for a job.

## Contents
<a name="API_TestReport_Contents"></a>

 ** message **   <a name="devicefarm-Type-TestReport-message"></a>
A message associated with the test report.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** metrics **   <a name="devicefarm-Type-TestReport-metrics"></a>
The aggregated test-level metrics for the job.
Type: [TestReportMetrics](API_TestReportMetrics.md) object
Required: No

 ** testDetailsUrl **   <a name="devicefarm-Type-TestReport-testDetailsUrl"></a>
A URL to the detailed test results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_TestReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/TestReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/TestReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/TestReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
