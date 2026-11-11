---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateBearerToken.html
---

# CreateBearerToken
<a name="API_dataplane-signin_CreateBearerToken"></a>

Creates a bearer token that represents your IAM credentials, which you can use to access a supported AWS service.

## Request Syntax
<a name="API_dataplane-signin_CreateBearerToken_RequestSyntax"></a>

```
POST /v1/token?x-amz-token-request-type=bearer HTTP/1.1
Content-type: application/json

{
   "duration": {{number}},
   "grant\_type": "{{string}}",
   "resource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_dataplane-signin_CreateBearerToken_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_dataplane-signin_CreateBearerToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [duration](#API_dataplane-signin_CreateBearerToken_RequestSyntax) **   <a name="signin-dataplane-signin_CreateBearerToken-request-duration"></a>
The token lifetime that you request, in seconds. The minimum is 300 (5 minutes). The maximum is the limit allowed for the service, currently 43200 (12 hours). If you omit this parameter, the token is valid for 12 hours.
Type: Integer
Valid Range: Minimum value of 300.
Required: No

 ** [grant\_type](#API_dataplane-signin_CreateBearerToken_RequestSyntax) **   <a name="signin-dataplane-signin_CreateBearerToken-request-grant_type"></a>
The grant type. Must be `client_credentials`.
Type: String
Pattern: `client_credentials`
Required: Yes

 ** [resource](#API_dataplane-signin_CreateBearerToken_RequestSyntax) **   <a name="signin-dataplane-signin_CreateBearerToken-request-resource"></a>
The AWS service that the bearer token is for.
Example: `ecr.amazonaws.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_dataplane-signin_CreateBearerToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "access\_token": "string",
   "expires\_in": number,
   "token\_type": "string"
}
```

## Response Elements
<a name="API_dataplane-signin_CreateBearerToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [access\_token](#API_dataplane-signin_CreateBearerToken_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateBearerToken-response-access_token"></a>
The bearer token. Present it to the AWS service that you named in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [expires\_in](#API_dataplane-signin_CreateBearerToken_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateBearerToken-response-expires_in"></a>
The token lifetime, in seconds.
Type: Integer
Valid Range: Minimum value of 1.

 ** [token\_type](#API_dataplane-signin_CreateBearerToken_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateBearerToken-response-token_type"></a>
The token type. Always `Bearer`.
Type: String
Pattern: `Bearer`

## Errors
<a name="API_dataplane-signin_CreateBearerToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed because of an internal server error.
HTTP Status Code: 500

 ** TooManyRequestsError **
The request failed because you exceeded the request rate limit for this operation.
HTTP Status Code: 429

 ** ValidationException **
The request failed because it contains a malformed, missing, or invalid parameter.
HTTP Status Code: 400

## See Also
<a name="API_dataplane-signin_CreateBearerToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signin-2023-01-01/CreateBearerToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signin-2023-01-01/CreateBearerToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/CreateBearerToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signin-2023-01-01/CreateBearerToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/CreateBearerToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signin-2023-01-01/CreateBearerToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signin-2023-01-01/CreateBearerToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signin-2023-01-01/CreateBearerToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signin-2023-01-01/CreateBearerToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/CreateBearerToken)
