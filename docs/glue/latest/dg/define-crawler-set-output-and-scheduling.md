---
source_url: https://docs.aws.amazon.com/glue/latest/dg/define-crawler-set-output-and-scheduling.html
---

# Step 4: Set output and scheduling
<a name="define-crawler-set-output-and-scheduling"></a>

**Output configuration**
Options include how the crawler should handle detected schema changes, deleted objects in the data store, and more. For more information, see [Customizing crawler behavior](crawler-configuration.md)

**Crawler schedule**
You can run a crawler on demand or define a time-based schedule for your crawlers and jobs in AWS Glue. The definition of these schedules uses the Unix-like cron syntax. For more information, see [Scheduling a crawler](schedule-crawler.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
