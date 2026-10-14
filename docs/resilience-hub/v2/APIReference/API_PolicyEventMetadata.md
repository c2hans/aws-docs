---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_PolicyEventMetadata.html
---

# PolicyEventMetadata
<a name="API_PolicyEventMetadata"></a>

Contains the event-specific metadata for a policy event. Exactly one member is populated, according to the event type.
+ policyAttachedToService — a service started using the policy.
+ policyDetachedFromService — a service stopped using the policy.
+ policySharingRevoked — cross-account sharing was disabled for the policy.
+ policyDeleted — the policy was deleted.

## Contents
<a name="API_PolicyEventMetadata_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** policyAttachedToService **   <a name="ngresiliencehub-Type-PolicyEventMetadata-policyAttachedToService"></a>
Contains details about the service that started using the policy, such as the account that owns the service.
Type: [PolicyAttachedToServiceMetadata](API_PolicyAttachedToServiceMetadata.md) object
Required: No

 ** policyDeleted **   <a name="ngresiliencehub-Type-PolicyEventMetadata-policyDeleted"></a>
Contains details about a policy that was deleted, including the number of services that were affected.
Type: [PolicyDeletedMetadata](API_PolicyDeletedMetadata.md) object
Required: No

 ** policyDetachedFromService **   <a name="ngresiliencehub-Type-PolicyEventMetadata-policyDetachedFromService"></a>
Contains details about the service that stopped using the policy, such as the account that owns the service.
Type: [PolicyDetachedFromServiceMetadata](API_PolicyDetachedFromServiceMetadata.md) object
Required: No

 ** policySharingRevoked **   <a name="ngresiliencehub-Type-PolicyEventMetadata-policySharingRevoked"></a>
Contains details about a policy for which organization sharing was revoked, including the number of services that were affected.
Type: [PolicySharingRevokedMetadata](API_PolicySharingRevokedMetadata.md) object
Required: No

## See Also
<a name="API_PolicyEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/PolicyEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/PolicyEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/PolicyEventMetadata)
