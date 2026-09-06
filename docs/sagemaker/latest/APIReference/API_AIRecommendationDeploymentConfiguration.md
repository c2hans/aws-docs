---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIRecommendationDeploymentConfiguration.html
---

# AIRecommendationDeploymentConfiguration
<a name="API_AIRecommendationDeploymentConfiguration"></a>

The deployment configuration for a recommendation.

## Contents
<a name="API_AIRecommendationDeploymentConfiguration_Contents"></a>

 ** CopyCountPerInstance **   <a name="sagemaker-Type-AIRecommendationDeploymentConfiguration-CopyCountPerInstance"></a>
The number of model copies per instance.
Type: Integer
Required: No

 ** EnvironmentVariables **   <a name="sagemaker-Type-AIRecommendationDeploymentConfiguration-EnvironmentVariables"></a>
The environment variables for the deployment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Value Pattern: `[\S\s]*`
Required: No

 ** ImageUri **   <a name="sagemaker-Type-AIRecommendationDeploymentConfiguration-ImageUri"></a>
The URI of the container image for the deployment.
Type: String
Required: No

 ** InstanceCount **   <a name="sagemaker-Type-AIRecommendationDeploymentConfiguration-InstanceCount"></a>
The recommended number of instances for the deployment.
Type: Integer
Required: No

 ** InstanceType **   <a name="sagemaker-Type-AIRecommendationDeploymentConfiguration-InstanceType"></a>
The recommended instance type for the deployment.
Type: String
Valid Values: `ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.4xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge`
Required: No

 ** MinCpuMemoryRequiredInMb **   <a name="sagemaker-Type-AIRecommendationDeploymentConfiguration-MinCpuMemoryRequiredInMb"></a>
The minimum host (CPU) memory, in MiB, to reserve for each model copy when deploying the recommendation as an Inference Component. This value maps to the Inference Component's `ComputeResourceRequirements$MinMemoryRequiredInMb` field.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** S3 **   <a name="sagemaker-Type-AIRecommendationDeploymentConfiguration-S3"></a>
The Amazon S3 data channels for the deployment.
Type: Array of [AIRecommendationDeploymentS3Channel](API_AIRecommendationDeploymentS3Channel.md) objects
Required: No

## See Also
<a name="API_AIRecommendationDeploymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIRecommendationDeploymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIRecommendationDeploymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIRecommendationDeploymentConfiguration)
