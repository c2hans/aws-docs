---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_WebAuthnCredentialDescription.html
---

# WebAuthnCredentialDescription
<a name="API_WebAuthnCredentialDescription"></a>

The details of a passkey, or webauthN, biometric or security-key authentication factor for a user.

This data type is a response parameter of [ListWebAuthnCredentials](API_ListWebAuthnCredentials.md). To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

## Contents
<a name="API_WebAuthnCredentialDescription_Contents"></a>

 ** AuthenticatorTransports **   <a name="CognitoUserPools-Type-WebAuthnCredentialDescription-AuthenticatorTransports"></a>
Information about the transport methods of the passkey credential, for example USB or Bluetooth Low Energy.
Type: Array of strings
Required: Yes

 ** CreatedAt **   <a name="CognitoUserPools-Type-WebAuthnCredentialDescription-CreatedAt"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: Yes

 ** CredentialId **   <a name="CognitoUserPools-Type-WebAuthnCredentialDescription-CredentialId"></a>
The unique identifier of the passkey credential.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: Yes

 ** FriendlyCredentialName **   <a name="CognitoUserPools-Type-WebAuthnCredentialDescription-FriendlyCredentialName"></a>
An automatically-generated friendly name for the passkey credential.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: Yes

 ** RelyingPartyId **   <a name="CognitoUserPools-Type-WebAuthnCredentialDescription-RelyingPartyId"></a>
The relying-party ID of the provider for the passkey credential.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: Yes

 ** AuthenticatorAttachment **   <a name="CognitoUserPools-Type-WebAuthnCredentialDescription-AuthenticatorAttachment"></a>
The general category of the passkey authenticator. Can be a platform, or on-device authenticator like a built-in fingerprint scanner, or a cross-platform device that's not attached to the device like a Bluetooth security key.
Type: String
Required: No

## See Also
<a name="API_WebAuthnCredentialDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/WebAuthnCredentialDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/WebAuthnCredentialDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/WebAuthnCredentialDescription)
