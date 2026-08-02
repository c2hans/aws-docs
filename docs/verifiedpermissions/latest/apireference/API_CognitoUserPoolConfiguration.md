---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfiguration.html
---

# CognitoUserPoolConfiguration
<a name="API_CognitoUserPoolConfiguration"></a>

The configuration for an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions.

This data type part of a [Configuration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Configuration.html) structure that is used as a parameter to [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

Example:`"CognitoUserPoolConfiguration":{"UserPoolArn":"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5","ClientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],"groupConfiguration": {"groupEntityType": "MyCorp::Group"}}`

## Contents
<a name="API_CognitoUserPoolConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** userPoolArn **   <a name="verifiedpermissions-Type-CognitoUserPoolConfiguration-userPoolArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon Cognito user pool that contains the identities to be authorized.
Example: `"UserPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5"`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:[a-zA-Z0-9-]+:cognito-idp:(([a-zA-Z0-9-]+:\d{12}:userpool/[\w-]+_[0-9a-zA-Z]+))`
Required: Yes

 ** clientIds **   <a name="verifiedpermissions-Type-CognitoUserPoolConfiguration-clientIds"></a>
The unique application client IDs that are associated with the specified Amazon Cognito user pool.
Example: `"ClientIds": ["&ExampleCogClientId;"]`
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** groupConfiguration **   <a name="verifiedpermissions-Type-CognitoUserPoolConfiguration-groupConfiguration"></a>
The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.
Type: [CognitoGroupConfiguration](API_CognitoGroupConfiguration.md) object
Required: No

## See Also
<a name="API_CognitoUserPoolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/CognitoUserPoolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/CognitoUserPoolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/CognitoUserPoolConfiguration)
