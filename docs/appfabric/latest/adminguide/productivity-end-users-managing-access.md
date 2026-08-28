---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/productivity-end-users-managing-access.html
---

# Manage access to AppFabric for productivity (preview) features for IT and security administrators
<a name="productivity-end-users-managing-access"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

The AppFabric for productivity user portal is publicly accessible to all users of SaaS applications who have integrated with AppFabric for productivity (preview) features. If you're an IT Administrator who wants to manage access to these generative AI features within your organization, consider these options:
+ Restrict Identity Provider (IdP) Login: You can block login access through your Identity Provider to control user access to generative AI features.
+ Disable OAuth for Specific Applications: Implement downstream restrictions by disabling OAuth. This action prevents users from connecting applications that require OAuth authentication to the company's workspace.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
