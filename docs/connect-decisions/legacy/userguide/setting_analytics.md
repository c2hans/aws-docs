---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/setting_analytics.html
---

# Setting AWS Supply Chain Analytics
<a name="setting_analytics"></a>

You must enable AWS Supply Chain Analytics before you can start using Quick dashboards.

1. In the left navigation pane on the Supply Chain dashboard, choose the **Settings** icon.

1. Under **Organization**, choose **Analytics**.

   The **Analytics** setting page appears.
![Setting AWS Supply Chain Analytics](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/analytics_settings.png)

1. Slide the **Enable data access for Analytics** button to enable AWS Supply Chain Analytics.

1. Under **User and Permissions**, choose **Permission Roles**.

   You can edit the permission roles for a current user or add a new permission role to enable Analytics access.
![Setting AWS Supply Chain Analytics permissions](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/analytics_permissions.png)

1. On the **Manage Permission Role** page, under **Analytics**, slide the **Manage** or **View** button to grant read or write access.
   + *Manage – Select this permission role if you want the Analytics user to create and view dashboards.*
   + *View – Select this permission role if you want the Analytics user to only view the dashboards.*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
