---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html
---

# AlgorithmSpecification
<a name="API_AlgorithmSpecification"></a>

Specifies the training algorithm to use in a [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) request.

**Important**
SageMaker uses its own SageMaker account credentials to pull and access built-in algorithms so built-in algorithms are universally accessible across all AWS accounts. As a result, built-in algorithms have standard, unrestricted access. You cannot restrict built-in algorithms using IAM roles. Use custom algorithms if you require specific access controls.

For more information about algorithms provided by SageMaker, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html). For information about using your own algorithms, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).

## Contents
<a name="API_AlgorithmSpecification_Contents"></a>

 ** TrainingInputMode **   <a name="sagemaker-Type-AlgorithmSpecification-TrainingInputMode"></a>
The training input mode that the algorithm supports. For more information about input modes, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).
 **Pipe mode**
If an algorithm supports `Pipe` mode, Amazon SageMaker streams data directly from Amazon S3 to the container.
 **File mode**
If an algorithm supports `File` mode, SageMaker downloads the training data from S3 to the provisioned ML storage volume, and mounts the directory to the Docker volume for the training container.
You must provision the ML storage volume with sufficient capacity to accommodate the data downloaded from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container uses the ML storage volume to also store intermediate information, if any.
For distributed algorithms, training data is distributed uniformly. Your training duration is predictable if the input data objects sizes are approximately the same. SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed when one host in a training cluster is overloaded, thus becoming a bottleneck in training.
 **FastFile mode**
If an algorithm supports `FastFile` mode, SageMaker streams data directly from S3 to the container with no code changes, and provides file system access to the data. Users can author their training script to interact with these files as if they were stored on disk.
 `FastFile` mode works best when the data is read sequentially. Augmented manifest files aren't supported. The startup time is lower when there are fewer files in the S3 bucket provided.
Type: String
Valid Values: `Pipe | File | FastFile`
Required: Yes

 ** AlgorithmName **   <a name="sagemaker-Type-AlgorithmSpecification-AlgorithmName"></a>
The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on AWS Marketplace.
You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.
Note that the `AlgorithmName` parameter is mutually exclusive with the `TrainingImage` parameter. If you specify a value for the `AlgorithmName` parameter, you can't specify a value for `TrainingImage`, and vice versa.
If you specify values for both parameters, the training job might break; if you don't specify any value for both parameters, the training job might raise a `null` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)`
Required: No

 ** ContainerArguments **   <a name="sagemaker-Type-AlgorithmSpecification-ContainerArguments"></a>
The arguments for a container used to run a training job. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for additional information.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** ContainerEntrypoint **   <a name="sagemaker-Type-AlgorithmSpecification-ContainerEntrypoint"></a>
The [entrypoint script for a Docker container](https://docs.docker.com/engine/reference/builder/) used to run a training job. This script takes precedence over the default train processing instructions. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for more information.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** EnableSageMakerMetricsTimeSeries **   <a name="sagemaker-Type-AlgorithmSpecification-EnableSageMakerMetricsTimeSeries"></a>
To generate and save time-series metrics during training, set to `true`. The default is `false` and time-series metrics aren't generated except in the following cases:
+ You use one of the SageMaker built-in algorithms
+ You use one of the following [Prebuilt SageMaker Docker Images](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html):
  + Tensorflow (version >= 1.15)
  + MXNet (version >= 1.6)
  + PyTorch (version >= 1.3)
+ You specify at least one [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html)
Type: Boolean
Required: No

 ** MetricDefinitions **   <a name="sagemaker-Type-AlgorithmSpecification-MetricDefinitions"></a>
A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. SageMaker publishes each metric to Amazon CloudWatch.
Type: Array of [MetricDefinition](API_MetricDefinition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

 ** TrainingImage **   <a name="sagemaker-Type-AlgorithmSpecification-TrainingImage"></a>
The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for SageMaker built-in algorithms, see [Docker Registry Paths and Example Code](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) in the *Amazon SageMaker developer guide*. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information about using your custom training container, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).
You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.
For more information, see the note in the `AlgorithmName` parameter description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** TrainingImageConfig **   <a name="sagemaker-Type-AlgorithmSpecification-TrainingImageConfig"></a>
The configuration to use an image from a private Docker registry for a training job.
Type: [TrainingImageConfig](API_TrainingImageConfig.md) object
Required: No

## See Also
<a name="API_AlgorithmSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AlgorithmSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AlgorithmSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AlgorithmSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
