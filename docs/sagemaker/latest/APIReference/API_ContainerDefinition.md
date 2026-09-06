---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html
---

# ContainerDefinition
<a name="API_ContainerDefinition"></a>

Describes the container, as part of model definition.

## Contents
<a name="API_ContainerDefinition_Contents"></a>

 ** AdditionalModelDataSources **   <a name="sagemaker-Type-ContainerDefinition-AdditionalModelDataSources"></a>
Data sources that are available to your model in addition to the one that you specify for `ModelDataSource` when you use the `CreateModel` action.
Type: Array of [AdditionalModelDataSource](API_AdditionalModelDataSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** ContainerHostname **   <a name="sagemaker-Type-ContainerDefinition-ContainerHostname"></a>
This parameter is ignored for models that contain only a `PrimaryContainer`.
When a `ContainerDefinition` is part of an inference pipeline, the value of the parameter uniquely identifies the container for the purposes of logging and metrics. For information, see [Use Logs and Metrics to Monitor an Inference Pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-logs-metrics.html). If you don't specify a value for this parameter for a `ContainerDefinition` that is part of an inference pipeline, a unique name is automatically assigned based on the position of the `ContainerDefinition` in the pipeline. If you specify a value for the `ContainerHostName` for any `ContainerDefinition` that is part of an inference pipeline, you must specify a value for the `ContainerHostName` parameter of every `ContainerDefinition` in that pipeline.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ContainerMetricsConfig **   <a name="sagemaker-Type-ContainerDefinition-ContainerMetricsConfig"></a>
The configuration for container metrics scraping. Specifies the metrics endpoint path and publishing frequency. If not specified when `EnableDetailedObservability` is `True`, the default path `/metrics` on port `8080` is used. For first-party and Deep Learning Containers (DLC), the endpoint path is determined automatically and this configuration is optional.
Type: [ContainerMetricsConfig](API_ContainerMetricsConfig.md) object
Required: No

 ** Environment **   <a name="sagemaker-Type-ContainerDefinition-Environment"></a>
The environment variables to set in the Docker container. Don't include any sensitive data in your environment variables.
The maximum length of each key and value in the `Environment` map is 1024 bytes. The maximum length of all keys and values in the map, combined, is 32 KB. If you pass multiple containers to a `CreateModel` request, then the maximum length of all of their maps, combined, is also 32 KB.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Value Pattern: `[\S\s]*`
Required: No

 ** Image **   <a name="sagemaker-Type-ContainerDefinition-Image"></a>
The path where inference code is stored. This can be either in Amazon EC2 Container Registry or in a Docker registry that is accessible from the same VPC that you configure for your endpoint. If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html).
The model artifacts in an Amazon S3 bucket and the Docker image for inference container in Amazon EC2 Container Registry must be in the same region as the model or endpoint you are creating.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\S]+`
Required: No

 ** ImageConfig **   <a name="sagemaker-Type-ContainerDefinition-ImageConfig"></a>
Specifies whether the model container is in Amazon ECR or a private Docker registry accessible from your Amazon Virtual Private Cloud (VPC). For information about storing containers in a private Docker registry, see [Use a Private Docker Registry for Real-Time Inference Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-containers-inference-private.html).
The model artifacts in an Amazon S3 bucket and the Docker image for inference container in Amazon EC2 Container Registry must be in the same region as the model or endpoint you are creating.
Type: [ImageConfig](API_ImageConfig.md) object
Required: No

 ** InferenceSpecificationName **   <a name="sagemaker-Type-ContainerDefinition-InferenceSpecificationName"></a>
The inference specification name in the model package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** Mode **   <a name="sagemaker-Type-ContainerDefinition-Mode"></a>
Whether the container hosts a single model or multiple models.
Type: String
Valid Values: `SingleModel | MultiModel`
Required: No

 ** ModelDataSource **   <a name="sagemaker-Type-ContainerDefinition-ModelDataSource"></a>
Specifies the location of ML model data to deploy.
Currently you cannot use `ModelDataSource` in conjunction with SageMaker batch transform, SageMaker serverless endpoints, SageMaker multi-model endpoints, and SageMaker Marketplace.
Type: [ModelDataSource](API_ModelDataSource.md) object
Required: No

 ** ModelDataUrl **   <a name="sagemaker-Type-ContainerDefinition-ModelDataUrl"></a>
The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). The S3 path is required for SageMaker built-in algorithms, but not if you use your own algorithms. For more information on built-in algorithms, see [Common Parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html).
The model artifacts must be in an S3 bucket that is in the same region as the model or endpoint you are creating.
If you provide a value for this parameter, SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provide. AWS STS is activated in your AWS account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see [Activating and Deactivating AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the * AWS Identity and Access Management User Guide*.
If you use a built-in algorithm to create a model, SageMaker requires that you provide a S3 path to the model artifacts in `ModelDataUrl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** ModelPackageName **   <a name="sagemaker-Type-ContainerDefinition-ModelPackageName"></a>
The name or Amazon Resource Name (ARN) of the model package to use to create the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 176.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)(\/[0-9]{1,9})?`
Required: No

 ** MultiModelConfig **   <a name="sagemaker-Type-ContainerDefinition-MultiModelConfig"></a>
Specifies additional configuration for multi-model endpoints.
Type: [MultiModelConfig](API_MultiModelConfig.md) object
Required: No

## See Also
<a name="API_ContainerDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ContainerDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ContainerDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ContainerDefinition)
