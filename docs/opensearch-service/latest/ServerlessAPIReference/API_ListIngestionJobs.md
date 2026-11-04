---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListIngestionJobs.html
---

# ListIngestionJobs
<a name="API_ListIngestionJobs"></a>

Returns a list of ingestion jobs in a collection.

## Request Syntax
<a name="API_ListIngestionJobs_RequestSyntax"></a>

```
{
   "collectionId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListIngestionJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [collectionId](#API_ListIngestionJobs_RequestSyntax) **   <a name="opensearchserverless-ListIngestionJobs-request-collectionId"></a>
The unique identifier of the collection to list ingestion jobs for.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [maxResults](#API_ListIngestionJobs_RequestSyntax) **   <a name="opensearchserverless-ListIngestionJobs-request-maxResults"></a>
The maximum number of results to return. Valid values are 1–100. If you don't specify a value, the default is 100. You can use `nextToken` to get the next page of results.
A response can contain fewer results than `maxResults`, or no results, and still include a `nextToken`. To retrieve all results, continue to make the call with the returned `nextToken` until no `nextToken` is returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListIngestionJobs_RequestSyntax) **   <a name="opensearchserverless-ListIngestionJobs-request-nextToken"></a>
If your initial `ListIngestionJobs` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListIngestionJobs` operations, which returns results in the next page.
Type: String
Required: No

## Response Syntax
<a name="API_ListIngestionJobs_ResponseSyntax"></a>

```
{
   "ingestionJobSummaries": [
      {
         "arn": "string",
         "createdAt": number,
         "indexName": "string",
         "ingestionJobId": "string",
         "ingestionJobName": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListIngestionJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestionJobSummaries](#API_ListIngestionJobs_ResponseSyntax) **   <a name="opensearchserverless-ListIngestionJobs-response-ingestionJobSummaries"></a>
Summary information about each ingestion job.
Type: Array of [IngestionJobSummary](API_IngestionJobSummary.md) objects

 ** [nextToken](#API_ListIngestionJobs_ResponseSyntax) **   <a name="opensearchserverless-ListIngestionJobs-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListIngestionJobs_Errors"></a>

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
<a name="API_ListIngestionJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/ListIngestionJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/ListIngestionJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/ListIngestionJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/ListIngestionJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/ListIngestionJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/ListIngestionJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/ListIngestionJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/ListIngestionJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/ListIngestionJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/ListIngestionJobs)
