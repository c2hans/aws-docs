---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SearchMessageTemplates.html
---

# SearchMessageTemplates
<a name="API_amazon-q-connect_SearchMessageTemplates"></a>

Searches for Amazon Q in Connect message templates in the specified knowledge base.

## Request Syntax
<a name="API_amazon-q-connect_SearchMessageTemplates_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/search/messageTemplates?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
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
<a name="API_amazon-q-connect_SearchMessageTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_SearchMessageTemplates_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchMessageTemplates-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [maxResults](#API_amazon-q-connect_SearchMessageTemplates_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchMessageTemplates-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_amazon-q-connect_SearchMessageTemplates_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchMessageTemplates-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_amazon-q-connect_SearchMessageTemplates_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [searchExpression](#API_amazon-q-connect_SearchMessageTemplates_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchMessageTemplates-request-searchExpression"></a>
The search expression for querying the message template.
Type: [MessageTemplateSearchExpression](API_amazon-q-connect_MessageTemplateSearchExpression.md) object
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_SearchMessageTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "results": [
      {
         "channel": "string",
         "channelSubtype": "string",
         "createdTime": "string",
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
         "lastModifiedTime": "string",
         "messageTemplateArn": "string",
         "messageTemplateId": "string",
         "name": "string",
         "sourceConfigurationSummary": { ... },
         "tags": {
            "string" : "string"
         },
         "versionNumber": number
      }
   ]
}
```

## Response Elements
<a name="API_amazon-q-connect_SearchMessageTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_amazon-q-connect_SearchMessageTemplates_ResponseSyntax) **   <a name="connect-amazon-q-connect_SearchMessageTemplates-response-nextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [results](#API_amazon-q-connect_SearchMessageTemplates_ResponseSyntax) **   <a name="connect-amazon-q-connect_SearchMessageTemplates-response-results"></a>
The results of the message template search.
Type: Array of [MessageTemplateSearchResultData](API_amazon-q-connect_MessageTemplateSearchResultData.md) objects

## Errors
<a name="API_amazon-q-connect_SearchMessageTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_SearchMessageTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/SearchMessageTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/SearchMessageTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SearchMessageTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/SearchMessageTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SearchMessageTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/SearchMessageTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/SearchMessageTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/SearchMessageTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/SearchMessageTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SearchMessageTemplates)
