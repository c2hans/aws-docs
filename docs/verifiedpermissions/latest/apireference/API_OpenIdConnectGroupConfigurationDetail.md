---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectGroupConfigurationDetail.html
---

# OpenIdConnectGroupConfigurationDetail
<a name="API_OpenIdConnectGroupConfigurationDetail"></a>

The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to. For example, this object can map the contents of a `groups` claim to `MyCorp::UserGroup`.

This data type is part of a [OpenIdConnectConfigurationDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfigurationDetail.html) structure, which is a parameter of [GetIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html).

## Contents
<a name="API_OpenIdConnectGroupConfigurationDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** groupClaim **   <a name="verifiedpermissions-Type-OpenIdConnectGroupConfigurationDetail-groupClaim"></a>
The token claim that you want Verified Permissions to interpret as group membership. For example, `groups`.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** groupEntityType **   <a name="verifiedpermissions-Type-OpenIdConnectGroupConfigurationDetail-groupEntityType"></a>
The policy store entity type that you want to map your users' group claim to. For example, `MyCorp::UserGroup`. A group entity type is an entity that can have a user entity type as a member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `([_a-zA-Z][_a-zA-Z0-9]*::)*[_a-zA-Z][_a-zA-Z0-9]*`
Required: Yes

## See Also
<a name="API_OpenIdConnectGroupConfigurationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/OpenIdConnectGroupConfigurationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/OpenIdConnectGroupConfigurationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/OpenIdConnectGroupConfigurationDetail)
