---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListIngestionStreams.html
---

# ListIngestionStreams
<a name="API_ListIngestionStreams"></a>

Returns a list of ingestion streams in a collection.

## Request Syntax
<a name="API_ListIngestionStreams_RequestSyntax"></a>

```
{
   "collectionId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListIngestionStreams_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [collectionId](#API_ListIngestionStreams_RequestSyntax) **   <a name="opensearchserverless-ListIngestionStreams-request-collectionId"></a>
The unique identifier of the collection to list ingestion streams for.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [maxResults](#API_ListIngestionStreams_RequestSyntax) **   <a name="opensearchserverless-ListIngestionStreams-request-maxResults"></a>
The maximum number of results to return. Valid values are 1–100. If you don't specify a value, the default is 100. You can use `nextToken` to get the next page of results.
A response can contain fewer results than `maxResults`, or no results, and still include a `nextToken`. To retrieve all results, continue to make the call with the returned `nextToken` until no `nextToken` is returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListIngestionStreams_RequestSyntax) **   <a name="opensearchserverless-ListIngestionStreams-request-nextToken"></a>
If your initial `ListIngestionStreams` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListIngestionStreams` operations, which returns results in the next page.
Type: String
Required: No

## Response Syntax
<a name="API_ListIngestionStreams_ResponseSyntax"></a>

```
{
   "ingestionStreamSummaries": [
      {
         "arn": "string",
         "createdAt": number,
         "indexName": "string",
         "ingestionStreamId": "string",
         "ingestionStreamName": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListIngestionStreams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestionStreamSummaries](#API_ListIngestionStreams_ResponseSyntax) **   <a name="opensearchserverless-ListIngestionStreams-response-ingestionStreamSummaries"></a>
Summary information about each ingestion stream.
Type: Array of [IngestionStreamSummary](API_IngestionStreamSummary.md) objects

 ** [nextToken](#API_ListIngestionStreams_ResponseSyntax) **   <a name="opensearchserverless-ListIngestionStreams-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListIngestionStreams_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when accessing or deleting a resource that does not exist.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_ListIngestionStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/ListIngestionStreams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/ListIngestionStreams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/ListIngestionStreams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/ListIngestionStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/ListIngestionStreams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/ListIngestionStreams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/ListIngestionStreams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/ListIngestionStreams)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/ListIngestionStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/ListIngestionStreams)
