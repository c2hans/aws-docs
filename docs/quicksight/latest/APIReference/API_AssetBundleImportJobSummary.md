---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobSummary.html
---

# AssetBundleImportJobSummary
<a name="API_AssetBundleImportJobSummary"></a>

A summary of the import job that includes details of the requested job's configuration and its current status.

## Contents
<a name="API_AssetBundleImportJobSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-AssetBundleImportJobSummary-Arn"></a>
The ARN of the import job.
Type: String
Required: No

 ** AssetBundleImportJobId **   <a name="QS-Type-AssetBundleImportJobSummary-AssetBundleImportJobId"></a>
The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** CreatedTime **   <a name="QS-Type-AssetBundleImportJobSummary-CreatedTime"></a>
The time that the import job was created.
Type: Timestamp
Required: No

 ** FailureAction **   <a name="QS-Type-AssetBundleImportJobSummary-FailureAction"></a>
The failure action for the import job.
Type: String
Valid Values: `DO_NOTHING | ROLLBACK`
Required: No

 ** JobStatus **   <a name="QS-Type-AssetBundleImportJobSummary-JobStatus"></a>
The current status of the import job.
Type: String
Valid Values: `QUEUED_FOR_IMMEDIATE_EXECUTION | IN_PROGRESS | SUCCESSFUL | FAILED | FAILED_ROLLBACK_IN_PROGRESS | FAILED_ROLLBACK_COMPLETED | FAILED_ROLLBACK_ERROR`
Required: No

## See Also
<a name="API_AssetBundleImportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
