---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/performance-measures.html
---

# Assessing performance by measuring
<a name="performance-measures"></a>

There are several features of the appliance that affect performance:
+ CPU usage
+ RAM usage
+ I/O bandwidth
+ Memory bandwidth

You should look at all these features when measuring performance and attempting to increase density. For example, it is possible that your workflows aren't stressing the CPU capabilities, but they are making maximum demands on the I/O bandwidth.

**Topics**
+ [CPU usage](performance-cpu-usage.md)
+ [RAM usage](performance-ram-usage.md)
+ [I/O bandwidth](performance-io-bandwidth.md)
+ [System bandwidth](performance-system-bandwidth.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
