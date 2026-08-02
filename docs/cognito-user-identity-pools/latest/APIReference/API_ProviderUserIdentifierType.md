---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ProviderUserIdentifierType.html
---

# ProviderUserIdentifierType
<a name="API_ProviderUserIdentifierType"></a>

The characteristics of a source or destination user for linking a federated user profile to a local user profile.

This data type is a request parameter of [AdminLinkProviderForUser](API_AdminLinkProviderForUser.md) and [AdminDisableProviderForUser](API_AdminDisableProviderForUser.md).

## Contents
<a name="API_ProviderUserIdentifierType_Contents"></a>

 ** ProviderAttributeName **   <a name="CognitoUserPools-Type-ProviderUserIdentifierType-ProviderAttributeName"></a>
The name of the provider attribute to link to, such as `NameID`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** ProviderAttributeValue **   <a name="CognitoUserPools-Type-ProviderUserIdentifierType-ProviderAttributeValue"></a>
The value of the provider attribute to link to, such as `xxxxx_account`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** ProviderName **   <a name="CognitoUserPools-Type-ProviderUserIdentifierType-ProviderName"></a>
The name of the provider, such as Facebook, Google, or Login with Amazon.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
Required: No

## See Also
<a name="API_ProviderUserIdentifierType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ProviderUserIdentifierType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ProviderUserIdentifierType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ProviderUserIdentifierType)
