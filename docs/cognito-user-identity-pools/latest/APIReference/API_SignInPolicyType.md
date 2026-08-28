---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignInPolicyType.html
---

# SignInPolicyType
<a name="API_SignInPolicyType"></a>

The policy for allowed types of authentication in a user pool. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_SignInPolicyType_Contents"></a>

 ** AllowedFirstAuthFactors **   <a name="CognitoUserPools-Type-SignInPolicyType-AllowedFirstAuthFactors"></a>
The sign-in methods that a user pool supports as the first factor. You can permit users to start authentication with a standard username and password, or with other one-time password and hardware factors.
 `SOFTWARE_TOKEN` is not currently supported as a first auth factor. Do not include this value in `AllowedFirstAuthFactors`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `PASSWORD | EMAIL_OTP | SMS_OTP | WEB_AUTHN | SOFTWARE_TOKEN`
Required: No

## See Also
<a name="API_SignInPolicyType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SignInPolicyType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SignInPolicyType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SignInPolicyType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
