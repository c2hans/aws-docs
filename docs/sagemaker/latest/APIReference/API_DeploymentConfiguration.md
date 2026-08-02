---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeploymentConfiguration.html
---

# DeploymentConfiguration
<a name="API_DeploymentConfiguration"></a>

The configuration to use when updating the AMI versions.

## Contents
<a name="API_DeploymentConfiguration_Contents"></a>

 ** AutoRollbackConfiguration **   <a name="sagemaker-Type-DeploymentConfiguration-AutoRollbackConfiguration"></a>
An array that contains the alarms that SageMaker monitors to know whether to roll back the AMI update.
Type: Array of [AlarmDetails](API_AlarmDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** RollingUpdatePolicy **   <a name="sagemaker-Type-DeploymentConfiguration-RollingUpdatePolicy"></a>
The policy that SageMaker uses when updating the AMI versions of the cluster.
Type: [RollingDeploymentPolicy](API_RollingDeploymentPolicy.md) object
Required: No

 ** WaitIntervalInSeconds **   <a name="sagemaker-Type-DeploymentConfiguration-WaitIntervalInSeconds"></a>
The duration in seconds that SageMaker waits before updating more instances in the cluster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: No

## See Also
<a name="API_DeploymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeploymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeploymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeploymentConfiguration)
