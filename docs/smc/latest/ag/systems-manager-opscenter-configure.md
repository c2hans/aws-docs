---
source_url: https://docs.aws.amazon.com/smc/latest/ag/systems-manager-opscenter-configure.html
---

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html).

# Configuring AWS Systems Manager OpsCenter integration
<a name="systems-manager-opscenter-configure"></a>

This section describes how to configure the AWS Systems Manager OpsCenter integration in Jira Service Management. For the connector to synchronize AWS Systems Manager OpsCenter data in a specific Region, you must enable OpsCenter in that account and Region. For more information, refer to [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html).

**Configuring AWS Systems Manager OpsCenter integration**

This section describes how to validate the AWS Systems Manager OpsCenter integration in Jira.

**Note**
To view an AWS OpsItem, you must have access to the relevant Jira projects.

1. Log in to your Jira Agent as an internal customer or Jira agent.

1. In the Jira Service Management (Agent) view, choose the Jira project associated with the AWS OpsCenter OpsItem.

1. Use Jira filters to show only issues with type *AWS OpsCenter OpsItem*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Management Connector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query smc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
