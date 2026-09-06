---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ProviderDescription.html
---

# ProviderDescription
<a name="API_ProviderDescription"></a>

The details of a user pool identity provider (IdP), including name and type.

This data type is a response parameter of [ListIdentityProviders](API_ListIdentityProviders.md).

## Contents
<a name="API_ProviderDescription_Contents"></a>

 ** CreationDate **   <a name="CognitoUserPools-Type-ProviderDescription-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-ProviderDescription-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** ProviderName **   <a name="CognitoUserPools-Type-ProviderDescription-ProviderName"></a>
The name of the IdP, for example `MySAMLProvider`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
Required: No

 ** ProviderType **   <a name="CognitoUserPools-Type-ProviderDescription-ProviderType"></a>
The type of the provider, for example `SAML`. Amazon Cognito supports SAML 2.0, OIDC, and social IdPs. User pools list supported social IdPs by name in this response parameter: Facebook, Google, Login with Amazon, and Sign in with Apple.
Type: String
Valid Values: `SAML | Facebook | Google | LoginWithAmazon | SignInWithApple | OIDC`
Required: No

## See Also
<a name="API_ProviderDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ProviderDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ProviderDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ProviderDescription)
