---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

Contains information about an IAM user entity.

This data type is used as a response element in the following operations:
+  [CreateUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateUser.html)
+  [GetUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUser.html)
+  [ListUsers](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html)

## Contents
<a name="API_User_Contents"></a>

 ** Arn **
The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** CreateDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the user was created.
Type: Timestamp
Required: Yes

 ** Path **
The path to the user. For more information about paths, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
The ARN of the policy used to set the permissions boundary for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
Required: Yes

 ** UserId **
The stable and unique string identifying the user. For more information about IDs, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** UserName **
The friendly name identifying the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** PasswordLastUsed **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the user's password was last used to sign in to an AWS website. For a list of AWS websites that capture a user's last sign-in time, see the [Credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html) topic in the *IAM User Guide*. If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value), then it indicates that they never signed in with a password. This can be because:
+ The user never had a password.
+ A password exists but has not been used since IAM started tracking this information on October 20, 2014.
A null value does not mean that the user *never* had a password. Also, if the user does not currently have a password but had one in the past, then this field contains the date and time the most recent password was used.
This value is returned only in the [GetUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUser.html) and [ListUsers](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html) operations.
Type: Timestamp
Required: No

 ** PermissionsBoundary **
For more information about permissions boundaries, see [Permissions boundaries for IAM identities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.
Type: [AttachedPermissionsBoundary](API_AttachedPermissionsBoundary.md) object
Required: No

 ** Tags.member.N **
A list of tags that are associated with the user. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/User)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
