---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServicePolicyDisassociatedMetadata.html
---

# ServicePolicyDisassociatedMetadata
<a name="API_ServicePolicyDisassociatedMetadata"></a>

Metadata for a service policy disassociated event.

## Contents
<a name="API_ServicePolicyDisassociatedMetadata_Contents"></a>

 ** policyArn **   <a name="ngresiliencehub-Type-ServicePolicyDisassociatedMetadata-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** policyName **   <a name="ngresiliencehub-Type-ServicePolicyDisassociatedMetadata-policyName"></a>
The name of the disassociated policy.
Type: String
Required: No

 ** policyOwnerAccountId **   <a name="ngresiliencehub-Type-ServicePolicyDisassociatedMetadata-policyOwnerAccountId"></a>
The account that owns the policy.
Type: String
Required: No

 ** policySource **   <a name="ngresiliencehub-Type-ServicePolicyDisassociatedMetadata-policySource"></a>
The source of the policy.
+ SELF — the policy belongs to the account that owns the service.
+ CROSS\_ACCOUNT — the policy belongs to another account and was shared with the organization.
Type: String
Valid Values: `SELF | CROSS_ACCOUNT`
Required: No

 ** reason **   <a name="ngresiliencehub-Type-ServicePolicyDisassociatedMetadata-reason"></a>
The reason the policy was disassociated from the service.
Type: String
Valid Values: `REPLACED_BY_UPDATE | SHARING_REVOKED | POLICY_DELETED`
Required: No

## See Also
<a name="API_ServicePolicyDisassociatedMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServicePolicyDisassociatedMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServicePolicyDisassociatedMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServicePolicyDisassociatedMetadata)
