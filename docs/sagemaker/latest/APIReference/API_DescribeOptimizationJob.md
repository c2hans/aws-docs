---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeOptimizationJob.html
---

# DescribeOptimizationJob
<a name="API_DescribeOptimizationJob"></a>

Provides the properties of the specified optimization job.

## Request Syntax
<a name="API_DescribeOptimizationJob_RequestSyntax"></a>

```
{
   "OptimizationJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeOptimizationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OptimizationJobName](#API_DescribeOptimizationJob_RequestSyntax) **   <a name="sagemaker-DescribeOptimizationJob-request-OptimizationJobName"></a>
The name that you assigned to the optimization job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeOptimizationJob_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "DeploymentInstanceType": "string",
   "FailureReason": "string",
   "LastModifiedTime": number,
   "MaxInstanceCount": number,
   "ModelSource": {
      "S3": {
         "ModelAccessConfig": {
            "AcceptEula": boolean
         },
         "S3Uri": "string"
      },
      "SageMakerModel": {
         "ModelName": "string"
      }
   },
   "OptimizationConfigs": [
      { ... }
   ],
   "OptimizationEndTime": number,
   "OptimizationEnvironment": {
      "string" : "string"
   },
   "OptimizationJobArn": "string",
   "OptimizationJobName": "string",
   "OptimizationJobStatus": "string",
   "OptimizationOutput": {
      "RecommendedInferenceImage": "string"
   },
   "OptimizationStartTime": number,
   "OutputConfig": {
      "KmsKeyId": "string",
      "S3OutputLocation": "string",
      "SageMakerModel": {
         "ModelName": "string"
      }
   },
   "RoleArn": "string",
   "StoppingCondition": {
      "MaxPendingTimeInSeconds": number,
      "MaxRuntimeInSeconds": number,
      "MaxWaitTimeInSeconds": number
   },
   "TrainingPlanArns": [ "string" ],
   "VpcConfig": {
      "SecurityGroupIds": [ "string" ],
      "Subnets": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeOptimizationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-CreationTime"></a>
The time when you created the optimization job.
Type: Timestamp

 ** [DeploymentInstanceType](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-DeploymentInstanceType"></a>
The type of instance that hosts the optimized model that you create with the optimization job.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.p6-b200.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge`

 ** [FailureReason](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-FailureReason"></a>
If the optimization job status is `FAILED`, the reason for the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastModifiedTime](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-LastModifiedTime"></a>
The time when the optimization job was last updated.
Type: Timestamp

 ** [MaxInstanceCount](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-MaxInstanceCount"></a>
The maximum number of instances to use for the optimization job.
Type: Integer
Valid Range: Minimum value of 1.

 ** [ModelSource](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-ModelSource"></a>
The location of the source model to optimize with an optimization job.
Type: [OptimizationJobModelSource](API_OptimizationJobModelSource.md) object

 ** [OptimizationConfigs](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-OptimizationConfigs"></a>
Settings for each of the optimization techniques that the job applies.
Type: Array of [OptimizationConfig](API_OptimizationConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [OptimizationEndTime](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-OptimizationEndTime"></a>
The time when the optimization job finished processing.
Type: Timestamp

 ** [OptimizationEnvironment](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-OptimizationEnvironment"></a>
The environment variables to set in the model container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `(?!\s*$).+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [OptimizationJobArn](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-OptimizationJobArn"></a>
The Amazon Resource Name (ARN) of the optimization job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:optimization-job/.*`

 ** [OptimizationJobName](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-OptimizationJobName"></a>
The name that you assigned to the optimization job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [OptimizationJobStatus](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-OptimizationJobStatus"></a>
The current status of the optimization job.
Type: String
Valid Values: `INPROGRESS | COMPLETED | FAILED | STARTING | STOPPING | STOPPED`

 ** [OptimizationOutput](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-OptimizationOutput"></a>
Output values produced by an optimization job.
Type: [OptimizationOutput](API_OptimizationOutput.md) object

 ** [OptimizationStartTime](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-OptimizationStartTime"></a>
The time when the optimization job started.
Type: Timestamp

 ** [OutputConfig](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-OutputConfig"></a>
Details for where to store the optimized model that you create with the optimization job.
Type: [OptimizationJobOutputConfig](API_OptimizationJobOutputConfig.md) object

 ** [RoleArn](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-RoleArn"></a>
The ARN of the IAM role that you assigned to the optimization job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StoppingCondition](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-StoppingCondition"></a>
Specifies a limit to how long a job can run. When the job reaches the time limit, SageMaker ends the job. Use this API to cap costs.
To stop a training job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.
The training algorithms provided by SageMaker automatically save the intermediate results of a model training job when possible. This attempt to save artifacts is only a best effort case as model might not be in a state from which it can be saved. For example, if training has just started, the model might not be ready to save. When saved, this intermediate data is a valid model artifact. You can use it to create a model with `CreateModel`.
The Neural Topic Model (NTM) currently does not support saving intermediate model artifacts. When training NTMs, make sure that the maximum runtime is sufficient for the training job to complete.
Type: [StoppingCondition](API_StoppingCondition.md) object

 ** [TrainingPlanArns](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-TrainingPlanArns"></a>
The Amazon Resource Name (ARN) of the training plan associated with this optimization job. This field appears only when you specified a training plan when you created the job. Optimization jobs that use on-demand capacity don't return this field.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`

 ** [VpcConfig](#API_DescribeOptimizationJob_ResponseSyntax) **   <a name="sagemaker-DescribeOptimizationJob-response-VpcConfig"></a>
A VPC in Amazon VPC that your optimized model has access to.
Type: [OptimizationVpcConfig](API_OptimizationVpcConfig.md) object

## Errors
<a name="API_DescribeOptimizationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeOptimizationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeOptimizationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeOptimizationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeOptimizationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeOptimizationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeOptimizationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeOptimizationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeOptimizationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeOptimizationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeOptimizationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeOptimizationJob)
