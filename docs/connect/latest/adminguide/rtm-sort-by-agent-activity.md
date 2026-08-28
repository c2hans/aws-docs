---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/rtm-sort-by-agent-activity.html
---

# Sort agents by activity in a real-time metrics report in Connect Customer
<a name="rtm-sort-by-agent-activity"></a>

On the real-time metrics **Agents** report, you can sort agents by **Activity** when agents are enabled to use the same channel.

For example, the following image shows that you can sort agents by the **Activity** column because all the agents are enabled to use the same channel: voice.

![The Agents report, the sort icon for the Activity column.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-activity-sortable.png)

However, if one or more agents are enabled to handle voice, chat, and tasks—or any two of the channels—you can't sort them by the **Activity** column because of the multiple channels. In this case, there's no option to sort by the **Activity** column, as shown in the following image:

![The Agents report, no sort icon appears in the Activity column.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-activity-not-sortable.png)

**Note**
The real-time metrics Agents report doesn't support secondary sorting. For example, you can't sort by **Activity**, and then sort by **Duration**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
