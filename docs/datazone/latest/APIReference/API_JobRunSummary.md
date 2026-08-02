---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_JobRunSummary.html
---

# JobRunSummary
<a name="API_JobRunSummary"></a>

The job run summary.

## Contents
<a name="API_JobRunSummary_Contents"></a>

 ** createdAt **   <a name="datazone-Type-JobRunSummary-createdAt"></a>
The timestamp at which job run was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-JobRunSummary-createdBy"></a>
The user who created the job run.
Type: String
Required: No

 ** domainId **   <a name="datazone-Type-JobRunSummary-domainId"></a>
The domain ID of the job run.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** endTime **   <a name="datazone-Type-JobRunSummary-endTime"></a>
The end time of a job run.
Type: Timestamp
Required: No

 ** error **   <a name="datazone-Type-JobRunSummary-error"></a>
The error of a job run.
Type: [JobRunError](API_JobRunError.md) object
Required: No

 ** jobId **   <a name="datazone-Type-JobRunSummary-jobId"></a>
The job ID of a job run.
Type: String
Required: No

 ** jobType **   <a name="datazone-Type-JobRunSummary-jobType"></a>
The job type of a job run.
Type: String
Valid Values: `LINEAGE`
Required: No

 ** runId **   <a name="datazone-Type-JobRunSummary-runId"></a>
The run ID of a job run.
Type: String
Required: No

 ** runMode **   <a name="datazone-Type-JobRunSummary-runMode"></a>
The run mode of a job run.
Type: String
Valid Values: `SCHEDULED | ON_DEMAND`
Required: No

 ** startTime **   <a name="datazone-Type-JobRunSummary-startTime"></a>
The start time of a job run.
Type: Timestamp
Required: No

 ** status **   <a name="datazone-Type-JobRunSummary-status"></a>
The status of a job run.
Type: String
Valid Values: `SCHEDULED | IN_PROGRESS | SUCCESS | PARTIALLY_SUCCEEDED | FAILED | ABORTED | TIMED_OUT | CANCELED`
Required: No

## See Also
<a name="API_JobRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/JobRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/JobRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/JobRunSummary)
