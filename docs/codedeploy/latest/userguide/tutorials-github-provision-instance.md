---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github-provision-instance.html
---

# Step 4: Provision an instance
<a name="tutorials-github-provision-instance"></a>

In this step, you will create or configure the instance that you will deploy the sample application to. You can deploy to an Amazon EC2 instance or an on-premises instance that is running one of the operating systems supported by CodeDeploy. For information see [Operating systems supported by the CodeDeploy agent](codedeploy-agent.md#codedeploy-agent-supported-operating-systems). (If you already have an instance configured for use in CodeDeploy deployments, skip to the next step.)

**To provision an instance**

1. Follow the instructions in [Launch an Amazon EC2 instance (console)](instances-ec2-create.md#instances-ec2-create-console) to provision an instance.

1. When launching the instance, remember to specify a tag on the **Add tags** page. For details on how to specify the tag, see [Launch an Amazon EC2 instance (console)](instances-ec2-create.md#instances-ec2-create-console).

**To verify that the CodeDeploy agent is running on the instance**
+ Follow the instructions in [Verify the CodeDeploy agent is running](codedeploy-agent-operations-verify.md) to verify that the agent is running.

After you have successfully provisioned the instance and verified the CodeDeploy agent is running, go to the next step.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
