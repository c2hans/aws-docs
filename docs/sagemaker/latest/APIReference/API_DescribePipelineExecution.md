---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribePipelineExecution.html
---

# DescribePipelineExecution
<a name="API_DescribePipelineExecution"></a>

Describes the details of a pipeline execution.

## Request Syntax
<a name="API_DescribePipelineExecution_RequestSyntax"></a>

```
{
   "PipelineExecutionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePipelineExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PipelineExecutionArn](#API_DescribePipelineExecution_RequestSyntax) **   <a name="sagemaker-DescribePipelineExecution-request-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: Yes

## Response Syntax
<a name="API_DescribePipelineExecution_ResponseSyntax"></a>

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
   "CreationTime": number,
   "FailureReason": "string",
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
   "LastModifiedTime": number,
   "MLflowConfig": {
      "MlflowExperimentName": "string",
      "MlflowResourceArn": "string"
   },
   "ParallelismConfiguration": {
      "MaxParallelExecutionSteps": number
   },
   "PipelineArn": "string",
   "PipelineExecutionArn": "string",
   "PipelineExecutionDescription": "string",
   "PipelineExecutionDisplayName": "string",
   "PipelineExecutionStatus": "string",
   "PipelineExperimentConfig": {
      "ExperimentName": "string",
      "TrialName": "string"
   },
   "PipelineVersionId": number,
   "SelectiveExecutionConfig": {
      "SelectedSteps": [
         {
            "StepName": "string"
         }
      ],
      "SourcePipelineExecutionArn": "string"
   }
}
```

## Response Elements
<a name="API_DescribePipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedBy](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-CreationTime"></a>
The time when the pipeline execution was created.
Type: Timestamp

 ** [FailureReason](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-FailureReason"></a>
If the execution failed, a message describing why.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1300.
Pattern: `.*`

 ** [LastModifiedBy](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedTime](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-LastModifiedTime"></a>
The time when the pipeline execution was modified last.
Type: Timestamp

 ** [MLflowConfig](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-MLflowConfig"></a>
 The MLflow configuration of the pipeline execution.
Type: [MLflowConfiguration](API_MLflowConfiguration.md) object

 ** [ParallelismConfiguration](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-ParallelismConfiguration"></a>
The parallelism configuration applied to the pipeline.
Type: [ParallelismConfiguration](API_ParallelismConfiguration.md) object

 ** [PipelineArn](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`

 ** [PipelineExecutionArn](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`

 ** [PipelineExecutionDescription](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-PipelineExecutionDescription"></a>
The description of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`

 ** [PipelineExecutionDisplayName](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-PipelineExecutionDisplayName"></a>
The display name of the pipeline execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`

 ** [PipelineExecutionStatus](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-PipelineExecutionStatus"></a>
The status of the pipeline execution.
Type: String
Valid Values: `Executing | Stopping | Stopped | Failed | Succeeded`

 ** [PipelineExperimentConfig](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-PipelineExperimentConfig"></a>
Specifies the names of the experiment and trial created by a pipeline.
Type: [PipelineExperimentConfig](API_PipelineExperimentConfig.md) object

 ** [PipelineVersionId](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-PipelineVersionId"></a>
The ID of the pipeline version.
Type: Long
Valid Range: Minimum value of 1.

 ** [SelectiveExecutionConfig](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineExecution-response-SelectiveExecutionConfig"></a>
The selective execution configuration applied to the pipeline run.
Type: [SelectiveExecutionConfig](API_SelectiveExecutionConfig.md) object

## Errors
<a name="API_DescribePipelineExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribePipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribePipelineExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribePipelineExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribePipelineExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribePipelineExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribePipelineExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribePipelineExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribePipelineExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribePipelineExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribePipelineExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribePipelineExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
