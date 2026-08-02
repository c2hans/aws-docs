---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_GetExclusionsPreview.html
---

# GetExclusionsPreview
<a name="API_GetExclusionsPreview"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Retrieves the exclusions preview (a list of ExclusionPreview objects) specified by the preview token. You can obtain the preview token by running the CreateExclusionsPreview API.

## Request Syntax
<a name="API_GetExclusionsPreview_RequestSyntax"></a>

```
{
   "assessmentTemplateArn": "{{string}}",
   "locale": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "previewToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetExclusionsPreview_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentTemplateArn](#API_GetExclusionsPreview_RequestSyntax) **   <a name="Inspector-GetExclusionsPreview-request-assessmentTemplateArn"></a>
The ARN that specifies the assessment template for which the exclusions preview was requested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [locale](#API_GetExclusionsPreview_RequestSyntax) **   <a name="Inspector-GetExclusionsPreview-request-locale"></a>
The locale into which you want to translate the exclusion's title, description, and recommendation.
Type: String
Valid Values: `EN_US`
Required: No

 ** [maxResults](#API_GetExclusionsPreview_RequestSyntax) **   <a name="Inspector-GetExclusionsPreview-request-maxResults"></a>
You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.
Type: Integer
Required: No

 ** [nextToken](#API_GetExclusionsPreview_RequestSyntax) **   <a name="Inspector-GetExclusionsPreview-request-nextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the GetExclusionsPreviewRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** [previewToken](#API_GetExclusionsPreview_RequestSyntax) **   <a name="Inspector-GetExclusionsPreview-request-previewToken"></a>
The unique identifier associated of the exclusions preview.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_GetExclusionsPreview_ResponseSyntax"></a>

```
{
   "exclusionPreviews": [
      {
         "attributes": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "description": "string",
         "recommendation": "string",
         "scopes": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "title": "string"
      }
   ],
   "nextToken": "string",
   "previewStatus": "string"
}
```

## Response Elements
<a name="API_GetExclusionsPreview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exclusionPreviews](#API_GetExclusionsPreview_ResponseSyntax) **   <a name="Inspector-GetExclusionsPreview-response-exclusionPreviews"></a>
Information about the exclusions included in the preview.
Type: Array of [ExclusionPreview](API_ExclusionPreview.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_GetExclusionsPreview_ResponseSyntax) **   <a name="Inspector-GetExclusionsPreview-response-nextToken"></a>
When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [previewStatus](#API_GetExclusionsPreview_ResponseSyntax) **   <a name="Inspector-GetExclusionsPreview-response-previewStatus"></a>
Specifies the status of the request to generate an exclusions preview.
Type: String
Valid Values: `WORK_IN_PROGRESS | COMPLETED`

## Errors
<a name="API_GetExclusionsPreview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** NoSuchEntityException **
The request was rejected because it referenced an entity that does not exist. The error code describes the entity.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

## See Also
<a name="API_GetExclusionsPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/GetExclusionsPreview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/GetExclusionsPreview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/GetExclusionsPreview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/GetExclusionsPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/GetExclusionsPreview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/GetExclusionsPreview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/GetExclusionsPreview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/GetExclusionsPreview)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/GetExclusionsPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/GetExclusionsPreview)
