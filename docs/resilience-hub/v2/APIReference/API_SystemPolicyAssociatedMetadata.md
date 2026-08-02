---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_SystemPolicyAssociatedMetadata.html
---

# SystemPolicyAssociatedMetadata
<a name="API_SystemPolicyAssociatedMetadata"></a>

Metadata for a system policy associated event.

## Contents
<a name="API_SystemPolicyAssociatedMetadata_Contents"></a>

 ** policyArn **   <a name="ngresiliencehub-Type-SystemPolicyAssociatedMetadata-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** policyName **   <a name="ngresiliencehub-Type-SystemPolicyAssociatedMetadata-policyName"></a>
The name of the associated policy.
Type: String
Required: No

## See Also
<a name="API_SystemPolicyAssociatedMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/SystemPolicyAssociatedMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/SystemPolicyAssociatedMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/SystemPolicyAssociatedMetadata)
