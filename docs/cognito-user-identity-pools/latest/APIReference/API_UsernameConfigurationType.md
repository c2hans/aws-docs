---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UsernameConfigurationType.html
---

# UsernameConfigurationType
<a name="API_UsernameConfigurationType"></a>

The configuration of a user pool for username case sensitivity.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_UsernameConfigurationType_Contents"></a>

 ** CaseSensitive **   <a name="CognitoUserPools-Type-UsernameConfigurationType-CaseSensitive"></a>
Specifies whether user name case sensitivity will be applied for all users in the user pool through Amazon Cognito APIs. For most use cases, set case sensitivity to `False` (case insensitive) as a best practice. When usernames and email addresses are case insensitive, users can sign in as the same user when they enter a different capitalization of their user name.
Valid values include:
true
Enables case sensitivity for all username input. When this option is set to `true`, users must sign in using the exact capitalization of their given username, such as “UserName”. This is the default value.
false
Enables case insensitivity for all username input. For example, when this option is set to `false`, users can sign in using `username`, `USERNAME`, or `UserName`. This option also enables both `preferred_username` and `email` alias to be case insensitive, in addition to the `username` attribute.
Type: Boolean
Required: Yes

## See Also
<a name="API_UsernameConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UsernameConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UsernameConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UsernameConfigurationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
