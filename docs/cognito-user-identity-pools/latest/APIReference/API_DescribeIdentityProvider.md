---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.html
---

# DescribeIdentityProvider
<a name="API_DescribeIdentityProvider"></a>

Given a user pool ID and identity provider (IdP) name, returns details about the IdP.

## Request Syntax
<a name="API_DescribeIdentityProvider_RequestSyntax"></a>

```
{
   "ProviderName": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeIdentityProvider_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProviderName](#API_DescribeIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-DescribeIdentityProvider-request-ProviderName"></a>
The name of the IdP that you want to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
Required: Yes

 ** [UserPoolId](#API_DescribeIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-DescribeIdentityProvider-request-UserPoolId"></a>
The ID of the user pool that has the IdP that you want to describe..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_DescribeIdentityProvider_ResponseSyntax"></a>

```
{
   "IdentityProvider": {
      "AcrMapping": {
         "string" : "string"
      },
      "AttributeMapping": {
         "string" : "string"
      },
      "CreationDate": number,
      "IdpIdentifiers": [ "string" ],
      "LastModifiedDate": number,
      "ProviderDetails": {
         "string" : "string"
      },
      "ProviderName": "string",
      "ProviderType": "string",
      "UserPoolId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeIdentityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityProvider](#API_DescribeIdentityProvider_ResponseSyntax) **   <a name="CognitoUserPools-DescribeIdentityProvider-response-IdentityProvider"></a>
The details of the requested IdP.
Type: [IdentityProviderType](API_IdentityProviderType.md) object

## Errors
<a name="API_DescribeIdentityProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
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

## Examples
<a name="API_DescribeIdentityProvider_Examples"></a>

### Example
<a name="API_DescribeIdentityProvider_Example_1"></a>

The following example request describes a Google IdP.

#### Sample Request
<a name="API_DescribeIdentityProvider_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.DescribeIdentityProvider
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "ProviderName": "Google",
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeIdentityProvider_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
	"IdentityProvider": {
		"AttributeMapping": {
			"email": "email",
			"username": "sub"
		},
		"CreationDate": 1635187122.265,
		"IdpIdentifiers": [],
		"LastModifiedDate": 1697051749.303,
		"ProviderDetails": {
			"attributes_url": "https://people.googleapis.com/v1/people/me?personFields=",
			"attributes_url_add_attributes": "true",
			"authorize_scopes": "email profile openid",
			"authorize_url": "https://accounts.google.com/o/oauth2/v2/auth",
			"client_id": "[client ID].apps.googleusercontent.com",
			"client_secret": "[client secret]",
			"oidc_issuer": "https://accounts.google.com",
			"token_request_method": "POST",
			"token_url": "https://www.googleapis.com/oauth2/v4/token"
		},
		"ProviderName": "Google",
		"ProviderType": "Google",
		"UserPoolId": "us-west-2_EXAMPLE"
	}
}
```

## See Also
<a name="API_DescribeIdentityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/DescribeIdentityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/DescribeIdentityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DescribeIdentityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/DescribeIdentityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DescribeIdentityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/DescribeIdentityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/DescribeIdentityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/DescribeIdentityProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/DescribeIdentityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DescribeIdentityProvider)
