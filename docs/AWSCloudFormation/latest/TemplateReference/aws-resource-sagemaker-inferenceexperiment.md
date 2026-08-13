---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-inferenceexperiment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceExperiment
<a name="aws-resource-sagemaker-inferenceexperiment"></a>

 Creates an inference experiment using the configurations specified in the request.

 Use this API to setup and schedule an experiment to compare model variants on a Amazon SageMaker inference endpoint. For more information about inference experiments, see [Shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html).

 Amazon SageMaker begins your experiment at the scheduled time and routes traffic to your endpoint's model variants based on your specified configuration.

 While the experiment is in progress or after it has concluded, you can view metrics that compare your model variants. For more information, see [View, monitor, and edit shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit.html).

## Syntax
<a name="aws-resource-sagemaker-inferenceexperiment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-inferenceexperiment-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::InferenceExperiment",
  "Properties" : {
      "[DataStorageConfig](#cfn-sagemaker-inferenceexperiment-datastorageconfig)" : {{DataStorageConfig}},
      "[Description](#cfn-sagemaker-inferenceexperiment-description)" : {{String}},
      "[DesiredState](#cfn-sagemaker-inferenceexperiment-desiredstate)" : {{String}},
      "[EndpointName](#cfn-sagemaker-inferenceexperiment-endpointname)" : {{String}},
      "[KmsKey](#cfn-sagemaker-inferenceexperiment-kmskey)" : {{String}},
      "[ModelVariants](#cfn-sagemaker-inferenceexperiment-modelvariants)" : {{[ ModelVariantConfig, ... ]}},
      "[Name](#cfn-sagemaker-inferenceexperiment-name)" : {{String}},
      "[RoleArn](#cfn-sagemaker-inferenceexperiment-rolearn)" : {{String}},
      "[Schedule](#cfn-sagemaker-inferenceexperiment-schedule)" : {{InferenceExperimentSchedule}},
      "[ShadowModeConfig](#cfn-sagemaker-inferenceexperiment-shadowmodeconfig)" : {{ShadowModeConfig}},
      "[StatusReason](#cfn-sagemaker-inferenceexperiment-statusreason)" : {{String}},
      "[Tags](#cfn-sagemaker-inferenceexperiment-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-sagemaker-inferenceexperiment-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-inferenceexperiment-syntax.yaml"></a>

```
Type: AWS::SageMaker::InferenceExperiment
Properties:
  [DataStorageConfig](#cfn-sagemaker-inferenceexperiment-datastorageconfig): {{
    DataStorageConfig}}
  [Description](#cfn-sagemaker-inferenceexperiment-description): {{String}}
  [DesiredState](#cfn-sagemaker-inferenceexperiment-desiredstate): {{String}}
  [EndpointName](#cfn-sagemaker-inferenceexperiment-endpointname): {{String}}
  [KmsKey](#cfn-sagemaker-inferenceexperiment-kmskey): {{String}}
  [ModelVariants](#cfn-sagemaker-inferenceexperiment-modelvariants): {{
    - ModelVariantConfig}}
  [Name](#cfn-sagemaker-inferenceexperiment-name): {{String}}
  [RoleArn](#cfn-sagemaker-inferenceexperiment-rolearn): {{String}}
  [Schedule](#cfn-sagemaker-inferenceexperiment-schedule): {{
    InferenceExperimentSchedule}}
  [ShadowModeConfig](#cfn-sagemaker-inferenceexperiment-shadowmodeconfig): {{
    ShadowModeConfig}}
  [StatusReason](#cfn-sagemaker-inferenceexperiment-statusreason): {{String}}
  [Tags](#cfn-sagemaker-inferenceexperiment-tags): {{
    - Tag}}
  [Type](#cfn-sagemaker-inferenceexperiment-type): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-inferenceexperiment-properties"></a>

`DataStorageConfig`  <a name="cfn-sagemaker-inferenceexperiment-datastorageconfig"></a>
The Amazon S3 location and configuration for storing inference request and response data.
*Required*: No
*Type*: [DataStorageConfig](aws-properties-sagemaker-inferenceexperiment-datastorageconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-sagemaker-inferenceexperiment-description"></a>
The description of the inference experiment.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DesiredState`  <a name="cfn-sagemaker-inferenceexperiment-desiredstate"></a>
 The desired state of the experiment after stopping. The possible states are the following:
+ `Completed`: The experiment completed successfully
+ `Cancelled`: The experiment was canceled
*Required*: No
*Type*: String
*Allowed values*: `Running | Completed | Cancelled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointName`  <a name="cfn-sagemaker-inferenceexperiment-endpointname"></a>
The name of the endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKey`  <a name="cfn-sagemaker-inferenceexperiment-kmskey"></a>
 The AWS Key Management Service key that Amazon SageMaker uses to encrypt captured data at rest using Amazon S3 server-side encryption.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelVariants`  <a name="cfn-sagemaker-inferenceexperiment-modelvariants"></a>
 An array of `ModelVariantConfigSummary` objects. There is one for each variant in the inference experiment. Each `ModelVariantConfigSummary` object in the array describes the infrastructure configuration for deploying the corresponding variant.
*Required*: Yes
*Type*: Array of [ModelVariantConfig](aws-properties-sagemaker-inferenceexperiment-modelvariantconfig.md)
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-inferenceexperiment-name"></a>
The name of the inference experiment.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-inferenceexperiment-rolearn"></a>
 The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Schedule`  <a name="cfn-sagemaker-inferenceexperiment-schedule"></a>
The duration for which the inference experiment ran or will run.
The maximum duration that you can set for an inference experiment is 30 days.
*Required*: No
*Type*: [InferenceExperimentSchedule](aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShadowModeConfig`  <a name="cfn-sagemaker-inferenceexperiment-shadowmodeconfig"></a>
 The configuration of `ShadowMode` inference experiment type, which shows the production variant that takes all the inference requests, and the shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant it also shows the percentage of requests that Amazon SageMaker replicates.
*Required*: No
*Type*: [ShadowModeConfig](aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusReason`  <a name="cfn-sagemaker-inferenceexperiment-statusreason"></a>
The error message for the inference experiment status result.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-inferenceexperiment-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-inferenceexperiment-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-sagemaker-inferenceexperiment-type"></a>
The type of the inference experiment.
*Required*: Yes
*Type*: String
*Allowed values*: `ShadowMode`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-inferenceexperiment-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-inferenceexperiment-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the inference experiment.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-inferenceexperiment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-inferenceexperiment-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN for your inference experiment.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The timestamp at which the inference experiment was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The timestamp at which you last modified the inference experiment.

`Status`  <a name="Status-fn::getatt"></a>
 The status of the inference experiment. The following are the possible statuses for an inference experiment:
+ `Creating` - Amazon SageMaker is creating your experiment.
+ `Created` - Amazon SageMaker has finished the creation of your experiment and will begin the experiment at the scheduled time.
+ `Updating` - When you make changes to your experiment, your experiment shows as updating.
+ `Starting` - Amazon SageMaker is beginning your experiment.
+ `Running` - Your experiment is in progress.
+ `Stopping` - Amazon SageMaker is stopping your experiment.
+ `Completed` - Your experiment has completed.
+ `Cancelled` - When you conclude your experiment early using the [StopInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html) API, or if any operation fails with an unexpected error, it shows as cancelled.
