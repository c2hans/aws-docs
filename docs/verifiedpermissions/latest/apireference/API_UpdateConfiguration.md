---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateConfiguration.html
---

# UpdateConfiguration
<a name="API_UpdateConfiguration"></a>

Contains an update to replace the configuration in an existing identity source.

## Contents
<a name="API_UpdateConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cognitoUserPoolConfiguration **   <a name="verifiedpermissions-Type-UpdateConfiguration-cognitoUserPoolConfiguration"></a>
Contains configuration details of a Amazon Cognito user pool.
Type: [UpdateCognitoUserPoolConfiguration](API_UpdateCognitoUserPoolConfiguration.md) object
Required: No

 ** openIdConnectConfiguration **   <a name="verifiedpermissions-Type-UpdateConfiguration-openIdConnectConfiguration"></a>
Contains configuration details of an OpenID Connect (OIDC) identity provider, or identity source, that Verified Permissions can use to generate entities from authenticated identities. It specifies the issuer URL, token type that you want to use, and policy store entity details.
Type: [UpdateOpenIdConnectConfiguration](API_UpdateOpenIdConnectConfiguration.md) object
Required: No

## See Also
<a name="API_UpdateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/UpdateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/UpdateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/UpdateConfiguration)
