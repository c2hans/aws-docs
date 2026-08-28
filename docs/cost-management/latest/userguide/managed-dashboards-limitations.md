---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/managed-dashboards-limitations.html
---

# Limitations of Managed Dashboards
<a name="managed-dashboards-limitations"></a>

Managed Dashboards are read-only. The following actions are not available for Managed Dashboards:
+ **Editing** - You cannot modify widget configurations, add new widgets, remove widgets, or change the dashboard layout permanently.
+ **Deleting** - You cannot delete Managed Dashboards. They are maintained by AWS and always available in your dashboard list.
+ **Sharing** - You cannot share Managed Dashboards with other accounts. They are already available in every account automatically.
+ **Tagging** - You cannot add tags to Managed Dashboards.
+ **Scheduling email delivery** - You cannot schedule email delivery directly on a Managed Dashboard. To schedule reports, duplicate the Managed Dashboard as a custom dashboard first, then configure the scheduled report on your custom copy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
