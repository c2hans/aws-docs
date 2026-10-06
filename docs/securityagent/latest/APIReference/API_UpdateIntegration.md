---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateIntegration.html
---

# UpdateIntegration
<a name="API_UpdateIntegration"></a>

Creates an integration's webhook, or rotates the HMAC signing secret of an existing one. The secret is returned only once, in this response, and cannot be retrieved again.

## Request Syntax
<a name="API_UpdateIntegration_RequestSyntax"></a>

```
POST /UpdateIntegration HTTP/1.1
Content-type: application/json

{
   "integrationId": "{{string}}",
   "webhookAction": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [integrationId](#API_UpdateIntegration_RequestSyntax) **   <a name="securityagent-UpdateIntegration-request-integrationId"></a>
The ID of the integration whose webhook you want to create or rotate.
Type: String
Required: Yes

 ** [webhookAction](#API_UpdateIntegration_RequestSyntax) **   <a name="securityagent-UpdateIntegration-request-webhookAction"></a>
The action to perform on the integration's webhook.
Type: String
Valid Values: `CREATE_IF_ABSENT | ROTATE`
Required: Yes

## Response Syntax
<a name="API_UpdateIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "integrationId": "string",
   "secret": "string",
   "webhookUrl": "string"
}
```

## Response Elements
<a name="API_UpdateIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [integrationId](#API_UpdateIntegration_ResponseSyntax) **   <a name="securityagent-UpdateIntegration-response-integrationId"></a>
The ID of the integration.
Type: String

 ** [secret](#API_UpdateIntegration_ResponseSyntax) **   <a name="securityagent-UpdateIntegration-response-secret"></a>
The HMAC signing secret for the webhook. Returned only once, in this response; it is never returned again.
Type: String

 ** [webhookUrl](#API_UpdateIntegration_ResponseSyntax) **   <a name="securityagent-UpdateIntegration-response-webhookUrl"></a>
The payload URL to configure on your provider instance. Returned when a webhook is created; unchanged by a rotate.
Type: String

## Errors
<a name="API_UpdateIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
Error description.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** message **
Error description.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
 ** message **
Error description.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.
 ** message **
Error description.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Error description.
 ** quotaCode **
Quota code for throttling limit.
 ** serviceCode **
Service code for throttling limit.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered during validation.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_UpdateIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdateIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdateIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdateIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdateIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdateIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdateIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdateIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateIntegration)
