---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListTrainedModelInferenceJobs.html
---

# ListTrainedModelInferenceJobs
<a name="API_ListTrainedModelInferenceJobs"></a>

Returns a list of trained model inference jobs that match the request parameters.

## Request Syntax
<a name="API_ListTrainedModelInferenceJobs_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/trained-model-inference-jobs?maxResults={{maxResults}}&nextToken={{nextToken}}&trainedModelArn={{trainedModelArn}}&trainedModelVersionIdentifier={{trainedModelVersionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrainedModelInferenceJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTrainedModelInferenceJobs_RequestSyntax) **   <a name="API-ListTrainedModelInferenceJobs-request-uri-maxResults"></a>
The maximum size of the results that is returned per call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [membershipIdentifier](#API_ListTrainedModelInferenceJobs_RequestSyntax) **   <a name="API-ListTrainedModelInferenceJobs-request-uri-membershipIdentifier"></a>
The membership
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [nextToken](#API_ListTrainedModelInferenceJobs_RequestSyntax) **   <a name="API-ListTrainedModelInferenceJobs-request-uri-nextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10240.

 ** [trainedModelArn](#API_ListTrainedModelInferenceJobs_RequestSyntax) **   <a name="API-ListTrainedModelInferenceJobs-request-uri-trainedModelArn"></a>
The Amazon Resource Name (ARN) of a trained model that was used to create the trained model inference jobs that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`

 ** [trainedModelVersionIdentifier](#API_ListTrainedModelInferenceJobs_RequestSyntax) **   <a name="API-ListTrainedModelInferenceJobs-request-uri-trainedModelVersionIdentifier"></a>
The version identifier of the trained model to filter inference jobs by. When specified, only inference jobs that used this specific version of the trained model are returned.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Request Body
<a name="API_ListTrainedModelInferenceJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrainedModelInferenceJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "trainedModelInferenceJobs": [
      {
         "collaborationIdentifier": "string",
         "configuredModelAlgorithmAssociationArn": "string",
         "createTime": "string",
         "description": "string",
         "logsStatus": "string",
         "logsStatusDetails": "string",
         "membershipIdentifier": "string",
         "metricsStatus": "string",
         "metricsStatusDetails": "string",
         "mlModelInferencePayerAccountId": "string",
         "name": "string",
         "outputConfiguration": {
            "accept": "string",
            "members": [
               {
                  "accountId": "string"
               }
            ]
         },
         "status": "string",
         "trainedModelArn": "string",
         "trainedModelInferenceJobArn": "string",
         "trainedModelVersionIdentifier": "string",
         "updateTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTrainedModelInferenceJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTrainedModelInferenceJobs_ResponseSyntax) **   <a name="API-ListTrainedModelInferenceJobs-response-nextToken"></a>
The token value used to access the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

 ** [trainedModelInferenceJobs](#API_ListTrainedModelInferenceJobs_ResponseSyntax) **   <a name="API-ListTrainedModelInferenceJobs-response-trainedModelInferenceJobs"></a>
Returns the requested trained model inference jobs.
Type: Array of [TrainedModelInferenceJobSummary](API_TrainedModelInferenceJobSummary.md) objects

## Errors
<a name="API_ListTrainedModelInferenceJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_ListTrainedModelInferenceJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ListTrainedModelInferenceJobs)
