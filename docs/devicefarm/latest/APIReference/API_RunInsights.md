---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_RunInsights.html
---

# RunInsights
<a name="API_RunInsights"></a>

Contains insights for a run, including report status, and job-level aggregated metrics such as per job execution time and median job execution time.

## Contents
<a name="API_RunInsights_Contents"></a>

 ** jobReport **   <a name="devicefarm-Type-RunInsights-jobReport"></a>
The job-level aggregated report for the run.
Type: [JobReport](API_JobReport.md) object
Required: No

 ** status **   <a name="devicefarm-Type-RunInsights-status"></a>
The status of the insights report for the run.
Type: String
Valid Values: `PENDING | RUNNING | COMPLETED | SKIPPED | ERRORED`
Required: No

## See Also
<a name="API_RunInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/RunInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/RunInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/RunInsights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
