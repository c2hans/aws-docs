---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentReadyOption.html
---

# DeploymentReadyOption
<a name="API_DeploymentReadyOption"></a>

Information about how traffic is rerouted to instances in a replacement environment in a blue/green deployment.

## Contents
<a name="API_DeploymentReadyOption_Contents"></a>

 ** actionOnTimeout **   <a name="CodeDeploy-Type-DeploymentReadyOption-actionOnTimeout"></a>
Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
+ CONTINUE\_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
+ STOP\_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using [ContinueDeployment](API_ContinueDeployment.md). If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.
Type: String
Valid Values: `CONTINUE_DEPLOYMENT | STOP_DEPLOYMENT`
Required: No

 ** waitTimeInMinutes **   <a name="CodeDeploy-Type-DeploymentReadyOption-waitTimeInMinutes"></a>
The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the `STOP_DEPLOYMENT` option for `actionOnTimeout`.
Type: Integer
Required: No

## See Also
<a name="API_DeploymentReadyOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeploymentReadyOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeploymentReadyOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeploymentReadyOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
