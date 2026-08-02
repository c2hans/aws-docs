---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachedPermissionsBoundary.html
---

# AttachedPermissionsBoundary
<a name="API_AttachedPermissionsBoundary"></a>

Contains information about an attached permissions boundary.

An attached permissions boundary is a managed policy that has been attached to a user or role to set the permissions boundary.

For more information about permissions boundaries, see [Permissions boundaries for IAM identities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.

## Contents
<a name="API_AttachedPermissionsBoundary_Contents"></a>

 ** PermissionsBoundaryArn **
 The ARN of the policy used to set the permissions boundary for the user or role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** PermissionsBoundaryType **
 The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of `Policy`.
Type: String
Valid Values: `PermissionsBoundaryPolicy`
Required: No

## See Also
<a name="API_AttachedPermissionsBoundary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/AttachedPermissionsBoundary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/AttachedPermissionsBoundary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/AttachedPermissionsBoundary)
