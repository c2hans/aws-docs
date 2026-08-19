---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-optimizationjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::OptimizationJob
<a name="aws-resource-sagemaker-optimizationjob"></a>

Creates a job that optimizes a model for inference performance. To create the job, you provide the location of a source model, and you provide the settings for the optimization techniques that you want the job to apply. When the job completes successfully, SageMaker uploads the new optimized model to the output destination that you specify.

For more information about how to use this action, and about the supported optimization techniques, see [Optimize model inference with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html).

## Syntax
<a name="aws-resource-sagemaker-optimizationjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-optimizationjob-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::OptimizationJob",
  "Properties" : {
      "[DeploymentInstanceType](#cfn-sagemaker-optimizationjob-deploymentinstancetype)" : {{String}},
      "[ModelSource](#cfn-sagemaker-optimizationjob-modelsource)" : {{OptimizationJobModelSource}},
      "[OptimizationConfigs](#cfn-sagemaker-optimizationjob-optimizationconfigs)" : {{[ OptimizationConfig, ... ]}},
      "[OptimizationEnvironment](#cfn-sagemaker-optimizationjob-optimizationenvironment)" : {{{{{Key}}: {{Value}}, ...}}},
      "[OptimizationJobName](#cfn-sagemaker-optimizationjob-optimizationjobname)" : {{String}},
      "[OutputConfig](#cfn-sagemaker-optimizationjob-outputconfig)" : {{OptimizationJobOutputConfig}},
      "[RoleArn](#cfn-sagemaker-optimizationjob-rolearn)" : {{String}},
      "[StoppingCondition](#cfn-sagemaker-optimizationjob-stoppingcondition)" : {{StoppingCondition}},
      "[Tags](#cfn-sagemaker-optimizationjob-tags)" : {{[ Tag, ... ]}},
      "[VpcConfig](#cfn-sagemaker-optimizationjob-vpcconfig)" : {{OptimizationVpcConfig}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-optimizationjob-syntax.yaml"></a>

```
Type: AWS::SageMaker::OptimizationJob
Properties:
  [DeploymentInstanceType](#cfn-sagemaker-optimizationjob-deploymentinstancetype): {{String}}
  [ModelSource](#cfn-sagemaker-optimizationjob-modelsource): {{
    OptimizationJobModelSource}}
  [OptimizationConfigs](#cfn-sagemaker-optimizationjob-optimizationconfigs): {{
    - OptimizationConfig}}
  [OptimizationEnvironment](#cfn-sagemaker-optimizationjob-optimizationenvironment): {{
    {{Key}}: {{Value}}}}
  [OptimizationJobName](#cfn-sagemaker-optimizationjob-optimizationjobname): {{String}}
  [OutputConfig](#cfn-sagemaker-optimizationjob-outputconfig): {{
    OptimizationJobOutputConfig}}
  [RoleArn](#cfn-sagemaker-optimizationjob-rolearn): {{String}}
  [StoppingCondition](#cfn-sagemaker-optimizationjob-stoppingcondition): {{
    StoppingCondition}}
  [Tags](#cfn-sagemaker-optimizationjob-tags): {{
    - Tag}}
  [VpcConfig](#cfn-sagemaker-optimizationjob-vpcconfig): {{
    OptimizationVpcConfig}}
```

## Properties
<a name="aws-resource-sagemaker-optimizationjob-properties"></a>

`DeploymentInstanceType`  <a name="cfn-sagemaker-optimizationjob-deploymentinstancetype"></a>
The type of instance that hosts the optimized model that you create with the optimization job.
*Required*: Yes
*Type*: String
*Allowed values*: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.p6-b200.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelSource`  <a name="cfn-sagemaker-optimizationjob-modelsource"></a>
Property description not available.
*Required*: Yes
*Type*: [OptimizationJobModelSource](aws-properties-sagemaker-optimizationjob-optimizationjobmodelsource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OptimizationConfigs`  <a name="cfn-sagemaker-optimizationjob-optimizationconfigs"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [OptimizationConfig](aws-properties-sagemaker-optimizationjob-optimizationconfig.md)
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OptimizationEnvironment`  <a name="cfn-sagemaker-optimizationjob-optimizationenvironment"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OptimizationJobName`  <a name="cfn-sagemaker-optimizationjob-optimizationjobname"></a>
The name that you assigned to the optimization job.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputConfig`  <a name="cfn-sagemaker-optimizationjob-outputconfig"></a>
Contains information about the output location for the compiled model and the target device that the model runs on. `TargetDevice` and `TargetPlatform` are mutually exclusive, so you need to choose one between the two to specify your target device or platform. If you cannot find your device you want to use from the `TargetDevice` list, use `TargetPlatform` to describe the platform of your edge device and `CompilerOptions` if there are specific settings that are required or recommended to use for particular TargetPlatform.
*Required*: Yes
*Type*: [OptimizationJobOutputConfig](aws-properties-sagemaker-optimizationjob-optimizationjoboutputconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-optimizationjob-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StoppingCondition`  <a name="cfn-sagemaker-optimizationjob-stoppingcondition"></a>
Specifies a limit to how long a job can run. When the job reaches the time limit, SageMaker ends the job. Use this API to cap costs.
To stop a training job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.
The training algorithms provided by SageMaker automatically save the intermediate results of a model training job when possible. This attempt to save artifacts is only a best effort case as model might not be in a state from which it can be saved. For example, if training has just started, the model might not be ready to save. When saved, this intermediate data is a valid model artifact. You can use it to create a model with `CreateModel`.
The Neural Topic Model (NTM) currently does not support saving intermediate model artifacts. When training NTMs, make sure that the maximum runtime is sufficient for the training job to complete.
*Required*: Yes
*Type*: [StoppingCondition](aws-properties-sagemaker-optimizationjob-stoppingcondition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-optimizationjob-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-optimizationjob-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-sagemaker-optimizationjob-vpcconfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
*Required*: No
*Type*: [OptimizationVpcConfig](aws-properties-sagemaker-optimizationjob-optimizationvpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-optimizationjob-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-optimizationjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-optimizationjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-optimizationjob-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time when you created the optimization job.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time when the optimization job was last updated.

`OptimizationJobArn`  <a name="OptimizationJobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the optimization job.

`OptimizationJobStatus`  <a name="OptimizationJobStatus-fn::getatt"></a>
The current status of the optimization job.
