---
source_url: https://docs.aws.amazon.com/iam-toolbox/latest/APIReference/API_Check.html
---

# Check

Represents one authorization requirement considered during an evaluation and its result.

## Contents
<a name="API_Check_Contents"></a>

 ** checkType **   <a name="iamtoolbox-Type-Check-checkType"></a>
The type of requirement that the check evaluates. Valid values:
+  `SERVICE_CONTROL_POLICY` - The service control policies (SCPs) attached to one organization target, such as a root, organizational unit, or account, that apply to the principal.
+  `RESOURCE_CONTROL_POLICY` - The resource control policies (RCPs) attached to one organization target that apply to the resource.
+  `VPC_ENDPOINT` - The VPC endpoint policy for the endpoint through which the request passes.
+  `RESOURCE` - The resource owner's resource-based policies, when the owner must allow the request separately, such as a cross-account request or a request to an AWS KMS key.
+  `PRINCIPAL` - The principal's identity-based policies attached to the IAM user or role.
+  `PERMISSIONS_BOUNDARY` - The permissions boundary on the IAM user or role.
+  `SESSION` - The role session that made the request, decided by its session policies.
Type: String
Valid Values: `SERVICE_CONTROL_POLICY | RESOURCE_CONTROL_POLICY | VPC_ENDPOINT | RESOURCE | PRINCIPAL | PERMISSIONS_BOUNDARY | SESSION`
Required: Yes

 ** evaluatedEffect **   <a name="iamtoolbox-Type-Check-evaluatedEffect"></a>
The result of evaluating this requirement. Valid values:
+  `ALLOW` - A statement that applies to this check allows the request.
+  `EXPLICIT_DENY` - A deny statement that applies to this check matches.
+  `IMPLICIT_DENY` - The check required an allow and nothing that applies to it allows the request.
+  `NO_IMPACT` - No statement in this check matched, and no allow was needed because another path allowed the request.
Type: String
Valid Values: `ALLOW | NO_IMPACT | IMPLICIT_DENY | EXPLICIT_DENY`
Required: Yes

 ** matchedPolicies **   <a name="iamtoolbox-Type-Check-matchedPolicies"></a>
Policies in this list have statements that matched for this check. Each URI corresponds to an entry in the top-level `policies` list. Only policies in the top-level list are included. The check effect can reflect a matched policy omitted from this list, so this list can be empty even when the effect is `ALLOW`.
Type: Array of [MatchedPolicy](API_MatchedPolicy.md) objects
Required: No

 ** relevantPolicyTypes **   <a name="iamtoolbox-Type-Check-relevantPolicyTypes"></a>
The policy types used to satisfy this check, plus the type of every policy with a statement that matched in it. `matchedPolicies` lists matching policies in the top-level `policies` list.
Type: Array of strings
Valid Values: `IDENTITY_BASED_POLICY | RESOURCE_BASED_POLICY | PERMISSIONS_BOUNDARY | SESSION_POLICY | SERVICE_CONTROL_POLICY | RESOURCE_CONTROL_POLICY | VPC_ENDPOINT_POLICY`
Required: No

 ** targetArn **   <a name="iamtoolbox-Type-Check-targetArn"></a>
The ARN that distinguishes this check from other checks of the same type. This value is absent when the check type alone identifies the check. For SCP and RCP checks, this is the AWS Organizations ARN of the root, organizational unit, or account that the evaluated policies are attached to.
Type: String
Required: No

## See Also
<a name="API_Check_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-toolbox-2018-05-10/Check)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-toolbox-2018-05-10/Check)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-toolbox-2018-05-10/Check)
