---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_multi-action.html
---

# Start, stop, delete, or update runtime for multiple canaries
<a name="synthetics_canaries_multi-action"></a>

You can stop, start, delete, or update the runtime of as many as five canaries with one action. If you update the runtime of a canary, it is updated to the latest runtime available for the language and framework that the canary uses.

If you select multiple canaries and only some of them are in a state that is valid for the action that you select, the action is performed only on the canaries where that action is valid. For example, if you select some canaries that are currently running and some that are not, and you select to start the canaries, the canaries that weren't already running will start, and the canaries that were already running are not affected.

If none of the canaries that you select are valid for an action, that action will not be available in the menu.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Application Signals**, **Synthetics Canaries**.

1. Select the check boxes next to the canaries that you want to stop, start, or delete.

1. Choose **Actions** and then choose either **Start**, ** Stop**, **Delete**, **Start Dry Run**, or **Update Runtime**.

   In addition, when choosing **Update Runtime**, you can choose to dry run the runtime update first before committing the change.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
