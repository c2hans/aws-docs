---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.monitor.html
---

# Step 7: Monitor Your Migration Task
<a name="chap-on-premoracle2aurora.steps.monitor"></a>

Three sections in the console provide visibility into what your migration task is doing:
+ Task monitoring — The **Task Monitoring** tab provides insight into your full load throughput and also your change capture and apply latencies.
+ Table statistics — The **Table Statistics** tab provides detailed information on the number of rows processed, type and number of transactions processed, and also information on DDL operations.
+ Logs — From the **Logs** tab you can view your task’s log file, (assuming you turned logging on.) If for some reason your task fails, search this file for errors. Additionally, you can look in the file for any warnings. Any data truncation in your task appears as a warning in the log file. If you need to, you can increase the logging level by using the AWS Command Line Interface (AWS CLI).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
