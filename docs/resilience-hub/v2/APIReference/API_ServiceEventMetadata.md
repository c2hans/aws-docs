---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceEventMetadata.html
---

# ServiceEventMetadata
<a name="API_ServiceEventMetadata"></a>

Type-specific metadata for each service event type.

## Contents
<a name="API_ServiceEventMetadata_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** assertionCreated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-assertionCreated"></a>
Metadata for an assertion created event.
Type: [AssertionCreatedMetadata](API_AssertionCreatedMetadata.md) object
Required: No

 ** assertionDeleted **   <a name="ngresiliencehub-Type-ServiceEventMetadata-assertionDeleted"></a>
Metadata for an assertion deleted event.
Type: [AssertionDeletedMetadata](API_AssertionDeletedMetadata.md) object
Required: No

 ** assertionUpdated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-assertionUpdated"></a>
Metadata for an assertion updated event.
Type: [AssertionUpdatedMetadata](API_AssertionUpdatedMetadata.md) object
Required: No

 ** serviceAchievabilityUpdated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceAchievabilityUpdated"></a>
Metadata for a service achievability updated event.
Type: [ServiceAchievabilityUpdatedMetadata](API_ServiceAchievabilityUpdatedMetadata.md) object
Required: No

 ** serviceCreated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceCreated"></a>
Metadata for a service created event.
Type: [ServiceCreatedMetadata](API_ServiceCreatedMetadata.md) object
Required: No

 ** serviceDeleted **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceDeleted"></a>
Metadata for a service deleted event.
Type: [ServiceDeletedMetadata](API_ServiceDeletedMetadata.md) object
Required: No

 ** serviceFunctionCreated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceFunctionCreated"></a>
Metadata for a service function created event.
Type: [ServiceFunctionCreatedMetadata](API_ServiceFunctionCreatedMetadata.md) object
Required: No

 ** serviceFunctionDeleted **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceFunctionDeleted"></a>
Metadata for a service function deleted event.
Type: [ServiceFunctionDeletedMetadata](API_ServiceFunctionDeletedMetadata.md) object
Required: No

 ** serviceFunctionResourcesAdded **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceFunctionResourcesAdded"></a>
Metadata for a service function resources added event.
Type: [ServiceFunctionResourcesAddedMetadata](API_ServiceFunctionResourcesAddedMetadata.md) object
Required: No

 ** serviceFunctionResourcesRemoved **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceFunctionResourcesRemoved"></a>
Metadata for a service function resources removed event.
Type: [ServiceFunctionResourcesRemovedMetadata](API_ServiceFunctionResourcesRemovedMetadata.md) object
Required: No

 ** serviceFunctionUpdated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceFunctionUpdated"></a>
Metadata for a service function updated event.
Type: [ServiceFunctionUpdatedMetadata](API_ServiceFunctionUpdatedMetadata.md) object
Required: No

 ** serviceInputSourcesUpdated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceInputSourcesUpdated"></a>
Metadata for a service input sources updated event.
Type: [ServiceInputSourcesUpdatedMetadata](API_ServiceInputSourcesUpdatedMetadata.md) object
Required: No

 ** servicePolicyAssociated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-servicePolicyAssociated"></a>
Metadata for a service policy associated event.
Type: [ServicePolicyAssociatedMetadata](API_ServicePolicyAssociatedMetadata.md) object
Required: No

 ** servicePolicyDisassociated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-servicePolicyDisassociated"></a>
Metadata for a service policy disassociated event.
Type: [ServicePolicyDisassociatedMetadata](API_ServicePolicyDisassociatedMetadata.md) object
Required: No

 ** serviceResourcesAssociated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceResourcesAssociated"></a>
Metadata for a service resources associated event.
Type: [ServiceResourcesAssociatedMetadata](API_ServiceResourcesAssociatedMetadata.md) object
Required: No

 ** serviceResourcesDisassociated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceResourcesDisassociated"></a>
Metadata for a service resources disassociated event.
Type: [ServiceResourcesDisassociatedMetadata](API_ServiceResourcesDisassociatedMetadata.md) object
Required: No

 ** serviceSystemAssociated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceSystemAssociated"></a>
Metadata for a service system associated event.
Type: [ServiceSystemAssociatedMetadata](API_ServiceSystemAssociatedMetadata.md) object
Required: No

 ** serviceSystemDisassociated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceSystemDisassociated"></a>
Metadata for a service system disassociated event.
Type: [ServiceSystemDisassociatedMetadata](API_ServiceSystemDisassociatedMetadata.md) object
Required: No

 ** serviceWorkflowUpdated **   <a name="ngresiliencehub-Type-ServiceEventMetadata-serviceWorkflowUpdated"></a>
Metadata for a service workflow updated event.
Type: [ServiceWorkflowUpdatedMetadata](API_ServiceWorkflowUpdatedMetadata.md) object
Required: No

## See Also
<a name="API_ServiceEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceEventMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
