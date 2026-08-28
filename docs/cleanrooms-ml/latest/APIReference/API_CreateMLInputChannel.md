---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateMLInputChannel.html
---

# CreateMLInputChannel
<a name="API_CreateMLInputChannel"></a>

Provides the information to create an ML input channel. An ML input channel is the result of a query that can be used for ML modeling.

## Request Syntax
<a name="API_CreateMLInputChannel_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/ml-input-channels HTTP/1.1
Content-type: application/json

{
   "configuredModelAlgorithmAssociations": [ "{{string}}" ],
   "description": "{{string}}",
   "inputChannel": {
      "dataSource": { ... },
      "roleArn": "{{string}}"
   },
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "payerConfiguration": {
      "computePayerAccountId": "{{string}}",
      "syntheticDataPayerAccountId": "{{string}}"
   },
   "retentionInDays": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateMLInputChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_CreateMLInputChannel_RequestSyntax) **   <a name="API-CreateMLInputChannel-request-uri-membershipIdentifier"></a>
The membership ID of the member that is creating the ML input channel.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateMLInputChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuredModelAlgorithmAssociations](#API_CreateMLInputChannel_RequestSyntax) **   <a name="API-CreateMLInputChannel-request-configuredModelAlgorithmAssociations"></a>
The associated configured model algorithms that are necessary to create this ML input channel.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [description](#API_CreateMLInputChannel_RequestSyntax) **   <a name="API-CreateMLInputChannel-request-description"></a>
The description of the ML input channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [inputChannel](#API_CreateMLInputChannel_RequestSyntax) **   <a name="API-CreateMLInputChannel-request-inputChannel"></a>
The input data that is used to create this ML input channel.
Type: [InputChannel](API_InputChannel.md) object
Required: Yes

 ** [kmsKeyArn](#API_CreateMLInputChannel_RequestSyntax) **   <a name="API-CreateMLInputChannel-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key that is used to access the input channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+`
Required: No

 ** [name](#API_CreateMLInputChannel_RequestSyntax) **   <a name="API-CreateMLInputChannel-request-name"></a>
The name of the ML input channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [payerConfiguration](#API_CreateMLInputChannel_RequestSyntax) **   <a name="API-CreateMLInputChannel-request-payerConfiguration"></a>
The payer configuration for the ML input channel. Determines which member account pays for compute and synthetic data costs.
Type: [PayerConfiguration](API_PayerConfiguration.md) object
Required: No

 ** [retentionInDays](#API_CreateMLInputChannel_RequestSyntax) **   <a name="API-CreateMLInputChannel-request-retentionInDays"></a>
The number of days that the data in the ML input channel is retained.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 30.
Required: Yes

 ** [tags](#API_CreateMLInputChannel_RequestSyntax) **   <a name="API-CreateMLInputChannel-request-tags"></a>
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

## Response Syntax
<a name="API_CreateMLInputChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "mlInputChannelArn": "string"
}
```

## Response Elements
<a name="API_CreateMLInputChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [mlInputChannelArn](#API_CreateMLInputChannel_ResponseSyntax) **   <a name="API-CreateMLInputChannel-response-mlInputChannelArn"></a>
The Amazon Resource Name (ARN) of the ML input channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/ml-input-channel/[-a-zA-Z0-9_/.]+`

## Errors
<a name="API_CreateMLInputChannel_Errors"></a>

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
<a name="API_CreateMLInputChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/CreateMLInputChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/CreateMLInputChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CreateMLInputChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/CreateMLInputChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CreateMLInputChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/CreateMLInputChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/CreateMLInputChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/CreateMLInputChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/CreateMLInputChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CreateMLInputChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
