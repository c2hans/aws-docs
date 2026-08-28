---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdatePipeline.html
---

# UpdatePipeline
<a name="API_UpdatePipeline"></a>

Updates a pipeline.

## Request Syntax
<a name="API_UpdatePipeline_RequestSyntax"></a>

```
{
   "ParallelismConfiguration": {
      "MaxParallelExecutionSteps": {{number}}
   },
   "PipelineDefinition": "{{string}}",
   "PipelineDefinitionS3Location": {
      "Bucket": "{{string}}",
      "ObjectKey": "{{string}}",
      "VersionId": "{{string}}"
   },
   "PipelineDescription": "{{string}}",
   "PipelineDisplayName": "{{string}}",
   "PipelineName": "{{string}}",
   "RoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePipeline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ParallelismConfiguration](#API_UpdatePipeline_RequestSyntax) **   <a name="sagemaker-UpdatePipeline-request-ParallelismConfiguration"></a>
If specified, it applies to all executions of this pipeline by default.
Type: [ParallelismConfiguration](API_ParallelismConfiguration.md) object
Required: No

 ** [PipelineDefinition](#API_UpdatePipeline_RequestSyntax) **   <a name="sagemaker-UpdatePipeline-request-PipelineDefinition"></a>
The JSON pipeline definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Pattern: `.*(?:[ \r\n\t].*)*`
Required: No

 ** [PipelineDefinitionS3Location](#API_UpdatePipeline_RequestSyntax) **   <a name="sagemaker-UpdatePipeline-request-PipelineDefinitionS3Location"></a>
The location of the pipeline definition stored in Amazon S3. If specified, SageMaker will retrieve the pipeline definition from this location.
Type: [PipelineDefinitionS3Location](API_PipelineDefinitionS3Location.md) object
Required: No

 ** [PipelineDescription](#API_UpdatePipeline_RequestSyntax) **   <a name="sagemaker-UpdatePipeline-request-PipelineDescription"></a>
The description of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** [PipelineDisplayName](#API_UpdatePipeline_RequestSyntax) **   <a name="sagemaker-UpdatePipeline-request-PipelineDisplayName"></a>
The display name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** [PipelineName](#API_UpdatePipeline_RequestSyntax) **   <a name="sagemaker-UpdatePipeline-request-PipelineName"></a>
The name of the pipeline to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: Yes

 ** [RoleArn](#API_UpdatePipeline_RequestSyntax) **   <a name="sagemaker-UpdatePipeline-request-RoleArn"></a>
The Amazon Resource Name (ARN) that the pipeline uses to execute.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## Response Syntax
<a name="API_UpdatePipeline_ResponseSyntax"></a>

```
{
   "PipelineArn": "string",
   "PipelineVersionId": number
}
```

## Response Elements
<a name="API_UpdatePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PipelineArn](#API_UpdatePipeline_ResponseSyntax) **   <a name="sagemaker-UpdatePipeline-response-PipelineArn"></a>
The Amazon Resource Name (ARN) of the updated pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`

 ** [PipelineVersionId](#API_UpdatePipeline_ResponseSyntax) **   <a name="sagemaker-UpdatePipeline-response-PipelineVersionId"></a>
The ID of the pipeline version.
Type: Long
Valid Range: Minimum value of 1.

## Errors
<a name="API_UpdatePipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdatePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdatePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdatePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdatePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdatePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdatePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdatePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdatePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdatePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdatePipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
