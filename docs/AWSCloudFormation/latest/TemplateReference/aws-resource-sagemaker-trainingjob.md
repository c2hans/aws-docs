---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-trainingjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob
<a name="aws-resource-sagemaker-trainingjob"></a>

Contains information about a training job.

## Syntax
<a name="aws-resource-sagemaker-trainingjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-trainingjob-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::TrainingJob",
  "Properties" : {
      "[AlgorithmSpecification](#cfn-sagemaker-trainingjob-algorithmspecification)" : {{AlgorithmSpecification}},
      "[CheckpointConfig](#cfn-sagemaker-trainingjob-checkpointconfig)" : {{CheckpointConfig}},
      "[DebugHookConfig](#cfn-sagemaker-trainingjob-debughookconfig)" : {{DebugHookConfig}},
      "[DebugRuleConfigurations](#cfn-sagemaker-trainingjob-debugruleconfigurations)" : {{[ DebugRuleConfiguration, ... ]}},
      "[EnableInterContainerTrafficEncryption](#cfn-sagemaker-trainingjob-enableintercontainertrafficencryption)" : {{Boolean}},
      "[EnableManagedSpotTraining](#cfn-sagemaker-trainingjob-enablemanagedspottraining)" : {{Boolean}},
      "[EnableNetworkIsolation](#cfn-sagemaker-trainingjob-enablenetworkisolation)" : {{Boolean}},
      "[Environment](#cfn-sagemaker-trainingjob-environment)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ExperimentConfig](#cfn-sagemaker-trainingjob-experimentconfig)" : {{ExperimentConfig}},
      "[HyperParameters](#cfn-sagemaker-trainingjob-hyperparameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[InfraCheckConfig](#cfn-sagemaker-trainingjob-infracheckconfig)" : {{InfraCheckConfig}},
      "[InputDataConfig](#cfn-sagemaker-trainingjob-inputdataconfig)" : {{[ Channel, ... ]}},
      "[OutputDataConfig](#cfn-sagemaker-trainingjob-outputdataconfig)" : {{OutputDataConfig}},
      "[ProfilerConfig](#cfn-sagemaker-trainingjob-profilerconfig)" : {{ProfilerConfig}},
      "[ProfilerRuleConfigurations](#cfn-sagemaker-trainingjob-profilerruleconfigurations)" : {{[ ProfilerRuleConfiguration, ... ]}},
      "[RemoteDebugConfig](#cfn-sagemaker-trainingjob-remotedebugconfig)" : {{RemoteDebugConfig}},
      "[ResourceConfig](#cfn-sagemaker-trainingjob-resourceconfig)" : {{ResourceConfig}},
      "[RetryStrategy](#cfn-sagemaker-trainingjob-retrystrategy)" : {{RetryStrategy}},
      "[RoleArn](#cfn-sagemaker-trainingjob-rolearn)" : {{String}},
      "[StoppingCondition](#cfn-sagemaker-trainingjob-stoppingcondition)" : {{StoppingCondition}},
      "[Tags](#cfn-sagemaker-trainingjob-tags)" : {{[ Tag, ... ]}},
      "[TensorBoardOutputConfig](#cfn-sagemaker-trainingjob-tensorboardoutputconfig)" : {{TensorBoardOutputConfig}},
      "[TrainingJobName](#cfn-sagemaker-trainingjob-trainingjobname)" : {{String}},
      "[VpcConfig](#cfn-sagemaker-trainingjob-vpcconfig)" : {{VpcConfig}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-trainingjob-syntax.yaml"></a>

```
Type: AWS::SageMaker::TrainingJob
Properties:
  [AlgorithmSpecification](#cfn-sagemaker-trainingjob-algorithmspecification): {{
    AlgorithmSpecification}}
  [CheckpointConfig](#cfn-sagemaker-trainingjob-checkpointconfig): {{
    CheckpointConfig}}
  [DebugHookConfig](#cfn-sagemaker-trainingjob-debughookconfig): {{
    DebugHookConfig}}
  [DebugRuleConfigurations](#cfn-sagemaker-trainingjob-debugruleconfigurations): {{
    - DebugRuleConfiguration}}
  [EnableInterContainerTrafficEncryption](#cfn-sagemaker-trainingjob-enableintercontainertrafficencryption): {{Boolean}}
  [EnableManagedSpotTraining](#cfn-sagemaker-trainingjob-enablemanagedspottraining): {{Boolean}}
  [EnableNetworkIsolation](#cfn-sagemaker-trainingjob-enablenetworkisolation): {{Boolean}}
  [Environment](#cfn-sagemaker-trainingjob-environment): {{
    {{Key}}: {{Value}}}}
  [ExperimentConfig](#cfn-sagemaker-trainingjob-experimentconfig): {{
    ExperimentConfig}}
  [HyperParameters](#cfn-sagemaker-trainingjob-hyperparameters): {{
    {{Key}}: {{Value}}}}
  [InfraCheckConfig](#cfn-sagemaker-trainingjob-infracheckconfig): {{
    InfraCheckConfig}}
  [InputDataConfig](#cfn-sagemaker-trainingjob-inputdataconfig): {{
    - Channel}}
  [OutputDataConfig](#cfn-sagemaker-trainingjob-outputdataconfig): {{
    OutputDataConfig}}
  [ProfilerConfig](#cfn-sagemaker-trainingjob-profilerconfig): {{
    ProfilerConfig}}
  [ProfilerRuleConfigurations](#cfn-sagemaker-trainingjob-profilerruleconfigurations): {{
    - ProfilerRuleConfiguration}}
  [RemoteDebugConfig](#cfn-sagemaker-trainingjob-remotedebugconfig): {{
    RemoteDebugConfig}}
  [ResourceConfig](#cfn-sagemaker-trainingjob-resourceconfig): {{
    ResourceConfig}}
  [RetryStrategy](#cfn-sagemaker-trainingjob-retrystrategy): {{
    RetryStrategy}}
  [RoleArn](#cfn-sagemaker-trainingjob-rolearn): {{String}}
  [StoppingCondition](#cfn-sagemaker-trainingjob-stoppingcondition): {{
    StoppingCondition}}
  [Tags](#cfn-sagemaker-trainingjob-tags): {{
    - Tag}}
  [TensorBoardOutputConfig](#cfn-sagemaker-trainingjob-tensorboardoutputconfig): {{
    TensorBoardOutputConfig}}
  [TrainingJobName](#cfn-sagemaker-trainingjob-trainingjobname): {{String}}
  [VpcConfig](#cfn-sagemaker-trainingjob-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-resource-sagemaker-trainingjob-properties"></a>

`AlgorithmSpecification`  <a name="cfn-sagemaker-trainingjob-algorithmspecification"></a>
Information about the algorithm used for training, and algorithm metadata.
*Required*: Yes
*Type*: [AlgorithmSpecification](aws-properties-sagemaker-trainingjob-algorithmspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CheckpointConfig`  <a name="cfn-sagemaker-trainingjob-checkpointconfig"></a>
Contains information about the output location for managed spot training checkpoint data.
*Required*: No
*Type*: [CheckpointConfig](aws-properties-sagemaker-trainingjob-checkpointconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DebugHookConfig`  <a name="cfn-sagemaker-trainingjob-debughookconfig"></a>
Configuration information for the Amazon SageMaker Debugger hook parameters, metric and tensor collections, and storage paths. To learn more about how to configure the `DebugHookConfig` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).
*Required*: No
*Type*: [DebugHookConfig](aws-properties-sagemaker-trainingjob-debughookconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DebugRuleConfigurations`  <a name="cfn-sagemaker-trainingjob-debugruleconfigurations"></a>
Information about the debug rule configuration.
*Required*: No
*Type*: Array of [DebugRuleConfiguration](aws-properties-sagemaker-trainingjob-debugruleconfiguration.md)
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableInterContainerTrafficEncryption`  <a name="cfn-sagemaker-trainingjob-enableintercontainertrafficencryption"></a>
To encrypt all communications between ML compute instances in distributed training, choose `True`. Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableManagedSpotTraining`  <a name="cfn-sagemaker-trainingjob-enablemanagedspottraining"></a>
When true, enables managed spot training using Amazon EC2 Spot instances to run training jobs instead of on-demand instances. For more information, see [Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html).
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableNetworkIsolation`  <a name="cfn-sagemaker-trainingjob-enablenetworkisolation"></a>
If the `TrainingJob` was created with network isolation, the value is set to `true`. If network isolation is enabled, nodes can't communicate beyond the VPC they run in.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-sagemaker-trainingjob-environment"></a>
The environment variables to set in the Docker container.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExperimentConfig`  <a name="cfn-sagemaker-trainingjob-experimentconfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
*Required*: No
*Type*: [ExperimentConfig](aws-properties-sagemaker-trainingjob-experimentconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HyperParameters`  <a name="cfn-sagemaker-trainingjob-hyperparameters"></a>
Algorithm-specific parameters.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Maximum*: `2500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InfraCheckConfig`  <a name="cfn-sagemaker-trainingjob-infracheckconfig"></a>
Configuration information for the infrastructure health check of a training job. A SageMaker-provided health check tests the health of instance hardware and cluster network connectivity.
*Required*: No
*Type*: [InfraCheckConfig](aws-properties-sagemaker-trainingjob-infracheckconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputDataConfig`  <a name="cfn-sagemaker-trainingjob-inputdataconfig"></a>
An array of `Channel` objects that describes each data input channel.
Your input must be in the same AWS region as your training job.
*Required*: No
*Type*: Array of [Channel](aws-properties-sagemaker-trainingjob-channel.md)
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputDataConfig`  <a name="cfn-sagemaker-trainingjob-outputdataconfig"></a>
The S3 path where model artifacts that you configured when creating the job are stored. SageMaker creates subfolders for model artifacts.
*Required*: Yes
*Type*: [OutputDataConfig](aws-properties-sagemaker-trainingjob-outputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfilerConfig`  <a name="cfn-sagemaker-trainingjob-profilerconfig"></a>
Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.
*Required*: No
*Type*: [ProfilerConfig](aws-properties-sagemaker-trainingjob-profilerconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfilerRuleConfigurations`  <a name="cfn-sagemaker-trainingjob-profilerruleconfigurations"></a>
Property description not available.
*Required*: No
*Type*: Array of [ProfilerRuleConfiguration](aws-properties-sagemaker-trainingjob-profilerruleconfiguration.md)
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RemoteDebugConfig`  <a name="cfn-sagemaker-trainingjob-remotedebugconfig"></a>
Configuration for remote debugging for the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API. To learn more about the remote debugging functionality of SageMaker, see [Access a training container through AWS Systems Manager (SSM) for remote debugging](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html).
*Required*: No
*Type*: [RemoteDebugConfig](aws-properties-sagemaker-trainingjob-remotedebugconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceConfig`  <a name="cfn-sagemaker-trainingjob-resourceconfig"></a>
Resources, including ML compute instances and ML storage volumes, that are configured for model training.
*Required*: Yes
*Type*: [ResourceConfig](aws-properties-sagemaker-trainingjob-resourceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetryStrategy`  <a name="cfn-sagemaker-trainingjob-retrystrategy"></a>
The number of times to retry the job when the job fails due to an `InternalServerError`.
*Required*: No
*Type*: [RetryStrategy](aws-properties-sagemaker-trainingjob-retrystrategy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-trainingjob-rolearn"></a>
The AWS Identity and Access Management (IAM) role configured for the training job.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StoppingCondition`  <a name="cfn-sagemaker-trainingjob-stoppingcondition"></a>
Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.
To stop a job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.
*Required*: Yes
*Type*: [StoppingCondition](aws-properties-sagemaker-trainingjob-stoppingcondition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-trainingjob-tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-trainingjob-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TensorBoardOutputConfig`  <a name="cfn-sagemaker-trainingjob-tensorboardoutputconfig"></a>
Contains information about the output location for the compiled model and the target device that the model runs on. `TargetDevice` and `TargetPlatform` are mutually exclusive, so you need to choose one between the two to specify your target device or platform. If you cannot find your device you want to use from the `TargetDevice` list, use `TargetPlatform` to describe the platform of your edge device and `CompilerOptions` if there are specific settings that are required or recommended to use for particular TargetPlatform.
*Required*: No
*Type*: [TensorBoardOutputConfig](aws-properties-sagemaker-trainingjob-tensorboardoutputconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingJobName`  <a name="cfn-sagemaker-trainingjob-trainingjobname"></a>
The name of the training job.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-sagemaker-trainingjob-vpcconfig"></a>
A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that this training job has access to. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html).
*Required*: No
*Type*: [VpcConfig](aws-properties-sagemaker-trainingjob-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-trainingjob-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-trainingjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-trainingjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-trainingjob-return-values-fn--getatt-fn--getatt"></a>

`BillableTimeInSeconds`  <a name="BillableTimeInSeconds-fn::getatt"></a>
The billable time in seconds.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
A timestamp that indicates when the training job was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
A timestamp that indicates when the status of the training job was last modified.

`ProfilingStatus`  <a name="ProfilingStatus-fn::getatt"></a>
Property description not available.

`SecondaryStatus`  <a name="SecondaryStatus-fn::getatt"></a>
 Provides detailed information about the state of the training job. For detailed information about the secondary status of the training job, see `StatusMessage` under [SecondaryStatusTransition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SecondaryStatusTransition.html).
SageMaker provides primary statuses and secondary statuses that apply to each of them:
InProgress
+ `Starting` - Starting the training job.
+ `Downloading` - An optional stage for algorithms that support `File` training input mode. It indicates that data is being downloaded to the ML storage volumes.
+ `Training` - Training is in progress.
+ `Uploading` - Training is complete and the model artifacts are being uploaded to the S3 location.
Completed
+ `Completed` - The training job has completed.
Failed
+ `Failed` - The training job has failed. The reason for the failure is returned in the `FailureReason` field of `DescribeTrainingJobResponse`.
Stopped
+ `MaxRuntimeExceeded` - The job stopped because it exceeded the maximum allowed runtime.
+ `Stopped` - The training job has stopped.
Stopping
+ `Stopping` - Stopping the training job.
Valid values for `SecondaryStatus` are subject to change.
We no longer support the following secondary statuses:
+  `LaunchingMLInstances`
+  `PreparingTrainingStack`
+  `DownloadingTrainingImage`

`SecondaryStatusTransitions`  <a name="SecondaryStatusTransitions-fn::getatt"></a>
A history of all of the secondary statuses that the training job has transitioned through.

`TrainingJobArn`  <a name="TrainingJobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the training job.

`TrainingJobStatus`  <a name="TrainingJobStatus-fn::getatt"></a>
The status of the training job.
Training job statuses are:
+ `InProgress` - The training is in progress.
+ `Completed` - The training job has completed.
+ `Failed` - The training job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTrainingJobResponse` call.
+ `Stopping` - The training job is stopping.
+ `Stopped` - The training job has stopped.
For more detailed information, see `SecondaryStatus`.

`TrainingTimeInSeconds`  <a name="TrainingTimeInSeconds-fn::getatt"></a>
The training time in seconds.
