---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DatabaseConfigurationMetadata.html
---

# DatabaseConfigurationMetadata
<a name="API_DatabaseConfigurationMetadata"></a>

Metadata information about a change to the external Slurm accounting database of a HyperPod cluster.

## Contents
<a name="API_DatabaseConfigurationMetadata_Contents"></a>

 ** Advisory **   <a name="sagemaker-Type-DatabaseConfigurationMetadata-Advisory"></a>
Additional information about a change that succeeded, such as an action to take on the cluster.
Type: String
Required: No

 ** FailureMessage **   <a name="sagemaker-Type-DatabaseConfigurationMetadata-FailureMessage"></a>
An error message describing why the accounting database change failed, and how to resolve it.
Type: String
Required: No

 ** RollbackStatus **   <a name="sagemaker-Type-DatabaseConfigurationMetadata-RollbackStatus"></a>
Whether HyperPod restored the previous accounting database configuration after the change failed. Valid values:
+  `NotApplicable`: The change failed before HyperPod modified the cluster, for example because the database could not be reached or rejected the credentials, so there was nothing to restore.
+  `Reverted`: The change failed after it was applied, and HyperPod restored the previous configuration. The cluster continues to use the previous accounting database.
+  `RevertFailed`: The change failed and HyperPod could not restore the previous configuration, so Slurm accounting on the cluster might not be working.
This field is omitted when the change succeeds.
Type: String
Valid Values: `NotApplicable | Reverted | RevertFailed`
Required: No

## See Also
<a name="API_DatabaseConfigurationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DatabaseConfigurationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DatabaseConfigurationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DatabaseConfigurationMetadata)
