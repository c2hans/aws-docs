---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SMSMfaSettingsType.html
---

# SMSMfaSettingsType
<a name="API_SMSMfaSettingsType"></a>

A user's preference for using SMS message multi-factor authentication (MFA). Turns SMS MFA on and off, and can set SMS as preferred when other MFA options are available. You can't turn off SMS MFA for any of your users when MFA is required in your user pool; you can only set the type that your user prefers.

This data type is a request parameter of [SetUserMFAPreference](API_SetUserMFAPreference.md) and [AdminSetUserMFAPreference](API_AdminSetUserMFAPreference.md).

## Contents
<a name="API_SMSMfaSettingsType_Contents"></a>

 ** Enabled **   <a name="CognitoUserPools-Type-SMSMfaSettingsType-Enabled"></a>
Specifies whether SMS message MFA is activated. If an MFA type is activated for a user, the user will be prompted for MFA during all sign-in attempts, unless device tracking is turned on and the device has been trusted.
Type: Boolean
Required: No

 ** PreferredMfa **   <a name="CognitoUserPools-Type-SMSMfaSettingsType-PreferredMfa"></a>
Specifies whether SMS is the preferred MFA method. If true, your user pool prompts the specified user for a code delivered by SMS message after username-password sign-in succeeds.
Type: Boolean
Required: No

## See Also
<a name="API_SMSMfaSettingsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SMSMfaSettingsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SMSMfaSettingsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SMSMfaSettingsType)
