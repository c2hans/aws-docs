---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_WebAuthnMfaSettingsType.html
---

# WebAuthnMfaSettingsType
<a name="API_WebAuthnMfaSettingsType"></a>

A user's preference for using passkey, or WebAuthn, multi-factor authentication (MFA). Turns passkey MFA on and off for the user. Unlike other MFA settings types, this type doesn't include a `PreferredMfa` option because passkey MFA applies only when passkey is the first authentication factor.

This data type is a request parameter of [SetUserMFAPreference](API_SetUserMFAPreference.md) and [AdminSetUserMFAPreference](API_AdminSetUserMFAPreference.md).

## Contents
<a name="API_WebAuthnMfaSettingsType_Contents"></a>

 ** Enabled **   <a name="CognitoUserPools-Type-WebAuthnMfaSettingsType-Enabled"></a>
Specifies whether passkey MFA is activated for a user. When activated, the user's passkey authentication requires user verification, and passkey sign-in is available when MFA is required. The user must also have at least one other MFA method such as SMS, TOTP, or email activated to prevent account lockout.
Type: Boolean
Required: No

## See Also
<a name="API_WebAuthnMfaSettingsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/WebAuthnMfaSettingsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/WebAuthnMfaSettingsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/WebAuthnMfaSettingsType)
