---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html
---

# CreateTrainingJob
<a name="API_CreateTrainingJob"></a>

Starts a model training job. After training completes, SageMaker saves the resulting model artifacts to an Amazon S3 location that you specify.

If you choose to host your model using SageMaker hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts in a machine learning service other than SageMaker, provided that you know how to use them for inference.

In the request body, you provide the following:
+  `AlgorithmSpecification` - Identifies the training algorithm to use.
+  `HyperParameters` - Specify these algorithm-specific parameters to enable the estimation of model parameters during training. Hyperparameters can be tuned to optimize this learning process. For a list of hyperparameters for each training algorithm provided by SageMaker, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).
**Important**
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request hyperparameter variable or plain text fields.
+  `InputDataConfig` - Describes the input required by the training job and the Amazon S3, EFS, or FSx location where it is stored.
+  `OutputDataConfig` - Identifies the Amazon S3 bucket where you want SageMaker to save the results of model training.
+  `ResourceConfig` - Identifies the resources, ML compute instances, and ML storage volumes to deploy for model training. In distributed training, you specify more than one instance.
+  `EnableManagedSpotTraining` - Optimize the cost of training machine learning models by up to 80% by using Amazon EC2 Spot instances. For more information, see [Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html).
+  `RoleArn` - The Amazon Resource Name (ARN) that SageMaker assumes to perform tasks on your behalf during model training. You must grant this role the necessary permissions so that SageMaker can successfully complete model training.
+  `StoppingCondition` - To help cap training costs, use `MaxRuntimeInSeconds` to set a time limit for training. Use `MaxWaitTimeInSeconds` to specify how long a managed spot training job has to complete.
+  `Environment` - The environment variables to set in the Docker container.
**Important**
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.
+  `RetryStrategy` - The number of times to retry the job when the job fails due to an `InternalServerError`.

 For more information about SageMaker, see [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html).

## Request Syntax
<a name="API_CreateTrainingJob_RequestSyntax"></a>

