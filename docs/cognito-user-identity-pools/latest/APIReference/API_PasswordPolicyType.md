---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_PasswordPolicyType.html
---

# PasswordPolicyType
<a name="API_PasswordPolicyType"></a>

The password policy settings for a user pool, including complexity, history, and length requirements.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_PasswordPolicyType_Contents"></a>

 ** MinimumLength **   <a name="CognitoUserPools-Type-PasswordPolicyType-MinimumLength"></a>
The minimum length of the password in the policy that you have set. This value can't be less than 6.
Type: Integer
Valid Range: Minimum value of 6. Maximum value of 99.
Required: No

 ** PasswordHistorySize **   <a name="CognitoUserPools-Type-PasswordPolicyType-PasswordHistorySize"></a>
The number of previous passwords that you want Amazon Cognito to restrict each user from reusing. Users can't set a password that matches any of `n` previous passwords, where `n` is the value of `PasswordHistorySize`.
Password history isn't enforced and isn't displayed in [DescribeUserPool](API_DescribeUserPool.md) responses when you set this value to `0` or don't provide it. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 24.
Required: No

 ** RequireLowercase **   <a name="CognitoUserPools-Type-PasswordPolicyType-RequireLowercase"></a>
The requirement in a password policy that users must include at least one lowercase letter in their password.
Type: Boolean
Required: No

 ** RequireNumbers **   <a name="CognitoUserPools-Type-PasswordPolicyType-RequireNumbers"></a>
The requirement in a password policy that users must include at least one number in their password.
Type: Boolean
Required: No

 ** RequireSymbols **   <a name="CognitoUserPools-Type-PasswordPolicyType-RequireSymbols"></a>
The requirement in a password policy that users must include at least one symbol in their password.
Type: Boolean
Required: No

 ** RequireUppercase **   <a name="CognitoUserPools-Type-PasswordPolicyType-RequireUppercase"></a>
The requirement in a password policy that users must include at least one uppercase letter in their password.
Type: Boolean
Required: No

 ** TemporaryPasswordValidityDays **   <a name="CognitoUserPools-Type-PasswordPolicyType-TemporaryPasswordValidityDays"></a>
The number of days a temporary password is valid in the password policy. If the user doesn't sign in during this time, an administrator must reset their password. Defaults to `7`. If you submit a value of `0`, Amazon Cognito treats it as a null value and sets `TemporaryPasswordValidityDays` to its default value.
When you set `TemporaryPasswordValidityDays` for a user pool, you can no longer set a value for the legacy `UnusedAccountValidityDays` parameter in that user pool.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 365.
Required: No

## See Also
<a name="API_PasswordPolicyType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/PasswordPolicyType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/PasswordPolicyType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/PasswordPolicyType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
