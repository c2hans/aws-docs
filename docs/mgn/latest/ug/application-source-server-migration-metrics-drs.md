---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/application-source-server-migration-metrics-drs.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Review source server data replication status
<a name="application-source-server-migration-metrics-drs"></a>

The source server **Data replication status** migration metric presents an aggregated overview of the application associated servers data replication status. You can look up an individual source server's **Data replication status** at the **Source servers** table at the bottom of the page.

![Pie chart showing data replication status: 33.3% Initial sync, 66.7% Healthy.](http://docs.aws.amazon.com/mgn/latest/ug/images/app-8.png)

Source server **Data replication status** can have one of the following values:
+  **Transferring snapshot**
+  **Initial sync**
+  **Finalizing sync**
+  **Lagging**
+  **Healthy**
+  **Stalled**
+  **Rescanning**
+  **Not started**
+  **Initiating**
+  **Creating snapshot**
+  **Paused**
+  **Disconnected**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
