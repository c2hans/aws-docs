---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListPipelines.html
---

# ListPipelines
<a name="API_osis_ListPipelines"></a>

Lists all OpenSearch Ingestion pipelines in the current AWS account and Region. For more information, see [Viewing Amazon OpenSearch Ingestion pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/list-pipeline.html).

## Request Syntax
<a name="API_osis_ListPipelines_RequestSyntax"></a>

```
GET /2022-01-01/osis/listPipelines?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_osis_ListPipelines_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_osis_ListPipelines_RequestSyntax) **   <a name="opensearchservice-osis_ListPipelines-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_osis_ListPipelines_RequestSyntax) **   <a name="opensearchservice-osis_ListPipelines-request-uri-NextToken"></a>
If your initial `ListPipelines` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListPipelines` operations, which returns results in the next page.
Length Constraints: Minimum length of 0. Maximum length of 3000.
Pattern: `^([\s\S]*)$`

## Request Body
<a name="API_osis_ListPipelines_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_osis_ListPipelines_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Pipelines": [
      {
         "CreatedAt": number,
         "Destinations": [
            {
               "Endpoint": "string",
               "ServiceName": "string"
            }
         ],
         "LastUpdatedAt": number,
         "MaxUnits": number,
         "MinUnits": number,
         "PipelineArn": "string",
         "PipelineName": "string",
         "Status": "string",
         "StatusReason": {
            "Description": "string"
         },
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_osis_ListPipelines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_osis_ListPipelines_ResponseSyntax) **   <a name="opensearchservice-osis_ListPipelines-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3000.
Pattern: `^([\s\S]*)$`

 ** [Pipelines](#API_osis_ListPipelines_ResponseSyntax) **   <a name="opensearchservice-osis_ListPipelines-response-Pipelines"></a>
A list of all existing Data Prepper pipelines.
Type: Array of [PipelineSummary](API_osis_PipelineSummary.md) objects

## Errors
<a name="API_osis_ListPipelines_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to access the resource.
HTTP Status Code: 403

 ** DisabledOperationException **
Exception is thrown when an operation has been disabled.
HTTP Status Code: 409

 ** InternalException **
The request failed because of an unknown error, exception, or failure (the failure is internal to the service).
HTTP Status Code: 500

 ** InvalidPaginationTokenException **
An invalid pagination token provided in the request.
HTTP Status Code: 400

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_ListPipelines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/ListPipelines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/ListPipelines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/ListPipelines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/ListPipelines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/ListPipelines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/ListPipelines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/ListPipelines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/ListPipelines)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/ListPipelines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/ListPipelines)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
