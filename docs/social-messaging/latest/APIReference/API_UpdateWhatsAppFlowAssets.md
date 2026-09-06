---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UpdateWhatsAppFlowAssets.html
---

# UpdateWhatsAppFlowAssets
<a name="API_UpdateWhatsAppFlowAssets"></a>

Updates the Flow JSON definition (assets) of a WhatsApp Flow. Updating a published Flow's assets reverts it to DRAFT status, requiring re-publishing.

## Request Syntax
<a name="API_UpdateWhatsAppFlowAssets_RequestSyntax"></a>

```
POST /v1/whatsapp/flow/assets/update HTTP/1.1
Content-type: application/json

{
   "flowId": "{{string}}",
   "flowJson": {{blob}},
   "id": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWhatsAppFlowAssets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateWhatsAppFlowAssets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [flowId](#API_UpdateWhatsAppFlowAssets_RequestSyntax) **   <a name="Social-UpdateWhatsAppFlowAssets-request-flowId"></a>
The unique identifier of the Flow whose assets to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: Yes

 ** [flowJson](#API_UpdateWhatsAppFlowAssets_RequestSyntax) **   <a name="Social-UpdateWhatsAppFlowAssets-request-flowJson"></a>
The updated Flow JSON definition. Maximum size is 10 MB.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 10485760.
Required: Yes

 ** [id](#API_UpdateWhatsAppFlowAssets_RequestSyntax) **   <a name="Social-UpdateWhatsAppFlowAssets-request-id"></a>
The ID of the WhatsApp Business Account associated with this Flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_UpdateWhatsAppFlowAssets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "validationErrors": [ "string" ]
}
```

## Response Elements
<a name="API_UpdateWhatsAppFlowAssets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [validationErrors](#API_UpdateWhatsAppFlowAssets_ResponseSyntax) **   <a name="Social-UpdateWhatsAppFlowAssets-response-validationErrors"></a>
A list of validation errors returned by Meta, if any. Validation errors must be resolved before the Flow can be published.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1048576.

## Errors
<a name="API_UpdateWhatsAppFlowAssets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedByMetaException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** DependencyException **
Thrown when performing an action because a dependency would be broken.
HTTP Status Code: 502

 ** InternalServiceException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found.
HTTP Status Code: 404

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_UpdateWhatsAppFlowAssets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/UpdateWhatsAppFlowAssets)
