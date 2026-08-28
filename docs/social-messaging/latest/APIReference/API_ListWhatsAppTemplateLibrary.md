---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListWhatsAppTemplateLibrary.html
---

# ListWhatsAppTemplateLibrary
<a name="API_ListWhatsAppTemplateLibrary"></a>

Lists templates available in Meta's template library for WhatsApp messaging.

## Request Syntax
<a name="API_ListWhatsAppTemplateLibrary_RequestSyntax"></a>

```
POST /v1/whatsapp/template/library?id={{id}} HTTP/1.1
Content-type: application/json

{
   "filters": {
      "{{string}}" : "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWhatsAppTemplateLibrary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_ListWhatsAppTemplateLibrary_RequestSyntax) **   <a name="Social-ListWhatsAppTemplateLibrary-request-uri-id"></a>
The ID of the WhatsApp Business Account to list library templates for.
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

## Request Body
<a name="API_ListWhatsAppTemplateLibrary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListWhatsAppTemplateLibrary_RequestSyntax) **   <a name="Social-ListWhatsAppTemplateLibrary-request-filters"></a>
Map of filters to apply (searchKey, topic, usecase, industry, language).
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Value Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [maxResults](#API_ListWhatsAppTemplateLibrary_RequestSyntax) **   <a name="Social-ListWhatsAppTemplateLibrary-request-maxResults"></a>
The maximum number of results to return per page (1-100).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListWhatsAppTemplateLibrary_RequestSyntax) **   <a name="Social-ListWhatsAppTemplateLibrary-request-nextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.
Required: No

## Response Syntax
<a name="API_ListWhatsAppTemplateLibrary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "metaLibraryTemplates": [
      {
         "templateBody": "string",
         "templateBodyExampleParams": [ "string" ],
         "templateButtons": [
            {
               "otpType": "string",
               "phoneNumber": "string",
               "supportedApps": [
                  {
                     "string" : "string"
                  }
               ],
               "text": "string",
               "type": "string",
               "url": "string",
               "zeroTapTermsAccepted": boolean
            }
         ],
         "templateCategory": "string",
         "templateHeader": "string",
         "templateId": "string",
         "templateIndustry": [ "string" ],
         "templateLanguage": "string",
         "templateName": "string",
         "templateTopic": "string",
         "templateUseCase": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListWhatsAppTemplateLibrary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metaLibraryTemplates](#API_ListWhatsAppTemplateLibrary_ResponseSyntax) **   <a name="Social-ListWhatsAppTemplateLibrary-response-metaLibraryTemplates"></a>
A list of templates from Meta's library.
Type: Array of [MetaLibraryTemplateDefinition](API_MetaLibraryTemplateDefinition.md) objects

 ** [nextToken](#API_ListWhatsAppTemplateLibrary_ResponseSyntax) **   <a name="Social-ListWhatsAppTemplateLibrary-response-nextToken"></a>
The token to retrieve the next page of results, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.

## Errors
<a name="API_ListWhatsAppTemplateLibrary_Errors"></a>

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
<a name="API_ListWhatsAppTemplateLibrary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/ListWhatsAppTemplateLibrary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
