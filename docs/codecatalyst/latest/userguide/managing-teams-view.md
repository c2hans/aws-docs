---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-view.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Viewing a team
<a name="managing-teams-view"></a>

In CodeCatalyst, you can view the projects and roles for your team. On the members page, you can view project roles and a list of users. For SSO group type teams, you will also be able to see a list of SSO groups associated with the team.

**To view a team**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your space. Choose **Settings**, and then choose **Teams**.

1. In **Space role**, view the role assigned to the team for this space.

1. On the **Project roles** tab, view the project and project role assigned to the team for each CodeCatalyst project in the space where the team has been added as a member (for an AWS Builder ID space only).

1. On the **Members** tab, view the list of members assigned to the team.

1. On the **SSO Groups** tab, view the list of SSO groups assigned to the team (for a space that supports identity federation only).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
