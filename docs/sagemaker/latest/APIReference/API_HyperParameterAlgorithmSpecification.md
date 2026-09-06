---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterAlgorithmSpecification.html
---

# HyperParameterAlgorithmSpecification
<a name="API_HyperParameterAlgorithmSpecification"></a>

Specifies which training algorithm to use for training jobs that a hyperparameter tuning job launches and the metrics to monitor.

## Contents
<a name="API_HyperParameterAlgorithmSpecification_Contents"></a>

 ** TrainingInputMode **   <a name="sagemaker-Type-HyperParameterAlgorithmSpecification-TrainingInputMode"></a>
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

 ** AlgorithmName **   <a name="sagemaker-Type-HyperParameterAlgorithmSpecification-AlgorithmName"></a>
The name of the resource algorithm to use for the hyperparameter tuning job. If you specify a value for this parameter, do not specify a value for `TrainingImage`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)`
Required: No

 ** MetricDefinitions **   <a name="sagemaker-Type-HyperParameterAlgorithmSpecification-MetricDefinitions"></a>
An array of [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html) objects that specify the metrics that the algorithm emits.
Type: Array of [MetricDefinition](API_MetricDefinition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

 ** TrainingImage **   <a name="sagemaker-Type-HyperParameterAlgorithmSpecification-TrainingImage"></a>
 The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see [Algorithms Provided by Amazon SageMaker: Common Parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html). SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

## See Also
<a name="API_HyperParameterAlgorithmSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterAlgorithmSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterAlgorithmSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterAlgorithmSpecification)
