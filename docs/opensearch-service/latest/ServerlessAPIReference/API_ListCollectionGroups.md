---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollectionGroups.html
---

# ListCollectionGroups
<a name="API_ListCollectionGroups"></a>

Returns a list of collection groups. For more information, see [Creating and managing Amazon OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html).

## Request Syntax
<a name="API_ListCollectionGroups_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCollectionGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListCollectionGroups_RequestSyntax) **   <a name="opensearchserverless-ListCollectionGroups-request-maxResults"></a>
The maximum number of results to return. Default is 20. You can use `nextToken` to get the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListCollectionGroups_RequestSyntax) **   <a name="opensearchserverless-ListCollectionGroups-request-nextToken"></a>
If your initial `ListCollectionGroups` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListCollectionGroups` operations, which returns results in the next page.
Type: String
Required: No

## Response Syntax
<a name="API_ListCollectionGroups_ResponseSyntax"></a>

```
{
   "collectionGroupSummaries": [
      {
         "arn": "string",
         "capacityLimits": {
            "maxIndexingCapacityInOCU": number,
            "maxSearchCapacityInOCU": number,
            "minIndexingCapacityInOCU": number,
            "minSearchCapacityInOCU": number
         },
         "createdDate": number,
         "generation": "string",
         "id": "string",
         "name": "string",
         "numberOfCollections": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCollectionGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collectionGroupSummaries](#API_ListCollectionGroups_ResponseSyntax) **   <a name="opensearchserverless-ListCollectionGroups-response-collectionGroupSummaries"></a>
Details about each collection group.
Type: Array of [CollectionGroupSummary](API_CollectionGroupSummary.md) objects

 ** [nextToken](#API_ListCollectionGroups_ResponseSyntax) **   <a name="opensearchserverless-ListCollectionGroups-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListCollectionGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_ListCollectionGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/ListCollectionGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/ListCollectionGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/ListCollectionGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/ListCollectionGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/ListCollectionGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/ListCollectionGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/ListCollectionGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/ListCollectionGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/ListCollectionGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/ListCollectionGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
