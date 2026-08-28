---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/show-agent-queues.html
---

# Show agent queues in a Queues table for historical metrics
<a name="show-agent-queues"></a>

By default agent queues don't appear in a Queues table in a historical metrics report. You can choose to show them.

**To show agent queues in a Queues table**

1. In a historical metrics report, choose the **Settings** icon, as shown in the following image.
![The historical metrics queues report, the settings icon.](http://docs.aws.amazon.com/connect/latest/adminguide/images/hmr-queues-settings.png)

1. Choose **Filters**, **Show agent queues**, **Agent queues**, and then use the drop-down to choose the agent's queues you want to include in the table. These options are shown in the following image.
![Tables settings page, Filters tab, show agent queues option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/hmr-queues-settings-agent-queues.png)

1. Choose **Apply**. The agent queues you selected appear in the Queues table in the historical metrics report.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
