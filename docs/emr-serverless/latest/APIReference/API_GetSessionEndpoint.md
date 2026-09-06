---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetSessionEndpoint.html
---

# GetSessionEndpoint
<a name="API_GetSessionEndpoint"></a>

Returns the session endpoint URL and a time-limited authentication token for the specified session. Use the endpoint and token to connect a client to the session. Call this operation again when the authentication token expires to obtain a new token.

## Request Syntax
<a name="API_GetSessionEndpoint_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/sessions/{{sessionId}}/endpoint HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSessionEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetSessionEndpoint_RequestSyntax) **   <a name="emrserverless-GetSessionEndpoint-request-uri-applicationId"></a>
The ID of the application that the session belongs to.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [sessionId](#API_GetSessionEndpoint_RequestSyntax) **   <a name="emrserverless-GetSessionEndpoint-request-uri-sessionId"></a>
The ID of the session.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_GetSessionEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSessionEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "authToken": "string",
   "authTokenExpiresAt": number,
   "endpoint": "string",
   "sessionId": "string"
}
```

## Response Elements
<a name="API_GetSessionEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_GetSessionEndpoint_ResponseSyntax) **   <a name="emrserverless-GetSessionEndpoint-response-applicationId"></a>
The output contains the ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [authToken](#API_GetSessionEndpoint_ResponseSyntax) **   <a name="emrserverless-GetSessionEndpoint-response-authToken"></a>
The authentication token for connecting to the session endpoint. Call `GetSessionEndpoint` again to obtain a new token before it expires.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.

 ** [authTokenExpiresAt](#API_GetSessionEndpoint_ResponseSyntax) **   <a name="emrserverless-GetSessionEndpoint-response-authTokenExpiresAt"></a>
The expiration time of the authentication token.
Type: Timestamp

 ** [endpoint](#API_GetSessionEndpoint_ResponseSyntax) **   <a name="emrserverless-GetSessionEndpoint-response-endpoint"></a>
The endpoint URL for connecting to the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [sessionId](#API_GetSessionEndpoint_ResponseSyntax) **   <a name="emrserverless-GetSessionEndpoint-response-sessionId"></a>
The output contains the ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

## Errors
<a name="API_GetSessionEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetSessionEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/GetSessionEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/GetSessionEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/GetSessionEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/GetSessionEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/GetSessionEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/GetSessionEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/GetSessionEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/GetSessionEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/GetSessionEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/GetSessionEndpoint)
