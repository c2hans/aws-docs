---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RunMetrics.html
---

# RunMetrics
<a name="API_RunMetrics"></a>

Metrics for the optimizer run.

This structure is deprecated. See the individual metric members for compaction, retention, and orphan file deletion.

## Contents
<a name="API_RunMetrics_Contents"></a>

 ** JobDurationInHour **   <a name="Glue-Type-RunMetrics-JobDurationInHour"></a>
The duration of the job in hours.
Type: String
Required: No

 ** NumberOfBytesCompacted **   <a name="Glue-Type-RunMetrics-NumberOfBytesCompacted"></a>
The number of bytes removed by the compaction job run.
Type: String
Required: No

 ** NumberOfDpus **   <a name="Glue-Type-RunMetrics-NumberOfDpus"></a>
The number of DPUs consumed by the job, rounded up to the nearest whole number.
Type: String
Required: No

 ** NumberOfFilesCompacted **   <a name="Glue-Type-RunMetrics-NumberOfFilesCompacted"></a>
The number of files removed by the compaction job run.
Type: String
Required: No

## See Also
<a name="API_RunMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RunMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RunMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RunMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
