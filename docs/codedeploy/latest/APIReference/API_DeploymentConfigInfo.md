---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentConfigInfo.html
---

# DeploymentConfigInfo
<a name="API_DeploymentConfigInfo"></a>

Information about a deployment configuration.

## Contents
<a name="API_DeploymentConfigInfo_Contents"></a>

 ** computePlatform **   <a name="CodeDeploy-Type-DeploymentConfigInfo-computePlatform"></a>
The destination platform type for the deployment (`Lambda`, `Server`, or `ECS`).
Type: String
Valid Values: `Server | Lambda | ECS | Kubernetes`
Required: No

 ** createTime **   <a name="CodeDeploy-Type-DeploymentConfigInfo-createTime"></a>
The time at which the deployment configuration was created.
Type: Timestamp
Required: No

 ** deploymentConfigId **   <a name="CodeDeploy-Type-DeploymentConfigInfo-deploymentConfigId"></a>
The deployment configuration ID.
Type: String
Required: No

 ** deploymentConfigName **   <a name="CodeDeploy-Type-DeploymentConfigInfo-deploymentConfigName"></a>
The deployment configuration name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** minimumHealthyHosts **   <a name="CodeDeploy-Type-DeploymentConfigInfo-minimumHealthyHosts"></a>
Information about the number or percentage of minimum healthy instances.
Type: [MinimumHealthyHosts](API_MinimumHealthyHosts.md) object
Required: No

 ** trafficRoutingConfig **   <a name="CodeDeploy-Type-DeploymentConfigInfo-trafficRoutingConfig"></a>
The configuration that specifies how the deployment traffic is routed. Used for deployments with a Lambda or Amazon ECS compute platform only.
Type: [TrafficRoutingConfig](API_TrafficRoutingConfig.md) object
Required: No

 ** zonalConfig **   <a name="CodeDeploy-Type-DeploymentConfigInfo-zonalConfig"></a>
Information about a zonal configuration.
Type: [ZonalConfig](API_ZonalConfig.md) object
Required: No

## See Also
<a name="API_DeploymentConfigInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeploymentConfigInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeploymentConfigInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeploymentConfigInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
