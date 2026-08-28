---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleExportJobSummary.html
---

# AssetBundleExportJobSummary
<a name="API_AssetBundleExportJobSummary"></a>

A summary of the export job that includes details of the job's configuration and its current status.

## Contents
<a name="API_AssetBundleExportJobSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-AssetBundleExportJobSummary-Arn"></a>
The ARN of the export job.
Type: String
Required: No

 ** AssetBundleExportJobId **   <a name="QS-Type-AssetBundleExportJobSummary-AssetBundleExportJobId"></a>
The ID of the export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** CreatedTime **   <a name="QS-Type-AssetBundleExportJobSummary-CreatedTime"></a>
The time that the export job was created.
Type: Timestamp
Required: No

 ** ExportFormat **   <a name="QS-Type-AssetBundleExportJobSummary-ExportFormat"></a>
The format for the export job.
Type: String
Valid Values: `CLOUDFORMATION_JSON | QUICKSIGHT_JSON`
Required: No

 ** IncludeAllDependencies **   <a name="QS-Type-AssetBundleExportJobSummary-IncludeAllDependencies"></a>
The flag that determines the inclusion of resource dependencies in the returned asset bundle.
Type: Boolean
Required: No

 ** IncludePermissions **   <a name="QS-Type-AssetBundleExportJobSummary-IncludePermissions"></a>
The flag that determines the inclusion of permissions associated with each resource ARN.
Type: Boolean
Required: No

 ** IncludeTags **   <a name="QS-Type-AssetBundleExportJobSummary-IncludeTags"></a>
The flag that determines the inclusion of tags associated with each resource ARN.
Type: Boolean
Required: No

 ** JobStatus **   <a name="QS-Type-AssetBundleExportJobSummary-JobStatus"></a>
The current status of the export job.
Type: String
Valid Values: `QUEUED_FOR_IMMEDIATE_EXECUTION | IN_PROGRESS | SUCCESSFUL | FAILED`
Required: No

## See Also
<a name="API_AssetBundleExportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleExportJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleExportJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleExportJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
