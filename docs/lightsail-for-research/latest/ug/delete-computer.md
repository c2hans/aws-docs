---
source_url: https://docs.aws.amazon.com/lightsail-for-research/latest/ug/delete-computer.html
---

# Delete a Lightsail for Research virtual computer
<a name="delete-computer"></a>

Complete the following steps to delete your Lightsail for Research virtual computer when you no longer need it. You stop incurring charges for the virtual computer as soon as it’s deleted. Resources that were attached to the deleted computer, such as snapshots, continue to incur charges until you delete them.

**Important**
Deleting a virtual computer is a permanent action, and the computer cannot be recovered. If you might need your data later, create a snapshot of your virtual computer before you delete it. For more information, see [Create a snapshot](create-snapshot.md).

1. Sign in to the [Lightsail for Research console](https://lfr.console.aws.amazon.com/ls/research).

1. Choose **Virtual computers** in the navigation pane.

1. Choose the virtual computer to delete.

1. Choose **Actions**, then choose **Delete virtual computer**.

1.  Type **confirm** in the text block. Then, choose **Delete virtual computer.**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail for Research. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail-for-research` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
