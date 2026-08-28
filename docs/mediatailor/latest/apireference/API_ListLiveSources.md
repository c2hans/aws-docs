---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListLiveSources.html
---

# ListLiveSources
<a name="API_ListLiveSources"></a>

Lists the live sources contained in a source location. A source represents a piece of content.

## Request Syntax
<a name="API_ListLiveSources_RequestSyntax"></a>

```
GET /sourceLocation/{{SourceLocationName}}/liveSources?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLiveSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListLiveSources_RequestSyntax) **   <a name="mediatailor-ListLiveSources-request-uri-MaxResults"></a>
The maximum number of live sources that you want MediaTailor to return in response to the current request. If there are more than `MaxResults` live sources, use the value of `NextToken` in the response to get the next page of results.
The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than `MaxResults` items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the `NextToken` value from each response until the response no longer includes a `NextToken` value.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListLiveSources_RequestSyntax) **   <a name="mediatailor-ListLiveSources-request-uri-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
For the first `ListLiveSources` request, omit this value. For subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request. Continue making requests until the response no longer includes a `NextToken` value, which indicates that all results have been retrieved.

 ** [SourceLocationName](#API_ListLiveSources_RequestSyntax) **   <a name="mediatailor-ListLiveSources-request-uri-SourceLocationName"></a>
The name of the source location associated with this Live Sources list.
Required: Yes

## Request Body
<a name="API_ListLiveSources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLiveSources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Arn": "string",
         "CreationTime": number,
         "HttpPackageConfigurations": [
            {
               "Path": "string",
               "SourceGroup": "string",
               "Type": "string"
            }
         ],
         "LastModifiedTime": number,
         "LiveSourceName": "string",
         "SourceLocationName": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLiveSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListLiveSources_ResponseSyntax) **   <a name="mediatailor-ListLiveSources-response-Items"></a>
Lists the live sources.
Type: Array of [LiveSource](API_LiveSource.md) objects

 ** [NextToken](#API_ListLiveSources_ResponseSyntax) **   <a name="mediatailor-ListLiveSources-response-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
Type: String

## Errors
<a name="API_ListLiveSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListLiveSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/ListLiveSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/ListLiveSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ListLiveSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/ListLiveSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ListLiveSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/ListLiveSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/ListLiveSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/ListLiveSources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/ListLiveSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ListLiveSources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
