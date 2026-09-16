---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppMessageTemplate.html
---

# GetWhatsAppMessageTemplate
<a name="API_GetWhatsAppMessageTemplate"></a>

Retrieves a specific WhatsApp message template.

## Request Syntax
<a name="API_GetWhatsAppMessageTemplate_RequestSyntax"></a>

```
GET /v1/whatsapp/template?id={{id}}&metaTemplateId={{metaTemplateId}}&templateLanguageCode={{templateLanguageCode}}&templateName={{templateName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWhatsAppMessageTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-GetWhatsAppMessageTemplate-request-uri-id"></a>
The ID of the WhatsApp Business Account associated with this template.
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** [metaTemplateId](#API_GetWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-GetWhatsAppMessageTemplate-request-uri-metaTemplateId"></a>
The numeric ID of the template assigned by Meta.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`

 ** [templateLanguageCode](#API_GetWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-GetWhatsAppMessageTemplate-request-uri-templateLanguageCode"></a>
The language code of the message template (for example, `en` or `en_US`). Use together with `templateName` as an alternative to `metaTemplateId` to identify a template.
Length Constraints: Minimum length of 1. Maximum length of 6.

 ** [templateName](#API_GetWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-GetWhatsAppMessageTemplate-request-uri-templateName"></a>
The name of the message template. Use together with `templateLanguageCode` as an alternative to `metaTemplateId` to identify a template.
Length Constraints: Minimum length of 1. Maximum length of 512.

## Request Body
<a name="API_GetWhatsAppMessageTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWhatsAppMessageTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "template": "string"
}
```

## Response Elements
<a name="API_GetWhatsAppMessageTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [template](#API_GetWhatsAppMessageTemplate_ResponseSyntax) **   <a name="Social-GetWhatsAppMessageTemplate-response-template"></a>
The complete template definition as a JSON string (maximum 6000 characters).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6000.

## Errors
<a name="API_GetWhatsAppMessageTemplate_Errors"></a>

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
<a name="API_GetWhatsAppMessageTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/GetWhatsAppMessageTemplate)
