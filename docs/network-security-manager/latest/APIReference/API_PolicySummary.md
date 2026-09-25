---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_PolicySummary.html
---

# PolicySummary
<a name="API_PolicySummary"></a>

Summary information about a policy.

## Contents
<a name="API_PolicySummary_Contents"></a>

 ** policyArn **   <a name="networksecuritymanager-Type-PolicySummary-policyArn"></a>
The Amazon Resource Name (ARN) of the policy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

 ** policyId **   <a name="networksecuritymanager-Type-PolicySummary-policyId"></a>
The service-generated id of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`
Required: Yes

 ** firewallType **   <a name="networksecuritymanager-Type-PolicySummary-firewallType"></a>
The firewall type associated with the resource.
Type: String
Valid Values: `WAF | SHIELD_ADVANCED`
Required: No

 ** hasPublishedVersion **   <a name="networksecuritymanager-Type-PolicySummary-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean
Required: No

 ** policyName **   <a name="networksecuritymanager-Type-PolicySummary-policyName"></a>
The name of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`
Required: No

 ** priority **   <a name="networksecuritymanager-Type-PolicySummary-priority"></a>
The priority of the resource. A lower number indicates a higher priority.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** status **   <a name="networksecuritymanager-Type-PolicySummary-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable) or `ACTIVE` (published, in use).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`
Required: No

 ** updatedAt **   <a name="networksecuritymanager-Type-PolicySummary-updatedAt"></a>
The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.
Type: Timestamp
Required: No

 ** version **   <a name="networksecuritymanager-Type-PolicySummary-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`
Required: No

## See Also
<a name="API_PolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/PolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/PolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/PolicySummary)
