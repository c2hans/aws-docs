---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetCollaborationTrainedModel.html
---

# GetCollaborationTrainedModel
<a name="API_GetCollaborationTrainedModel"></a>

Returns information about a trained model in a collaboration.

## Request Syntax
<a name="API_GetCollaborationTrainedModel_RequestSyntax"></a>

```
GET /collaborations/{{collaborationIdentifier}}/trained-models/{{trainedModelArn}}?versionIdentifier={{versionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCollaborationTrainedModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationIdentifier](#API_GetCollaborationTrainedModel_RequestSyntax) **   <a name="API-GetCollaborationTrainedModel-request-uri-collaborationIdentifier"></a>
The collaboration ID that contains the trained model that you want to return information about.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [trainedModelArn](#API_GetCollaborationTrainedModel_RequestSyntax) **   <a name="API-GetCollaborationTrainedModel-request-uri-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model that you want to return information about.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [versionIdentifier](#API_GetCollaborationTrainedModel_RequestSyntax) **   <a name="API-GetCollaborationTrainedModel-request-uri-versionIdentifier"></a>
The version identifier of the trained model to retrieve. If not specified, the operation returns information about the latest version of the trained model.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Request Body
<a name="API_GetCollaborationTrainedModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCollaborationTrainedModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaborationIdentifier": "string",
   "configuredModelAlgorithmAssociationArn": "string",
   "createTime": "string",
   "creatorAccountId": "string",
   "description": "string",
   "incrementalTrainingDataChannels": [
      {
         "channelName": "string",
         "modelName": "string",
         "versionIdentifier": "string"
      }
   ],
   "logsStatus": "string",
   "logsStatusDetails": "string",
   "membershipIdentifier": "string",
   "metricsStatus": "string",
   "metricsStatusDetails": "string",
   "mlModelTrainingPayerAccountId": "string",
   "name": "string",
   "resourceConfig": {
      "instanceCount": number,
      "instanceType": "string",
      "volumeSizeInGB": number
   },
   "status": "string",
   "statusDetails": {
      "message": "string",
      "statusCode": "string"
   },
   "stoppingCondition": {
      "maxRuntimeInSeconds": number
   },
   "trainedModelArn": "string",
   "trainingContainerImageDigest": "string",
   "trainingInputMode": "string",
   "updateTime": "string",
   "versionIdentifier": "string"
}
```

## Response Elements
<a name="API_GetCollaborationTrainedModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationIdentifier](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the trained model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [configuredModelAlgorithmAssociationArn](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association that was used to create this trained model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`

 ** [createTime](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-createTime"></a>
The time at which the trained model was created.
Type: Timestamp

 ** [creatorAccountId](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-creatorAccountId"></a>
The account ID of the member that created the trained model.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [description](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-description"></a>
The description of the trained model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [incrementalTrainingDataChannels](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-incrementalTrainingDataChannels"></a>
Information about the incremental training data channels used to create this version of the trained model. This includes details about the base model that was used for incremental training and the channel configuration.
Type: Array of [IncrementalTrainingDataChannelOutput](API_IncrementalTrainingDataChannelOutput.md) objects
Array Members: Fixed number of 1 item.

 ** [logsStatus](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-logsStatus"></a>
Status information for the logs.
Type: String
Valid Values: `PUBLISH_SUCCEEDED | PUBLISH_FAILED`

 ** [logsStatusDetails](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-logsStatusDetails"></a>
Details about the status information for the logs.
Type: String

 ** [membershipIdentifier](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-membershipIdentifier"></a>
The membership ID of the member that created the trained model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [metricsStatus](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-metricsStatus"></a>
The status of the model metrics.
Type: String
Valid Values: `PUBLISH_SUCCEEDED | PUBLISH_FAILED`

 ** [metricsStatusDetails](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-metricsStatusDetails"></a>
Details about the status information for the model metrics.
Type: String

 ** [mlModelTrainingPayerAccountId](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-mlModelTrainingPayerAccountId"></a>
The account ID of the member that is responsible for paying for model training costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [name](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-name"></a>
The name of the trained model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [resourceConfig](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-resourceConfig"></a>
The EC2 resource configuration that was used to train this model.
Type: [ResourceConfig](API_ResourceConfig.md) object

 ** [status](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-status"></a>
The status of the trained model.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_FAILED | INACTIVE | CANCEL_PENDING | CANCEL_IN_PROGRESS | CANCEL_FAILED`

 ** [statusDetails](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-statusDetails"></a>
Details about the status of a resource.
Type: [StatusDetails](API_StatusDetails.md) object

 ** [stoppingCondition](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-stoppingCondition"></a>
The stopping condition that determined when model training ended.
Type: [StoppingCondition](API_StoppingCondition.md) object

 ** [trainedModelArn](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`

 ** [trainingContainerImageDigest](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-trainingContainerImageDigest"></a>
Information about the training container image.
Type: String

 ** [trainingInputMode](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-trainingInputMode"></a>
The input mode that was used for accessing the training data when this trained model was created. This indicates how the training data was made available to the training algorithm.
Type: String
Valid Values: `File | FastFile | Pipe`

 ** [updateTime](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-updateTime"></a>
The most recent time at which the trained model was updated.
Type: Timestamp

 ** [versionIdentifier](#API_GetCollaborationTrainedModel_ResponseSyntax) **   <a name="API-GetCollaborationTrainedModel-response-versionIdentifier"></a>
The version identifier of the trained model. This unique identifier distinguishes this version from other versions of the same trained model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_GetCollaborationTrainedModel_Errors"></a>

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
<a name="API_GetCollaborationTrainedModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetCollaborationTrainedModel)
