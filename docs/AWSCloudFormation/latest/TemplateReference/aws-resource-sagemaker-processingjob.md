---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-processingjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob
<a name="aws-resource-sagemaker-processingjob"></a>

An Amazon SageMaker processing job that is used to analyze data and evaluate models. For more information, see [Process Data and Evaluate Models](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html).

Also, note the following details specific to processing jobs created using CloudFormation stacks:
+ When you delete a CloudFormation stack with a processing job resource, the processing job is stopped using the [StopProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopProcessingJob.html) API but not deleted. Any tags associated with the processing job are deleted using the [DeleteTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTags.html) API.
+ If any part of your CloudFormation stack deployment fails and a rollback initiates, processing jobs with a specified `ProcessingJobName` value might cause the stack to become stuck in a failed state. This occurs because during a rollback, CloudFormation attempts to recreate the stack resources. Processing job names must be unique, so when CloudFormation attempts to recreate a processing job using the already defined name, this results in an `AlreadyExists` error. To prevent this, we recommend that you don't specify the optional `ProcessingJobName` property, thereby allowing SageMaker to auto-generate a unique name for your processing job. This ensures successful stack rollbacks when necessary. If you must use custom job names, you have to manually modify the `ProcessingJobName` and redeploy the stack to recover from a failed rollback.

