---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterSummary.html
---

# ClusterSummary
<a name="API_ClusterSummary"></a>

Lists a summary of the properties of a SageMaker HyperPod cluster.

## Contents
<a name="API_ClusterSummary_Contents"></a>

 ** ClusterArn **   <a name="sagemaker-Type-ClusterSummary-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** ClusterName **   <a name="sagemaker-Type-ClusterSummary-ClusterName"></a>
The name of the SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** ClusterStatus **   <a name="sagemaker-Type-ClusterSummary-ClusterStatus"></a>
The status of the SageMaker HyperPod cluster.
Type: String
Valid Values: `Creating | Deleting | Failed | InService | RollingBack | SystemUpdating | Updating`
Required: Yes

 ** ImageVersionStatus **   <a name="sagemaker-Type-ClusterSummary-ImageVersionStatus"></a>
The aggregate status of the image version across the cluster's instance groups.
Type: String
Valid Values: `UpToDate | UpdateAvailable | SecurityUpdateRequired | EndOfLife`
Required: No

 ** TrainingPlanArns **   <a name="sagemaker-Type-ClusterSummary-TrainingPlanArns"></a>
A list of Amazon Resource Names (ARNs) of the training plans associated with this cluster.
For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.
Type: Array of strings
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

## See Also
<a name="API_ClusterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterSummary)
