---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonDeploymentRevisionDetail.html
---

# DaemonDeploymentRevisionDetail
<a name="API_DaemonDeploymentRevisionDetail"></a>

Details about a daemon revision during a deployment, including running and draining instance counts per capacity provider.

## Contents
<a name="API_DaemonDeploymentRevisionDetail_Contents"></a>

 ** arn **   <a name="ECS-Type-DaemonDeploymentRevisionDetail-arn"></a>
The Amazon Resource Name (ARN) of the daemon revision.
Type: String
Required: No

 ** capacityProviders **   <a name="ECS-Type-DaemonDeploymentRevisionDetail-capacityProviders"></a>
The capacity providers associated with this daemon revision during the deployment.
Type: Array of [DaemonDeploymentCapacityProvider](API_DaemonDeploymentCapacityProvider.md) objects
Required: No

 ** totalDrainingInstanceCount **   <a name="ECS-Type-DaemonDeploymentRevisionDetail-totalDrainingInstanceCount"></a>
The total number of instances being drained for this revision during the deployment.
Type: Integer
Required: No

 ** totalRunningInstanceCount **   <a name="ECS-Type-DaemonDeploymentRevisionDetail-totalRunningInstanceCount"></a>
The total number of instances running daemon tasks for this revision.
Type: Integer
Required: No

## See Also
<a name="API_DaemonDeploymentRevisionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonDeploymentRevisionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonDeploymentRevisionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonDeploymentRevisionDetail)
