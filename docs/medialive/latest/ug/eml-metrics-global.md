---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/eml-metrics-global.html
---

# Global metrics
<a name="eml-metrics-global"></a>

Global metrics relate to general performance and information for AWS Elemental MediaLive.

## Active alerts
<a name="eml-metrics-active-alerts"></a>

The total number of alerts that are active.

**Details:**
+ Name: ActiveAlerts
+ Units: Count
+ Meaning of zero: There are no active alerts
+ Meaning of no datapoints: The channel isn’t running
+ Supported dimension sets: ChannelID, Pipeline
+ Recommended statistic: Max

  All the statistics are useful for this metric.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
