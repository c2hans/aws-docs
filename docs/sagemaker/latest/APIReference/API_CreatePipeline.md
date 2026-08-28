---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePipeline.html
---

# CreatePipeline
<a name="API_CreatePipeline"></a>

Creates a pipeline using a JSON pipeline definition.

## Request Syntax
<a name="API_CreatePipeline_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
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
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreatePipeline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreatePipeline_RequestSyntax) **   <a name="sagemaker-CreatePipeline-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: Yes

 ** [ParallelismConfiguration](#API_CreatePipeline_RequestSyntax) **   <a name="sagemaker-CreatePipeline-request-ParallelismConfiguration"></a>
This is the configuration that controls the parallelism of the pipeline. If specified, it applies to all runs of this pipeline by default.
Type: [ParallelismConfiguration](API_ParallelismConfiguration.md) object
Required: No

 ** [PipelineDefinition](#API_CreatePipeline_RequestSyntax) **   <a name="sagemaker-CreatePipeline-request-PipelineDefinition"></a>
The [JSON pipeline definition](https://aws-sagemaker-mlops.github.io/sagemaker-model-building-pipeline-definition-JSON-schema/) of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Pattern: `.*(?:[ \r\n\t].*)*`
Required: No

 ** [PipelineDefinitionS3Location](#API_CreatePipeline_RequestSyntax) **   <a name="sagemaker-CreatePipeline-request-PipelineDefinitionS3Location"></a>
The location of the pipeline definition stored in Amazon S3. If specified, SageMaker will retrieve the pipeline definition from this location.
Type: [PipelineDefinitionS3Location](API_PipelineDefinitionS3Location.md) object
Required: No

 ** [PipelineDescription](#API_CreatePipeline_RequestSyntax) **   <a name="sagemaker-CreatePipeline-request-PipelineDescription"></a>
A description of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** [PipelineDisplayName](#API_CreatePipeline_RequestSyntax) **   <a name="sagemaker-CreatePipeline-request-PipelineDisplayName"></a>
The display name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** [PipelineName](#API_CreatePipeline_RequestSyntax) **   <a name="sagemaker-CreatePipeline-request-PipelineName"></a>
The name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: Yes

 ** [RoleArn](#API_CreatePipeline_RequestSyntax) **   <a name="sagemaker-CreatePipeline-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the role used by the pipeline to access and create resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Tags](#API_CreatePipeline_RequestSyntax) **   <a name="sagemaker-CreatePipeline-request-Tags"></a>
A list of tags to apply to the created pipeline.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreatePipeline_ResponseSyntax"></a>

```
{
   "PipelineArn": "string"
}
```

## Response Elements
<a name="API_CreatePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PipelineArn](#API_CreatePipeline_ResponseSyntax) **   <a name="sagemaker-CreatePipeline-response-PipelineArn"></a>
The Amazon Resource Name (ARN) of the created pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`

## Errors
<a name="API_CreatePipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreatePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreatePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreatePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreatePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreatePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreatePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreatePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreatePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreatePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreatePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreatePipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
