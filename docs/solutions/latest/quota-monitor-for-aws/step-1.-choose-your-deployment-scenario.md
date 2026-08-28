---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-1.-choose-your-deployment-scenario.html
---

# Step 1. Choose your deployment scenario
<a name="step-1.-choose-your-deployment-scenario"></a>

You can deploy Quota Monitor for AWS in three deployment scenarios:
+  **Scenario 1** - Environments where all AWS accounts are part of one or more Organizations.
+  **Scenario 2** - Hybrid environments with Organizations and independent AWS accounts.
+  **Scenario 3** - Environments that do not use Organizations and use single accounts instead.

To leverage all the benefits of this solution for automated monitoring and automated deployment, we recommend using Organizations.

The following sections describe how to deploy Quota Monitor for AWS in each of these deployment scenarios.

## Deploying in AWS Organizations environments and hybrid environments (scenarios 1 and 2)
<a name="deploying-in-aws-organizations-environments-and-hybrid-environments-scenarios-1-and-2"></a>

Choose this scenario if you are using Organizations and the AWS account that you are using for monitoring quotas is registered as a delegated administrator for StackSets in the organization.

You can choose from the two deployment modes provided as template input parameters:
+  **Organizations (default mode)** - If you want to monitor quota utilization across your Organizations or across different OUs under your organization, choose this mode.
+  **Hybrid** - If you want to monitor quota utilization across your Organizations, OUs, and accounts outside your Organizations, choose this mode.

The following figure depicts an example of deploying the solution in your monitoring account.

 **Image depicts the workflow for deploying a monitoring account**

![deployment workflow](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/deployment-workflow.png)

After you choose the deployment mode, the resources needed for that mode are provisioned. The deployment workflow is invoked when you update the deployed Systems Manager Parameter Store.
+ The `helper` Lambda function updates the permissions on the centralized EventBridge bus, so all monitored accounts can send their quota utilization events to the monitoring account.
+ CloudFormation StackSets automates spoke template deployments in the secondary accounts under targeted OUs.
+ For additional accounts not under the purview of Organizations, you can manually deploy spoke templates.

## Deploying when not using AWS Organizations (scenarios 2 and 3)
<a name="deploying-when-not-using-aws-organizations-scenarios-2-and-3"></a>

While we recommend using Organizations so that you can leverage the benefits of automated monitoring and automated deployment, you might have use cases where you are not using Organizations.

When you are not using Organizations and your monitoring account is not an organization member account—​rather, an independent standalone account—​use the supplemental `quota-monitor-hub-no-ou.template`.

**Note**
You are responsible for the cost of the AWS services used while running this solution. Review the [Cost](cost.md) section for more details. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

The following flowchart depicts which templates you need to deploy, depending on your deployment scenario.

![Image depicts a decision diagram for selecting the templates for your deployment scenario](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/choose-deployment-scenario.png)

The following table summarizes the decision criteria for choosing templates, regions, and accounts for monitoring your quotas.

| Question | Using AWS Organizations | Using single accounts |
| --- | --- | --- |
| Where do you deploy a prerequisite template? | Deploy in a management account | N/A |
| Which AWS Region should you use for the prerequisite template? | Any AWS Region | N/A |
| Which hub template should you use? |  `quota-monitor-hub.template`  |  `quota-monitor-hub-no-ou.template`  |
| Which hub account should you use? | Any account | Any account |
| Where do you the deploy spoke templates? | \* StackSets for Organizations and OU deployment scenarios<br />\* StackSets and manual deployment for hybrid deployment scenarios | Manual deployment |
| Which spoke account should you use? | Any | Any |
| Which AWS Region should you use for the Trusted Advisor spoke template? |  `us-east-1` or `us-gov-west-1` Region |  `us-east-1` or `us-gov-west-1` Region |
| Which AWS Region should you use for the Service Quota spoke template? | Any | Any |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
