---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_SyncResourceSummary.html
---

# SyncResourceSummary
<a name="API_SyncResourceSummary"></a>

The sync resource summary.

## Contents
<a name="API_SyncResourceSummary_Contents"></a>

 ** externalId **   <a name="tm-Type-SyncResourceSummary-externalId"></a>
The external ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: No

 ** resourceId **   <a name="tm-Type-SyncResourceSummary-resourceId"></a>
The resource ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: No

 ** resourceType **   <a name="tm-Type-SyncResourceSummary-resourceType"></a>
The resource type.
Type: String
Valid Values: `ENTITY | COMPONENT_TYPE`
Required: No

 ** status **   <a name="tm-Type-SyncResourceSummary-status"></a>
The sync resource summary status.
Type: [SyncResourceStatus](API_SyncResourceStatus.md) object
Required: No

 ** updateDateTime **   <a name="tm-Type-SyncResourceSummary-updateDateTime"></a>
The update date and time.
Type: Timestamp
Required: No

## See Also
<a name="API_SyncResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/SyncResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/SyncResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/SyncResourceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
