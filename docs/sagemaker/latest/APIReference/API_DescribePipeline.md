---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribePipeline.html
---

# DescribePipeline
<a name="API_DescribePipeline"></a>

Describes the details of a pipeline.

## Request Syntax
<a name="API_DescribePipeline_RequestSyntax"></a>

```
{
   "PipelineName": "{{string}}",
   "PipelineVersionId": {{number}}
}
```

## Request Parameters
<a name="API_DescribePipeline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PipelineName](#API_DescribePipeline_RequestSyntax) **   <a name="sagemaker-DescribePipeline-request-PipelineName"></a>
The name or Amazon Resource Name (ARN) of the pipeline to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,255})`
Required: Yes

 ** [PipelineVersionId](#API_DescribePipeline_RequestSyntax) **   <a name="sagemaker-DescribePipeline-request-PipelineVersionId"></a>
The ID of the pipeline version to describe.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_DescribePipeline_ResponseSyntax"></a>

```
{
   "CreatedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "LastModifiedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "ParallelismConfiguration": {
      "MaxParallelExecutionSteps": number
   },
   "PipelineArn": "string",
   "PipelineDefinition": "string",
   "PipelineDescription": "string",
   "PipelineDisplayName": "string",
   "PipelineName": "string",
   "PipelineStatus": "string",
   "PipelineVersionDescription": "string",
   "PipelineVersionDisplayName": "string",
   "RoleArn": "string"
}
```

## Response Elements
<a name="API_DescribePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedBy](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedBy](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [ParallelismConfiguration](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-ParallelismConfiguration"></a>
Lists the parallelism configuration applied to the pipeline.
Type: [ParallelismConfiguration](API_ParallelismConfiguration.md) object

 ** [PipelineArn](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`

 ** [PipelineDefinition](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-PipelineDefinition"></a>
The JSON pipeline definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Pattern: `.*(?:[ \r\n\t].*)*`

 ** [PipelineDescription](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-PipelineDescription"></a>
The description of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`

 ** [PipelineDisplayName](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-PipelineDisplayName"></a>
The display name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`

 ** [PipelineName](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-PipelineName"></a>
The name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`

 ** [PipelineStatus](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-PipelineStatus"></a>
The status of the pipeline execution.
Type: String
Valid Values: `Active | Deleting`

 ** [PipelineVersionDescription](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-PipelineVersionDescription"></a>
The description of the pipeline version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`

 ** [PipelineVersionDisplayName](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-PipelineVersionDisplayName"></a>
The display name of the pipeline version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`

 ** [RoleArn](#API_DescribePipeline_ResponseSyntax) **   <a name="sagemaker-DescribePipeline-response-RoleArn"></a>
The Amazon Resource Name (ARN) that the pipeline uses to execute.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

## Errors
<a name="API_DescribePipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribePipeline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribePipeline)
