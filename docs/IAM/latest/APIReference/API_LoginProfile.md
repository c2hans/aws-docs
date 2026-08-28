---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_LoginProfile.html
---

# LoginProfile
<a name="API_LoginProfile"></a>

Contains the user name and password create date for a user.

 This data type is used as a response element in the [CreateLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateLoginProfile.html) and [GetLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetLoginProfile.html) operations.

## Contents
<a name="API_LoginProfile_Contents"></a>

 ** CreateDate **
The date when the password for the user was created.
Type: Timestamp
Required: Yes

 ** UserName **
The name of the user, which can be used for signing in to the AWS Management Console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** PasswordResetRequired **
Specifies whether the user is required to set a new password on next sign-in.
Type: Boolean
Required: No

## See Also
<a name="API_LoginProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/LoginProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/LoginProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/LoginProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
