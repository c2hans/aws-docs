---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListModels.html
---

# ListModels
<a name="API_ListModels"></a>

Lists all available AI models that can be used for workflow execution, including their status and compatibility information.

## Request Syntax
<a name="API_ListModels_RequestSyntax"></a>

```
POST /models?clientCompatibilityVersion={{clientCompatibilityVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListModels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientCompatibilityVersion](#API_ListModels_RequestSyntax) **   <a name="novaact-ListModels-request-uri-clientCompatibilityVersion"></a>
The client compatibility version to filter models by compatibility.
Required: Yes

## Request Body
<a name="API_ListModels_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListModels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "compatibilityInformation": {
      "clientCompatibilityVersion": number,
      "message": "string",
      "supportedModelIds": [ "string" ]
   },
   "modelAliases": [
      {
         "aliasName": "string",
         "latestModelId": "string",
         "resolvedModelId": "string"
      }
   ],
   "modelSummaries": [
      {
         "minimumCompatibilityVersion": number,
         "modelId": "string",
         "modelLifecycle": {
            "status": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [compatibilityInformation](#API_ListModels_ResponseSyntax) **   <a name="novaact-ListModels-response-compatibilityInformation"></a>
Information about client compatibility and supported models.
Type: [CompatibilityInformation](API_CompatibilityInformation.md) object

 ** [modelAliases](#API_ListModels_ResponseSyntax) **   <a name="novaact-ListModels-response-modelAliases"></a>
A list of model aliases that provide stable references to model versions.
Type: Array of [ModelAlias](API_ModelAlias.md) objects

 ** [modelSummaries](#API_ListModels_ResponseSyntax) **   <a name="novaact-ListModels-response-modelSummaries"></a>
A list of available AI models with their status and compatibility information.
Type: Array of [ModelSummary](API_ModelSummary.md) objects

## Errors
<a name="API_ListModels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient permissions to perform this action.
 ** message **
You don't have sufficient permissions to perform this action. Verify your IAM permissions and try again.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
An internal server error occurred. Please try again later.
 ** message **
The service encountered an internal error. Try again later.
 ** reason **
The reason for the internal server error.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 [ThrottlingException](API_ThrottlingException.md)
The request was throttled due to too many requests. Please try again later.
 ** message **
The request was denied due to request throttling.
 ** quotaCode **
The quota code related to the throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the throttled request.
 ** serviceCode **
The service code where throttling occurred.
HTTP Status Code: 429

## See Also
<a name="API_ListModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/nova-act-2025-08-22/ListModels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/nova-act-2025-08-22/ListModels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/ListModels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/nova-act-2025-08-22/ListModels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/ListModels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/nova-act-2025-08-22/ListModels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/nova-act-2025-08-22/ListModels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/nova-act-2025-08-22/ListModels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/nova-act-2025-08-22/ListModels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ListModels)
