---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html
---

# IAM permissions
<a name="AMG-and-IAM"></a>

Access to Amazon Managed Grafana actions and data requires credentials. Those credentials must have permissions to perform the actions and to access the AWS resources, such as retrieving Amazon Managed Grafana data about your cloud resources. The following sections provide details about how you can use AWS Identity and Access Management and Amazon Managed Grafana to help secure your resources, by controlling who can access them. For more information, see [Policies and permissions in IAM.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

## Amazon Managed Grafana permissions
<a name="AMG-permissions"></a>

The following table displays possible Amazon Managed Grafana actions and their required permissions:

| Action | Required permission |
| --- | --- |
| Create an Amazon Managed Grafana workspace. A workspace is a logically isolated Grafana server used to create and visualize metrics, logs, and traces. | `grafana:CreateWorkspace` |
| Delete an Amazon Managed Grafana workspace.  | `grafana:DeleteWorkspace` |
| Retrieve detailed information about an Amazon Managed Grafana workspace.  | `grafana:DescribeWorkspace` |
| Retrieve the authentication configuration associated with a workspace. | `grafana:DescribeWorkspaceAuthentication` |
| Retrieve a list of permissions associated with workspace users and groups. | `grafana:ListPermissions` |
| Retrieve a list of the Amazon Managed Grafana workspaces that exist in the account. | `grafana:ListWorkspaces` |
| Update the permissions associated with workspace users and groups. | `grafana:UpdatePermissions` |
| Update Amazon Managed Grafana workspaces. | `grafana:UpdateWorkspace` |
| Update the authentication configuration associated with a workspace. | `grafana:UpdateWorkspaceAuthentication` |
| Associate a Grafana enterprise license with a workspace. | `grafana:AssociateLicense` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
