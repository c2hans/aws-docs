---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BlueGreenDeploymentConfiguration.html
---

# BlueGreenDeploymentConfiguration
<a name="API_BlueGreenDeploymentConfiguration"></a>

Information about blue/green deployment options for a deployment group.

## Contents
<a name="API_BlueGreenDeploymentConfiguration_Contents"></a>

 ** deploymentReadyOption **   <a name="CodeDeploy-Type-BlueGreenDeploymentConfiguration-deploymentReadyOption"></a>
Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.
Type: [DeploymentReadyOption](API_DeploymentReadyOption.md) object
Required: No

 ** greenFleetProvisioningOption **   <a name="CodeDeploy-Type-BlueGreenDeploymentConfiguration-greenFleetProvisioningOption"></a>
Information about how instances are provisioned for a replacement environment in a blue/green deployment.
Type: [GreenFleetProvisioningOption](API_GreenFleetProvisioningOption.md) object
Required: No

 ** terminateBlueInstancesOnDeploymentSuccess **   <a name="CodeDeploy-Type-BlueGreenDeploymentConfiguration-terminateBlueInstancesOnDeploymentSuccess"></a>
Information about whether to terminate instances in the original fleet during a blue/green deployment.
Type: [BlueInstanceTerminationOption](API_BlueInstanceTerminationOption.md) object
Required: No

## See Also
<a name="API_BlueGreenDeploymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/BlueGreenDeploymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/BlueGreenDeploymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/BlueGreenDeploymentConfiguration)
