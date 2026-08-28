---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_SystemEventMetadata.html
---

# SystemEventMetadata
<a name="API_SystemEventMetadata"></a>

Type-specific metadata for each system event type.

## Contents
<a name="API_SystemEventMetadata_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** systemCreated **   <a name="ngresiliencehub-Type-SystemEventMetadata-systemCreated"></a>
Metadata for a system created event.
Type: [SystemCreatedMetadata](API_SystemCreatedMetadata.md) object
Required: No

 ** systemDeleted **   <a name="ngresiliencehub-Type-SystemEventMetadata-systemDeleted"></a>
Metadata for a system deleted event.
Type: [SystemDeletedMetadata](API_SystemDeletedMetadata.md) object
Required: No

 ** systemPolicyAssociated **   <a name="ngresiliencehub-Type-SystemEventMetadata-systemPolicyAssociated"></a>
Metadata for a system policy associated event.
Type: [SystemPolicyAssociatedMetadata](API_SystemPolicyAssociatedMetadata.md) object
Required: No

 ** systemPolicyDisassociated **   <a name="ngresiliencehub-Type-SystemEventMetadata-systemPolicyDisassociated"></a>
Metadata for a system policy disassociated event.
Type: [SystemPolicyDisassociatedMetadata](API_SystemPolicyDisassociatedMetadata.md) object
Required: No

 ** systemServiceAssociated **   <a name="ngresiliencehub-Type-SystemEventMetadata-systemServiceAssociated"></a>
Metadata for a system service associated event.
Type: [SystemServiceAssociatedMetadata](API_SystemServiceAssociatedMetadata.md) object
Required: No

 ** systemServiceDisassociated **   <a name="ngresiliencehub-Type-SystemEventMetadata-systemServiceDisassociated"></a>
Metadata for a system service disassociated event.
Type: [SystemServiceDisassociatedMetadata](API_SystemServiceDisassociatedMetadata.md) object
Required: No

 ** systemUserJourneyCreated **   <a name="ngresiliencehub-Type-SystemEventMetadata-systemUserJourneyCreated"></a>
Metadata for a system user journey created event.
Type: [SystemUserJourneyCreatedMetadata](API_SystemUserJourneyCreatedMetadata.md) object
Required: No

 ** systemUserJourneyDeleted **   <a name="ngresiliencehub-Type-SystemEventMetadata-systemUserJourneyDeleted"></a>
Metadata for a system user journey deleted event.
Type: [SystemUserJourneyDeletedMetadata](API_SystemUserJourneyDeletedMetadata.md) object
Required: No

 ** systemUserJourneyUpdated **   <a name="ngresiliencehub-Type-SystemEventMetadata-systemUserJourneyUpdated"></a>
Metadata for a system user journey updated event.
Type: [SystemUserJourneyUpdatedMetadata](API_SystemUserJourneyUpdatedMetadata.md) object
Required: No

## See Also
<a name="API_SystemEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/SystemEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/SystemEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/SystemEventMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
