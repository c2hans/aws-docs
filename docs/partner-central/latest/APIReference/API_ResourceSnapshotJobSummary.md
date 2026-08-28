---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ResourceSnapshotJobSummary.html
---

# ResourceSnapshotJobSummary
<a name="API_ResourceSnapshotJobSummary"></a>

 An object that contains a `Resource Snapshot Job`'s subset of fields.

## Contents
<a name="API_ResourceSnapshotJobSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-ResourceSnapshotJobSummary-Arn"></a>
 The Amazon Resource Name (ARN) for the resource snapshot job.
Type: String
Pattern: `arn:.*`
Required: No

 ** EngagementId **   <a name="AWSPartnerCentral-Type-ResourceSnapshotJobSummary-EngagementId"></a>
The unique identifier of the Engagement.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: No

 ** Id **   <a name="AWSPartnerCentral-Type-ResourceSnapshotJobSummary-Id"></a>
 The unique identifier for the resource snapshot job within the AWS Partner Central system. This ID is used for direct references to the job within the service.
Type: String
Pattern: `job-[0-9a-z]{13}`
Required: No

 ** Status **   <a name="AWSPartnerCentral-Type-ResourceSnapshotJobSummary-Status"></a>
The current status of the snapshot job.
Valid values:
+  STOPPED: The job is not currently running.
+  RUNNING: The job is actively executing.
Type: String
Valid Values: `Running | Stopped`
Required: No

## See Also
<a name="API_ResourceSnapshotJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ResourceSnapshotJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ResourceSnapshotJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ResourceSnapshotJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
