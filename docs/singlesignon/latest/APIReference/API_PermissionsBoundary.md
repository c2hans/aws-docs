---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PermissionsBoundary.html
---

# PermissionsBoundary
<a name="API_PermissionsBoundary"></a>

Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary. Specify either `CustomerManagedPolicyReference` to use the name and path of a customer managed policy, or `ManagedPolicyArn` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.

**Important**
Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see [IAM JSON policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the *IAM User Guide*.

## Contents
<a name="API_PermissionsBoundary_Contents"></a>

 ** CustomerManagedPolicyReference **   <a name="singlesignon-Type-PermissionsBoundary-CustomerManagedPolicyReference"></a>
Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.
Type: [CustomerManagedPolicyReference](API_CustomerManagedPolicyReference.md) object
Required: No

 ** ManagedPolicyArn **   <a name="singlesignon-Type-PermissionsBoundary-ManagedPolicyArn"></a>
The AWS managed policy ARN that you want to attach to a permission set as a permissions boundary.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:iam::aws:policy((/[A-Za-z0-9\.,\+@=_-]+)*)/([A-Za-z0-9\.,\+=@_-]+)`
Required: No

## See Also
<a name="API_PermissionsBoundary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/PermissionsBoundary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/PermissionsBoundary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/PermissionsBoundary)
