---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetTrainedModelInferenceJob.html
---

# GetTrainedModelInferenceJob
<a name="API_GetTrainedModelInferenceJob"></a>

Returns information about a trained model inference job.

## Request Syntax
<a name="API_GetTrainedModelInferenceJob_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/trained-model-inference-jobs/{{trainedModelInferenceJobArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTrainedModelInferenceJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_GetTrainedModelInferenceJob_RequestSyntax) **   <a name="API-GetTrainedModelInferenceJob-request-uri-membershipIdentifier"></a>
Provides the membership ID of the membership that contains the trained model inference job that you are interested in.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [trainedModelInferenceJobArn](#API_GetTrainedModelInferenceJob_RequestSyntax) **   <a name="API-GetTrainedModelInferenceJob-request-uri-trainedModelInferenceJobArn"></a>
Provides the Amazon Resource Name (ARN) of the trained model inference job that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model-inference-job/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_GetTrainedModelInferenceJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTrainedModelInferenceJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredModelAlgorithmAssociationArn": "string",
   "containerExecutionParameters": {
      "maxPayloadInMB": number
   },
   "createTime": "string",
   "dataSource": {
      "mlInputChannelArn": "string"
   },
   "description": "string",
   "environment": {
      "string" : "string"
   },
   "inferenceContainerImageDigest": "string",
   "kmsKeyArn": "string",
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
   "resourceConfig": {
      "instanceCount": number,
      "instanceType": "string"
   },
   "status": "string",
   "statusDetails": {
      "message": "string",
      "statusCode": "string"
   },
   "tags": {
      "string" : "string"
   },
   "trainedModelArn": "string",
   "trainedModelInferenceJobArn": "string",
   "trainedModelVersionIdentifier": "string",
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetTrainedModelInferenceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredModelAlgorithmAssociationArn](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association that was used for the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`

 ** [containerExecutionParameters](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-containerExecutionParameters"></a>
The execution parameters for the model inference job container.
Type: [InferenceContainerExecutionParameters](API_InferenceContainerExecutionParameters.md) object

 ** [createTime](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-createTime"></a>
The time at which the trained model inference job was created.
Type: Timestamp

 ** [dataSource](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-dataSource"></a>
The data source that was used for the trained model inference job.
Type: [ModelInferenceDataSource](API_ModelInferenceDataSource.md) object

 ** [description](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-description"></a>
The description of the trained model inference job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [environment](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-environment"></a>
The environment variables to set in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 16 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 1. Maximum length of 10240.
Value Pattern: `[\S\s]*`

 ** [inferenceContainerImageDigest](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-inferenceContainerImageDigest"></a>
Information about the training container image.
Type: String

 ** [kmsKeyArn](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key. This key is used to encrypt and decrypt customer-owned data in the ML inference job and associated data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+`

 ** [logsStatus](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-logsStatus"></a>
The logs status for the trained model inference job.
Type: String
Valid Values: `PUBLISH_SUCCEEDED | PUBLISH_FAILED`

 ** [logsStatusDetails](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-logsStatusDetails"></a>
Details about the logs status for the trained model inference job.
Type: String

 ** [membershipIdentifier](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-membershipIdentifier"></a>
The membership ID of the membership that contains the trained model inference job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [metricsStatus](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-metricsStatus"></a>
The metrics status for the trained model inference job.
Type: String
Valid Values: `PUBLISH_SUCCEEDED | PUBLISH_FAILED`

 ** [metricsStatusDetails](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-metricsStatusDetails"></a>
Details about the metrics status for the trained model inference job.
Type: String

 ** [mlModelInferencePayerAccountId](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-mlModelInferencePayerAccountId"></a>
The account ID of the member that is responsible for paying for model inference costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [name](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-name"></a>
The name of the trained model inference job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [outputConfiguration](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-outputConfiguration"></a>
The output configuration information for the trained model inference job.
Type: [InferenceOutputConfiguration](API_InferenceOutputConfiguration.md) object

 ** [resourceConfig](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-resourceConfig"></a>
The resource configuration information for the trained model inference job.
Type: [InferenceResourceConfig](API_InferenceResourceConfig.md) object

 ** [status](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-status"></a>
The status of the trained model inference job.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | CANCEL_PENDING | CANCEL_IN_PROGRESS | CANCEL_FAILED | INACTIVE`

 ** [statusDetails](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-statusDetails"></a>
Details about the status of a resource.
Type: [StatusDetails](API_StatusDetails.md) object

 ** [tags](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-tags"></a>
The optional metadata that you applied to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.
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

 ** [trainedModelArn](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-trainedModelArn"></a>
The Amazon Resource Name (ARN) for the trained model that was used for the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`

 ** [trainedModelInferenceJobArn](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-trainedModelInferenceJobArn"></a>
The Amazon Resource Name (ARN) of the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model-inference-job/[-a-zA-Z0-9_/.]+`

 ** [trainedModelVersionIdentifier](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-trainedModelVersionIdentifier"></a>
The version identifier of the trained model used for this inference job. This identifies the specific version of the trained model that was used to generate the inference results.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [updateTime](#API_GetTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-GetTrainedModelInferenceJob-response-updateTime"></a>
The most recent time at which the trained model inference job was updated.
Type: Timestamp

## Errors
<a name="API_GetTrainedModelInferenceJob_Errors"></a>

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
<a name="API_GetTrainedModelInferenceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetTrainedModelInferenceJob)
