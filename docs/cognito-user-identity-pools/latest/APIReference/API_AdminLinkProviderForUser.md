---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.html
---

# AdminLinkProviderForUser
<a name="API_AdminLinkProviderForUser"></a>

Links an existing user account in a user pool, or `DestinationUser`, to an identity from an external IdP, or `SourceUser`, based on a specified attribute name and value from the external IdP.

This operation connects a local user profile with a user identity who hasn't yet signed in from their third-party IdP. When the user signs in with their IdP, they get access-control configuration from the local user profile. Linked local users can also sign in with SDK-based API operations like `InitiateAuth` after they sign in at least once through their IdP. For more information, see [Linking federated users](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html).

**Note**
The maximum number of federated identities linked to a user is five.

**Important**
Because this API allows a user with an external federated identity to sign in as a local user, it is critical that it only be used with external IdPs and linked attributes that you trust.

See also [AdminDisableProviderForUser](API_AdminDisableProviderForUser.md).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AdminLinkProviderForUser_RequestSyntax"></a>

```
{
   "DestinationUser": {
      "ProviderAttributeName": "{{string}}",
      "ProviderAttributeValue": "{{string}}",
      "ProviderName": "{{string}}"
   },
   "SourceUser": {
      "ProviderAttributeName": "{{string}}",
      "ProviderAttributeValue": "{{string}}",
      "ProviderName": "{{string}}"
   },
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminLinkProviderForUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationUser](#API_AdminLinkProviderForUser_RequestSyntax) **   <a name="CognitoUserPools-AdminLinkProviderForUser-request-DestinationUser"></a>
The existing user in the user pool that you want to assign to the external IdP user account. This user can be a local (Username \+ Password) Amazon Cognito user pools user or a federated user (for example, a SAML or Facebook user). If the user doesn't exist, Amazon Cognito generates an exception. Amazon Cognito returns this user when the new user (with the linked IdP attribute) signs in.
For a native username \+ password user, the `ProviderAttributeValue` for the `DestinationUser` should be the username in the user pool. For a federated user, it should be the provider-specific `user_id`.
The `ProviderAttributeName` of the `DestinationUser` is ignored.
The `ProviderName` should be set to `Cognito` for users in Cognito user pools.
Type: [ProviderUserIdentifierType](API_ProviderUserIdentifierType.md) object
Required: Yes

 ** [SourceUser](#API_AdminLinkProviderForUser_RequestSyntax) **   <a name="CognitoUserPools-AdminLinkProviderForUser-request-SourceUser"></a>
An external IdP account for a user who doesn't exist yet in the user pool. This user must be a federated user (for example, a SAML or Facebook user), not another native user.
If the `SourceUser` is using a federated social IdP, such as Facebook, Google, or Login with Amazon, you must set the `ProviderAttributeName` to `Cognito_Subject`. For social IdPs, the `ProviderName` will be `Facebook`, `Google`, or `LoginWithAmazon`, and Amazon Cognito will automatically parse the Facebook, Google, and Login with Amazon tokens for `id`, `sub`, and `user_id`, respectively. The `ProviderAttributeValue` for the user must be the same value as the `id`, `sub`, or `user_id` value found in the social IdP token.
For OIDC, the `ProviderAttributeName` can be any mapped value from a claim in the ID token, or that your app retrieves from the `userInfo` endpoint. For SAML, the `ProviderAttributeName` can be any mapped value from a claim in the SAML assertion.
The following additional considerations apply to `SourceUser` for OIDC and SAML providers.
+ You must map the claim to a user pool attribute in your IdP configuration, and set the user pool attribute name as the value of `ProviderAttributeName` in your `AdminLinkProviderForUser` request. For example, `email`.
+ When you set `ProviderAttributeName` to `Cognito_Subject`, Amazon Cognito will automatically parse the default unique identifier found in the subject from the IdP token.
Type: [ProviderUserIdentifierType](API_ProviderUserIdentifierType.md) object
Required: Yes

 ** [UserPoolId](#API_AdminLinkProviderForUser_RequestSyntax) **   <a name="CognitoUserPools-AdminLinkProviderForUser-request-UserPoolId"></a>
The ID of the user pool where you want to link a federated identity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: Yes

## Response Elements
<a name="API_AdminLinkProviderForUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AdminLinkProviderForUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AliasExistsException **
This exception is thrown when a user tries to confirm the account with an email address or phone number that has already been supplied as an alias for a different user profile. This exception indicates that an account with this email address or phone already exists in a user pool that you've configured to use email address or phone number as a sign-in alias.
 ** message **
The message that Amazon Cognito sends to the user when the value of an alias attribute is already linked to another user profile.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** LimitExceededException **
This exception is thrown when a user exceeds the limit for a requested AWS resource.
 ** message **
The message returned when Amazon Cognito throws a limit exceeded exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## Examples
<a name="API_AdminLinkProviderForUser_Examples"></a>

### Example
<a name="API_AdminLinkProviderForUser_Example_1"></a>

The following example links a Facebook user to the user pool user "adminlink-testuser." The user's unique identifier with Facebook is represented in the value of `ProviderAttributeValue`.

#### Sample Request
<a name="API_AdminLinkProviderForUser_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminLinkProviderForUser
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
  "DestinationUser": {
    "ProviderAttributeValue": "adminlink-testuser",
    "ProviderName": "Cognito"
  },
  "SourceUser": {
    "ProviderAttributeName": "Cognito_Subject",
    "ProviderAttributeValue": "123456789012345",
    "ProviderName": "Facebook"
  },
  "UserPoolId": "us-west-2_EXAMPLE"}
```

