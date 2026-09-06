---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterSlurmConfigDetails.html
---

# ClusterSlurmConfigDetails
<a name="API_ClusterSlurmConfigDetails"></a>

The Slurm configuration details for an instance group in a SageMaker HyperPod cluster.

## Contents
<a name="API_ClusterSlurmConfigDetails_Contents"></a>

 ** NodeType **   <a name="sagemaker-Type-ClusterSlurmConfigDetails-NodeType"></a>
The type of Slurm node for the instance group. Valid values are `Controller`, `Worker`, and `Login`.
Type: String
Valid Values: `Controller | Login | Compute`
Required: Yes

 ** PartitionNames **   <a name="sagemaker-Type-ClusterSlurmConfigDetails-PartitionNames"></a>
The list of Slurm partition names that the instance group belongs to.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

## See Also
<a name="API_ClusterSlurmConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterSlurmConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterSlurmConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterSlurmConfigDetails)
