---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentContainerSpecificationSummary.html
---

# InferenceComponentContainerSpecificationSummary
<a name="API_InferenceComponentContainerSpecificationSummary"></a>

Details about the resources that are deployed with this inference component.

## Contents
<a name="API_InferenceComponentContainerSpecificationSummary_Contents"></a>

 ** ArtifactUrl **   <a name="sagemaker-Type-InferenceComponentContainerSpecificationSummary-ArtifactUrl"></a>
The Amazon S3 path where the model artifacts are stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** ContainerMetricsConfig **   <a name="sagemaker-Type-InferenceComponentContainerSpecificationSummary-ContainerMetricsConfig"></a>
The container metrics scraping configuration for this inference component, including the metrics endpoint path and publishing frequency.
Type: [ContainerMetricsConfig](API_ContainerMetricsConfig.md) object
Required: No

 ** DeployedImage **   <a name="sagemaker-Type-InferenceComponentContainerSpecificationSummary-DeployedImage"></a>
Gets the Amazon EC2 Container Registry path of the docker image of the model that is hosted in this [ProductionVariant](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html).
If you used the `registry/repository[:tag]` form to specify the image path of the primary container when you created the model hosted in this `ProductionVariant`, the path resolves to a path of the form `registry/repository[@digest]`. A digest is a hash value that identifies a specific version of an image. For information about Amazon ECR paths, see [Pulling an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide*.
Type: [DeployedImage](API_DeployedImage.md) object
Required: No

 ** Environment **   <a name="sagemaker-Type-InferenceComponentContainerSpecificationSummary-Environment"></a>
The environment variables to set in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Value Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_InferenceComponentContainerSpecificationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentContainerSpecificationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentContainerSpecificationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentContainerSpecificationSummary)
