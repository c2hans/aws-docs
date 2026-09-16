---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SearchRelevantContent.html
---

# SearchRelevantContent
<a name="API_SearchRelevantContent"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Searches for relevant content in a Amazon Q Business application based on a query. This operation takes a search query text, the Amazon Q Business application identifier, and optional filters (such as content source and maximum results) as input. It returns a list of relevant content items, where each item includes the content text, the unique document identifier, the document title, the document URI, any relevant document attributes, and score attributes indicating the confidence level of the relevance.

## Request Syntax
<a name="API_SearchRelevantContent_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/relevant-content HTTP/1.1
Content-type: application/json

{
   "attributeFilter": {
      "andAllFilters": [
         "AttributeFilter"
      ],
      "containsAll": {
         "name": "{{string}}",
         "value": { ... }
      },
      "containsAny": {
         "name": "{{string}}",
         "value": { ... }
      },
      "equalsTo": {
         "name": "{{string}}",
         "value": { ... }
      },
      "greaterThan": {
         "name": "{{string}}",
         "value": { ... }
      },
      "greaterThanOrEquals": {
         "name": "{{string}}",
         "value": { ... }
      },
      "lessThan": {
         "name": "{{string}}",
         "value": { ... }
      },
      "lessThanOrEquals": {
         "name": "{{string}}",
         "value": { ... }
      },
      "notFilter": "AttributeFilter",
      "orAllFilters": [
         "AttributeFilter"
      ]
   },
   "contentSource": { ... },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "queryText": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchRelevantContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_SearchRelevantContent_RequestSyntax) **   <a name="qbusiness-SearchRelevantContent-request-uri-applicationId"></a>
The unique identifier of the Amazon Q Business application to search.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_SearchRelevantContent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributeFilter](#API_SearchRelevantContent_RequestSyntax) **   <a name="qbusiness-SearchRelevantContent-request-attributeFilter"></a>
Enables filtering of responses based on document attributes or metadata fields.
Type: [AttributeFilter](API_AttributeFilter.md) object
Required: No

 ** [contentSource](#API_SearchRelevantContent_RequestSyntax) **   <a name="qbusiness-SearchRelevantContent-request-contentSource"></a>
The source of content to search in.
Type: [ContentSource](API_ContentSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [maxResults](#API_SearchRelevantContent_RequestSyntax) **   <a name="qbusiness-SearchRelevantContent-request-maxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_SearchRelevantContent_RequestSyntax) **   <a name="qbusiness-SearchRelevantContent-request-nextToken"></a>
The token for the next set of results. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.
Required: No

 ** [queryText](#API_SearchRelevantContent_RequestSyntax) **   <a name="qbusiness-SearchRelevantContent-request-queryText"></a>
The text to search for.
Type: String
Required: Yes

## Response Syntax
<a name="API_SearchRelevantContent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "relevantContent": [
      {
         "content": "string",
         "documentAttributes": [
            {
               "name": "string",
               "value": { ... }
            }
         ],
         "documentId": "string",
         "documentTitle": "string",
         "documentUri": "string",
         "scoreAttributes": {
            "scoreConfidence": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchRelevantContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_SearchRelevantContent_ResponseSyntax) **   <a name="qbusiness-SearchRelevantContent-response-nextToken"></a>
The token to use to retrieve the next set of results, if there are any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [relevantContent](#API_SearchRelevantContent_ResponseSyntax) **   <a name="qbusiness-SearchRelevantContent-response-relevantContent"></a>
The list of relevant content items found.
Type: Array of [RelevantContent](API_RelevantContent.md) objects

## Errors
<a name="API_SearchRelevantContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** LicenseNotFoundException **
You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_SearchRelevantContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/SearchRelevantContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/SearchRelevantContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/SearchRelevantContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/SearchRelevantContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/SearchRelevantContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/SearchRelevantContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/SearchRelevantContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/SearchRelevantContent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/SearchRelevantContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/SearchRelevantContent)
