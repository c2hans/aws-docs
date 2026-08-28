---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartTrainedModelInferenceJob.html
---

# StartTrainedModelInferenceJob
<a name="API_StartTrainedModelInferenceJob"></a>

Defines the information necessary to begin a trained model inference job.

## Request Syntax
<a name="API_StartTrainedModelInferenceJob_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/trained-model-inference-jobs HTTP/1.1
Content-type: application/json

{
   "configuredModelAlgorithmAssociationArn": "{{string}}",
   "containerExecutionParameters": {
      "maxPayloadInMB": {{number}}
   },
   "dataSource": {
      "mlInputChannelArn": "{{string}}"
   },
   "description": "{{string}}",
   "environment": {
      "{{string}}" : "{{string}}"
   },
   "kmsKeyArn": "{{string}}",
   "mlModelInferencePayerAccountId": "{{string}}",
   "name": "{{string}}",
   "outputConfiguration": {
      "accept": "{{string}}",
      "members": [
         {
            "accountId": "{{string}}"
         }
      ]
   },
   "resourceConfig": {
      "instanceCount": {{number}},
      "instanceType": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "trainedModelArn": "{{string}}",
   "trainedModelVersionIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartTrainedModelInferenceJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-uri-membershipIdentifier"></a>
The membership ID of the membership that contains the trained model inference job.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_StartTrainedModelInferenceJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuredModelAlgorithmAssociationArn](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association that is used for this trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: No

 ** [containerExecutionParameters](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-containerExecutionParameters"></a>
The execution parameters for the container.
Type: [InferenceContainerExecutionParameters](API_InferenceContainerExecutionParameters.md) object
Required: No

 ** [dataSource](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-dataSource"></a>
Defines the data source that is used for the trained model inference job.
Type: [ModelInferenceDataSource](API_ModelInferenceDataSource.md) object
Required: Yes

 ** [description](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-description"></a>
The description of the trained model inference job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [environment](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-environment"></a>
The environment variables to set in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 16 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 1. Maximum length of 10240.
Value Pattern: `[\S\s]*`
Required: No

 ** [kmsKeyArn](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key. This key is used to encrypt and decrypt customer-owned data in the ML inference job and associated data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+`
Required: No

 ** [mlModelInferencePayerAccountId](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-mlModelInferencePayerAccountId"></a>
The account ID of the member that is responsible for paying for model inference costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** [name](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-name"></a>
The name of the trained model inference job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [outputConfiguration](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-outputConfiguration"></a>
Defines the output configuration information for the trained model inference job.
Type: [InferenceOutputConfiguration](API_InferenceOutputConfiguration.md) object
Required: Yes

 ** [resourceConfig](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-resourceConfig"></a>
Defines the resource configuration for the trained model inference job.
Type: [InferenceResourceConfig](API_InferenceResourceConfig.md) object
Required: Yes

 ** [tags](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-tags"></a>
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

 ** [trainedModelArn](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model that is used for this trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [trainedModelVersionIdentifier](#API_StartTrainedModelInferenceJob_RequestSyntax) **   <a name="API-StartTrainedModelInferenceJob-request-trainedModelVersionIdentifier"></a>
The version identifier of the trained model to use for inference. This specifies which version of the trained model should be used to generate predictions on the input data.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## Response Syntax
<a name="API_StartTrainedModelInferenceJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "trainedModelInferenceJobArn": "string"
}
```

## Response Elements
<a name="API_StartTrainedModelInferenceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [trainedModelInferenceJobArn](#API_StartTrainedModelInferenceJob_ResponseSyntax) **   <a name="API-StartTrainedModelInferenceJob-response-trainedModelInferenceJobArn"></a>
The Amazon Resource Name (ARN) of the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model-inference-job/[-a-zA-Z0-9_/.]+`

## Errors
<a name="API_StartTrainedModelInferenceJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can't complete this action because another resource depends on this resource.
HTTP Status Code: 409

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
<a name="API_StartTrainedModelInferenceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/StartTrainedModelInferenceJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
