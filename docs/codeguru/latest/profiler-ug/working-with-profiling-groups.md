---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-profiling-groups.html
---

# Working with profiling groups
<a name="working-with-profiling-groups"></a>

A *profiling group* is a set of applications that are profiled together as a unit. Application data is sent by the Amazon CodeGuru Profiler profiling agent to a single profile group. Data from all applications in a profiling group are aggregated and analyzed together.

You manage profiling groups from the **Profiling groups** page in the [CodeGuru Profiler console](https://console.aws.amazon.com/codeguru/profiler/). The page provides a list of your profiling groups and the status. You can also create or delete a profiling group. When you select a profiling group, you can explore your profiling data by using different [visualizations](working-with-visualizations.md).

**Topics**
+ [Creating a profiling group](working-with-profiling-groups-create.md)
+ [Deleting a profiling group](working-with-profiling-groups-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
