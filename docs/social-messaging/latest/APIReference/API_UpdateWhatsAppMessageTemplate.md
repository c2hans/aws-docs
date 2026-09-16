---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UpdateWhatsAppMessageTemplate.html
---

# UpdateWhatsAppMessageTemplate
<a name="API_UpdateWhatsAppMessageTemplate"></a>

Updates an existing WhatsApp message template.

## Request Syntax
<a name="API_UpdateWhatsAppMessageTemplate_RequestSyntax"></a>

```
POST /v1/whatsapp/template HTTP/1.1
Content-type: application/json

{
   "ctaUrlLinkTrackingOptedOut": {{boolean}},
   "id": "{{string}}",
   "metaTemplateId": "{{string}}",
   "parameterFormat": "{{string}}",
   "templateCategory": "{{string}}",
   "templateComponents": {{blob}},
   "templateLanguageCode": "{{string}}",
   "templateName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWhatsAppMessageTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateWhatsAppMessageTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ctaUrlLinkTrackingOptedOut](#API_UpdateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-UpdateWhatsAppMessageTemplate-request-ctaUrlLinkTrackingOptedOut"></a>
When true, disables click tracking for call-to-action URL buttons in the template.
Type: Boolean
Required: No

 ** [id](#API_UpdateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-UpdateWhatsAppMessageTemplate-request-id"></a>
The ID of the WhatsApp Business Account associated with this template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** [metaTemplateId](#API_UpdateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-UpdateWhatsAppMessageTemplate-request-metaTemplateId"></a>
The numeric ID of the template assigned by Meta.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: No

 ** [parameterFormat](#API_UpdateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-UpdateWhatsAppMessageTemplate-request-parameterFormat"></a>
The format specification for parameters in the template, this can be either 'named' or 'positional'.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Required: No

 ** [templateCategory](#API_UpdateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-UpdateWhatsAppMessageTemplate-request-templateCategory"></a>
The new category for the template (for example, UTILITY or MARKETING).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [templateComponents](#API_UpdateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-UpdateWhatsAppMessageTemplate-request-templateComponents"></a>
The updated components of the template as a JSON blob (maximum 3000 characters).
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: No

 ** [templateLanguageCode](#API_UpdateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-UpdateWhatsAppMessageTemplate-request-templateLanguageCode"></a>
The language code of the message template (for example, `en` or `en_US`). Use together with `templateName` as an alternative to `metaTemplateId` to identify a template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Required: No

 ** [templateName](#API_UpdateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-UpdateWhatsAppMessageTemplate-request-templateName"></a>
The name of the message template. Use together with `templateLanguageCode` as an alternative to `metaTemplateId` to identify a template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_UpdateWhatsAppMessageTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateWhatsAppMessageTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateWhatsAppMessageTemplate_Errors"></a>

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
<a name="API_UpdateWhatsAppMessageTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/UpdateWhatsAppMessageTemplate)
