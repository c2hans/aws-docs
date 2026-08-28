---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-deployment-groups.html
---

# Troubleshoot deployment group issues
<a name="troubleshooting-deployment-groups"></a>

## Tagging an instance as part of a deployment group does not automatically deploy your application to the new instance
<a name="troubleshooting-adding-instance-to-group"></a>

CodeDeploy does not automatically deploy your application to a newly tagged instance. You must create a new deployment in the deployment group.

You can use CodeDeploy to enable automatic deployments to new EC2 instances in Amazon EC2 Auto Scaling groups. For more information, see [Integrating CodeDeploy with Amazon EC2 Auto Scaling](integrations-aws-auto-scaling.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
