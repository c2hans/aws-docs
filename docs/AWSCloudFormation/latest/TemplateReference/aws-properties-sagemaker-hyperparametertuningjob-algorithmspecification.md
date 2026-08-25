---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-algorithmspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob AlgorithmSpecification
<a name="aws-properties-sagemaker-hyperparametertuningjob-algorithmspecification"></a>

Specifies the training algorithm to use in a [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) request.

**Important**
SageMaker uses its own SageMaker account credentials to pull and access built-in algorithms so built-in algorithms are universally accessible across all AWS accounts. As a result, built-in algorithms have standard, unrestricted access. You cannot restrict built-in algorithms using IAM roles. Use custom algorithms if you require specific access controls.

For more information about algorithms provided by SageMaker, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). For information about using your own algorithms, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-algorithmspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-algorithmspecification-syntax.json"></a>

```
{
  "[AlgorithmName](#cfn-sagemaker-hyperparametertuningjob-algorithmspecification-algorithmname)" : {{String}},
  "[MetricDefinitions](#cfn-sagemaker-hyperparametertuningjob-algorithmspecification-metricdefinitions)" : {{[ MetricDefinitionsItems, ... ]}},
  "[TrainingImage](#cfn-sagemaker-hyperparametertuningjob-algorithmspecification-trainingimage)" : {{String}},
  "[TrainingInputMode](#cfn-sagemaker-hyperparametertuningjob-algorithmspecification-traininginputmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-algorithmspecification-syntax.yaml"></a>

```
  [AlgorithmName](#cfn-sagemaker-hyperparametertuningjob-algorithmspecification-algorithmname): {{String}}
  [MetricDefinitions](#cfn-sagemaker-hyperparametertuningjob-algorithmspecification-metricdefinitions): {{
    - MetricDefinitionsItems}}
  [TrainingImage](#cfn-sagemaker-hyperparametertuningjob-algorithmspecification-trainingimage): {{String}}
  [TrainingInputMode](#cfn-sagemaker-hyperparametertuningjob-algorithmspecification-traininginputmode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-algorithmspecification-properties"></a>

`AlgorithmName`  <a name="cfn-sagemaker-hyperparametertuningjob-algorithmspecification-algorithmname"></a>
The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on AWS Marketplace.
You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.
Note that the `AlgorithmName` parameter is mutually exclusive with the `TrainingImage` parameter. If you specify a value for the `AlgorithmName` parameter, you can't specify a value for `TrainingImage`, and vice versa.
If you specify values for both parameters, the training job might break; if you don't specify any value for both parameters, the training job might raise a `null` error.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:algorithm\/[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])$`
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricDefinitions`  <a name="cfn-sagemaker-hyperparametertuningjob-algorithmspecification-metricdefinitions"></a>
A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. SageMaker publishes each metric to Amazon CloudWatch.
*Required*: No
*Type*: Array of [MetricDefinitionsItems](aws-properties-sagemaker-hyperparametertuningjob-metricdefinitionsitems.md)
*Minimum*: `0`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingImage`  <a name="cfn-sagemaker-hyperparametertuningjob-algorithmspecification-trainingimage"></a>
The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for SageMaker built-in algorithms, see [Docker Registry Paths and Example Code](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) in the *Amazon SageMaker developer guide*. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information about using your custom training container, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).
You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.
For more information, see the note in the `AlgorithmName` parameter description.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingInputMode`  <a name="cfn-sagemaker-hyperparametertuningjob-algorithmspecification-traininginputmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `Pipe | File | FastFile`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
