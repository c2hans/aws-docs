---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentContainerSpecification.html
---

# InferenceComponentContainerSpecification
<a name="API_InferenceComponentContainerSpecification"></a>

Defines a container that provides the runtime environment for a model that you deploy with an inference component.

## Contents
<a name="API_InferenceComponentContainerSpecification_Contents"></a>

 ** ArtifactUrl **   <a name="sagemaker-Type-InferenceComponentContainerSpecification-ArtifactUrl"></a>
The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** ContainerMetricsConfig **   <a name="sagemaker-Type-InferenceComponentContainerSpecification-ContainerMetricsConfig"></a>
The configuration for container metrics scraping. Specifies the metrics endpoint path and publishing frequency for the inference component's container. If not specified when `EnableDetailedObservability` is `True`, the default path `/metrics` on port `8080` is used. For first-party and Deep Learning Containers (DLC), the endpoint path is determined automatically and this configuration is optional.
Type: [ContainerMetricsConfig](API_ContainerMetricsConfig.md) object
Required: No

 ** Environment **   <a name="sagemaker-Type-InferenceComponentContainerSpecification-Environment"></a>
The environment variables to set in the Docker container. Each key and value in the Environment string-to-string map can have length of up to 1024. We support up to 16 entries in the map.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Value Pattern: `[\S\s]*`
Required: No

 ** Image **   <a name="sagemaker-Type-InferenceComponentContainerSpecification-Image"></a>
The Amazon Elastic Container Registry (Amazon ECR) path where the Docker image for the model is stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_InferenceComponentContainerSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentContainerSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentContainerSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentContainerSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
