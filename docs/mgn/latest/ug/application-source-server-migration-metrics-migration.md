---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/application-source-server-migration-metrics-migration.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Review the application source server migration lifecycle
<a name="application-source-server-migration-metrics-migration"></a>

The source server **Migration lifecycle** metric shows an aggregated overview of the application associated servers migration lifecycle. You can look up an individual source server **Migration lifecycle** status at the **Source servers** table at the bottom of the page.

![Pie chart showing migration lifecycle status with three equal segments at 33.3% each.](http://docs.aws.amazon.com/mgn/latest/ug/images/app-9.png)

Source server **Migration lifecycle** can have one of the following values:
+  **Stopped**
+  **Not ready**
+  **Ready for testing**
+  **Test in progress**
+  **Ready for cutover**
+  **Cutover in progress**
+  **Cutover complete**
+  **Disconnected**
+  **Discovered**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
