---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_JobSummary.html
---

# JobSummary
<a name="API_JobSummary"></a>

An object containing the `jobId`, `status`, `startTime`, and `endTime` of a job.

## Contents
<a name="API_JobSummary_Contents"></a>

 ** jobId **   <a name="API-Type-JobSummary-jobId"></a>
The ID of the job.
Type: String
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** startTime **   <a name="API-Type-JobSummary-startTime"></a>
The time at which the job was started.
Type: Timestamp
Required: Yes

 ** status **   <a name="API-Type-JobSummary-status"></a>
The current status of the job.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | QUEUED`
Required: Yes

 ** endTime **   <a name="API-Type-JobSummary-endTime"></a>
The time at which the job has finished.
Type: Timestamp
Required: No

## See Also
<a name="API_JobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/JobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/JobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/JobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
