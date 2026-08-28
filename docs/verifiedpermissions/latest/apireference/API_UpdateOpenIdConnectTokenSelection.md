---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectTokenSelection.html
---

# UpdateOpenIdConnectTokenSelection
<a name="API_UpdateOpenIdConnectTokenSelection"></a>

The token type that you want to process from your OIDC identity provider. Your policy store can process either identity (ID) or access tokens from a given OIDC identity source.

This data type is part of a [UpdateOpenIdConnectConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectConfiguration.html) structure, which is a parameter to [UpdateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html).

## Contents
<a name="API_UpdateOpenIdConnectTokenSelection_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accessTokenOnly **   <a name="verifiedpermissions-Type-UpdateOpenIdConnectTokenSelection-accessTokenOnly"></a>
The OIDC configuration for processing access tokens. Contains allowed audience claims, for example `https://auth.example.com`, and the claim that you want to map to the principal, for example `sub`.
Type: [UpdateOpenIdConnectAccessTokenConfiguration](API_UpdateOpenIdConnectAccessTokenConfiguration.md) object
Required: No

 ** identityTokenOnly **   <a name="verifiedpermissions-Type-UpdateOpenIdConnectTokenSelection-identityTokenOnly"></a>
The OIDC configuration for processing identity (ID) tokens. Contains allowed client ID claims, for example `1example23456789`, and the claim that you want to map to the principal, for example `sub`.
Type: [UpdateOpenIdConnectIdentityTokenConfiguration](API_UpdateOpenIdConnectIdentityTokenConfiguration.md) object
Required: No

## See Also
<a name="API_UpdateOpenIdConnectTokenSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/UpdateOpenIdConnectTokenSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/UpdateOpenIdConnectTokenSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/UpdateOpenIdConnectTokenSelection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
