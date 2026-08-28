---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_SyncJobSummary.html
---

# SyncJobSummary
<a name="API_SyncJobSummary"></a>

The SyncJob summary.

## Contents
<a name="API_SyncJobSummary_Contents"></a>

 ** arn **   <a name="tm-Type-SyncJobSummary-arn"></a>
The SyncJob summary ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`
Required: No

 ** creationDateTime **   <a name="tm-Type-SyncJobSummary-creationDateTime"></a>
The creation date and time.
Type: Timestamp
Required: No

 ** status **   <a name="tm-Type-SyncJobSummary-status"></a>
The SyncJob summaries status.
Type: [SyncJobStatus](API_SyncJobStatus.md) object
Required: No

 ** syncSource **   <a name="tm-Type-SyncJobSummary-syncSource"></a>
The sync source.
Type: String
Pattern: `[a-zA-Z_0-9]+`
Required: No

 ** updateDateTime **   <a name="tm-Type-SyncJobSummary-updateDateTime"></a>
The update date and time.
Type: Timestamp
Required: No

 ** workspaceId **   <a name="tm-Type-SyncJobSummary-workspaceId"></a>
The ID of the workspace that contains the sync job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_SyncJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/SyncJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/SyncJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/SyncJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
