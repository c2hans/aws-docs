---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateConfiguredAudienceModel.html
---

# CreateConfiguredAudienceModel
<a name="API_CreateConfiguredAudienceModel"></a>

Defines the information necessary to create a configured audience model.

## Request Syntax
<a name="API_CreateConfiguredAudienceModel_RequestSyntax"></a>

```
POST /configured-audience-model HTTP/1.1
Content-type: application/json

{
   "audienceModelArn": "{{string}}",
   "audienceSizeConfig": {
      "audienceSizeBins": [ {{number}} ],
      "audienceSizeType": "{{string}}"
   },
   "childResourceTagOnCreatePolicy": "{{string}}",
   "description": "{{string}}",
   "minMatchingSeedSize": {{number}},
   "name": "{{string}}",
   "outputConfig": {
      "destination": {
         "s3Destination": {
            "s3Uri": "{{string}}"
         }
      },
      "roleArn": "{{string}}"
   },
   "sharedAudienceMetrics": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConfiguredAudienceModel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConfiguredAudienceModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [audienceModelArn](#API_CreateConfiguredAudienceModel_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModel-request-audienceModelArn"></a>
The Amazon Resource Name (ARN) of the audience model to use for the configured audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [audienceSizeConfig](#API_CreateConfiguredAudienceModel_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModel-request-audienceSizeConfig"></a>
Configure the list of output sizes of audiences that can be created using this configured audience model. A request to [StartAudienceGenerationJob](API_StartAudienceGenerationJob.md) that uses this configured audience model must have an `audienceSize` selected from this list. You can use the `ABSOLUTE` [AudienceSize](API_AudienceSize.md) to configure out audience sizes using the count of identifiers in the output. You can use the `Percentage` [AudienceSize](API_AudienceSize.md) to configure sizes in the range 1-100 percent.
Type: [AudienceSizeConfig](API_AudienceSizeConfig.md) object
Required: No

 ** [childResourceTagOnCreatePolicy](#API_CreateConfiguredAudienceModel_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModel-request-childResourceTagOnCreatePolicy"></a>
Configure how the service tags audience generation jobs created using this configured audience model. If you specify `NONE`, the tags from the [StartAudienceGenerationJob](API_StartAudienceGenerationJob.md) request determine the tags of the audience generation job. If you specify `FROM_PARENT_RESOURCE`, the audience generation job inherits the tags from the configured audience model, by default. Tags in the [StartAudienceGenerationJob](API_StartAudienceGenerationJob.md) will override the default.
When the client is in a different account than the configured audience model, the tags from the client are never applied to a resource in the caller's account.
Type: String
Valid Values: `FROM_PARENT_RESOURCE | NONE`
Required: No

 ** [description](#API_CreateConfiguredAudienceModel_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModel-request-description"></a>
The description of the configured audience model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [minMatchingSeedSize](#API_CreateConfiguredAudienceModel_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModel-request-minMatchingSeedSize"></a>
The minimum number of users from the seed audience that must match with users in the training data of the audience model. The default value is 500.
Type: Integer
Valid Range: Minimum value of 25. Maximum value of 500000.
Required: No

 ** [name](#API_CreateConfiguredAudienceModel_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModel-request-name"></a>
The name of the configured audience model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [outputConfig](#API_CreateConfiguredAudienceModel_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModel-request-outputConfig"></a>
Configure the Amazon S3 location and IAM Role for audiences created using this configured audience model. Each audience will have a unique location. The IAM Role must have `s3:PutObject` permission on the destination Amazon S3 location. If the destination is protected with Amazon S3 KMS-SSE, then the Role must also have the required AWS KMS permissions.
Type: [ConfiguredAudienceModelOutputConfig](API_ConfiguredAudienceModelOutputConfig.md) object
Required: Yes

 ** [sharedAudienceMetrics](#API_CreateConfiguredAudienceModel_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModel-request-sharedAudienceMetrics"></a>
Whether audience metrics are shared.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ALL | NONE`
Required: Yes

 ** [tags](#API_CreateConfiguredAudienceModel_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModel-request-tags"></a>
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
<a name="API_CreateConfiguredAudienceModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredAudienceModelArn": "string"
}
```

## Response Elements
<a name="API_CreateConfiguredAudienceModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredAudienceModelArn](#API_CreateConfiguredAudienceModel_ResponseSyntax) **   <a name="API-CreateConfiguredAudienceModel-response-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`

## Errors
<a name="API_CreateConfiguredAudienceModel_Errors"></a>

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

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_CreateConfiguredAudienceModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CreateConfiguredAudienceModel)
