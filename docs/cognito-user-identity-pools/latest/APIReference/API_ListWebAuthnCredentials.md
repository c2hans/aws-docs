---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListWebAuthnCredentials.html
---

# ListWebAuthnCredentials
<a name="API_ListWebAuthnCredentials"></a>

Generates a list of the currently signed-in user's registered passkey, or WebAuthn, credentials.

Authorize this action with a signed-in user's access token. It must include the scope `aws.cognito.signin.user.admin`.

**Note**
Amazon Cognito doesn't evaluate AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can't use IAM credentials to authorize requests, and you can't grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html).

## Request Syntax
<a name="API_ListWebAuthnCredentials_RequestSyntax"></a>

```
{
   "AccessToken": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListWebAuthnCredentials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessToken](#API_ListWebAuthnCredentials_RequestSyntax) **   <a name="CognitoUserPools-ListWebAuthnCredentials-request-AccessToken"></a>
A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for `aws.cognito.signin.user.admin`.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: Yes

 ** [MaxResults](#API_ListWebAuthnCredentials_RequestSyntax) **   <a name="CognitoUserPools-ListWebAuthnCredentials-request-MaxResults"></a>
The maximum number of the user's passkey credentials that you want to return.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [NextToken](#API_ListWebAuthnCredentials_RequestSyntax) **   <a name="CognitoUserPools-ListWebAuthnCredentials-request-NextToken"></a>
This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`
Required: No

## Response Syntax
<a name="API_ListWebAuthnCredentials_ResponseSyntax"></a>

```
{
   "Credentials": [
      {
         "AuthenticatorAttachment": "string",
         "AuthenticatorTransports": [ "string" ],
         "CreatedAt": number,
         "CredentialId": "string",
         "FriendlyCredentialName": "string",
         "RelyingPartyId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListWebAuthnCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Credentials](#API_ListWebAuthnCredentials_ResponseSyntax) **   <a name="CognitoUserPools-ListWebAuthnCredentials-response-Credentials"></a>
A list of registered passkeys for a user.
Type: Array of [WebAuthnCredentialDescription](API_WebAuthnCredentialDescription.md) objects

 ** [NextToken](#API_ListWebAuthnCredentials_ResponseSyntax) **   <a name="CognitoUserPools-ListWebAuthnCredentials-response-NextToken"></a>
The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`

## Errors
<a name="API_ListWebAuthnCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ForbiddenException **
This exception is thrown when AWS WAF doesn't allow your request based on a web ACL that's associated with your user pool.
 ** message **
The message returned when AWS WAF doesn't allow your request based on a web ACL that's associated with your user pool.
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

 ** PasswordResetRequiredException **
This exception is thrown when a password reset is required.
 ** message **
The message returned when a password reset is required.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_ListWebAuthnCredentials_Examples"></a>

### Example
<a name="API_ListWebAuthnCredentials_Example_1"></a>

The following example request returns details about the one registered passkey for the current user.

#### Sample Request
<a name="API_ListWebAuthnCredentials_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.ListWebAuthnCredentials
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "AccessToken": "eyJra456defEXAMPLE"
}
```

#### Sample Response
<a name="API_ListWebAuthnCredentials_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "Credentials": [
        {
            "AuthenticatorAttachment": "cross-platform",
            "CreatedAt": 1736293876.115,
            "CredentialId": "8LApgk4-lNUFHbhm2w6Und7-uxcc8coJGsPxiogvHoItc64xWQc3r4CEXAMPLE",
            "FriendlyCredentialName": "Roaming passkey",
            "RelyingPartyId": "auth.example.com"
        }
    ]
}
```

## See Also
<a name="API_ListWebAuthnCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/ListWebAuthnCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/ListWebAuthnCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ListWebAuthnCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/ListWebAuthnCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ListWebAuthnCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/ListWebAuthnCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/ListWebAuthnCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/ListWebAuthnCredentials)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/ListWebAuthnCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ListWebAuthnCredentials)