## Syntax
<a name="aws-resource-sagemaker-processingjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-processingjob-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::ProcessingJob",
  "Properties" : {
      "[AppSpecification](#cfn-sagemaker-processingjob-appspecification)" : {{AppSpecification}},
      "[Environment](#cfn-sagemaker-processingjob-environment)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ExperimentConfig](#cfn-sagemaker-processingjob-experimentconfig)" : {{ExperimentConfig}},
      "[NetworkConfig](#cfn-sagemaker-processingjob-networkconfig)" : {{NetworkConfig}},
      "[ProcessingInputs](#cfn-sagemaker-processingjob-processinginputs)" : {{[ ProcessingInputsObject, ... ]}},
      "[ProcessingJobName](#cfn-sagemaker-processingjob-processingjobname)" : {{String}},
      "[ProcessingOutputConfig](#cfn-sagemaker-processingjob-processingoutputconfig)" : {{ProcessingOutputConfig}},
      "[ProcessingResources](#cfn-sagemaker-processingjob-processingresources)" : {{ProcessingResources}},
      "[RoleArn](#cfn-sagemaker-processingjob-rolearn)" : {{String}},
      "[StoppingCondition](#cfn-sagemaker-processingjob-stoppingcondition)" : {{StoppingCondition}},
      "[Tags](#cfn-sagemaker-processingjob-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-processingjob-syntax.yaml"></a>

```
Type: AWS::SageMaker::ProcessingJob
Properties:
  [AppSpecification](#cfn-sagemaker-processingjob-appspecification): {{
    AppSpecification}}
  [Environment](#cfn-sagemaker-processingjob-environment): {{
    {{Key}}: {{Value}}}}
  [ExperimentConfig](#cfn-sagemaker-processingjob-experimentconfig): {{
    ExperimentConfig}}
  [NetworkConfig](#cfn-sagemaker-processingjob-networkconfig): {{
    NetworkConfig}}
  [ProcessingInputs](#cfn-sagemaker-processingjob-processinginputs): {{
    - ProcessingInputsObject}}
  [ProcessingJobName](#cfn-sagemaker-processingjob-processingjobname): {{String}}
  [ProcessingOutputConfig](#cfn-sagemaker-processingjob-processingoutputconfig): {{
    ProcessingOutputConfig}}
  [ProcessingResources](#cfn-sagemaker-processingjob-processingresources): {{
    ProcessingResources}}
  [RoleArn](#cfn-sagemaker-processingjob-rolearn): {{String}}
  [StoppingCondition](#cfn-sagemaker-processingjob-stoppingcondition): {{
    StoppingCondition}}
  [Tags](#cfn-sagemaker-processingjob-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-processingjob-properties"></a>

`AppSpecification`  <a name="cfn-sagemaker-processingjob-appspecification"></a>
Configuration to run a processing job in a specified container image.
*Required*: Yes
*Type*: [AppSpecification](aws-properties-sagemaker-processingjob-appspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-sagemaker-processingjob-environment"></a>
Sets the environment variables in the Docker container.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]{0,255}$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExperimentConfig`  <a name="cfn-sagemaker-processingjob-experimentconfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html) API.
*Required*: No
*Type*: [ExperimentConfig](aws-properties-sagemaker-processingjob-experimentconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkConfig`  <a name="cfn-sagemaker-processingjob-networkconfig"></a>
Networking options for a job, such as network traffic encryption between containers, whether to allow inbound and outbound network calls to and from containers, and the VPC subnets and security groups to use for VPC-enabled jobs.
*Required*: No
*Type*: [NetworkConfig](aws-properties-sagemaker-processingjob-networkconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProcessingInputs`  <a name="cfn-sagemaker-processingjob-processinginputs"></a>
List of input configurations for the processing job.
*Required*: No
*Type*: Array of [ProcessingInputsObject](aws-properties-sagemaker-processingjob-processinginputsobject.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProcessingJobName`  <a name="cfn-sagemaker-processingjob-processingjobname"></a>
The name of the processing job. If you don't provide a job name, then a unique name is automatically created for the job.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProcessingOutputConfig`  <a name="cfn-sagemaker-processingjob-processingoutputconfig"></a>
Contains information about the output location for the compiled model and the target device that the model runs on. `TargetDevice` and `TargetPlatform` are mutually exclusive, so you need to choose one between the two to specify your target device or platform. If you cannot find your device you want to use from the `TargetDevice` list, use `TargetPlatform` to describe the platform of your edge device and `CompilerOptions` if there are specific settings that are required or recommended to use for particular TargetPlatform.
*Required*: No
*Type*: [ProcessingOutputConfig](aws-properties-sagemaker-processingjob-processingoutputconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProcessingResources`  <a name="cfn-sagemaker-processingjob-processingresources"></a>
Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.
*Required*: Yes
*Type*: [ProcessingResources](aws-properties-sagemaker-processingjob-processingresources.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-processingjob-rolearn"></a>
The ARN of the role used to create the processing job.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StoppingCondition`  <a name="cfn-sagemaker-processingjob-stoppingcondition"></a>
Configures conditions under which the processing job should be stopped, such as how long the processing job has been running. After the condition is met, the processing job is stopped.
*Required*: No
*Type*: [StoppingCondition](aws-properties-sagemaker-processingjob-stoppingcondition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-processingjob-tags"></a>
An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL) in the *AWS Billing and Cost Management User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-processingjob-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-processingjob-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-processingjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-processingjob-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-processingjob-return-values-fn--getatt-fn--getatt"></a>

`AutoMLJobArn`  <a name="AutoMLJobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AutoML job associated with this processing job.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the processing job was created.

`ExitMessage`  <a name="ExitMessage-fn::getatt"></a>
A string, up to one KB in size, that contains metadata from the processing container when the processing job exits.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
A string, up to one KB in size, that contains the reason a processing job failed, if it failed.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time the processing job was last modified.

`MonitoringScheduleArn`  <a name="MonitoringScheduleArn-fn::getatt"></a>
The ARN of a monitoring schedule for an endpoint associated with this processing job.

`ProcessingEndTime`  <a name="ProcessingEndTime-fn::getatt"></a>
The time that the processing job ended.

`ProcessingJobArn`  <a name="ProcessingJobArn-fn::getatt"></a>
The ARN of the processing job.

`ProcessingJobStatus`  <a name="ProcessingJobStatus-fn::getatt"></a>
The status of the processing job.

`ProcessingStartTime`  <a name="ProcessingStartTime-fn::getatt"></a>
The time that the processing job started.

`TrainingJobArn`  <a name="TrainingJobArn-fn::getatt"></a>
The ARN of the training job associated with this processing job.
