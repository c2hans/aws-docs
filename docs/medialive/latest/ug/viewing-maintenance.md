---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/viewing-maintenance.html
---

# Viewing maintenance information
<a name="viewing-maintenance"></a>

You can view maintenance information from the MediaLive console or from the Personal Health Dashboard in Health Dashboard.

## Viewing information on the MediaLive console
<a name="viewing-maintenance-medialive"></a>

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Channels**.

   In the list of channels that appears, there are two columns on the right-hand side: **Maintenance status** and **Maintenance window**, which shows the upcoming maintenance

## Viewing information on the Personal Health Dashboard
<a name="viewing-maintenance-phd"></a>

On the Personal Health Dashboard, you can view information upcoming maintenance events for all channels in your AWS account.

1. Open the Health Dashboard at [https://phd.aws.amazon.com/phd/home\#/](https://phd.aws.amazon.com/phd/).

1. In the navigation pane, choose **Your account health**, then choose **Other notifications**. Use the filter to find events with a title that includes **MediaLive maintenance event**.

   Each event lists the channels, the Region, and the state date.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
