---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectAccessTokenConfiguration.html
---

# OpenIdConnectAccessTokenConfiguration
<a name="API_OpenIdConnectAccessTokenConfiguration"></a>

The configuration of an OpenID Connect (OIDC) identity source for handling access token claims. Contains the claim that you want to identify as the principal in an authorization request, and the values of the `aud` claim, or audiences, that you want to accept.

This data type is part of a [OpenIdConnectTokenSelection](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelection.html) structure, which is a parameter of [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

## Contents
<a name="API_OpenIdConnectAccessTokenConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** audiences **   <a name="verifiedpermissions-Type-OpenIdConnectAccessTokenConfiguration-audiences"></a>
The access token `aud` claim values that you want to accept in your policy store. For example, `https://myapp.example.com, https://myapp2.example.com`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 255 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** principalIdClaim **   <a name="verifiedpermissions-Type-OpenIdConnectAccessTokenConfiguration-principalIdClaim"></a>
The claim that determines the principal in OIDC access tokens. For example, `sub`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_OpenIdConnectAccessTokenConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/OpenIdConnectAccessTokenConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/OpenIdConnectAccessTokenConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/OpenIdConnectAccessTokenConfiguration)
