---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonDeploymentCapacityProvider.html
---

# DaemonDeploymentCapacityProvider
<a name="API_DaemonDeploymentCapacityProvider"></a>

Information about a capacity provider during a daemon deployment.

## Contents
<a name="API_DaemonDeploymentCapacityProvider_Contents"></a>

 ** arn **   <a name="ECS-Type-DaemonDeploymentCapacityProvider-arn"></a>
The Amazon Resource Name (ARN) of the capacity provider.
Type: String
Required: No

 ** drainingInstanceCount **   <a name="ECS-Type-DaemonDeploymentCapacityProvider-drainingInstanceCount"></a>
The number of instances being drained on this capacity provider during the deployment.
Type: Integer
Required: No

 ** runningInstanceCount **   <a name="ECS-Type-DaemonDeploymentCapacityProvider-runningInstanceCount"></a>
The number of instances running daemon tasks on this capacity provider.
Type: Integer
Required: No

## See Also
<a name="API_DaemonDeploymentCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonDeploymentCapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonDeploymentCapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonDeploymentCapacityProvider)
