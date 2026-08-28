---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RestoreJobSummary.html
---

# RestoreJobSummary
<a name="API_RestoreJobSummary"></a>

This is a summary of restore jobs created or running within the most recent 14 days.

The returned summary may contain the following: Region, Account, State, ResourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.

## Contents
<a name="API_RestoreJobSummary_Contents"></a>

 ** AccountId **   <a name="Backup-Type-RestoreJobSummary-AccountId"></a>
The account ID that owns the jobs within the summary.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** Count **   <a name="Backup-Type-RestoreJobSummary-Count"></a>
The value as a number of jobs in a job summary.
Type: Integer
Required: No

 ** EndTime **   <a name="Backup-Type-RestoreJobSummary-EndTime"></a>
The value of time in number format of a job end time.
This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** Region **   <a name="Backup-Type-RestoreJobSummary-Region"></a>
The AWS Regions within the job summary.
Type: String
Required: No

 ** ResourceType **   <a name="Backup-Type-RestoreJobSummary-ResourceType"></a>
This value is the job count for the specified resource type. The request `GetSupportedResourceTypes` returns strings for supported resource types.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

 ** StartTime **   <a name="Backup-Type-RestoreJobSummary-StartTime"></a>
The value of time in number format of a job start time.
This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** State **   <a name="Backup-Type-RestoreJobSummary-State"></a>
This value is job count for jobs with the specified state.
Type: String
Valid Values: `CREATED | PENDING | RUNNING | ABORTED | COMPLETED | FAILED | AGGREGATE_ALL | ANY`
Required: No

## See Also
<a name="API_RestoreJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RestoreJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RestoreJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RestoreJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
