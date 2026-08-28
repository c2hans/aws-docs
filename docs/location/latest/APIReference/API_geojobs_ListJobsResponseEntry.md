---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_ListJobsResponseEntry.html
---

# ListJobsResponseEntry
<a name="API_geojobs_ListJobsResponseEntry"></a>

Job summary information returned in list operations.

## Contents
<a name="API_geojobs_ListJobsResponseEntry_Contents"></a>

 ** Action **   <a name="location-Type-geojobs_ListJobsResponseEntry-Action"></a>
Action performed by the job.
Type: String
Valid Values: `ValidateAddress`
Required: Yes

 ** CreatedAt **   <a name="location-Type-geojobs_ListJobsResponseEntry-CreatedAt"></a>
Job creation time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** ExecutionRoleArn **   <a name="location-Type-geojobs_ListJobsResponseEntry-ExecutionRoleArn"></a>
IAM role used for job execution.
Type: String
Required: Yes

 ** InputOptions **   <a name="location-Type-geojobs_ListJobsResponseEntry-InputOptions"></a>
Input configuration.
Type: [JobInputOptions](API_geojobs_JobInputOptions.md) object
Required: Yes

 ** JobArn **   <a name="location-Type-geojobs_ListJobsResponseEntry-JobArn"></a>
Amazon Resource Name (ARN) of the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`
Required: Yes

 ** JobId **   <a name="location-Type-geojobs_ListJobsResponseEntry-JobId"></a>
Unique job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[-._\w]+`
Required: Yes

 ** OutputOptions **   <a name="location-Type-geojobs_ListJobsResponseEntry-OutputOptions"></a>
Output configuration.
Type: [JobOutputOptions](API_geojobs_JobOutputOptions.md) object
Required: Yes

 ** Status **   <a name="location-Type-geojobs_ListJobsResponseEntry-Status"></a>
Current job status.
Type: String
Valid Values: `Pending | Running | Completed | Failed | Cancelling | Cancelled`
Required: Yes

 ** UpdatedAt **   <a name="location-Type-geojobs_ListJobsResponseEntry-UpdatedAt"></a>
Last update time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** ActionOptions **   <a name="location-Type-geojobs_ListJobsResponseEntry-ActionOptions"></a>
Additional options for configuring job action parameters.
Type: [JobActionOptions](API_geojobs_JobActionOptions.md) object
Required: No

 ** EndedAt **   <a name="location-Type-geojobs_ListJobsResponseEntry-EndedAt"></a>
Job completion time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`. Only returned for jobs in a terminal status: `Completed` \| `Failed` \| `Cancelled`.
Type: Timestamp
Required: No

 ** Error **   <a name="location-Type-geojobs_ListJobsResponseEntry-Error"></a>
Error information if the job failed.
Type: [JobError](API_geojobs_JobError.md) object
Required: No

 ** Name **   <a name="location-Type-geojobs_ListJobsResponseEntry-Name"></a>
Job name (if provided during creation).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: No

## See Also
<a name="API_geojobs_ListJobsResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geojobs-2020-11-19/ListJobsResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geojobs-2020-11-19/ListJobsResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geojobs-2020-11-19/ListJobsResponseEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
