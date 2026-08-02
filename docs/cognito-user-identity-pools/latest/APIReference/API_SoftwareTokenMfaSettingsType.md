---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SoftwareTokenMfaSettingsType.html
---

# SoftwareTokenMfaSettingsType
<a name="API_SoftwareTokenMfaSettingsType"></a>

A user's preference for using time-based one-time password (TOTP) multi-factor authentication (MFA). Turns TOTP MFA on and off, and can set TOTP as preferred when other MFA options are available. You can't turn off TOTP MFA for any of your users when MFA is required in your user pool; you can only set the type that your user prefers.

This data type is a request parameter of [SetUserMFAPreference](API_SetUserMFAPreference.md) and [AdminSetUserMFAPreference](API_AdminSetUserMFAPreference.md).

## Contents
<a name="API_SoftwareTokenMfaSettingsType_Contents"></a>

 ** Enabled **   <a name="CognitoUserPools-Type-SoftwareTokenMfaSettingsType-Enabled"></a>
Specifies whether software token MFA is activated. If an MFA type is activated for a user, the user will be prompted for MFA during all sign-in attempts, unless device tracking is turned on and the device has been trusted.
Type: Boolean
Required: No

 ** PreferredMfa **   <a name="CognitoUserPools-Type-SoftwareTokenMfaSettingsType-PreferredMfa"></a>
Specifies whether software token MFA is the preferred MFA method.
Type: Boolean
Required: No

## See Also
<a name="API_SoftwareTokenMfaSettingsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SoftwareTokenMfaSettingsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SoftwareTokenMfaSettingsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SoftwareTokenMfaSettingsType)
