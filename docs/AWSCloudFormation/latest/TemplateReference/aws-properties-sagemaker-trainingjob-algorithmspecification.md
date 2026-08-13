---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-algorithmspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob AlgorithmSpecification
<a name="aws-properties-sagemaker-trainingjob-algorithmspecification"></a>

Specifies the training algorithm to use in a [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) request.

**Important**
SageMaker uses its own SageMaker account credentials to pull and access built-in algorithms so built-in algorithms are universally accessible across all AWS accounts. As a result, built-in algorithms have standard, unrestricted access. You cannot restrict built-in algorithms using IAM roles. Use custom algorithms if you require specific access controls.

For more information about algorithms provided by SageMaker, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). For information about using your own algorithms, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).

## Syntax
<a name="aws-properties-sagemaker-trainingjob-algorithmspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-algorithmspecification-syntax.json"></a>

```
{
  "[AlgorithmName](#cfn-sagemaker-trainingjob-algorithmspecification-algorithmname)" : {{String}},
  "[ContainerArguments](#cfn-sagemaker-trainingjob-algorithmspecification-containerarguments)" : {{[ String, ... ]}},
  "[ContainerEntrypoint](#cfn-sagemaker-trainingjob-algorithmspecification-containerentrypoint)" : {{[ String, ... ]}},
  "[EnableSageMakerMetricsTimeSeries](#cfn-sagemaker-trainingjob-algorithmspecification-enablesagemakermetricstimeseries)" : {{Boolean}},
  "[MetricDefinitions](#cfn-sagemaker-trainingjob-algorithmspecification-metricdefinitions)" : {{[ MetricDefinition, ... ]}},
  "[TrainingImage](#cfn-sagemaker-trainingjob-algorithmspecification-trainingimage)" : {{String}},
  "[TrainingImageConfig](#cfn-sagemaker-trainingjob-algorithmspecification-trainingimageconfig)" : {{TrainingImageConfig}},
  "[TrainingInputMode](#cfn-sagemaker-trainingjob-algorithmspecification-traininginputmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-algorithmspecification-syntax.yaml"></a>

```
  [AlgorithmName](#cfn-sagemaker-trainingjob-algorithmspecification-algorithmname): {{String}}
  [ContainerArguments](#cfn-sagemaker-trainingjob-algorithmspecification-containerarguments): {{
    - String}}
  [ContainerEntrypoint](#cfn-sagemaker-trainingjob-algorithmspecification-containerentrypoint): {{
    - String}}
  [EnableSageMakerMetricsTimeSeries](#cfn-sagemaker-trainingjob-algorithmspecification-enablesagemakermetricstimeseries): {{Boolean}}
  [MetricDefinitions](#cfn-sagemaker-trainingjob-algorithmspecification-metricdefinitions): {{
    - MetricDefinition}}
  [TrainingImage](#cfn-sagemaker-trainingjob-algorithmspecification-trainingimage): {{String}}
  [TrainingImageConfig](#cfn-sagemaker-trainingjob-algorithmspecification-trainingimageconfig): {{
    TrainingImageConfig}}
  [TrainingInputMode](#cfn-sagemaker-trainingjob-algorithmspecification-traininginputmode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-algorithmspecification-properties"></a>

`AlgorithmName`  <a name="cfn-sagemaker-trainingjob-algorithmspecification-algorithmname"></a>
The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on AWS Marketplace.
You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.
Note that the `AlgorithmName` parameter is mutually exclusive with the `TrainingImage` parameter. If you specify a value for the `AlgorithmName` parameter, you can't specify a value for `TrainingImage`, and vice versa.
If you specify values for both parameters, the training job might break; if you don't specify any value for both parameters, the training job might raise a `null` error.
*Required*: No
*Type*: String
*Pattern*: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)$`
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerArguments`  <a name="cfn-sagemaker-trainingjob-algorithmspecification-containerarguments"></a>
The arguments for a container used to run a training job. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for additional information.
*Required*: No
*Type*: Array of String
*Maximum*: `256 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerEntrypoint`  <a name="cfn-sagemaker-trainingjob-algorithmspecification-containerentrypoint"></a>
The [entrypoint script for a Docker container](https://docs.docker.com/engine/reference/builder/) used to run a training job. This script takes precedence over the default train processing instructions. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for more information.
*Required*: No
*Type*: Array of String
*Maximum*: `256 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableSageMakerMetricsTimeSeries`  <a name="cfn-sagemaker-trainingjob-algorithmspecification-enablesagemakermetricstimeseries"></a>
To generate and save time-series metrics during training, set to `true`. The default is `false` and time-series metrics aren't generated except in the following cases:
+ You use one of the SageMaker built-in algorithms
+ You use one of the following [Prebuilt SageMaker Docker Images](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html):
  + Tensorflow (version >= 1.15)
  + MXNet (version >= 1.6)
  + PyTorch (version >= 1.3)
+ You specify at least one [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html)
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricDefinitions`  <a name="cfn-sagemaker-trainingjob-algorithmspecification-metricdefinitions"></a>
A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. SageMaker publishes each metric to Amazon CloudWatch.
*Required*: No
*Type*: Array of [MetricDefinition](aws-properties-sagemaker-trainingjob-metricdefinition.md)
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingImage`  <a name="cfn-sagemaker-trainingjob-algorithmspecification-trainingimage"></a>
The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for SageMaker built-in algorithms, see [Docker Registry Paths and Example Code](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) in the *Amazon SageMaker developer guide*. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information about using your custom training container, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).
You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.
For more information, see the note in the `AlgorithmName` parameter description.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingImageConfig`  <a name="cfn-sagemaker-trainingjob-algorithmspecification-trainingimageconfig"></a>
The configuration to use an image from a private Docker registry for a training job.
*Required*: No
*Type*: [TrainingImageConfig](aws-properties-sagemaker-trainingjob-trainingimageconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingInputMode`  <a name="cfn-sagemaker-trainingjob-algorithmspecification-traininginputmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `Pipe | File | FastFile`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
