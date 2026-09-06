---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListJobsResponseEntry.html
---

# ListJobsResponseEntry
<a name="API_ListJobsResponseEntry"></a>

Job summary information returned in list operations.

## Contents
<a name="API_ListJobsResponseEntry_Contents"></a>

 ** Action **   <a name="location-Type-ListJobsResponseEntry-Action"></a>
Action performed by the job.
Type: String
Valid Values: `ValidateAddress`
Required: Yes

 ** CreatedAt **   <a name="location-Type-ListJobsResponseEntry-CreatedAt"></a>
Job creation time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** ExecutionRoleArn **   <a name="location-Type-ListJobsResponseEntry-ExecutionRoleArn"></a>
IAM role used for job execution.
Type: String
Required: Yes

 ** InputOptions **   <a name="location-Type-ListJobsResponseEntry-InputOptions"></a>
Input configuration.
Type: [JobInputOptions](API_JobInputOptions.md) object
Required: Yes

 ** JobArn **   <a name="location-Type-ListJobsResponseEntry-JobArn"></a>
Amazon Resource Name (ARN) of the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`
Required: Yes

 ** JobId **   <a name="location-Type-ListJobsResponseEntry-JobId"></a>
Unique job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[-._\w]+`
Required: Yes

 ** OutputOptions **   <a name="location-Type-ListJobsResponseEntry-OutputOptions"></a>
Output configuration.
Type: [JobOutputOptions](API_JobOutputOptions.md) object
Required: Yes

 ** Status **   <a name="location-Type-ListJobsResponseEntry-Status"></a>
Current job status.
Type: String
Valid Values: `Pending | Running | Completed | Failed | Cancelling | Cancelled`
Required: Yes

 ** UpdatedAt **   <a name="location-Type-ListJobsResponseEntry-UpdatedAt"></a>
Last update time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** ActionOptions **   <a name="location-Type-ListJobsResponseEntry-ActionOptions"></a>
Additional options for configuring job action parameters.
Type: [JobActionOptions](API_JobActionOptions.md) object
Required: No

 ** EndedAt **   <a name="location-Type-ListJobsResponseEntry-EndedAt"></a>
Job completion time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`. Only returned for jobs in a terminal status: `Completed` \| `Failed` \| `Cancelled`.
Type: Timestamp
Required: No

 ** Error **   <a name="location-Type-ListJobsResponseEntry-Error"></a>
Error information if the job failed.
Type: [JobError](API_JobError.md) object
Required: No

 ** Name **   <a name="location-Type-ListJobsResponseEntry-Name"></a>
Job name (if provided during creation).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: No

## See Also
<a name="API_ListJobsResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListJobsResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListJobsResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListJobsResponseEntry)
