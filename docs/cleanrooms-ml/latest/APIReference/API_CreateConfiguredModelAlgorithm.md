---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateConfiguredModelAlgorithm.html
---

# CreateConfiguredModelAlgorithm
<a name="API_CreateConfiguredModelAlgorithm"></a>

Creates a configured model algorithm using a container image stored in an ECR repository.

## Request Syntax
<a name="API_CreateConfiguredModelAlgorithm_RequestSyntax"></a>

```
POST /configured-model-algorithms HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "inferenceContainerConfig": {
      "imageUri": "{{string}}"
   },
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "roleArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "trainingContainerConfig": {
      "arguments": [ "{{string}}" ],
      "entrypoint": [ "{{string}}" ],
      "imageUri": "{{string}}",
      "metricDefinitions": [
         {
            "name": "{{string}}",
            "regex": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_CreateConfiguredModelAlgorithm_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConfiguredModelAlgorithm_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateConfiguredModelAlgorithm_RequestSyntax) **   <a name="API-CreateConfiguredModelAlgorithm-request-description"></a>
The description of the configured model algorithm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [inferenceContainerConfig](#API_CreateConfiguredModelAlgorithm_RequestSyntax) **   <a name="API-CreateConfiguredModelAlgorithm-request-inferenceContainerConfig"></a>
Configuration information for the inference container that is used when you run an inference job on a configured model algorithm.
Type: [InferenceContainerConfig](API_InferenceContainerConfig.md) object
Required: No

 ** [kmsKeyArn](#API_CreateConfiguredModelAlgorithm_RequestSyntax) **   <a name="API-CreateConfiguredModelAlgorithm-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model algorithm and associated data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+`
Required: No

 ** [name](#API_CreateConfiguredModelAlgorithm_RequestSyntax) **   <a name="API-CreateConfiguredModelAlgorithm-request-name"></a>
The name of the configured model algorithm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [roleArn](#API_CreateConfiguredModelAlgorithm_RequestSyntax) **   <a name="API-CreateConfiguredModelAlgorithm-request-roleArn"></a>
The Amazon Resource Name (ARN) of the role that is used to access the repository.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [tags](#API_CreateConfiguredModelAlgorithm_RequestSyntax) **   <a name="API-CreateConfiguredModelAlgorithm-request-tags"></a>
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

 ** [trainingContainerConfig](#API_CreateConfiguredModelAlgorithm_RequestSyntax) **   <a name="API-CreateConfiguredModelAlgorithm-request-trainingContainerConfig"></a>
Configuration information for the training container, including entrypoints and arguments.
Type: [ContainerConfig](API_ContainerConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateConfiguredModelAlgorithm_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredModelAlgorithmArn": "string"
}
```

## Response Elements
<a name="API_CreateConfiguredModelAlgorithm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredModelAlgorithmArn](#API_CreateConfiguredModelAlgorithm_ResponseSyntax) **   <a name="API-CreateConfiguredModelAlgorithm-response-configuredModelAlgorithmArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-model-algorithm/[-a-zA-Z0-9_/.]+`

## Errors
<a name="API_CreateConfiguredModelAlgorithm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can't complete this action because another resource depends on this resource.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
You have exceeded your service quota.
HTTP Status Code: 402

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_CreateConfiguredModelAlgorithm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CreateConfiguredModelAlgorithm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
