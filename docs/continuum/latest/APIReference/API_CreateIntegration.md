---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateIntegration.html
---

# CreateIntegration
<a name="API_CreateIntegration"></a>

Creates a new integration with an external source provider. Repeating an identical request with the same clientToken returns the original integrationId, integrationArn, and createdAt. Token records are retained for eight hours after success or terminal failure, including after the integration is deleted; replaying a deleted integration's token does not recreate it. An identical request with a retained terminal failure returns the recorded error.

Reusing a token with different parameters returns ValidationException. A fresh token starts a new create attempt; if the name is already owned by another integration, ConflictException includes that integration's identifier. An attempt still in progress may return ThrottlingException with retryAfterSeconds set to 1; retry with the same token and identical parameters.

GitHub authorization codes are single use. Retry an unresolved attempt with its original token and unchanged parameters first. If the service reports a terminal failure, an expired attempt, or a successful token exchange whose integration could not be saved, restart GitHub authorization with a fresh token and authorization code. The service does not checkpoint provider results for recovery by another request.

## Request Syntax
<a name="API_CreateIntegration_RequestSyntax"></a>

```
POST /integrations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "name": "{{string}}",
   "providerConfiguration": { ... }
}
```

## URI Request Parameters
<a name="API_CreateIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateIntegration_RequestSyntax) **   <a name="continuum-CreateIntegration-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [name](#API_CreateIntegration_RequestSyntax) **   <a name="continuum-CreateIntegration-request-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [providerConfiguration](#API_CreateIntegration_RequestSyntax) **   <a name="continuum-CreateIntegration-request-providerConfiguration"></a>
The provider Configuration.
Type: [ProviderConfiguration](API_ProviderConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateIntegration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": "string",
   "integrationArn": "string",
   "integrationId": "string"
}
```

## Response Elements
<a name="API_CreateIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateIntegration_ResponseSyntax) **   <a name="continuum-CreateIntegration-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [integrationArn](#API_CreateIntegration_ResponseSyntax) **   <a name="continuum-CreateIntegration-response-integrationArn"></a>
The Amazon Resource Name (ARN) of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:integrations/[a-z0-9]+`

 ** [integrationId](#API_CreateIntegration_ResponseSyntax) **   <a name="continuum-CreateIntegration-response-integrationId"></a>
The identifier of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

## Errors
<a name="API_CreateIntegration_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would exceed a service quota. Review your quota and request an increase if needed.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/CreateIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/CreateIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/CreateIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/CreateIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/CreateIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/CreateIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/CreateIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/CreateIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/CreateIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/CreateIntegration)
