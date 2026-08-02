---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectIdentityTokenConfiguration.html
---

# OpenIdConnectIdentityTokenConfiguration
<a name="API_OpenIdConnectIdentityTokenConfiguration"></a>

The configuration of an OpenID Connect (OIDC) identity source for handling identity (ID) token claims. Contains the claim that you want to identify as the principal in an authorization request, and the values of the `aud` claim, or audiences, that you want to accept.

This data type is part of a [OpenIdConnectTokenSelection](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelection.html) structure, which is a parameter of [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

## Contents
<a name="API_OpenIdConnectIdentityTokenConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** clientIds **   <a name="verifiedpermissions-Type-OpenIdConnectIdentityTokenConfiguration-clientIds"></a>
The ID token audience, or client ID, claim values that you want to accept in your policy store from an OIDC identity provider. For example, `1example23456789, 2example10111213`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** principalIdClaim **   <a name="verifiedpermissions-Type-OpenIdConnectIdentityTokenConfiguration-principalIdClaim"></a>
The claim that determines the principal in OIDC access tokens. For example, `sub`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_OpenIdConnectIdentityTokenConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/OpenIdConnectIdentityTokenConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/OpenIdConnectIdentityTokenConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/OpenIdConnectIdentityTokenConfiguration)
