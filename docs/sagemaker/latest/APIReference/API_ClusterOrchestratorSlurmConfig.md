---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterOrchestratorSlurmConfig.html
---

# ClusterOrchestratorSlurmConfig
<a name="API_ClusterOrchestratorSlurmConfig"></a>

The configuration settings for the Slurm orchestrator used with the SageMaker HyperPod cluster.

## Contents
<a name="API_ClusterOrchestratorSlurmConfig_Contents"></a>

 ** AccountingDatabase **   <a name="sagemaker-Type-ClusterOrchestratorSlurmConfig-AccountingDatabase"></a>
The external database that stores the Slurm accounting data for the cluster, such as job history, associations, and usage. When you omit this field, Slurm accounting uses a database on the cluster's controller node.
This field is only supported for clusters using `Continuous` as the `NodeProvisioningMode`.
Type: [ClusterAccountingDatabase](API_ClusterAccountingDatabase.md) object
Required: No

 ** SlurmConfigStrategy **   <a name="sagemaker-Type-ClusterOrchestratorSlurmConfig-SlurmConfigStrategy"></a>
The strategy for managing partitions for the Slurm configuration. Valid values are `Managed`, `Overwrite`, and `Merge`.
Type: String
Valid Values: `Overwrite | Managed | Merge`
Required: No

## See Also
<a name="API_ClusterOrchestratorSlurmConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterOrchestratorSlurmConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterOrchestratorSlurmConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterOrchestratorSlurmConfig)
