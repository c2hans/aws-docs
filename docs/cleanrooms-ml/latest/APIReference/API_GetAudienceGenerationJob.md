---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetAudienceGenerationJob.html
---

# GetAudienceGenerationJob
<a name="API_GetAudienceGenerationJob"></a>

Returns information about an audience generation job.

## Request Syntax
<a name="API_GetAudienceGenerationJob_RequestSyntax"></a>

```
GET /audience-generation-job/{{audienceGenerationJobArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAudienceGenerationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [audienceGenerationJobArn](#API_GetAudienceGenerationJob_RequestSyntax) **   <a name="API-GetAudienceGenerationJob-request-uri-audienceGenerationJobArn"></a>
The Amazon Resource Name (ARN) of the audience generation job that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-generation-job/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_GetAudienceGenerationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAudienceGenerationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "audienceGenerationJobArn": "string",
   "collaborationId": "string",
   "configuredAudienceModelArn": "string",
   "createTime": "string",
   "description": "string",
   "includeSeedInOutput": boolean,
   "metrics": {
      "recallMetric": number,
      "relevanceMetrics": [
         {
            "audienceSize": {
               "type": "string",
               "value": number
            },
            "score": number
         }
      ]
   },
   "name": "string",
   "protectedQueryIdentifier": "string",
   "seedAudience": {
      "dataSource": {
         "s3Uri": "string"
      },
      "roleArn": "string",
      "sqlComputeConfiguration": { ... },
      "sqlParameters": {
         "analysisTemplateArn": "string",
         "parameters": {
            "string" : "string"
         },
         "queryString": "string"
      }
   },
   "startedBy": "string",
   "status": "string",
   "statusDetails": {
      "message": "string",
      "statusCode": "string"
   },
   "tags": {
      "string" : "string"
   },
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetAudienceGenerationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [audienceGenerationJobArn](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-audienceGenerationJobArn"></a>
The Amazon Resource Name (ARN) of the audience generation job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-generation-job/[-a-zA-Z0-9_/.]+`

 ** [collaborationId](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-collaborationId"></a>
The identifier of the collaboration that this audience generation job is associated with.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [configuredAudienceModelArn](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model used for this audience generation job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`

 ** [createTime](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-createTime"></a>
The time at which the audience generation job was created.
Type: Timestamp

 ** [description](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-description"></a>
The description of the audience generation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [includeSeedInOutput](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-includeSeedInOutput"></a>
Configure whether the seed users are included in the output audience. By default, Clean Rooms ML removes seed users from the output audience. If you specify `TRUE`, the seed users will appear first in the output. Clean Rooms ML does not explicitly reveal whether a user was in the seed, but the recipient of the audience will know that the first `minimumSeedSize` count of users are from the seed.
Type: Boolean

 ** [metrics](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-metrics"></a>
The relevance scores for different audience sizes and the recall score of the generated audience.
Type: [AudienceQualityMetrics](API_AudienceQualityMetrics.md) object

 ** [name](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-name"></a>
The name of the audience generation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [protectedQueryIdentifier](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-protectedQueryIdentifier"></a>
The unique identifier of the protected query for this audience generation job.
Type: String

 ** [seedAudience](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-seedAudience"></a>
The seed audience that was used for this audience generation job. This field will be null if the account calling the API is the account that started this audience generation job.
Type: [AudienceGenerationJobDataSource](API_AudienceGenerationJobDataSource.md) object

 ** [startedBy](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-startedBy"></a>
The AWS account that started this audience generation job.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [status](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-status"></a>
The status of the audience generation job.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_FAILED`

 ** [statusDetails](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-statusDetails"></a>
Details about the status of the audience generation job.
Type: [StatusDetails](API_StatusDetails.md) object

 ** [tags](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-tags"></a>
The tags that are associated to this audience generation job.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updateTime](#API_GetAudienceGenerationJob_ResponseSyntax) **   <a name="API-GetAudienceGenerationJob-response-updateTime"></a>
The most recent time at which the audience generation job was updated.
Type: Timestamp

## Errors
<a name="API_GetAudienceGenerationJob_Errors"></a>

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
<a name="API_GetAudienceGenerationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetAudienceGenerationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetAudienceGenerationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetAudienceGenerationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetAudienceGenerationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetAudienceGenerationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetAudienceGenerationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetAudienceGenerationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetAudienceGenerationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetAudienceGenerationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetAudienceGenerationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
