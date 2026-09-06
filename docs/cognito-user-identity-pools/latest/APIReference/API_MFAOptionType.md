---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_MFAOptionType.html
---

# MFAOptionType
<a name="API_MFAOptionType"></a>

 *This data type is no longer supported.* Applies only to SMS multi-factor authentication (MFA) configurations. Does not apply to time-based one-time password (TOTP) software token MFA configurations.

To set either type of MFA configuration, use the [AdminSetUserMFAPreference](API_AdminSetUserMFAPreference.md) or [SetUserMFAPreference](API_SetUserMFAPreference.md) actions.

To look up information about either type of MFA configuration, use the [AdminGetUser:UserMFASettingList](API_AdminGetUser.md#CognitoUserPools-AdminGetUser-response-UserMFASettingList) or [GetUser:UserMFASettingList](API_GetUser.md#CognitoUserPools-GetUser-response-UserMFASettingList) responses.

## Contents
<a name="API_MFAOptionType_Contents"></a>

 ** AttributeName **   <a name="CognitoUserPools-Type-MFAOptionType-AttributeName"></a>
The attribute name of the MFA option type. The only valid value is `phone_number`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+`
Required: No

 ** DeliveryMedium **   <a name="CognitoUserPools-Type-MFAOptionType-DeliveryMedium"></a>
The delivery medium to send the MFA code. You can use this parameter to set only the `SMS` delivery medium value.
Type: String
Valid Values: `SMS | EMAIL`
Required: No

## See Also
<a name="API_MFAOptionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/MFAOptionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/MFAOptionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/MFAOptionType)
