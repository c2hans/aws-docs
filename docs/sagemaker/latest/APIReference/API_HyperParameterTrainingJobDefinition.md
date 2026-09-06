---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html
---

# HyperParameterTrainingJobDefinition
<a name="API_HyperParameterTrainingJobDefinition"></a>

Defines the training jobs launched by a hyperparameter tuning job.

## Contents
<a name="API_HyperParameterTrainingJobDefinition_Contents"></a>

 ** AlgorithmSpecification **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-AlgorithmSpecification"></a>
The [HyperParameterAlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterAlgorithmSpecification.html) object that specifies the resource algorithm to use for the training jobs that the tuning job launches.
Type: [HyperParameterAlgorithmSpecification](API_HyperParameterAlgorithmSpecification.md) object
Required: Yes

 ** OutputDataConfig **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-OutputDataConfig"></a>
Specifies the path to the Amazon S3 bucket where you store model artifacts from the training jobs that the tuning job launches.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: Yes

 ** RoleArn **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** StoppingCondition **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-StoppingCondition"></a>
Specifies a limit to how long a model hyperparameter training job can run. It also specifies how long a managed spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.
Type: [StoppingCondition](API_StoppingCondition.md) object
Required: Yes

 ** CheckpointConfig **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-CheckpointConfig"></a>
Contains information about the output location for managed spot training checkpoint data.
Type: [CheckpointConfig](API_CheckpointConfig.md) object
Required: No

 ** DefinitionName **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-DefinitionName"></a>
The job definition name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: No

 ** EnableInterContainerTrafficEncryption **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-EnableInterContainerTrafficEncryption"></a>
To encrypt all communications between ML compute instances in distributed training, choose `True`. Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.
Type: Boolean
Required: No

 ** EnableManagedSpotTraining **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-EnableManagedSpotTraining"></a>
A Boolean indicating whether managed spot training is enabled (`True`) or not (`False`).
Type: Boolean
Required: No

 ** EnableNetworkIsolation **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-EnableNetworkIsolation"></a>
Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.
Type: Boolean
Required: No

 ** Environment **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-Environment"></a>
An environment variable that you can pass into the SageMaker [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API. You can use an existing [environment variable from the training container](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html#sagemaker-CreateTrainingJob-request-Environment) or use your own. See [Define metrics and variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) for more information.
The maximum number of items specified for `Map Entries` refers to the maximum number of environment variables for each `TrainingJobDefinition` and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of environment variables for all the training job definitions can't exceed the maximum number specified.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 48 items.
Key Length Constraints: Minimum length of 0. Maximum length of 512.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 512.
Value Pattern: `[\S\s]*`
Required: No

 ** HyperParameterRanges **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-HyperParameterRanges"></a>
Specifies ranges of integer, continuous, and categorical hyperparameters that a hyperparameter tuning job searches. The hyperparameter tuning job launches training jobs with hyperparameter values within these ranges to find the combination of values that result in the training job with the best performance as measured by the objective metric of the hyperparameter tuning job.
The maximum number of items specified for `Array Members` refers to the maximum number of hyperparameters for each range and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of hyperparameters for all the ranges can't exceed the maximum number specified.
Type: [ParameterRanges](API_ParameterRanges.md) object
Required: No

 ** HyperParameterTuningResourceConfig **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-HyperParameterTuningResourceConfig"></a>
The configuration for the hyperparameter tuning resources, including the compute instances and storage volumes, used for training jobs launched by the tuning job. By default, storage volumes hold model artifacts and incremental states. Choose `File` for `TrainingInputMode` in the `AlgorithmSpecification` parameter to additionally store training data in the storage volume (optional).
Type: [HyperParameterTuningResourceConfig](API_HyperParameterTuningResourceConfig.md) object
Required: No

 ** InputDataConfig **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-InputDataConfig"></a>
An array of [Channel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html) objects that specify the input for the training jobs that the tuning job launches.
Type: Array of [Channel](API_Channel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** ResourceConfig **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-ResourceConfig"></a>
The resources, including the compute instances and storage volumes, to use for the training jobs that the tuning job launches.
Storage volumes store model artifacts and incremental states. Training algorithms might also use storage volumes for scratch space. If you want SageMaker to use the storage volume to store the training data, choose `File` as the `TrainingInputMode` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
If you want to use hyperparameter optimization with instance type flexibility, use `HyperParameterTuningResourceConfig` instead.
Type: [ResourceConfig](API_ResourceConfig.md) object
Required: No

 ** RetryStrategy **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-RetryStrategy"></a>
The number of times to retry the job when the job fails due to an `InternalServerError`.
Type: [RetryStrategy](API_RetryStrategy.md) object
Required: No

 ** StaticHyperParameters **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-StaticHyperParameters"></a>
Specifies the values of hyperparameters that do not change for the tuning job.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`
Required: No

 ** TuningObjective **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective"></a>
Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the `Type` parameter. If you want to define a custom objective metric, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html).
Type: [HyperParameterTuningJobObjective](API_HyperParameterTuningJobObjective.md) object
Required: No

 ** VpcConfig **   <a name="sagemaker-Type-HyperParameterTrainingJobDefinition-VpcConfig"></a>
The [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_HyperParameterTrainingJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterTrainingJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterTrainingJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterTrainingJobDefinition)
