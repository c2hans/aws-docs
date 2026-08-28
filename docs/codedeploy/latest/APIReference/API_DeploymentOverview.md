---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentOverview.html
---

# DeploymentOverview
<a name="API_DeploymentOverview"></a>

Information about the deployment status of the instances in the deployment.

## Contents
<a name="API_DeploymentOverview_Contents"></a>

 ** Failed **   <a name="CodeDeploy-Type-DeploymentOverview-Failed"></a>
The number of instances in the deployment in a failed state.
Type: Long
Required: No

 ** InProgress **   <a name="CodeDeploy-Type-DeploymentOverview-InProgress"></a>
The number of instances in which the deployment is in progress.
Type: Long
Required: No

 ** Pending **   <a name="CodeDeploy-Type-DeploymentOverview-Pending"></a>
The number of instances in the deployment in a pending state.
Type: Long
Required: No

 ** Ready **   <a name="CodeDeploy-Type-DeploymentOverview-Ready"></a>
The number of instances in a replacement environment ready to receive traffic in a blue/green deployment.
Type: Long
Required: No

 ** Skipped **   <a name="CodeDeploy-Type-DeploymentOverview-Skipped"></a>
The number of instances in the deployment in a skipped state.
Type: Long
Required: No

 ** Succeeded **   <a name="CodeDeploy-Type-DeploymentOverview-Succeeded"></a>
The number of instances in the deployment to which revisions have been successfully deployed.
Type: Long
Required: No

## See Also
<a name="API_DeploymentOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeploymentOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeploymentOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeploymentOverview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
