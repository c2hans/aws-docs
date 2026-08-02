---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DeleteWhatsAppMessageTemplate.html
---

# DeleteWhatsAppMessageTemplate
<a name="API_DeleteWhatsAppMessageTemplate"></a>

Deletes a WhatsApp message template.

## Request Syntax
<a name="API_DeleteWhatsAppMessageTemplate_RequestSyntax"></a>

```
DELETE /v1/whatsapp/template?deleteAllTemplates={{deleteAllLanguages}}&id={{id}}&metaTemplateId={{metaTemplateId}}&templateName={{templateName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWhatsAppMessageTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [deleteAllLanguages](#API_DeleteWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-DeleteWhatsAppMessageTemplate-request-uri-deleteAllLanguages"></a>
If true, deletes all language versions of the template.

 ** [id](#API_DeleteWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-DeleteWhatsAppMessageTemplate-request-uri-id"></a>
The ID of the WhatsApp Business Account associated with this template.
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** [metaTemplateId](#API_DeleteWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-DeleteWhatsAppMessageTemplate-request-uri-metaTemplateId"></a>
The numeric ID of the template assigned by Meta.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`

 ** [templateName](#API_DeleteWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-DeleteWhatsAppMessageTemplate-request-uri-templateName"></a>
The name of the template to delete.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

## Request Body
<a name="API_DeleteWhatsAppMessageTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWhatsAppMessageTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteWhatsAppMessageTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWhatsAppMessageTemplate_Errors"></a>

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
<a name="API_DeleteWhatsAppMessageTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/DeleteWhatsAppMessageTemplate)
