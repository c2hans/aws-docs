---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/support-devops-agent-removing.html
---

# Removing AWS DevOps Agent
<a name="support-devops-agent-removing"></a>

To remove the resources that were created when you enabled AWS DevOps Agent from the Support Center Console, see [Deleting an agent space](https://docs.aws.amazon.com/devopsagent/latest/userguide/deleting-an-agent-space.html) in the *AWS DevOps Agent User Guide*. The procedures cover deleting the agent space, the two IAM roles, and any customer-managed policies that start with `AIDevOps`. The procedure also documents how to re-enable AWS DevOps Agent later and what to watch out for when you do.

**Note**
The AWS-managed policies attached to the IAM roles (`AIDevOpsAgentAccessPolicy` and `AIDevOpsOperatorAppAccessPolicy`) are detached but not deleted, because these policies are owned by AWS.

When you follow that procedure, note that your resources have the names listed in [Resources created for AWS DevOps Agent activated from AWS Support](support-devops-agent-resources.md), and they are all in `us-east-1`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
