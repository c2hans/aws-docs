---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelection.html
---

# OpenIdConnectTokenSelection
<a name="API_OpenIdConnectTokenSelection"></a>

The token type that you want to process from your OIDC identity provider. Your policy store can process either identity (ID) or access tokens from a given OIDC identity source.

This data type is part of a [OpenIdConnectConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfiguration.html) structure, which is a parameter of [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

## Contents
<a name="API_OpenIdConnectTokenSelection_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accessTokenOnly **   <a name="verifiedpermissions-Type-OpenIdConnectTokenSelection-accessTokenOnly"></a>
The OIDC configuration for processing access tokens. Contains allowed audience claims, for example `https://auth.example.com`, and the claim that you want to map to the principal, for example `sub`.
Type: [OpenIdConnectAccessTokenConfiguration](API_OpenIdConnectAccessTokenConfiguration.md) object
Required: No

 ** identityTokenOnly **   <a name="verifiedpermissions-Type-OpenIdConnectTokenSelection-identityTokenOnly"></a>
The OIDC configuration for processing identity (ID) tokens. Contains allowed client ID claims, for example `1example23456789`, and the claim that you want to map to the principal, for example `sub`.
Type: [OpenIdConnectIdentityTokenConfiguration](API_OpenIdConnectIdentityTokenConfiguration.md) object
Required: No

## See Also
<a name="API_OpenIdConnectTokenSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/OpenIdConnectTokenSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/OpenIdConnectTokenSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/OpenIdConnectTokenSelection)
