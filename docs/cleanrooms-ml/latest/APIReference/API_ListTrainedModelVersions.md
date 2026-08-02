---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListTrainedModelVersions.html
---

# ListTrainedModelVersions
<a name="API_ListTrainedModelVersions"></a>

Returns a list of trained model versions for a specified trained model. This operation allows you to view all versions of a trained model, including information about their status and creation details. You can use this to track the evolution of your trained models and select specific versions for inference or further training.

## Request Syntax
<a name="API_ListTrainedModelVersions_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/trained-models/{{trainedModelArn}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrainedModelVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTrainedModelVersions_RequestSyntax) **   <a name="API-ListTrainedModelVersions-request-uri-maxResults"></a>
The maximum number of trained model versions to return in a single page. The default value is 10, and the maximum value is 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [membershipIdentifier](#API_ListTrainedModelVersions_RequestSyntax) **   <a name="API-ListTrainedModelVersions-request-uri-membershipIdentifier"></a>
The membership identifier for the collaboration that contains the trained model.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [nextToken](#API_ListTrainedModelVersions_RequestSyntax) **   <a name="API-ListTrainedModelVersions-request-uri-nextToken"></a>
The pagination token from a previous `ListTrainedModelVersions` request. Use this token to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10240.

 ** [status](#API_ListTrainedModelVersions_RequestSyntax) **   <a name="API-ListTrainedModelVersions-request-uri-status"></a>
Filter the results to only include trained model versions with the specified status. Valid values include `CREATE_PENDING`, `CREATE_IN_PROGRESS`, `ACTIVE`, `CREATE_FAILED`, and others.
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_FAILED | INACTIVE | CANCEL_PENDING | CANCEL_IN_PROGRESS | CANCEL_FAILED`

 ** [trainedModelArn](#API_ListTrainedModelVersions_RequestSyntax) **   <a name="API-ListTrainedModelVersions-request-uri-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model for which to list versions.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_ListTrainedModelVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrainedModelVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "trainedModels": [
      {
         "collaborationIdentifier": "string",
         "configuredModelAlgorithmAssociationArn": "string",
         "createTime": "string",
         "description": "string",
         "incrementalTrainingDataChannels": [
            {
               "channelName": "string",
               "modelName": "string",
               "versionIdentifier": "string"
            }
         ],
         "membershipIdentifier": "string",
         "mlModelTrainingPayerAccountId": "string",
         "name": "string",
         "status": "string",
         "trainedModelArn": "string",
         "updateTime": "string",
         "versionIdentifier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTrainedModelVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTrainedModelVersions_ResponseSyntax) **   <a name="API-ListTrainedModelVersions-response-nextToken"></a>
The pagination token to use in a subsequent `ListTrainedModelVersions` request to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

 ** [trainedModels](#API_ListTrainedModelVersions_ResponseSyntax) **   <a name="API-ListTrainedModelVersions-response-trainedModels"></a>
A list of trained model versions that match the specified criteria. Each entry contains summary information about a trained model version, including its version identifier, status, and creation details.
Type: Array of [TrainedModelSummary](API_TrainedModelSummary.md) objects

## Errors
<a name="API_ListTrainedModelVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_ListTrainedModelVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/ListTrainedModelVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/ListTrainedModelVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ListTrainedModelVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/ListTrainedModelVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ListTrainedModelVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/ListTrainedModelVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/ListTrainedModelVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/ListTrainedModelVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/ListTrainedModelVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ListTrainedModelVersions)
