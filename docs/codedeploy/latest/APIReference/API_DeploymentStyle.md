---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentStyle.html
---

# DeploymentStyle
<a name="API_DeploymentStyle"></a>

Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

## Contents
<a name="API_DeploymentStyle_Contents"></a>

 ** deploymentOption **   <a name="CodeDeploy-Type-DeploymentStyle-deploymentOption"></a>
Indicates whether to route deployment traffic behind a load balancer.
Type: String
Valid Values: `WITH_TRAFFIC_CONTROL | WITHOUT_TRAFFIC_CONTROL`
Required: No

 ** deploymentType **   <a name="CodeDeploy-Type-DeploymentStyle-deploymentType"></a>
Indicates whether to run an in-place deployment or a blue/green deployment.
Type: String
Valid Values: `IN_PLACE | BLUE_GREEN`
Required: No

## See Also
<a name="API_DeploymentStyle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeploymentStyle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeploymentStyle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeploymentStyle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
