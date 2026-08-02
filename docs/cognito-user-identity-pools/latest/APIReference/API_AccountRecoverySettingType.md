---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AccountRecoverySettingType.html
---

# AccountRecoverySettingType
<a name="API_AccountRecoverySettingType"></a>

The settings for user message delivery in forgot-password operations. Contains preference for email or SMS message delivery of password reset codes, or for admin-only password reset.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_AccountRecoverySettingType_Contents"></a>

 ** RecoveryMechanisms **   <a name="CognitoUserPools-Type-AccountRecoverySettingType-RecoveryMechanisms"></a>
The list of options and priorities for user message delivery in forgot-password operations. Sets or displays user pool preferences for email or SMS message priority, whether users should fall back to a second delivery method, and whether passwords should only be reset by administrators.
Type: Array of [RecoveryOptionType](API_RecoveryOptionType.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

## See Also
<a name="API_AccountRecoverySettingType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AccountRecoverySettingType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AccountRecoverySettingType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AccountRecoverySettingType)
