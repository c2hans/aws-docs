---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/detach-input.html
---

# Detaching an input
<a name="detach-input"></a>

You can detach an input from a MediaLive channel. The channel must be idle.

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Inputs**. Find the input in the list and choose its name. On the **Input Details**, find the ID of the channel that the input is attached to.

1. Choose that ID. The **Channel details** page for that channel appears.

1. Choose **Channel actions**, then choose **Edit channel**.

1. In the list of input attachments on the left, find the the name of the input to detach. Choose the name.

1. In the **Input attachment details** panel, choose **Remove**. The input is detached.

1. Choose **Update channel** at the bottom of the page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
