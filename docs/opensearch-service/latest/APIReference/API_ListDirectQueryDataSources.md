---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDirectQueryDataSources.html
---

# ListDirectQueryDataSources
<a name="API_ListDirectQueryDataSources"></a>

 Lists an inventory of all the direct query data sources that you have configured within Amazon OpenSearch Service.

## Request Syntax
<a name="API_ListDirectQueryDataSources_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/directQueryDataSource?nexttoken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDirectQueryDataSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_ListDirectQueryDataSources_RequestSyntax) **   <a name="opensearchservice-ListDirectQueryDataSources-request-uri-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.

## Request Body
<a name="API_ListDirectQueryDataSources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDirectQueryDataSources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DirectQueryDataSources": [
      {
         "DataSourceArn": "string",
         "DataSourceName": "string",
         "DataSourceType": { ... },
         "Description": "string",
         "OpenSearchArns": [ "string" ],
         "TagList": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDirectQueryDataSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectQueryDataSources](#API_ListDirectQueryDataSources_ResponseSyntax) **   <a name="opensearchservice-ListDirectQueryDataSources-response-DirectQueryDataSources"></a>
 A list of the direct query data sources that are returned by the `ListDirectQueryDataSources` API operation.
Type: Array of [DirectQueryDataSource](API_DirectQueryDataSource.md) objects

 ** [NextToken](#API_ListDirectQueryDataSources_ResponseSyntax) **   <a name="opensearchservice-ListDirectQueryDataSources-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListDirectQueryDataSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_ListDirectQueryDataSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListDirectQueryDataSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListDirectQueryDataSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListDirectQueryDataSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListDirectQueryDataSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListDirectQueryDataSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListDirectQueryDataSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListDirectQueryDataSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListDirectQueryDataSources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListDirectQueryDataSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListDirectQueryDataSources)