```
{
   "AlgorithmSpecification": {
      "AlgorithmName": "{{string}}",
      "ContainerArguments": [ "{{string}}" ],
      "ContainerEntrypoint": [ "{{string}}" ],
      "EnableSageMakerMetricsTimeSeries": {{boolean}},
      "MetricDefinitions": [
         {
            "Name": "{{string}}",
            "Regex": "{{string}}"
         }
      ],
      "TrainingImage": "{{string}}",
      "TrainingImageConfig": {
         "TrainingRepositoryAccessMode": "{{string}}",
         "TrainingRepositoryAuthConfig": {
            "TrainingRepositoryCredentialsProviderArn": "{{string}}"
         }
      },
      "TrainingInputMode": "{{string}}"
   },
   "CheckpointConfig": {
      "LocalPath": "{{string}}",
      "S3Uri": "{{string}}"
   },
   "DebugHookConfig": {
      "CollectionConfigurations": [
         {
            "CollectionName": "{{string}}",
            "CollectionParameters": {
               "{{string}}" : "{{string}}"
            }
         }
      ],
      "HookParameters": {
         "{{string}}" : "{{string}}"
      },
      "LocalPath": "{{string}}",
      "S3OutputPath": "{{string}}"
   },
   "DebugRuleConfigurations": [
      {
         "InstanceType": "{{string}}",
         "LocalPath": "{{string}}",
         "RuleConfigurationName": "{{string}}",
         "RuleEvaluatorImage": "{{string}}",
         "RuleParameters": {
            "{{string}}" : "{{string}}"
         },
         "S3OutputPath": "{{string}}",
         "VolumeSizeInGB": {{number}}
      }
   ],
   "EnableInterContainerTrafficEncryption": {{boolean}},
   "EnableManagedSpotTraining": {{boolean}},
   "EnableNetworkIsolation": {{boolean}},
   "Environment": {
      "{{string}}" : "{{string}}"
   },
   "ExperimentConfig": {
      "ExperimentName": "{{string}}",
      "RunName": "{{string}}",
      "TrialComponentDisplayName": "{{string}}",
      "TrialName": "{{string}}"
   },
   "HyperParameters": {
      "{{string}}" : "{{string}}"
   },
   "InfraCheckConfig": {
      "EnableInfraCheck": {{boolean}}
   },
   "InputDataConfig": [
      {
         "ChannelName": "{{string}}",
         "CompressionType": "{{string}}",
         "ContentType": "{{string}}",
         "DataSource": {
            "DatasetSource": {
               "DatasetArn": "{{string}}"
            },
            "FileSystemDataSource": {
               "DirectoryPath": "{{string}}",
               "FileSystemAccessMode": "{{string}}",
               "FileSystemId": "{{string}}",
               "FileSystemType": "{{string}}"
            },
            "S3DataSource": {
               "AttributeNames": [ "{{string}}" ],
               "HubAccessConfig": {
                  "HubContentArn": "{{string}}"
               },
               "InstanceGroupNames": [ "{{string}}" ],
               "ModelAccessConfig": {
                  "AcceptEula": {{boolean}}
               },
               "S3DataDistributionType": "{{string}}",
               "S3DataType": "{{string}}",
               "S3Uri": "{{string}}"
            }
         },
         "InputMode": "{{string}}",
         "RecordWrapperType": "{{string}}",
         "ShuffleConfig": {
            "Seed": {{number}}
         }
      }
   ],
   "MlflowConfig": {
      "MlflowExperimentName": "{{string}}",
      "MlflowResourceArn": "{{string}}",
      "MlflowRunName": "{{string}}"
   },
   "ModelPackageConfig": {
      "ModelPackageGroupArn": "{{string}}",
      "SourceModelPackageArn": "{{string}}"
   },
   "OutputDataConfig": {
      "CompressionType": "{{string}}",
      "KmsKeyId": "{{string}}",
      "S3OutputPath": "{{string}}"
   },
   "ProfilerConfig": {
      "DisableProfiler": {{boolean}},
      "ProfilingIntervalInMilliseconds": {{number}},
      "ProfilingParameters": {
         "{{string}}" : "{{string}}"
      },
      "S3OutputPath": "{{string}}"
   },
   "ProfilerRuleConfigurations": [
      {
         "InstanceType": "{{string}}",
         "LocalPath": "{{string}}",
         "RuleConfigurationName": "{{string}}",
         "RuleEvaluatorImage": "{{string}}",
         "RuleParameters": {
            "{{string}}" : "{{string}}"
         },
         "S3OutputPath": "{{string}}",
         "VolumeSizeInGB": {{number}}
      }
   ],
   "RemoteDebugConfig": {
      "EnableRemoteDebug": {{boolean}}
   },
   "ResourceConfig": {
      "InstanceCount": {{number}},
      "InstanceGroups": [
         {
            "InstanceCount": {{number}},
            "InstanceGroupName": "{{string}}",
            "InstanceType": "{{string}}"
         }
      ],
      "InstancePlacementConfig": {
         "EnableMultipleJobs": {{boolean}},
         "PlacementSpecifications": [
            {
               "InstanceCount": {{number}},
               "UltraServerId": "{{string}}"
            }
         ]
      },
      "InstanceType": "{{string}}",
      "KeepAlivePeriodInSeconds": {{number}},
      "TrainingPlanArn": "{{string}}",
      "VolumeKmsKeyId": "{{string}}",
      "VolumeSizeInGB": {{number}}
   },
   "RetryStrategy": {
      "MaximumRetryAttempts": {{number}}
   },
   "RoleArn": "{{string}}",
   "ServerlessJobConfig": {
      "AcceptEula": {{boolean}},
      "BaseModelArn": "{{string}}",
      "CustomizationTechnique": "{{string}}",
      "EvaluationType": "{{string}}",
      "EvaluatorArn": "{{string}}",
      "JobType": "{{string}}",
      "Peft": "{{string}}"
   },
   "SessionChainingConfig": {
      "EnableSessionTagChaining": {{boolean}}
   },
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
   "TensorBoardOutputConfig": {
      "LocalPath": "{{string}}",
      "S3OutputPath": "{{string}}"
   },
   "TrainingJobName": "{{string}}",
   "VpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "Subnets": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_CreateTrainingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlgorithmSpecification](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-AlgorithmSpecification"></a>
The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by SageMaker, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). For information about providing your own algorithms, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).
Type: [AlgorithmSpecification](API_AlgorithmSpecification.md) object
Required: No

 ** [CheckpointConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-CheckpointConfig"></a>
Contains information about the output location for managed spot training checkpoint data.
Type: [CheckpointConfig](API_CheckpointConfig.md) object
Required: No

 ** [DebugHookConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-DebugHookConfig"></a>
Configuration information for the Amazon SageMaker Debugger hook parameters, metric and tensor collections, and storage paths. To learn more about how to configure the `DebugHookConfig` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).
Type: [DebugHookConfig](API_DebugHookConfig.md) object
Required: No

 ** [DebugRuleConfigurations](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-DebugRuleConfigurations"></a>
Configuration information for Amazon SageMaker Debugger rules for debugging output tensors.
Type: Array of [DebugRuleConfiguration](API_DebugRuleConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [EnableInterContainerTrafficEncryption](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-EnableInterContainerTrafficEncryption"></a>
To encrypt all communications between ML compute instances in distributed training, choose `True`. Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training. For more information, see [Protect Communications Between ML Compute Instances in a Distributed Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/train-encrypt.html).
Type: Boolean
Required: No

 ** [EnableManagedSpotTraining](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-EnableManagedSpotTraining"></a>
To train models using managed spot training, choose `True`. Managed spot training provides a fully managed and scalable infrastructure for training machine learning models. this option is useful when training jobs can be interrupted and when there is flexibility when the training job is run.
The complete and intermediate results of jobs are stored in an Amazon S3 bucket, and can be used as a starting point to train models incrementally. Amazon SageMaker provides metrics and logs in CloudWatch. They can be used to see when managed spot training jobs are running, interrupted, resumed, or completed.
Type: Boolean
Required: No

 ** [EnableNetworkIsolation](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-EnableNetworkIsolation"></a>
Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If you enable network isolation for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.
Type: Boolean
Required: No

 ** [Environment](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-Environment"></a>
The environment variables to set in the Docker container.
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 512.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 512.
Value Pattern: `[\S\s]*`
Required: No

 ** [ExperimentConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-ExperimentConfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
Type: [ExperimentConfig](API_ExperimentConfig.md) object
Required: No

 ** [HyperParameters](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-HyperParameters"></a>
Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process. For a list of hyperparameters for each training algorithm provided by SageMaker, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).
You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the `Length Constraint`.
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by any security-sensitive information included in the request hyperparameter variable or plain text fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`
Required: No

 ** [InfraCheckConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-InfraCheckConfig"></a>
Contains information about the infrastructure health check configuration for the training job.
Type: [InfraCheckConfig](API_InfraCheckConfig.md) object
Required: No

 ** [InputDataConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-InputDataConfig"></a>
An array of `Channel` objects. Each channel is a named input source. `InputDataConfig` describes the input data and its location.
Algorithms can accept input data from one or more channels. For example, an algorithm might have two channels of input data, `training_data` and `validation_data`. The configuration for each channel provides the S3, EFS, or FSx location where the input data is stored. It also provides information about the stored data: the MIME type, compression method, and whether the data is wrapped in RecordIO format.
Depending on the input mode that the algorithm supports, SageMaker either copies input data files from an S3 bucket to a local directory in the Docker container, or makes it available as input streams. For example, if you specify an EFS location, input data files are available as input streams. They do not need to be downloaded.
Your input must be in the same AWS region as your training job.
Type: Array of [Channel](API_Channel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [MlflowConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-MlflowConfig"></a>
 The MLflow configuration using SageMaker managed MLflow.
Type: [MlflowConfig](API_MlflowConfig.md) object
Required: No

 ** [ModelPackageConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-ModelPackageConfig"></a>
 The configuration for the model package.
Type: [ModelPackageConfig](API_ModelPackageConfig.md) object
Required: No

 ** [OutputDataConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-OutputDataConfig"></a>
Specifies the path to the S3 location where you want to store model artifacts. SageMaker creates subfolders for the artifacts.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: Yes

 ** [ProfilerConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-ProfilerConfig"></a>
Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.
Type: [ProfilerConfig](API_ProfilerConfig.md) object
Required: No

 ** [ProfilerRuleConfigurations](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-ProfilerRuleConfigurations"></a>
Configuration information for Amazon SageMaker Debugger rules for profiling system and framework metrics.
Type: Array of [ProfilerRuleConfiguration](API_ProfilerRuleConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [RemoteDebugConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-RemoteDebugConfig"></a>
Configuration for remote debugging. To learn more about the remote debugging functionality of SageMaker, see [Access a training container through AWS Systems Manager (SSM) for remote debugging](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html).
Type: [RemoteDebugConfig](API_RemoteDebugConfig.md) object
Required: No

 ** [ResourceConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-ResourceConfig"></a>
The resources, including the ML compute instances and ML storage volumes, to use for model training.
ML storage volumes store model artifacts and incremental states. Training algorithms might also use ML storage volumes for scratch space. If you want SageMaker to use the ML storage volume to store the training data, choose `File` as the `TrainingInputMode` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
Type: [ResourceConfig](API_ResourceConfig.md) object
Required: No

 ** [RetryStrategy](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-RetryStrategy"></a>
The number of times to retry the job when the job fails due to an `InternalServerError`.
Type: [RetryStrategy](API_RetryStrategy.md) object
Required: No

 ** [RoleArn](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that SageMaker can assume to perform tasks on your behalf.
During model training, SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see [SageMaker Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html).
To be able to pass this role to SageMaker, the caller of this API must have the `iam:PassRole` permission.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [ServerlessJobConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-ServerlessJobConfig"></a>
 The configuration for serverless training jobs.
Type: [ServerlessJobConfig](API_ServerlessJobConfig.md) object
Required: No

 ** [SessionChainingConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-SessionChainingConfig"></a>
Contains information about attribute-based access control (ABAC) for the training job.
Type: [SessionChainingConfig](API_SessionChainingConfig.md) object
Required: No

 ** [StoppingCondition](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-StoppingCondition"></a>
Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.
To stop a job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.
Type: [StoppingCondition](API_StoppingCondition.md) object
Required: No

 ** [Tags](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any tags. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by any security-sensitive information included in the request tag variable or plain text fields.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TensorBoardOutputConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-TensorBoardOutputConfig"></a>
Configuration of storage locations for the Amazon SageMaker Debugger TensorBoard output data.
Type: [TensorBoardOutputConfig](API_TensorBoardOutputConfig.md) object
Required: No

 ** [TrainingJobName](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-TrainingJobName"></a>
The name of the training job. The name must be unique within an AWS Region in an AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [VpcConfig](#API_CreateTrainingJob_RequestSyntax) **   <a name="sagemaker-CreateTrainingJob-request-VpcConfig"></a>
A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want your training job to connect to. Control access to and from your training container by configuring the VPC. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateTrainingJob_ResponseSyntax"></a>

```
{
   "TrainingJobArn": "string"
}
```

## Response Elements
<a name="API_CreateTrainingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrainingJobArn](#API_CreateTrainingJob_ResponseSyntax) **   <a name="sagemaker-CreateTrainingJob-response-TrainingJobArn"></a>
The Amazon Resource Name (ARN) of the training job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateTrainingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateTrainingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateTrainingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateTrainingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateTrainingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateTrainingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateTrainingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateTrainingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateTrainingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateTrainingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateTrainingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateTrainingJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
