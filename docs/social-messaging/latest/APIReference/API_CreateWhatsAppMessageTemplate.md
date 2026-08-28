---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppMessageTemplate.html
---

# CreateWhatsAppMessageTemplate
<a name="API_CreateWhatsAppMessageTemplate"></a>

Creates a new WhatsApp message template from a custom definition.

**Note**
 AWS End User Messaging Social does not store any WhatsApp message template content.

## Request Syntax
<a name="API_CreateWhatsAppMessageTemplate_RequestSyntax"></a>

```
POST /v1/whatsapp/template/put HTTP/1.1
Content-type: application/json

{
   "id": "{{string}}",
   "templateDefinition": {{blob}}
}
```

## URI Request Parameters
<a name="API_CreateWhatsAppMessageTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWhatsAppMessageTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [id](#API_CreateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-CreateWhatsAppMessageTemplate-request-id"></a>
The ID of the WhatsApp Business Account to associate with this template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** [templateDefinition](#API_CreateWhatsAppMessageTemplate_RequestSyntax) **   <a name="Social-CreateWhatsAppMessageTemplate-request-templateDefinition"></a>
The complete template definition as a JSON blob.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6000.
Required: Yes

## Response Syntax
<a name="API_CreateWhatsAppMessageTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "category": "string",
   "metaTemplateId": "string",
   "templateStatus": "string"
}
```

## Response Elements
<a name="API_CreateWhatsAppMessageTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [category](#API_CreateWhatsAppMessageTemplate_ResponseSyntax) **   <a name="Social-CreateWhatsAppMessageTemplate-response-category"></a>
The category of the template, such as UTILITY or MARKETING.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [metaTemplateId](#API_CreateWhatsAppMessageTemplate_ResponseSyntax) **   <a name="Social-CreateWhatsAppMessageTemplate-response-metaTemplateId"></a>
The numeric ID assigned to the template by Meta.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`

 ** [templateStatus](#API_CreateWhatsAppMessageTemplate_ResponseSyntax) **   <a name="Social-CreateWhatsAppMessageTemplate-response-templateStatus"></a>
The status of the created template, such as PENDING or APPROVED..
Type: String

## Errors
<a name="API_CreateWhatsAppMessageTemplate_Errors"></a>

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
<a name="API_CreateWhatsAppMessageTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/CreateWhatsAppMessageTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
