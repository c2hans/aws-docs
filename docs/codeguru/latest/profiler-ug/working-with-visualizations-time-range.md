---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-time-range.html
---

# Selecting a custom time range
<a name="working-with-visualizations-time-range"></a>

By default, visualizations display the latest hour of data from the profiling group. You can select a different start time and end time to explore other data for other time ranges. This can be helpful to see how performance has changed over time.

**To select a custom time range**

1. In the **Profiling group detail** page, at the top of the visualization, select the date/time displayed. For example, **2019-12-04 @ 7:30 - 7:40 PST**.

1. In the **Select a custom time range** page, choose a **Start time**. You can optionally keep the existing start time.

1. Choose an **End time**. You can optionally keep the existing end time.

1. Choose **Confirm** to update the visualization.

If there is not enough data for the selected range, select a different time range. For the CodeGuru Profiler preview, you can reset the time range back to the default by choosing **Profiler**, **Profiling groups** in the navigation pane, and then selecting the profiling group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
