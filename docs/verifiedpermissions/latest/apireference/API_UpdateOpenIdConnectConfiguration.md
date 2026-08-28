---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectConfiguration.html
---

# UpdateOpenIdConnectConfiguration
<a name="API_UpdateOpenIdConnectConfiguration"></a>

Contains configuration details of an OpenID Connect (OIDC) identity provider, or identity source, that Verified Permissions can use to generate entities from authenticated identities. It specifies the issuer URL, token type that you want to use, and policy store entity details.

This data type is part of a [UpdateConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateConfiguration.html) structure, which is a parameter to [UpdateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html).

## Contents
<a name="API_UpdateOpenIdConnectConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** issuer **   <a name="verifiedpermissions-Type-UpdateOpenIdConnectConfiguration-issuer"></a>
The issuer URL of an OIDC identity provider. This URL must have an OIDC discovery endpoint at the path `.well-known/openid-configuration`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://.*`
Required: Yes

 ** tokenSelection **   <a name="verifiedpermissions-Type-UpdateOpenIdConnectConfiguration-tokenSelection"></a>
The token type that you want to process from your OIDC identity provider. Your policy store can process either identity (ID) or access tokens from a given OIDC identity source.
Type: [UpdateOpenIdConnectTokenSelection](API_UpdateOpenIdConnectTokenSelection.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** entityIdPrefix **   <a name="verifiedpermissions-Type-UpdateOpenIdConnectConfiguration-entityIdPrefix"></a>
A descriptive string that you want to prefix to user entities from your OIDC identity provider. For example, if you set an `entityIdPrefix` of `MyOIDCProvider`, you can reference principals in your policies in the format `MyCorp::User::MyOIDCProvider|Carlos`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** groupConfiguration **   <a name="verifiedpermissions-Type-UpdateOpenIdConnectConfiguration-groupConfiguration"></a>
The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to. For example, this object can map the contents of a `groups` claim to `MyCorp::UserGroup`.
Type: [UpdateOpenIdConnectGroupConfiguration](API_UpdateOpenIdConnectGroupConfiguration.md) object
Required: No

## See Also
<a name="API_UpdateOpenIdConnectConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/UpdateOpenIdConnectConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/UpdateOpenIdConnectConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/UpdateOpenIdConnectConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
