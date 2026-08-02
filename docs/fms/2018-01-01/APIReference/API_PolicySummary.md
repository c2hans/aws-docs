---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicySummary.html
---

# PolicySummary
<a name="API_PolicySummary"></a>

Details of the AWS Firewall Manager policy.

## Contents
<a name="API_PolicySummary_Contents"></a>

 ** DeleteUnusedFMManagedResources **   <a name="fms-Type-PolicySummary-DeleteUnusedFMManagedResources"></a>
Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope.
By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources.
This option is not available for Shield Advanced or AWS WAF Classic policies.
Type: Boolean
Required: No

 ** PolicyArn **   <a name="fms-Type-PolicySummary-PolicyArn"></a>
The Amazon Resource Name (ARN) of the specified policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** PolicyId **   <a name="fms-Type-PolicySummary-PolicyId"></a>
The ID of the specified policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: No

 ** PolicyName **   <a name="fms-Type-PolicySummary-PolicyName"></a>
The name of the specified policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** PolicyStatus **   <a name="fms-Type-PolicySummary-PolicyStatus"></a>
Indicates whether the policy is in or out of an admin's policy or Region scope.
+  `ACTIVE` - The administrator can manage and delete the policy.
+  `OUT_OF_ADMIN_SCOPE` - The administrator can view the policy, but they can't edit or delete the policy. Existing policy protections stay in place. Any new resources that come into scope of the policy won't be protected.
Type: String
Valid Values: `ACTIVE | OUT_OF_ADMIN_SCOPE`
Required: No

 ** RemediationEnabled **   <a name="fms-Type-PolicySummary-RemediationEnabled"></a>
Indicates if the policy should be automatically applied to new resources.
Type: Boolean
Required: No

 ** ResourceType **   <a name="fms-Type-PolicySummary-ResourceType"></a>
The type of resource protected by or in scope of the policy. This is in the format shown in the [AWS Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** SecurityServiceType **   <a name="fms-Type-PolicySummary-SecurityServiceType"></a>
The service that the policy is using to protect the resources. This specifies the type of policy that is created, either an AWS WAF policy, a Shield Advanced policy, or a security group policy.
Type: String
Valid Values: `WAF | WAFV2 | SHIELD_ADVANCED | SECURITY_GROUPS_COMMON | SECURITY_GROUPS_CONTENT_AUDIT | SECURITY_GROUPS_USAGE_AUDIT | NETWORK_FIREWALL | DNS_FIREWALL | THIRD_PARTY_FIREWALL | IMPORT_NETWORK_FIREWALL | NETWORK_ACL_COMMON`
Required: No

## See Also
<a name="API_PolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PolicySummary)
