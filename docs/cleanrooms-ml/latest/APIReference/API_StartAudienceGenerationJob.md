---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.html
---

# StartAudienceGenerationJob
<a name="API_StartAudienceGenerationJob"></a>

Information necessary to start the audience generation job.

## Request Syntax
<a name="API_StartAudienceGenerationJob_RequestSyntax"></a>

```
POST /audience-generation-job HTTP/1.1
Content-type: application/json

{
   "collaborationId": "{{string}}",
   "configuredAudienceModelArn": "{{string}}",
   "description": "{{string}}",
   "includeSeedInOutput": {{boolean}},
   "name": "{{string}}",
   "seedAudience": {
      "dataSource": {
         "s3Uri": "{{string}}"
      },
      "roleArn": "{{string}}",
      "sqlComputeConfiguration": { ... },
      "sqlParameters": {
         "analysisTemplateArn": "{{string}}",
         "parameters": {
            "{{string}}" : "{{string}}"
         },
         "queryString": "{{string}}"
      }
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartAudienceGenerationJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartAudienceGenerationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [collaborationId](#API_StartAudienceGenerationJob_RequestSyntax) **   <a name="API-StartAudienceGenerationJob-request-collaborationId"></a>
The identifier of the collaboration that contains the audience generation job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [configuredAudienceModelArn](#API_StartAudienceGenerationJob_RequestSyntax) **   <a name="API-StartAudienceGenerationJob-request-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that is used for this audience generation job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [description](#API_StartAudienceGenerationJob_RequestSyntax) **   <a name="API-StartAudienceGenerationJob-request-description"></a>
The description of the audience generation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [includeSeedInOutput](#API_StartAudienceGenerationJob_RequestSyntax) **   <a name="API-StartAudienceGenerationJob-request-includeSeedInOutput"></a>
Whether the seed audience is included in the audience generation output.
Type: Boolean
Required: No

 ** [name](#API_StartAudienceGenerationJob_RequestSyntax) **   <a name="API-StartAudienceGenerationJob-request-name"></a>
The name of the audience generation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [seedAudience](#API_StartAudienceGenerationJob_RequestSyntax) **   <a name="API-StartAudienceGenerationJob-request-seedAudience"></a>
The seed audience that is used to generate the audience.
Type: [AudienceGenerationJobDataSource](API_AudienceGenerationJobDataSource.md) object
Required: Yes

 ** [tags](#API_StartAudienceGenerationJob_RequestSyntax) **   <a name="API-StartAudienceGenerationJob-request-tags"></a>
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
<a name="API_StartAudienceGenerationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "audienceGenerationJobArn": "string"
}
```

## Response Elements
<a name="API_StartAudienceGenerationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [audienceGenerationJobArn](#API_StartAudienceGenerationJob_ResponseSyntax) **   <a name="API-StartAudienceGenerationJob-response-audienceGenerationJobArn"></a>
The Amazon Resource Name (ARN) of the audience generation job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-generation-job/[-a-zA-Z0-9_/.]+`

## Errors
<a name="API_StartAudienceGenerationJob_Errors"></a>

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
<a name="API_StartAudienceGenerationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/StartAudienceGenerationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/StartAudienceGenerationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/StartAudienceGenerationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/StartAudienceGenerationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/StartAudienceGenerationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/StartAudienceGenerationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/StartAudienceGenerationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/StartAudienceGenerationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/StartAudienceGenerationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/StartAudienceGenerationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
