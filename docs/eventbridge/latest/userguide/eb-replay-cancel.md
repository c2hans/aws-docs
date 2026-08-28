---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-replay-cancel.html
---

# Canceling replays of archived events in Amazon EventBridge
<a name="eb-replay-cancel"></a>

If you start a replay and then want to stop it, you can cancel it while its status is `Starting` or `Running`.

**To cancel a replay (console)**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the left navigation pane, choose **Replays**.

1. Choose the replay to cancel.

1. Choose **Cancel**.

**To cancel a replay (AWS CLI)**
+ Use [cancel-replay](https://docs.aws.amazon.com/cli/latest/reference/events/cancel-replay.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
