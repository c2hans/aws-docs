---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListDatasets.html
---

# ListDatasets

 Lists all datasets in the caller's account, paginated.

## Request Syntax
<a name="API_ListDatasets_RequestSyntax"></a>

```
POST /datasets/list HTTP/1.1
Content-type: application/json

{
   "filter": {
      "exampleCountByField": [
         {
            "anyOf": [ "{{string}}" ],
            "max": {{number}},
            "min": {{number}}
         }
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListDatasets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDatasets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListDatasets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasets-request-filter"></a>
 A filter to apply to the datasets.
Type: [ListDatasetsFilter](API_ListDatasetsFilter.md) object
Required: No

 ** [maxResults](#API_ListDatasets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasets-request-maxResults"></a>
 The maximum number of datasets to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListDatasets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasets-request-nextToken"></a>
 The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListDatasets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasets": [
      {
         "createdAt": number,
         "datasetArn": "string",
         "datasetId": "string",
         "datasetName": "string",
         "description": "string",
         "draftStatus": "string",
         "exampleCount": number,
         "exampleCountByField": {
            "actorProfile": number,
            "input": number,
            "turns": number
         },
         "schemaType": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasets](#API_ListDatasets_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasets-response-datasets"></a>
 The list of datasets.
Type: Array of [DatasetSummary](API_DatasetSummary.md) objects

 ** [nextToken](#API_ListDatasets_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasets-response-nextToken"></a>
 The token for the next page of results, or null if there are no more results.
Type: String

## Errors
<a name="API_ListDatasets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This exception is thrown when a request is denied per access permissions
HTTP Status Code: 403

 ** InternalServerException **
This exception is thrown if there was an unexpected error during processing of request
HTTP Status Code: 500

 ** ThrottlingException **
This exception is thrown when the number of requests exceeds the limit
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_ListDatasets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListDatasets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListDatasets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListDatasets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListDatasets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListDatasets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListDatasets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListDatasets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListDatasets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListDatasets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListDatasets)
