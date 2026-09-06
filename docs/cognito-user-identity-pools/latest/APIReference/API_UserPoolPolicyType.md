---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolPolicyType.html
---

# UserPoolPolicyType
<a name="API_UserPoolPolicyType"></a>

A list of user pool policies. Contains the policy that sets password-complexity requirements.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_UserPoolPolicyType_Contents"></a>

 ** PasswordPolicy **   <a name="CognitoUserPools-Type-UserPoolPolicyType-PasswordPolicy"></a>
The password policy settings for a user pool, including complexity, history, and length requirements.
Type: [PasswordPolicyType](API_PasswordPolicyType.md) object
Required: No

 ** SignInPolicy **   <a name="CognitoUserPools-Type-UserPoolPolicyType-SignInPolicy"></a>
The policy for allowed types of authentication in a user pool.
Type: [SignInPolicyType](API_SignInPolicyType.md) object
Required: No

## See Also
<a name="API_UserPoolPolicyType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserPoolPolicyType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserPoolPolicyType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserPoolPolicyType)
