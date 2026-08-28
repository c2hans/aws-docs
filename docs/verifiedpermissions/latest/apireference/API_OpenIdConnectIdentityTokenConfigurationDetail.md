---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectIdentityTokenConfigurationDetail.html
---

# OpenIdConnectIdentityTokenConfigurationDetail
<a name="API_OpenIdConnectIdentityTokenConfigurationDetail"></a>

The configuration of an OpenID Connect (OIDC) identity source for handling identity (ID) token claims. Contains the claim that you want to identify as the principal in an authorization request, and the values of the `aud` claim, or audiences, that you want to accept.

This data type is part of a [OpenIdConnectTokenSelectionDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelectionDetail.html) structure, which is a parameter of [GetIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html).

## Contents
<a name="API_OpenIdConnectIdentityTokenConfigurationDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** clientIds **   <a name="verifiedpermissions-Type-OpenIdConnectIdentityTokenConfigurationDetail-clientIds"></a>
The ID token audience, or client ID, claim values that you want to accept in your policy store from an OIDC identity provider. For example, `1example23456789, 2example10111213`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** principalIdClaim **   <a name="verifiedpermissions-Type-OpenIdConnectIdentityTokenConfigurationDetail-principalIdClaim"></a>
The claim that determines the principal in OIDC access tokens. For example, `sub`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_OpenIdConnectIdentityTokenConfigurationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/OpenIdConnectIdentityTokenConfigurationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/OpenIdConnectIdentityTokenConfigurationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/OpenIdConnectIdentityTokenConfigurationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
