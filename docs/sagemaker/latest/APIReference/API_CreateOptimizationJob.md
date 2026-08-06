---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateOptimizationJob.html
---

# CreateOptimizationJob
<a name="API_CreateOptimizationJob"></a>

Creates a job that optimizes a model for inference performance. To create the job, you provide the location of a source model, and you provide the settings for the optimization techniques that you want the job to apply. When the job completes successfully, SageMaker uploads the new optimized model to the output destination that you specify.

For more information about how to use this action, and about the supported optimization techniques, see [Optimize model inference with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html).

## Request Syntax
<a name="API_CreateOptimizationJob_RequestSyntax"></a>

```
{
   "DeploymentInstanceType": "{{string}}",
   "MaxInstanceCount": {{number}},
   "ModelSource": {
      "S3": {
         "ModelAccessConfig": {
            "AcceptEula": {{boolean}}
         },
         "S3Uri": "{{string}}"
      },
      "SageMakerModel": {
         "ModelName": "{{string}}"
      }
   },
   "OptimizationConfigs": [
      { ... }
   ],
   "OptimizationEnvironment": {
      "{{string}}" : "{{string}}"
   },
   "OptimizationJobName": "{{string}}",
   "OutputConfig": {
      "KmsKeyId": "{{string}}",
      "S3OutputLocation": "{{string}}",
      "SageMakerModel": {
         "ModelName": "{{string}}"
      }
   },
   "RoleArn": "{{string}}",
   "StoppingCondition": {
      "MaxPendingTimeInSeconds": {{number}},
      "MaxRuntimeInSeconds": {{number}},
      "MaxWaitTimeInSeconds": {{number}}
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrainingPlanArns": [ "{{string}}" ],
   "VpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "Subnets": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_CreateOptimizationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeploymentInstanceType](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-DeploymentInstanceType"></a>
The type of instance that hosts the optimized model that you create with the optimization job.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.p6-b200.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge`
Required: Yes

 ** [MaxInstanceCount](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-MaxInstanceCount"></a>
The maximum number of instances to use for the optimization job.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [ModelSource](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-ModelSource"></a>
The location of the source model to optimize with an optimization job.
Type: [OptimizationJobModelSource](API_OptimizationJobModelSource.md) object
Required: Yes

 ** [OptimizationConfigs](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-OptimizationConfigs"></a>
Settings for each of the optimization techniques that the job applies.
Type: Array of [OptimizationConfig](API_OptimizationConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** [OptimizationEnvironment](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-OptimizationEnvironment"></a>
The environment variables to set in the model container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `(?!\s*$).+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [OptimizationJobName](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-OptimizationJobName"></a>
A custom name for the new optimization job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [OutputConfig](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-OutputConfig"></a>
Details for where to store the optimized model that you create with the optimization job.
Type: [OptimizationJobOutputConfig](API_OptimizationJobOutputConfig.md) object
Required: Yes

 ** [RoleArn](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.
During model optimization, Amazon SageMaker AI needs your permission to:
+ Read input data from an S3 bucket
+ Write model artifacts to an S3 bucket
+ Write logs to Amazon CloudWatch Logs
+ Publish metrics to Amazon CloudWatch
You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker AI, the caller of this API must have the `iam:PassRole` permission. For more information, see [Amazon SageMaker AI Roles.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html)
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [StoppingCondition](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-StoppingCondition"></a>
Specifies a limit to how long a job can run. When the job reaches the time limit, SageMaker ends the job. Use this API to cap costs.
To stop a training job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.
The training algorithms provided by SageMaker automatically save the intermediate results of a model training job when possible. This attempt to save artifacts is only a best effort case as model might not be in a state from which it can be saved. For example, if training has just started, the model might not be ready to save. When saved, this intermediate data is a valid model artifact. You can use it to create a model with `CreateModel`.
The Neural Topic Model (NTM) currently does not support saving intermediate model artifacts. When training NTMs, make sure that the maximum runtime is sufficient for the training job to complete.
Type: [StoppingCondition](API_StoppingCondition.md) object
Required: Yes

 ** [Tags](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-Tags"></a>
A list of key-value pairs associated with the optimization job. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TrainingPlanArns](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-TrainingPlanArns"></a>
The Amazon Resource Name (ARN) of the training plan to use for this optimization job.
When you use reserved capacity from a training plan, the optimization job runs on that reserved capacity instead of on-demand capacity. If you omit this field, the job uses on-demand capacity. You can specify at most one training plan.
For more information about how to reserve GPU capacity for your optimization jobs using Amazon SageMaker Training Plans, see [Reserve capacity with training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

 ** [VpcConfig](#API_CreateOptimizationJob_RequestSyntax) **   <a name="sagemaker-CreateOptimizationJob-request-VpcConfig"></a>
A VPC in Amazon VPC that your optimized model has access to.
Type: [OptimizationVpcConfig](API_OptimizationVpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateOptimizationJob_ResponseSyntax"></a>

```
{
   "OptimizationJobArn": "string"
}
```

## Response Elements
<a name="API_CreateOptimizationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OptimizationJobArn](#API_CreateOptimizationJob_ResponseSyntax) **   <a name="sagemaker-CreateOptimizationJob-response-OptimizationJobArn"></a>
The Amazon Resource Name (ARN) of the optimization job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:optimization-job/.*`

## Errors
<a name="API_CreateOptimizationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateOptimizationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateOptimizationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateOptimizationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateOptimizationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateOptimizationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateOptimizationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateOptimizationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateOptimizationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateOptimizationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateOptimizationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateOptimizationJob)
