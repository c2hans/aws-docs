---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_TransformationJobSummary.html
---

# TransformationJobSummary
<a name="API_TransformationJobSummary"></a>

Contains summary information about a data transformation job. To retrieve full job details, call `DescribeDataTransformationJob`.

## Contents
<a name="API_TransformationJobSummary_Contents"></a>

 ** JobId **   <a name="HealthLake-Type-TransformationJobSummary-JobId"></a>
The unique identifier of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** JobStatus **   <a name="HealthLake-Type-TransformationJobSummary-JobStatus"></a>
The current status of the job.
Type: String
Valid Values: `SUBMITTED | QUEUED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`
Required: Yes

 ** SubmitTime **   <a name="HealthLake-Type-TransformationJobSummary-SubmitTime"></a>
The timestamp when the job was submitted.
Type: Timestamp
Required: Yes

 ** EndTime **   <a name="HealthLake-Type-TransformationJobSummary-EndTime"></a>
The timestamp when the job completed.
Type: Timestamp
Required: No

 ** JobName **   <a name="HealthLake-Type-TransformationJobSummary-JobName"></a>
The name of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-%@]*`
Required: No

 ** SourceFormat **   <a name="HealthLake-Type-TransformationJobSummary-SourceFormat"></a>
The source data format for this job.
Type: String
Valid Values: `CCDA | CSV`
Required: No

## See Also
<a name="API_TransformationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/TransformationJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/TransformationJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/TransformationJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
