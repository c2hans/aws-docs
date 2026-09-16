---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateIntegratedResources.html
---

# UpdateIntegratedResources
<a name="API_UpdateIntegratedResources"></a>

Updates the integrated resources for an agent space, including their capabilities.

## Request Syntax
<a name="API_UpdateIntegratedResources_RequestSyntax"></a>

```
POST /UpdateIntegratedResources HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "integrationId": "{{string}}",
   "items": [
      {
         "capabilities": { ... },
         "resource": { ... }
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateIntegratedResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateIntegratedResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_UpdateIntegratedResources_RequestSyntax) **   <a name="securityagent-UpdateIntegratedResources-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [integrationId](#API_UpdateIntegratedResources_RequestSyntax) **   <a name="securityagent-UpdateIntegratedResources-request-integrationId"></a>
The unique identifier of the integration.
Type: String
Required: Yes

 ** [items](#API_UpdateIntegratedResources_RequestSyntax) **   <a name="securityagent-UpdateIntegratedResources-request-items"></a>
The list of integrated resource items to update.
Type: Array of [IntegratedResourceInputItem](API_IntegratedResourceInputItem.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateIntegratedResources_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateIntegratedResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateIntegratedResources_Errors"></a>

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
<a name="API_UpdateIntegratedResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdateIntegratedResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdateIntegratedResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateIntegratedResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdateIntegratedResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateIntegratedResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdateIntegratedResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdateIntegratedResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdateIntegratedResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdateIntegratedResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateIntegratedResources)
