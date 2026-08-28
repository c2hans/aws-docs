---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-alerts.html
---

# Alerts that MediaLive generates
<a name="monitor-activity-alerts"></a>

MediaLive can generate alerts when a channel is running. For a list of alerts, see [List of alerts for channels](monitor-activity-types-alerts-channels.md).

You can view the alerts for each channel on the MediaLive console. For more information, see [Alerts tab – Viewing alerts](monitoring-console-general.md#view-alerts).

MediaLive turns alerts into CloudWatch events with the detailType set to `MediaLive Channel Alert`. For an example of the JSON for these events, see [JSON for a state change event](monitoring-cloudwatch-json-state-change.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
