---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateTrainedModel.html
---

# CreateTrainedModel
<a name="API_CreateTrainedModel"></a>

Creates a trained model from an associated configured model algorithm using data from any member of the collaboration.

## Request Syntax
<a name="API_CreateTrainedModel_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/trained-models HTTP/1.1
Content-type: application/json

{
   "configuredModelAlgorithmAssociationArn": "{{string}}",
   "dataChannels": [
      {
         "channelName": "{{string}}",
         "mlInputChannelArn": "{{string}}",
         "s3DataDistributionType": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "environment": {
      "{{string}}" : "{{string}}"
   },
   "hyperparameters": {
      "{{string}}" : "{{string}}"
   },
   "incrementalTrainingDataChannels": [
      {
         "channelName": "{{string}}",
         "trainedModelArn": "{{string}}",
         "versionIdentifier": "{{string}}"
      }
   ],
   "kmsKeyArn": "{{string}}",
   "mlModelTrainingPayerAccountId": "{{string}}",
   "name": "{{string}}",
   "resourceConfig": {
      "instanceCount": {{number}},
      "instanceType": "{{string}}",
      "volumeSizeInGB": {{number}}
   },
   "stoppingCondition": {
      "maxRuntimeInSeconds": {{number}}
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "trainingInputMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTrainedModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-uri-membershipIdentifier"></a>
The membership ID of the member that is creating the trained model.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateTrainedModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuredModelAlgorithmAssociationArn](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-configuredModelAlgorithmAssociationArn"></a>
The associated configured model algorithm used to train this model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [dataChannels](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-dataChannels"></a>
Defines the data channels that are used as input for the trained model request.
Limit: Maximum of 20 channels total (including both `dataChannels` and `incrementalTrainingDataChannels`).
Type: Array of [ModelTrainingDataChannel](API_ModelTrainingDataChannel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** [description](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-description"></a>
The description of the trained model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [environment](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-environment"></a>
The environment variables to set in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 512.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 1. Maximum length of 512.
Value Pattern: `[\S\s]*`
Required: No

 ** [hyperparameters](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-hyperparameters"></a>
Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 1. Maximum length of 2500.
Value Pattern: `.*`
Required: No

 ** [incrementalTrainingDataChannels](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-incrementalTrainingDataChannels"></a>
Specifies the incremental training data channels for the trained model.
Incremental training allows you to create a new trained model with updates without retraining from scratch. You can specify up to one incremental training data channel that references a previously trained model and its version.
Limit: Maximum of 20 channels total (including both `incrementalTrainingDataChannels` and `dataChannels`).
Type: Array of [IncrementalTrainingDataChannel](API_IncrementalTrainingDataChannel.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [kmsKeyArn](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+`
Required: No

 ** [mlModelTrainingPayerAccountId](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-mlModelTrainingPayerAccountId"></a>
The account ID of the member that is responsible for paying for model training costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** [name](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-name"></a>
The name of the trained model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [resourceConfig](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-resourceConfig"></a>
Information about the EC2 resources that are used to train this model.
Type: [ResourceConfig](API_ResourceConfig.md) object
Required: Yes

 ** [stoppingCondition](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-stoppingCondition"></a>
The criteria that is used to stop model training.
Type: [StoppingCondition](API_StoppingCondition.md) object
Required: No

 ** [tags](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-tags"></a>
The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50.
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8.
+ Maximum value length - 256 Unicode characters in UTF-8.
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case sensitive.
+ Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [trainingInputMode](#API_CreateTrainedModel_RequestSyntax) **   <a name="API-CreateTrainedModel-request-trainingInputMode"></a>
The input mode for accessing the training data. This parameter determines how the training data is made available to the training algorithm. Valid values are:
+  `File` - The training data is downloaded to the training instance and made available as files.
+  `FastFile` - The training data is streamed directly from Amazon S3 to the training algorithm, providing faster access for large datasets.
+  `Pipe` - The training data is streamed to the training algorithm using named pipes, which can improve performance for certain algorithms.
Type: String
Valid Values: `File | FastFile | Pipe`
Required: No

## Response Syntax
<a name="API_CreateTrainedModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "trainedModelArn": "string",
   "versionIdentifier": "string"
}
```

## Response Elements
<a name="API_CreateTrainedModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [trainedModelArn](#API_CreateTrainedModel_ResponseSyntax) **   <a name="API-CreateTrainedModel-response-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`

 ** [versionIdentifier](#API_CreateTrainedModel_ResponseSyntax) **   <a name="API-CreateTrainedModel-response-versionIdentifier"></a>
The unique version identifier assigned to the newly created trained model. This identifier can be used to reference this specific version of the trained model in subsequent operations such as inference jobs or incremental training.
The initial version identifier for the base version of the trained model is "NULL".
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_CreateTrainedModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can't complete this action because another resource depends on this resource.
HTTP Status Code: 409

 ** InternalServiceException **
An internal service error occurred. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded your service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_CreateTrainedModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/CreateTrainedModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/CreateTrainedModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CreateTrainedModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/CreateTrainedModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CreateTrainedModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/CreateTrainedModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/CreateTrainedModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/CreateTrainedModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/CreateTrainedModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CreateTrainedModel)
