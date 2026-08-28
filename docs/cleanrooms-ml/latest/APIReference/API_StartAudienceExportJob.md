---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartAudienceExportJob.html
---

# StartAudienceExportJob
<a name="API_StartAudienceExportJob"></a>

Export an audience of a specified size after you have generated an audience.

## Request Syntax
<a name="API_StartAudienceExportJob_RequestSyntax"></a>

```
POST /audience-export-job HTTP/1.1
Content-type: application/json

{
   "audienceGenerationJobArn": "{{string}}",
   "audienceSize": {
      "type": "{{string}}",
      "value": {{number}}
   },
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartAudienceExportJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartAudienceExportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [audienceGenerationJobArn](#API_StartAudienceExportJob_RequestSyntax) **   <a name="API-StartAudienceExportJob-request-audienceGenerationJobArn"></a>
The Amazon Resource Name (ARN) of the audience generation job that you want to export.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-generation-job/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [audienceSize](#API_StartAudienceExportJob_RequestSyntax) **   <a name="API-StartAudienceExportJob-request-audienceSize"></a>
The size of the generated audience. Must match one of the sizes in the configured audience model.
Type: [AudienceSize](API_AudienceSize.md) object
Required: Yes

 ** [description](#API_StartAudienceExportJob_RequestSyntax) **   <a name="API-StartAudienceExportJob-request-description"></a>
The description of the audience export job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [name](#API_StartAudienceExportJob_RequestSyntax) **   <a name="API-StartAudienceExportJob-request-name"></a>
The name of the audience export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_StartAudienceExportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StartAudienceExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartAudienceExportJob_Errors"></a>

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
<a name="API_StartAudienceExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/StartAudienceExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/StartAudienceExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/StartAudienceExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/StartAudienceExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/StartAudienceExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/StartAudienceExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/StartAudienceExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/StartAudienceExportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/StartAudienceExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/StartAudienceExportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