#### Sample Response
<a name="API_AdminLinkProviderForUser_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

### Example
<a name="API_AdminLinkProviderForUser_Example_2"></a>

The following example links a Google user to the user pool user "adminlink-testuser." The user's unique identifier with Google is represented in the value of `ProviderAttributeValue`.

#### Sample Request
<a name="API_AdminLinkProviderForUser_Example_2_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminLinkProviderForUser
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
  "DestinationUser": {
    "ProviderAttributeValue": "adminlink-testuser",
    "ProviderName": "Cognito"
  },
  "SourceUser": {
    "ProviderAttributeName": "Cognito_Subject",
    "ProviderAttributeValue": "5432109876543210",
    "ProviderName": "Google"
  },
  "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_AdminLinkProviderForUser_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

### Example
<a name="API_AdminLinkProviderForUser_Example_3"></a>

The following example links a Login With Amazon user to the user pool user "adminlink-testuser." The user's unique identifier with Amazon is represented in the value of `ProviderAttributeValue`.

#### Sample Request
<a name="API_AdminLinkProviderForUser_Example_3_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminLinkProviderForUser
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
  "DestinationUser": {
    "ProviderAttributeValue": "adminlink-testuser",
    "ProviderName": "Cognito"
  },
  "SourceUser": {
    "ProviderAttributeName": "Cognito_Subject",
    "ProviderAttributeValue": "amzn1.account.AFALI...",
    "ProviderName": "LoginWithAmazon"
  },
  "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_AdminLinkProviderForUser_Example_3_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

### Example
<a name="API_AdminLinkProviderForUser_Example_4"></a>

The following example links a Sign In With Apple user to the user pool user "adminlink-testuser." The user's unique identifier with Apple is represented in the value of `ProviderAttributeValue`.

#### Sample Request
<a name="API_AdminLinkProviderForUser_Example_4_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminLinkProviderForUser
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
	"DestinationUser": {
		"ProviderAttributeValue": "adminlink-testuser",
		"ProviderName": "Cognito"
	},
	"SourceUser": {
		"ProviderAttributeName": "Cognito_Subject",
		"ProviderAttributeValue": "000111.11111111111111111111111111111111111111.1111",
		"ProviderName": "SignInWithApple"
	},
	"UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_AdminLinkProviderForUser_Example_4_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

### Example
<a name="API_AdminLinkProviderForUser_Example_5"></a>

The following example links a user from OIDC provider "MyOIDCProvider" to the user pool user "adminlink-testuser." This request links the local user to an IdP user that has a `preferred_username` attribute of `testuser@example.com`. For this user to sync, your application must request scopes that return the `preferred_username` attribute from the IdP.

#### Sample Request
<a name="API_AdminLinkProviderForUser_Example_5_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminLinkProviderForUser
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
	"DestinationUser": {
		"ProviderAttributeValue": "adminlink-testuser",
		"ProviderName": "Cognito"
	},
	"SourceUser": {
		"ProviderAttributeName": "preferred_username",
		"ProviderAttributeValue": "testuser@example.com",
		"ProviderName": "MyOIDCProvider"
	},
	"UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_AdminLinkProviderForUser_Example_5_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

### Example
<a name="API_AdminLinkProviderForUser_Example_6"></a>

The following example links a user from SAML 2.0 provider "MySAMLProvider" to the user pool user "adminlink-testuser." This request links the local user to an IdP user that has a `email` attribute of `testuser@example.com`. For this user to sync, your application must receive an `email` claim in the SAML assertion.

#### Sample Request
<a name="API_AdminLinkProviderForUser_Example_6_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminLinkProviderForUser
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
	"DestinationUser": {
		"ProviderAttributeValue": "adminlink-testuser",
		"ProviderName": "Cognito"
	},
	"SourceUser": {
		"ProviderAttributeName": "email",
		"ProviderAttributeValue": "testuser@example.com",
		"ProviderName": "MySAMLProvider"
	},
	"UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_AdminLinkProviderForUser_Example_6_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

## See Also
<a name="API_AdminLinkProviderForUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminLinkProviderForUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminLinkProviderForUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminLinkProviderForUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminLinkProviderForUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminLinkProviderForUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminLinkProviderForUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminLinkProviderForUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminLinkProviderForUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminLinkProviderForUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminLinkProviderForUser)
