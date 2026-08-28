---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_JobReport.html
---

# JobReport
<a name="API_JobReport"></a>

Contains aggregated job-level metrics for a run.

## Contents
<a name="API_JobReport_Contents"></a>

 ** jobDetailsUrl **   <a name="devicefarm-Type-JobReport-jobDetailsUrl"></a>
A URL to the detailed job results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** message **   <a name="devicefarm-Type-JobReport-message"></a>
A message associated with the job report.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** metrics **   <a name="devicefarm-Type-JobReport-metrics"></a>
The aggregated job-level metrics for the run.
Type: [JobReportMetrics](API_JobReportMetrics.md) object
Required: No

## See Also
<a name="API_JobReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/JobReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/JobReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/JobReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
