---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppConversionEvent.html
---

# SendWhatsAppConversionEvent
<a name="API_SendWhatsAppConversionEvent"></a>

Sends a conversion event to Meta's Conversions API for the specified WhatsApp Business Account dataset.

## Request Syntax
<a name="API_SendWhatsAppConversionEvent_RequestSyntax"></a>

```
POST /v1/whatsapp/waba/dataset/events HTTP/1.1
Content-type: application/json

{
   "datasetId": "{{string}}",
   "eventData": {{blob}},
   "id": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendWhatsAppConversionEvent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendWhatsAppConversionEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [datasetId](#API_SendWhatsAppConversionEvent_RequestSyntax) **   <a name="Social-SendWhatsAppConversionEvent-request-datasetId"></a>
The Meta-generated dataset ID to send the event to.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `[0-9]+`
Required: Yes

 ** [eventData](#API_SendWhatsAppConversionEvent_RequestSyntax) **   <a name="Social-SendWhatsAppConversionEvent-request-eventData"></a>
The raw Meta Conversions API event payload as a JSON blob. See [Meta's server event parameters](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event) for the supported format.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 1024000.
Required: Yes

 ** [id](#API_SendWhatsAppConversionEvent_RequestSyntax) **   <a name="Social-SendWhatsAppConversionEvent-request-id"></a>
The ID of the WhatsApp Business Account associated with the dataset, formatted as `waba-01234567890123456789012345678901`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_SendWhatsAppConversionEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "requestId": "string"
}
```

## Response Elements
<a name="API_SendWhatsAppConversionEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [requestId](#API_SendWhatsAppConversionEvent_ResponseSyntax) **   <a name="Social-SendWhatsAppConversionEvent-response-requestId"></a>
The unique identifier for the conversion event request.
Type: String

## Errors
<a name="API_SendWhatsAppConversionEvent_Errors"></a>

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
<a name="API_SendWhatsAppConversionEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/SendWhatsAppConversionEvent)
