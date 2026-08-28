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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
