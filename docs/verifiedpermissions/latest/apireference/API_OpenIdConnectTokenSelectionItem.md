---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelectionItem.html
---

# OpenIdConnectTokenSelectionItem
<a name="API_OpenIdConnectTokenSelectionItem"></a>

The token type that you want to process from your OIDC identity provider. Your policy store can process either identity (ID) or access tokens from a given OIDC identity source.

This data type is part of a [OpenIdConnectConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfigurationItem.html) structure, which is a parameter of [ListIdentitySources](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html).

## Contents
<a name="API_OpenIdConnectTokenSelectionItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accessTokenOnly **   <a name="verifiedpermissions-Type-OpenIdConnectTokenSelectionItem-accessTokenOnly"></a>
The OIDC configuration for processing access tokens. Contains allowed audience claims, for example `https://auth.example.com`, and the claim that you want to map to the principal, for example `sub`.
Type: [OpenIdConnectAccessTokenConfigurationItem](API_OpenIdConnectAccessTokenConfigurationItem.md) object
Required: No

 ** identityTokenOnly **   <a name="verifiedpermissions-Type-OpenIdConnectTokenSelectionItem-identityTokenOnly"></a>
The OIDC configuration for processing identity (ID) tokens. Contains allowed client ID claims, for example `1example23456789`, and the claim that you want to map to the principal, for example `sub`.
Type: [OpenIdConnectIdentityTokenConfigurationItem](API_OpenIdConnectIdentityTokenConfigurationItem.md) object
Required: No

## See Also
<a name="API_OpenIdConnectTokenSelectionItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/OpenIdConnectTokenSelectionItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/OpenIdConnectTokenSelectionItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/OpenIdConnectTokenSelectionItem)
