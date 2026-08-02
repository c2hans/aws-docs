---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfigurationItem.html
---

# CognitoUserPoolConfigurationItem
<a name="API_CognitoUserPoolConfigurationItem"></a>

The configuration for an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions.

This data type is used as a field that is part of the [ConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationItem.html) structure that is part of the response to [ListIdentitySources](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html).

Example:`"CognitoUserPoolConfiguration":{"UserPoolArn":"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5","ClientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],"groupConfiguration": {"groupEntityType": "MyCorp::Group"}}`

## Contents
<a name="API_CognitoUserPoolConfigurationItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** clientIds **   <a name="verifiedpermissions-Type-CognitoUserPoolConfigurationItem-clientIds"></a>
The unique application client IDs that are associated with the specified Amazon Cognito user pool.
Example: `"clientIds": ["&ExampleCogClientId;"]`
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** issuer **   <a name="verifiedpermissions-Type-CognitoUserPoolConfigurationItem-issuer"></a>
The OpenID Connect (OIDC) `issuer` ID of the Amazon Cognito user pool that contains the identities to be authorized.
Example: `"issuer": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_1a2b3c4d5"`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://.*`
Required: Yes

 ** userPoolArn **   <a name="verifiedpermissions-Type-CognitoUserPoolConfigurationItem-userPoolArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon Cognito user pool that contains the identities to be authorized.
Example: `"userPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5"`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:[a-zA-Z0-9-]+:cognito-idp:(([a-zA-Z0-9-]+:\d{12}:userpool/[\w-]+_[0-9a-zA-Z]+))`
Required: Yes

 ** groupConfiguration **   <a name="verifiedpermissions-Type-CognitoUserPoolConfigurationItem-groupConfiguration"></a>
The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.
Type: [CognitoGroupConfigurationItem](API_CognitoGroupConfigurationItem.md) object
Required: No

## See Also
<a name="API_CognitoUserPoolConfigurationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/CognitoUserPoolConfigurationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/CognitoUserPoolConfigurationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/CognitoUserPoolConfigurationItem)
