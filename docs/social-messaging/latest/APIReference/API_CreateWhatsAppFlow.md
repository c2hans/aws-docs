---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppFlow.html
---

# CreateWhatsAppFlow
<a name="API_CreateWhatsAppFlow"></a>

Creates a new WhatsApp Flow. Flows enable businesses to create rich, interactive forms and experiences that users can complete without leaving WhatsApp. The Flow is created in DRAFT status. If `publish` is set to `true` and a valid `flowJson` is provided, the Flow is published immediately.

## Request Syntax
<a name="API_CreateWhatsAppFlow_RequestSyntax"></a>

```
POST /v1/whatsapp/flow/create HTTP/1.1
Content-type: application/json

{
   "categories": [ "{{string}}" ],
   "cloneFlowId": "{{string}}",
   "endpointUri": "{{string}}",
   "flowJson": {{blob}},
   "flowName": "{{string}}",
   "id": "{{string}}",
   "publish": {{boolean}}
}
```

## URI Request Parameters
<a name="API_CreateWhatsAppFlow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWhatsAppFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [categories](#API_CreateWhatsAppFlow_RequestSyntax) **   <a name="Social-CreateWhatsAppFlow-request-categories"></a>
The categories that classify the business purpose of the Flow. At least one category is required.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 9 items.
Valid Values: `SIGN_UP | SIGN_IN | APPOINTMENT_BOOKING | LEAD_GENERATION | SHOPPING | CONTACT_US | CUSTOMER_SUPPORT | SURVEY | OTHER`
Required: Yes

 ** [cloneFlowId](#API_CreateWhatsAppFlow_RequestSyntax) **   <a name="Social-CreateWhatsAppFlow-request-cloneFlowId"></a>
The ID of an existing Flow within the same WhatsApp Business Account to clone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: No

 ** [endpointUri](#API_CreateWhatsAppFlow_RequestSyntax) **   <a name="Social-CreateWhatsAppFlow-request-endpointUri"></a>
The HTTPS endpoint that Meta calls for a data exchange Flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [flowJson](#API_CreateWhatsAppFlow_RequestSyntax) **   <a name="Social-CreateWhatsAppFlow-request-flowJson"></a>
The Flow JSON definition that describes the screens, components, and logic of the Flow. Maximum size is 10 MB.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 10485760.
Required: No

 ** [flowName](#API_CreateWhatsAppFlow_RequestSyntax) **   <a name="Social-CreateWhatsAppFlow-request-flowName"></a>
The name of the Flow. Must be unique within the WhatsApp Business Account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** [id](#API_CreateWhatsAppFlow_RequestSyntax) **   <a name="Social-CreateWhatsAppFlow-request-id"></a>
The ID of the WhatsApp Business Account to associate with this Flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** [publish](#API_CreateWhatsAppFlow_RequestSyntax) **   <a name="Social-CreateWhatsAppFlow-request-publish"></a>
Set to `true` to publish the Flow immediately after creation. Requires a valid `flowJson` that passes Meta's validation.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateWhatsAppFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowId": "string",
   "validationErrors": [ "string" ]
}
```

## Response Elements
<a name="API_CreateWhatsAppFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowId](#API_CreateWhatsAppFlow_ResponseSyntax) **   <a name="Social-CreateWhatsAppFlow-response-flowId"></a>
The unique identifier assigned to the Flow by Meta.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`

 ** [validationErrors](#API_CreateWhatsAppFlow_ResponseSyntax) **   <a name="Social-CreateWhatsAppFlow-response-validationErrors"></a>
A list of validation errors returned by Meta, if any. Validation errors must be resolved before the Flow can be published.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1048576.

## Errors
<a name="API_CreateWhatsAppFlow_Errors"></a>

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
<a name="API_CreateWhatsAppFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/CreateWhatsAppFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/CreateWhatsAppFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/CreateWhatsAppFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/CreateWhatsAppFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/CreateWhatsAppFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/CreateWhatsAppFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/CreateWhatsAppFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/CreateWhatsAppFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/CreateWhatsAppFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/CreateWhatsAppFlow)
