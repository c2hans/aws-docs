---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/v12-drilldown-logs.html
---

# Logs Drilldown
<a name="v12-drilldown-logs"></a>

The Logs Drilldown app provides a queryless experience for browsing Loki logs. You can discover or narrow down your search by using volume and text patterns without needing to compose LogQL queries.

Key capabilities include:
+ Visualize log volumes to detect anomalies or significant changes over time.
+ Customizable top-level filtering by any indexed label.
+ Regex filtering for pattern matching in raw log lines.
+ Log patterns for identifying common log structures.
+ JSON viewer for structured log lines.
+ Infinite scrolling to browse large log volumes without pagination.
+ Shareable links to specific log lines or result sets.

To access Logs Drilldown, choose **Drilldown** and then **Logs** from the Grafana navigation menu.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
