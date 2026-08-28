---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppFlow.html
---

# GetWhatsAppFlow
<a name="API_GetWhatsAppFlow"></a>

Retrieves the metadata and status of a WhatsApp Flow, including validation errors, preview information, and health status.

## Request Syntax
<a name="API_GetWhatsAppFlow_RequestSyntax"></a>

```
GET /v1/whatsapp/flow?flowId={{flowId}}&id={{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWhatsAppFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowId](#API_GetWhatsAppFlow_RequestSyntax) **   <a name="Social-GetWhatsAppFlow-request-uri-flowId"></a>
The unique identifier of the Flow to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: Yes

 ** [id](#API_GetWhatsAppFlow_RequestSyntax) **   <a name="Social-GetWhatsAppFlow-request-uri-id"></a>
The ID of the WhatsApp Business Account associated with this Flow.
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

## Request Body
<a name="API_GetWhatsAppFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWhatsAppFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "application": {
      "id": "string",
      "link": "string",
      "name": "string"
   },
   "categories": [ "string" ],
   "dataApiVersion": "string",
   "endpointUri": "string",
   "flowId": "string",
   "flowName": "string",
   "flowStatus": "string",
   "healthStatus": {
      "canSendMessage": "string",
      "entities": [
         {
            "canSendMessage": "string",
            "entityType": "string",
            "id": "string"
         }
      ]
   },
   "jsonVersion": "string",
   "preview": {
      "expiresAt": "string",
      "previewUrl": "string"
   },
   "validationErrors": [ "string" ],
   "whatsAppBusinessAccount": {
      "currency": "string",
      "id": "string",
      "messageTemplateNamespace": "string",
      "name": "string",
      "timezoneId": "string"
   }
}
```

## Response Elements
<a name="API_GetWhatsAppFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [application](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-application"></a>
The Meta application information associated with this Flow.
Type: [MetaFlowApplicationInfo](API_MetaFlowApplicationInfo.md) object

 ** [categories](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-categories"></a>
The categories that classify the business purpose of the Flow.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 9 items.
Valid Values: `SIGN_UP | SIGN_IN | APPOINTMENT_BOOKING | LEAD_GENERATION | SHOPPING | CONTACT_US | CUSTOMER_SUPPORT | SURVEY | OTHER`

 ** [dataApiVersion](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-dataApiVersion"></a>
The data API version for data exchange endpoint Flows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.

 ** [endpointUri](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-endpointUri"></a>
The endpoint URI for data exchange Flows, if configured.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [flowId](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-flowId"></a>
The unique identifier of the Flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`

 ** [flowName](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-flowName"></a>
The name of the Flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [flowStatus](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-flowStatus"></a>
The lifecycle status of the Flow. Valid values are DRAFT, PUBLISHED, DEPRECATED, BLOCKED, and THROTTLED.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.

 ** [healthStatus](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-healthStatus"></a>
The health status information for this Flow from Meta.
Type: [MetaFlowHealthStatus](API_MetaFlowHealthStatus.md) object

 ** [jsonVersion](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-jsonVersion"></a>
The version of the Flow JSON schema used by this Flow (for example, 7.3).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.

 ** [preview](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-preview"></a>
The preview URL and its expiration timestamp for testing the Flow.
Type: [MetaFlowPreviewInfo](API_MetaFlowPreviewInfo.md) object

 ** [validationErrors](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-validationErrors"></a>
A list of validation errors from Meta, if any.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1048576.

 ** [whatsAppBusinessAccount](#API_GetWhatsAppFlow_ResponseSyntax) **   <a name="Social-GetWhatsAppFlow-response-whatsAppBusinessAccount"></a>
The WhatsApp Business Account information from Meta associated with this Flow.
Type: [MetaFlowWhatsAppBusinessAccountInfo](API_MetaFlowWhatsAppBusinessAccountInfo.md) object

## Errors
<a name="API_GetWhatsAppFlow_Errors"></a>

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
<a name="API_GetWhatsAppFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/GetWhatsAppFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/GetWhatsAppFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/GetWhatsAppFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/GetWhatsAppFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/GetWhatsAppFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/GetWhatsAppFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/GetWhatsAppFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/GetWhatsAppFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/GetWhatsAppFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/GetWhatsAppFlow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
