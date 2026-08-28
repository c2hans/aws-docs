---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_WebAuthnConfigurationType.html
---

# WebAuthnConfigurationType
<a name="API_WebAuthnConfigurationType"></a>

Settings for authentication (MFA) with passkey, or webauthN, biometric and security-key devices in a user pool. Configures the following:
+ Configuration for requiring user-verification support in passkeys.
+ The user pool relying-party ID. This is the domain, typically your user pool domain, that user's passkey providers should trust as a receiver of passkey authentication.
+ The providers that you want to allow as origins for passkey authentication.

This data type is a request parameter of [SetUserPoolMfaConfig](API_SetUserPoolMfaConfig.md) and a response parameter of [GetUserPoolMfaConfig](API_GetUserPoolMfaConfig.md). To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

## Contents
<a name="API_WebAuthnConfigurationType_Contents"></a>

 ** FactorConfiguration **   <a name="CognitoUserPools-Type-WebAuthnConfigurationType-FactorConfiguration"></a>
Sets whether passkeys can be used as multi-factor authentication (MFA). When set to `MULTI_FACTOR_WITH_USER_VERIFICATION`, passkey authentication with user verification satisfies MFA requirements. When set to `SINGLE_FACTOR` or not set, passkeys are a single authentication factor. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
Type: String
Valid Values: `SINGLE_FACTOR | MULTI_FACTOR_WITH_USER_VERIFICATION`
Required: No

 ** RelyingPartyId **   <a name="CognitoUserPools-Type-WebAuthnConfigurationType-RelyingPartyId"></a>
Sets or displays the authentication domain, typically your user pool domain, that passkey providers must use as a relying party (RP) in their configuration.
Under the following conditions, the passkey relying party ID must be the fully-qualified domain name of your custom domain:
+ The user pool is configured for passkey authentication.
+ The user pool has a custom domain, whether or not it also has a prefix domain.
+ Your application performs authentication with managed login or the classic hosted UI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** UserVerification **   <a name="CognitoUserPools-Type-WebAuthnConfigurationType-UserVerification"></a>
When `required`, users can only register and sign in users with passkeys that are capable of [user verification](https://www.w3.org/TR/webauthn-2/#enum-userVerificationRequirement). When `preferred`, your user pool doesn't require the use of authenticators with user verification but encourages it.
Type: String
Valid Values: `required | preferred`
Required: No

## See Also
<a name="API_WebAuthnConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/WebAuthnConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/WebAuthnConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/WebAuthnConfigurationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
