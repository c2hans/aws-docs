---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/mu-remove-project-admin.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Removing an admin user
<a name="mu-remove-project-admin"></a>

Every project must have at least one admin user. Before removing an admin user from a project, make sure that there is at least one other admin user assigned to it.

**Topics**
+ [To remove an admin user](#remove-project-admin)

## To remove an admin user
<a name="remove-project-admin"></a>

1. Open the Amazon Monitron console at [ https://console.aws.amazon.com/monitron ](https://console.aws.amazon.com/monitron/).

1. Choose **Create Project**.

1. In the navigation pane, choose the project you want.

1. From the **Admin Users** list, choose the user that you want to remove.

1. Choose **Remove**.

1. Choose **Remove** again.

   The user is removed from the list of admin users for that project.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
