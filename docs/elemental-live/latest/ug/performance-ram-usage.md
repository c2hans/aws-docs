---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/performance-ram-usage.html
---

# RAM usage
<a name="performance-ram-usage"></a>

RAM usage is the percentage of the memory being used on the appliance memory cards.

You can measure free memory using the `top` or `free` commands.

In Elemental Live versions 2.19.1 and later, the status bar at the top of the Elemental Live web interface includes a memory usage indicator.

Typically, RAM usage doesn't create performance problems on Elemental Live appliances. However, you should still monitor RAM usage to make sure that you always have enough free memory. If the appliance runs out of memory and starts to swap memory, there will be performance and video quality issues.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
