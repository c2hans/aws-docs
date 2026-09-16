---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SearchQuickResponses.html
---

# SearchQuickResponses
<a name="API_amazon-q-connect_SearchQuickResponses"></a>

Searches existing Amazon Q in Connect quick responses in an Amazon Q in Connect knowledge base.

## Request Syntax
<a name="API_amazon-q-connect_SearchQuickResponses_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/search/quickResponses?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "attributes": {
      "{{string}}" : "{{string}}"
   },
   "searchExpression": {
      "filters": [
         {
            "includeNoExistence": {{boolean}},
            "name": "{{string}}",
            "operator": "{{string}}",
            "values": [ "{{string}}" ]
         }
      ],
      "orderOnField": {
         "name": "{{string}}",
         "order": "{{string}}"
      },
      "queries": [
         {
            "allowFuzziness": {{boolean}},
            "name": "{{string}}",
            "operator": "{{string}}",
            "priority": "{{string}}",
            "values": [ "{{string}}" ]
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_SearchQuickResponses_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_SearchQuickResponses_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchQuickResponses-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. This should be a QUICK\_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [maxResults](#API_amazon-q-connect_SearchQuickResponses_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchQuickResponses-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_amazon-q-connect_SearchQuickResponses_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchQuickResponses-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Request Body
<a name="API_amazon-q-connect_SearchQuickResponses_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_amazon-q-connect_SearchQuickResponses_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchQuickResponses-request-attributes"></a>
The [user-defined Connect Customer contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/connect-attrib-list.html#user-defined-attributes) to be resolved when search results are returned.
Type: String to string map
Required: No

 ** [searchExpression](#API_amazon-q-connect_SearchQuickResponses_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchQuickResponses-request-searchExpression"></a>
The search expression for querying the quick response.
Type: [QuickResponseSearchExpression](API_amazon-q-connect_QuickResponseSearchExpression.md) object
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_SearchQuickResponses_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "results": [
      {
         "attributesInterpolated": [ "string" ],
         "attributesNotInterpolated": [ "string" ],
         "channels": [ "string" ],
         "contents": {
            "markdown": { ... },
            "plainText": { ... }
         },
         "contentType": "string",
         "createdTime": number,
         "description": "string",
         "groupingConfiguration": {
            "criteria": "string",
            "values": [ "string" ]
         },
         "isActive": boolean,
         "knowledgeBaseArn": "string",
         "knowledgeBaseId": "string",
         "language": "string",
         "lastModifiedBy": "string",
         "lastModifiedTime": number,
         "name": "string",
         "quickResponseArn": "string",
         "quickResponseId": "string",
         "shortcutKey": "string",
         "status": "string",
         "tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_amazon-q-connect_SearchQuickResponses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_amazon-q-connect_SearchQuickResponses_ResponseSyntax) **   <a name="connect-amazon-q-connect_SearchQuickResponses-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [results](#API_amazon-q-connect_SearchQuickResponses_ResponseSyntax) **   <a name="connect-amazon-q-connect_SearchQuickResponses-response-results"></a>
The results of the quick response search.
Type: Array of [QuickResponseSearchResultData](API_amazon-q-connect_QuickResponseSearchResultData.md) objects

## Errors
<a name="API_amazon-q-connect_SearchQuickResponses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** RequestTimeoutException **
The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_SearchQuickResponses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/SearchQuickResponses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/SearchQuickResponses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SearchQuickResponses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/SearchQuickResponses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SearchQuickResponses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/SearchQuickResponses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/SearchQuickResponses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/SearchQuickResponses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/SearchQuickResponses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SearchQuickResponses)
