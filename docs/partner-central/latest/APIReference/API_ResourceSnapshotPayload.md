---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ResourceSnapshotPayload.html
---

# ResourceSnapshotPayload
<a name="API_ResourceSnapshotPayload"></a>

 Represents the payload of a resource snapshot. This structure is designed to accommodate different types of resource snapshots, currently supporting opportunity summaries.

## Contents
<a name="API_ResourceSnapshotPayload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AwsOpportunitySummaryFullView **   <a name="AWSPartnerCentral-Type-ResourceSnapshotPayload-AwsOpportunitySummaryFullView"></a>
Provides a comprehensive view of AwsOpportunitySummaryFullView template.
Type: [AwsOpportunitySummaryFullView](API_AwsOpportunitySummaryFullView.md) object
Required: No

 ** OpportunitySummary **   <a name="AWSPartnerCentral-Type-ResourceSnapshotPayload-OpportunitySummary"></a>
 An object that contains an `opportunity`'s subset of fields.
Type: [OpportunitySummaryView](API_OpportunitySummaryView.md) object
Required: No

## See Also
<a name="API_ResourceSnapshotPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ResourceSnapshotPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ResourceSnapshotPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ResourceSnapshotPayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
