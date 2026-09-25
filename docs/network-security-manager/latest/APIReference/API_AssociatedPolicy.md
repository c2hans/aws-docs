---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AssociatedPolicy.html
---

# AssociatedPolicy
<a name="API_AssociatedPolicy"></a>

An association between a deployment and a policy, as returned in outputs. The corresponding request structure is `PolicyReference`.

## Contents
<a name="API_AssociatedPolicy_Contents"></a>

 ** policyArn **   <a name="networksecuritymanager-Type-AssociatedPolicy-policyArn"></a>
The ARN of the associated policy, including its version qualifier when a specific published version is pinned (for example, `...:policy:abc123:3`).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

## See Also
<a name="API_AssociatedPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AssociatedPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AssociatedPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AssociatedPolicy)
