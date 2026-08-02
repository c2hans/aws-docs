---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailMfaSettingsType.html
---

# EmailMfaSettingsType
<a name="API_EmailMfaSettingsType"></a>

User preferences for multi-factor authentication with email messages. Activates or deactivates email MFA and sets it as the preferred MFA method when multiple methods are available. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

This data type is a request parameter of [SetUserMFAPreference](API_SetUserMFAPreference.md) and [AdminSetUserMFAPreference](API_AdminSetUserMFAPreference.md).

## Contents
<a name="API_EmailMfaSettingsType_Contents"></a>

 ** Enabled **   <a name="CognitoUserPools-Type-EmailMfaSettingsType-Enabled"></a>
Specifies whether email message MFA is active for a user. When the value of this parameter is `Enabled`, the user will be prompted for MFA during all sign-in attempts, unless device tracking is turned on and the device has been trusted.
Type: Boolean
Required: No

 ** PreferredMfa **   <a name="CognitoUserPools-Type-EmailMfaSettingsType-PreferredMfa"></a>
Specifies whether email message MFA is the user's preferred method.
Type: Boolean
Required: No

## See Also
<a name="API_EmailMfaSettingsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/EmailMfaSettingsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/EmailMfaSettingsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/EmailMfaSettingsType)
