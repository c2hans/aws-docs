---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ManagedPolicyDetail.html
---

# ManagedPolicyDetail
<a name="API_ManagedPolicyDetail"></a>

Contains information about a managed policy, including the policy's ARN, versions, and the number of principal entities (users, groups, and roles) that the policy is attached to.

This data type is used as a response element in the [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html) operation.

For more information about managed policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.

## Contents
<a name="API_ManagedPolicyDetail_Contents"></a>

 ** Arn **
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** AttachmentCount **
The number of principal entities (users, groups, and roles) that the policy is attached to.
Type: Integer
Required: No

 ** CreateDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the policy was created.
Type: Timestamp
Required: No

 ** DefaultVersionId **
The identifier for the version of the policy that is set as the default (operative) version.
For more information about policy versions, see [Versioning for managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html) in the *IAM User Guide*.
Type: String
Pattern: `v[1-9][0-9]*(\.[A-Za-z0-9-]*)?`
Required: No

 ** Description **
A friendly description of the policy.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** IsAttachable **
Specifies whether the policy can be attached to an IAM user, group, or role.
Type: Boolean
Required: No

 ** Path **
The path to the policy.
For more information about paths, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `((/[A-Za-z0-9\.,\+@=_-]+)*)/`
Required: No

 ** PermissionsBoundaryUsageCount **
The number of entities (users and roles) for which the policy is used as the permissions boundary.
For more information about permissions boundaries, see [Permissions boundaries for IAM identities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.
Type: Integer
Required: No

 ** PolicyId **
The stable and unique string identifying the policy.
For more information about IDs, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: No

 ** PolicyName **
The friendly name (not ARN) identifying the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

 ** PolicyVersionList.member.N **
A list containing information about the versions of the policy.
Type: Array of [PolicyVersion](API_PolicyVersion.md) objects
Required: No

 ** UpdateDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the policy was last updated.
When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.
Type: Timestamp
Required: No

## See Also
<a name="API_ManagedPolicyDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ManagedPolicyDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ManagedPolicyDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ManagedPolicyDetail)
