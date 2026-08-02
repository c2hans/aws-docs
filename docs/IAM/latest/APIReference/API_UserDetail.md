---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UserDetail.html
---

# UserDetail
<a name="API_UserDetail"></a>

Contains information about an IAM user, including all the user's policies and all the IAM groups the user is in.

This data type is used as a response element in the [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html) operation.

## Contents
<a name="API_UserDetail_Contents"></a>

 ** Arn **
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** AttachedManagedPolicies.member.N **
A list of the managed policies attached to the user.
Type: Array of [AttachedPolicy](API_AttachedPolicy.md) objects
Required: No

 ** CreateDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the user was created.
Type: Timestamp
Required: No

 ** GroupList.member.N **
A list of IAM groups that the user is in.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

 ** Path **
The path to the user. For more information about paths, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
Required: No

 ** PermissionsBoundary **
The ARN of the policy used to set the permissions boundary for the user.
For more information about permissions boundaries, see [Permissions boundaries for IAM identities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.
Type: [AttachedPermissionsBoundary](API_AttachedPermissionsBoundary.md) object
Required: No

 ** Tags.member.N **
A list of tags that are associated with the user. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** UserId **
The stable and unique string identifying the user. For more information about IDs, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: No

 ** UserName **
The friendly name identifying the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

 ** UserPolicyList.member.N **
A list of the inline policies embedded in the user.
Type: Array of [PolicyDetail](API_PolicyDetail.md) objects
Required: No

## See Also
<a name="API_UserDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UserDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UserDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UserDetail)
