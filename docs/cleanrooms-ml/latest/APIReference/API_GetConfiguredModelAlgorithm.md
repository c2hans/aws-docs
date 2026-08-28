---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetConfiguredModelAlgorithm.html
---

# GetConfiguredModelAlgorithm
<a name="API_GetConfiguredModelAlgorithm"></a>

Returns information about a configured model algorithm.

## Request Syntax
<a name="API_GetConfiguredModelAlgorithm_RequestSyntax"></a>

```
GET /configured-model-algorithms/{{configuredModelAlgorithmArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfiguredModelAlgorithm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredModelAlgorithmArn](#API_GetConfiguredModelAlgorithm_RequestSyntax) **   <a name="API-GetConfiguredModelAlgorithm-request-uri-configuredModelAlgorithmArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm that you want to return information about.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-model-algorithm/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_GetConfiguredModelAlgorithm_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfiguredModelAlgorithm_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredModelAlgorithmArn": "string",
   "createTime": "string",
   "description": "string",
   "inferenceContainerConfig": {
      "imageUri": "string"
   },
   "kmsKeyArn": "string",
   "name": "string",
   "roleArn": "string",
   "tags": {
      "string" : "string"
   },
   "trainingContainerConfig": {
      "arguments": [ "string" ],
      "entrypoint": [ "string" ],
      "imageUri": "string",
      "metricDefinitions": [
         {
            "name": "string",
            "regex": "string"
         }
      ]
   },
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetConfiguredModelAlgorithm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredModelAlgorithmArn](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-configuredModelAlgorithmArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-model-algorithm/[-a-zA-Z0-9_/.]+`

 ** [createTime](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-createTime"></a>
The time at which the configured model algorithm was created.
Type: Timestamp

 ** [description](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-description"></a>
The description of the configured model algorithm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [inferenceContainerConfig](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-inferenceContainerConfig"></a>
Configuration information for the inference container.
Type: [InferenceContainerConfig](API_InferenceContainerConfig.md) object

 ** [kmsKeyArn](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model and associated data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+`

 ** [name](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-name"></a>
The name of the configured model algorithm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [roleArn](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-roleArn"></a>
The Amazon Resource Name (ARN) of the service role that was used to create the configured model algorithm.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`

 ** [tags](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-tags"></a>
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

 ** [trainingContainerConfig](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-trainingContainerConfig"></a>
The configuration information of the training container for the configured model algorithm.
Type: [ContainerConfig](API_ContainerConfig.md) object

 ** [updateTime](#API_GetConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithm-response-updateTime"></a>
The most recent time at which the configured model algorithm was updated.
Type: Timestamp

## Errors
<a name="API_GetConfiguredModelAlgorithm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_GetConfiguredModelAlgorithm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
