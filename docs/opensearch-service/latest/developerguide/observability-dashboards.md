---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-dashboards.html
---

# Dashboards

Dashboards combine visualizations from logs, traces, and metrics into a single view. You can use dashboards to monitor operational health, respond to incidents, and track resource utilization across your distributed system.

The following table describes common use cases for dashboards.

| Use case | Example |
| --- | --- |
| Operational monitoring | Track service health, throughput, and error rates in real time. |
| Incident response | Correlate logs, traces, and metrics during an active incident. |
| Capacity planning | Monitor resource utilization trends to plan for scaling. |
| Availability tracking | Measure uptime and availability against service-level objectives. |
| Post-incident review | Analyze historical data to understand the root cause of past incidents. |

![Dashboard showing business metrics and telemetry including product reviews, cart additions, average charge, app availability gauge, request status codes, fault rates, throughput, and API calls.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/otel-dashboard.png)

**Topics**
+ [Dashboard structure](#observability-dashboards-structure)
+ [Building dashboards from Discover](#observability-dashboards-discover)
+ [Dashboard filters](#observability-dashboards-filters)
+ [Building dashboards](observability-dashboards-build.md)
+ [Sharing dashboards](observability-dashboards-sharing.md)
+ [Troubleshooting dashboards](observability-dashboards-troubleshooting.md)

## Dashboard structure
<a name="observability-dashboards-structure"></a>

A dashboard is a collection of panels arranged on a grid. Each panel consists of the following components.
+ **Data source** – The OpenSearch index or Amazon Managed Service for Prometheus data source that the panel queries.
+ **Query** – A PPL or PromQL query that retrieves the data for the panel.
+ **Visualization type** – The chart type used to render the query results, such as line, bar, or metric value.
+ **Optional configuration** – Axes, legends, thresholds, and formatting options.

The time range picker at the top of the dashboard applies to all panels. You can override the time range for individual panels when needed.

## Building dashboards from Discover
<a name="observability-dashboards-discover"></a>

The recommended workflow for building dashboards starts in Discover. This workflow is consistent across logs, traces, and metrics.

1. **Query your data in Discover** – Navigate to Discover Logs, Discover Traces, or Discover Metrics and write a query using PPL (for logs and traces) or PromQL (for metrics).

1. **Build a visualization** – When your query returns results, use the visualization tab to choose a chart type and configure the display. For log and trace queries, aggregation commands like `stats` automatically switch to the visualization view.

1. **Save to a dashboard** – Choose **Add to dashboard** to save the visualization to a new or existing dashboard. The panel stays live, updating as new data arrives.

1. **Iterate** – Repeat for each question you want the dashboard to answer. When something looks wrong on a dashboard, choose any panel to open the underlying query in Discover for further investigation.

**Important**
Visualizations created through the **Visualizations** page in OpenSearch UI use DQL (Dashboards Query Language) and DSL (Domain Specific Language), which do not support Piped Processing Language (PPL) at this time. To create PPL-based visualizations, use the Discover workflow described above.

## Dashboard filters
<a name="observability-dashboards-filters"></a>

Filters let you narrow the data displayed across all panels on a dashboard without editing individual queries.

**To add a filter**

1. Open the dashboard you want to filter.

1. Choose **Add filter** in the filter bar.

1. Select a field name from the dropdown list.

1. Select an operator and enter a value.

1. Choose **Save**.

The following table describes common filter use cases.

| Scenario | Field | Operator | Value |
| --- | --- | --- | --- |
| View a single environment | environment | is | production |
| Isolate errors | status\_code | is greater than or equal to | 400 |
| Focus on a specific service | service.name | is | order-service |
| Exclude health checks | http.url | is not | /health |

**Pinned compared to unpinned filters** – A pinned filter persists when you navigate between dashboards. An unpinned filter applies only to the current dashboard. To pin a filter, choose the pin icon next to the filter badge.
