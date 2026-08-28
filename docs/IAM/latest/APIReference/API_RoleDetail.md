---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_RoleDetail.html
---

# RoleDetail
<a name="API_RoleDetail"></a>

Contains information about an IAM role, including all of the role's policies.

This data type is used as a response element in the [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html) operation.

## Contents
<a name="API_RoleDetail_Contents"></a>

 ** Arn **
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** AssumeRolePolicyDocument **
The trust policy that grants permission to assume the role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** AttachedManagedPolicies.member.N **
A list of managed policies attached to the role. These policies are the role's access (permissions) policies.
Type: Array of [AttachedPolicy](API_AttachedPolicy.md) objects
Required: No

 ** CreateDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the role was created.
Type: Timestamp
Required: No

 ** InstanceProfileList.member.N **
A list of instance profiles that contain this role.
Type: Array of [InstanceProfile](API_InstanceProfile.md) objects
Required: No

 ** Path **
The path to the role. For more information about paths, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
Required: No

 ** PermissionsBoundary **
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see [Permissions boundaries for IAM identities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.
Type: [AttachedPermissionsBoundary](API_AttachedPermissionsBoundary.md) object
Required: No

 ** RoleId **
The stable and unique string identifying the role. For more information about IDs, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: No

 ** RoleLastUsed **
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see [Regions where data is tracked](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period) in the *IAM User Guide*.
Type: [RoleLastUsed](API_RoleLastUsed.md) object
Required: No

 ** RoleName **
The friendly name that identifies the role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

 ** RolePolicyList.member.N **
A list of inline policies embedded in the role. These policies are the role's access (permissions) policies.
Type: Array of [PolicyDetail](API_PolicyDetail.md) objects
Required: No

 ** Tags.member.N **
A list of tags that are attached to the role. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

## See Also
<a name="API_RoleDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/RoleDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/RoleDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/RoleDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
