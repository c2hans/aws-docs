---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_StartIntegrationAuthorization.html
---

# StartIntegrationAuthorization
<a name="API_StartIntegrationAuthorization"></a>

Starts an OAuth authorization for a new integration and returns the values the caller sends to the provider's authorization endpoint. The authorization belongs to the calling AWS account, can be redeemed once by CreateIntegration from that same account, and expires after ten minutes.

## Request Syntax
<a name="API_StartIntegrationAuthorization_RequestSyntax"></a>

```
POST /integration-authorizations HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "providerType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartIntegrationAuthorization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartIntegrationAuthorization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_StartIntegrationAuthorization_RequestSyntax) **   <a name="continuum-StartIntegrationAuthorization-request-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [providerType](#API_StartIntegrationAuthorization_RequestSyntax) **   <a name="continuum-StartIntegrationAuthorization-request-providerType"></a>
The provider Type.
Type: String
Valid Values: `GITHUB`
Required: Yes

## Response Syntax
<a name="API_StartIntegrationAuthorization_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "codeChallenge": "string",
   "codeChallengeMethod": "string",
   "expiresAt": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_StartIntegrationAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [codeChallenge](#API_StartIntegrationAuthorization_ResponseSyntax) **   <a name="continuum-StartIntegrationAuthorization-response-codeChallenge"></a>
The code Challenge.
Type: String
Length Constraints: Minimum length of 43. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`

 ** [codeChallengeMethod](#API_StartIntegrationAuthorization_ResponseSyntax) **   <a name="continuum-StartIntegrationAuthorization-response-codeChallengeMethod"></a>
The code Challenge Method.
Type: String
Valid Values: `S256`

 ** [expiresAt](#API_StartIntegrationAuthorization_ResponseSyntax) **   <a name="continuum-StartIntegrationAuthorization-response-expiresAt"></a>
The expires At.
Type: Timestamp

 ** [state](#API_StartIntegrationAuthorization_ResponseSyntax) **   <a name="continuum-StartIntegrationAuthorization-response-state"></a>
The state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_StartIntegrationAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_StartIntegrationAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/StartIntegrationAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/StartIntegrationAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/StartIntegrationAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/StartIntegrationAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/StartIntegrationAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/StartIntegrationAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/StartIntegrationAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/StartIntegrationAuthorization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/StartIntegrationAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/StartIntegrationAuthorization)
