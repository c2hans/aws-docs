---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListWhatsAppMessageTemplates.html
---

# ListWhatsAppMessageTemplates
<a name="API_ListWhatsAppMessageTemplates"></a>

Lists WhatsApp message templates for a specific WhatsApp Business Account.

## Request Syntax
<a name="API_ListWhatsAppMessageTemplates_RequestSyntax"></a>

```
GET /v1/whatsapp/template/list?id={{id}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWhatsAppMessageTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_ListWhatsAppMessageTemplates_RequestSyntax) **   <a name="Social-ListWhatsAppMessageTemplates-request-uri-id"></a>
The ID of the WhatsApp Business Account to list templates for.
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** [maxResults](#API_ListWhatsAppMessageTemplates_RequestSyntax) **   <a name="Social-ListWhatsAppMessageTemplates-request-uri-maxResults"></a>
The maximum number of results to return per page (1-100).
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListWhatsAppMessageTemplates_RequestSyntax) **   <a name="Social-ListWhatsAppMessageTemplates-request-uri-nextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 600.

## Request Body
<a name="API_ListWhatsAppMessageTemplates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWhatsAppMessageTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "templates": [
      {
         "metaTemplateId": "string",
         "templateCategory": "string",
         "templateLanguage": "string",
         "templateName": "string",
         "templateQualityScore": "string",
         "templateStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWhatsAppMessageTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWhatsAppMessageTemplates_ResponseSyntax) **   <a name="Social-ListWhatsAppMessageTemplates-response-nextToken"></a>
The token to retrieve the next page of results, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.

 ** [templates](#API_ListWhatsAppMessageTemplates_ResponseSyntax) **   <a name="Social-ListWhatsAppMessageTemplates-response-templates"></a>
A list of template summaries.
Type: Array of [TemplateSummary](API_TemplateSummary.md) objects

## Errors
<a name="API_ListWhatsAppMessageTemplates_Errors"></a>

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
<a name="API_ListWhatsAppMessageTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/ListWhatsAppMessageTemplates)
