---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-trainingjobdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob TrainingJobDefinition
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobdefinition"></a>

Defines the input needed to run a training job using the algorithm.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobdefinition-syntax.json"></a>

```
{
  "[AlgorithmSpecification](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-algorithmspecification)" : {{AlgorithmSpecification}},
  "[CheckpointConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-checkpointconfig)" : {{CheckpointConfig}},
  "[DefinitionName](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-definitionname)" : {{String}},
  "[EnableInterContainerTrafficEncryption](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-enableintercontainertrafficencryption)" : {{Boolean}},
  "[EnableManagedSpotTraining](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-enablemanagedspottraining)" : {{Boolean}},
  "[EnableNetworkIsolation](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-enablenetworkisolation)" : {{Boolean}},
  "[Environment](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-environment)" : {{{{{Key}}: {{Value}}, ...}}},
  "[HyperParameterRanges](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-hyperparameterranges)" : {{ParameterRanges}},
  "[InputDataConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-inputdataconfig)" : {{[ InputDataConfigItems, ... ]}},
  "[OutputDataConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-outputdataconfig)" : {{OutputDataConfig}},
  "[ResourceConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-resourceconfig)" : {{ResourceConfig}},
  "[RetryStrategy](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-retrystrategy)" : {{RetryStrategy}},
  "[RoleArn](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-rolearn)" : {{String}},
  "[StaticHyperParameters](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-statichyperparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[StoppingCondition](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-stoppingcondition)" : {{StoppingCondition}},
  "[TuningObjective](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-tuningobjective)" : {{TuningObjective}},
  "[VpcConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-vpcconfig)" : {{VpcConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobdefinition-syntax.yaml"></a>

```
  [AlgorithmSpecification](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-algorithmspecification): {{
    AlgorithmSpecification}}
  [CheckpointConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-checkpointconfig): {{
    CheckpointConfig}}
  [DefinitionName](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-definitionname): {{String}}
  [EnableInterContainerTrafficEncryption](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-enableintercontainertrafficencryption): {{Boolean}}
  [EnableManagedSpotTraining](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-enablemanagedspottraining): {{Boolean}}
  [EnableNetworkIsolation](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-enablenetworkisolation): {{Boolean}}
  [Environment](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-environment): {{
    {{Key}}: {{Value}}}}
  [HyperParameterRanges](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-hyperparameterranges): {{
    ParameterRanges}}
  [InputDataConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-inputdataconfig): {{
    - InputDataConfigItems}}
  [OutputDataConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-outputdataconfig): {{
    OutputDataConfig}}
  [ResourceConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-resourceconfig): {{
    ResourceConfig}}
  [RetryStrategy](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-retrystrategy): {{
    RetryStrategy}}
  [RoleArn](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-rolearn): {{String}}
  [StaticHyperParameters](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-statichyperparameters): {{
    {{Key}}: {{Value}}}}
  [StoppingCondition](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-stoppingcondition): {{
    StoppingCondition}}
  [TuningObjective](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-tuningobjective): {{
    TuningObjective}}
  [VpcConfig](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-trainingjobdefinition-properties"></a>

`AlgorithmSpecification`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-algorithmspecification"></a>
Property description not available.
*Required*: Yes
*Type*: [AlgorithmSpecification](aws-properties-sagemaker-hyperparametertuningjob-algorithmspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CheckpointConfig`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-checkpointconfig"></a>
Property description not available.
*Required*: No
*Type*: [CheckpointConfig](aws-properties-sagemaker-hyperparametertuningjob-checkpointconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefinitionName`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-definitionname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableInterContainerTrafficEncryption`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-enableintercontainertrafficencryption"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableManagedSpotTraining`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-enablemanagedspottraining"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableNetworkIsolation`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-enablenetworkisolation"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-environment"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]*$`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HyperParameterRanges`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-hyperparameterranges"></a>
Property description not available.
*Required*: No
*Type*: [ParameterRanges](aws-properties-sagemaker-hyperparametertuningjob-parameterranges.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputDataConfig`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-inputdataconfig"></a>
An array of `Channel` objects, each of which specifies an input source.
*Required*: No
*Type*: Array of [InputDataConfigItems](aws-properties-sagemaker-hyperparametertuningjob-inputdataconfigitems.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputDataConfig`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-outputdataconfig"></a>
the path to the S3 bucket where you want to store model artifacts. SageMaker creates subfolders for the artifacts.
*Required*: Yes
*Type*: [OutputDataConfig](aws-properties-sagemaker-hyperparametertuningjob-outputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceConfig`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-resourceconfig"></a>
The resources, including the ML compute instances and ML storage volumes, to use for model training.
*Required*: No
*Type*: [ResourceConfig](aws-properties-sagemaker-hyperparametertuningjob-resourceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetryStrategy`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-retrystrategy"></a>
Property description not available.
*Required*: No
*Type*: [RetryStrategy](aws-properties-sagemaker-hyperparametertuningjob-retrystrategy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StaticHyperParameters`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-statichyperparameters"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `2500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StoppingCondition`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-stoppingcondition"></a>
Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.
To stop a job, SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts.
*Required*: Yes
*Type*: [StoppingCondition](aws-properties-sagemaker-hyperparametertuningjob-stoppingcondition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TuningObjective`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-tuningobjective"></a>
Property description not available.
*Required*: No
*Type*: [TuningObjective](aws-properties-sagemaker-hyperparametertuningjob-tuningobjective.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition-vpcconfig"></a>
Property description not available.
*Required*: No
*Type*: [VpcConfig](aws-properties-sagemaker-hyperparametertuningjob-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
