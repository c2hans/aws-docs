---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdatePipelineVersion.html
---

# UpdatePipelineVersion
<a name="API_UpdatePipelineVersion"></a>

Updates a pipeline version.

## Request Syntax
<a name="API_UpdatePipelineVersion_RequestSyntax"></a>

```
{
   "PipelineArn": "{{string}}",
   "PipelineVersionDescription": "{{string}}",
   "PipelineVersionDisplayName": "{{string}}",
   "PipelineVersionId": {{number}}
}
```

## Request Parameters
<a name="API_UpdatePipelineVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PipelineArn](#API_UpdatePipelineVersion_RequestSyntax) **   <a name="sagemaker-UpdatePipelineVersion-request-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`
Required: Yes

 ** [PipelineVersionDescription](#API_UpdatePipelineVersion_RequestSyntax) **   <a name="sagemaker-UpdatePipelineVersion-request-PipelineVersionDescription"></a>
The description of the pipeline version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** [PipelineVersionDisplayName](#API_UpdatePipelineVersion_RequestSyntax) **   <a name="sagemaker-UpdatePipelineVersion-request-PipelineVersionDisplayName"></a>
The display name of the pipeline version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`
Required: No

 ** [PipelineVersionId](#API_UpdatePipelineVersion_RequestSyntax) **   <a name="sagemaker-UpdatePipelineVersion-request-PipelineVersionId"></a>
The pipeline version ID to update.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## Response Syntax
<a name="API_UpdatePipelineVersion_ResponseSyntax"></a>

```
{
   "PipelineArn": "string",
   "PipelineVersionId": number
}
```

## Response Elements
<a name="API_UpdatePipelineVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PipelineArn](#API_UpdatePipelineVersion_ResponseSyntax) **   <a name="sagemaker-UpdatePipelineVersion-response-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`

 ** [PipelineVersionId](#API_UpdatePipelineVersion_ResponseSyntax) **   <a name="sagemaker-UpdatePipelineVersion-response-PipelineVersionId"></a>
The ID of the pipeline version.
Type: Long
Valid Range: Minimum value of 1.

## Errors
<a name="API_UpdatePipelineVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePipelineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdatePipelineVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdatePipelineVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdatePipelineVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdatePipelineVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdatePipelineVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdatePipelineVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdatePipelineVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdatePipelineVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdatePipelineVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdatePipelineVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
