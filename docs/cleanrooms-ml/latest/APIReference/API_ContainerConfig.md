---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ContainerConfig.html
---

# ContainerConfig
<a name="API_ContainerConfig"></a>

Provides configuration information for the dockerized container where the model algorithm is stored.

## Contents
<a name="API_ContainerConfig_Contents"></a>

 ** imageUri **   <a name="API-Type-ContainerConfig-imageUri"></a>
The registry path of the docker image that contains the algorithm. Clean Rooms ML currently only supports the `registry/repository[:tag]` image path format. For more information about using images in Clean Rooms ML, see the [Sagemaker API reference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html#sagemaker-Type-AlgorithmSpecification-TrainingImage).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** arguments **   <a name="API-Type-ContainerConfig-arguments"></a>
The arguments for a container used to run a training job. See How Amazon SageMaker Runs Your Training Image for additional information. For more information, see [How Sagemaker runs your training image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** entrypoint **   <a name="API-Type-ContainerConfig-entrypoint"></a>
The entrypoint script for a Docker container used to run a training job. This script takes precedence over the default train processing instructions. See How Amazon SageMaker Runs Your Training Image for additional information. For more information, see [How Sagemaker runs your training image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** metricDefinitions **   <a name="API-Type-ContainerConfig-metricDefinitions"></a>
A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. AWS Clean Rooms ML publishes each metric to all members' Amazon CloudWatch using IAM role configured in [PutMLConfiguration](API_PutMLConfiguration.md).
Type: Array of [MetricDefinition](API_MetricDefinition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

## See Also
<a name="API_ContainerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ContainerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ContainerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ContainerConfig)
