---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeploymentConfigurationValidationPolicy.html
---

# DeploymentConfigurationValidationPolicy
<a name="API_DeploymentConfigurationValidationPolicy"></a>

Contains information about how long a component on a core device can validate its configuration updates before it times out. Components can use the [SubscribeToValidateConfigurationUpdates](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-subscribetovalidateconfigurationupdates) IPC operation to receive notifications when a deployment specifies a configuration update. Then, components can respond with the [SendConfigurationValidityReport](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-sendconfigurationvalidityreport) IPC operation. For more information, see [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) in the * AWS IoT Greengrass V2 Developer Guide*.

## Contents
<a name="API_DeploymentConfigurationValidationPolicy_Contents"></a>

 ** timeoutInSeconds **   <a name="greengrassv2-Type-DeploymentConfigurationValidationPolicy-timeoutInSeconds"></a>
The amount of time in seconds that a component can validate its configuration updates. If the validation time exceeds this timeout, then the deployment proceeds for the device.
Default: `30`
Type: Integer
Required: No

## See Also
<a name="API_DeploymentConfigurationValidationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/DeploymentConfigurationValidationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/DeploymentConfigurationValidationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/DeploymentConfigurationValidationPolicy)
