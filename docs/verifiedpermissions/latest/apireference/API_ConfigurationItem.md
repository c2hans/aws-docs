---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationItem.html
---

# ConfigurationItem
<a name="API_ConfigurationItem"></a>

Contains configuration information about an identity source.

This data type is a response parameter to the [ListIdentitySources](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html) operation.

## Contents
<a name="API_ConfigurationItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cognitoUserPoolConfiguration **   <a name="verifiedpermissions-Type-ConfigurationItem-cognitoUserPoolConfiguration"></a>
Contains configuration details of a Amazon Cognito user pool that Verified Permissions can use as a source of authenticated identities as entities. It specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a Amazon Cognito user pool, the policy store entity that you want to assign to user groups, and one or more application client IDs.
Example: `"configuration":{"cognitoUserPoolConfiguration":{"userPoolArn":"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5","clientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],"groupConfiguration": {"groupEntityType": "MyCorp::Group"}}}`
Type: [CognitoUserPoolConfigurationItem](API_CognitoUserPoolConfigurationItem.md) object
Required: No

 ** openIdConnectConfiguration **   <a name="verifiedpermissions-Type-ConfigurationItem-openIdConnectConfiguration"></a>
Contains configuration details of an OpenID Connect (OIDC) identity provider, or identity source, that Verified Permissions can use to generate entities from authenticated identities. It specifies the issuer URL, token type that you want to use, and policy store entity details.
Example:`"configuration":{"openIdConnectConfiguration":{"issuer":"https://auth.example.com","tokenSelection":{"accessTokenOnly":{"audiences":["https://myapp.example.com","https://myapp2.example.com"],"principalIdClaim":"sub"}},"entityIdPrefix":"MyOIDCProvider","groupConfiguration":{"groupClaim":"groups","groupEntityType":"MyCorp::UserGroup"}}}`
Type: [OpenIdConnectConfigurationItem](API_OpenIdConnectConfigurationItem.md) object
Required: No

## See Also
<a name="API_ConfigurationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/ConfigurationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/ConfigurationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/ConfigurationItem)
