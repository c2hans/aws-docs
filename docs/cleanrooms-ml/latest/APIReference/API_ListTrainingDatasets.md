---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListTrainingDatasets.html
---

# ListTrainingDatasets
<a name="API_ListTrainingDatasets"></a>

Returns a list of training datasets.

## Request Syntax
<a name="API_ListTrainingDatasets_RequestSyntax"></a>

```
GET /training-dataset?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrainingDatasets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTrainingDatasets_RequestSyntax) **   <a name="API-ListTrainingDatasets-request-uri-maxResults"></a>
The maximum size of the results that is returned per call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListTrainingDatasets_RequestSyntax) **   <a name="API-ListTrainingDatasets-request-uri-nextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Request Body
<a name="API_ListTrainingDatasets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrainingDatasets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "trainingDatasets": [
      {
         "createTime": "string",
         "description": "string",
         "name": "string",
         "status": "string",
         "trainingDatasetArn": "string",
         "updateTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTrainingDatasets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTrainingDatasets_ResponseSyntax) **   <a name="API-ListTrainingDatasets-response-nextToken"></a>
The token value used to access the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

 ** [trainingDatasets](#API_ListTrainingDatasets_ResponseSyntax) **   <a name="API-ListTrainingDatasets-response-trainingDatasets"></a>
The training datasets that match the request.
Type: Array of [TrainingDatasetSummary](API_TrainingDatasetSummary.md) objects

## Errors
<a name="API_ListTrainingDatasets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_ListTrainingDatasets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/ListTrainingDatasets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/ListTrainingDatasets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ListTrainingDatasets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/ListTrainingDatasets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ListTrainingDatasets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/ListTrainingDatasets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/ListTrainingDatasets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/ListTrainingDatasets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/ListTrainingDatasets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ListTrainingDatasets)
