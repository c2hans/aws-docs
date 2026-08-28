---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/application-source-server-migration-metrics-alerts.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Review source server alerts
<a name="application-source-server-migration-metrics-alerts"></a>

The source server **Alerts** migration metric presents an aggregated overview of the application associated servers alerts. You can look up an individual source server **Alerts** status at the **Source servers** table at the bottom of the page.

![Pie chart showing server alerts: 2 servers healthy (66.7%), 1 server launched (33.3%).](http://docs.aws.amazon.com/mgn/latest/ug/images/app-7.png)

+ A healthy server for which a test or cutover instance has not been launched will display a **Healthy** status.
+ A healthy server for which a test or cutover instance has been launched will display a **Healthy** status.
+ A server that is experiencing a temporary issue such as lag or backlog will display a **Lagging** status.
+ A server that is experiencing significant issues, such as a stall, will display a **Stalled** status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
