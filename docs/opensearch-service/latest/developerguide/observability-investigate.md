---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-investigate.html
---

# Investigate

The Discover experience in OpenSearch Service provides a unified investigation starting point for your observability data. From Discover, you can query logs, traces, and metrics using purpose-built query languages, create visualizations from query results, and save your work to dashboards for ongoing monitoring.

Datasets define the indexes and configuration for each Discover page, and you must create a dataset before you can query data in Discover. Correlations link traces and logs datasets so that you can view related log entries when investigating trace spans.

**Topics**
+ [Discover as an investigation starting point](#observability-investigate-starting-point)
+ [Query languages at a glance](#observability-investigate-query-languages)
+ [Autocomplete and query assistance](#observability-investigate-autocomplete)
+ [Visualizations in Discover](#observability-investigate-visualizations)
+ [Add to dashboard](#observability-investigate-save-dashboard)
+ [Save and share queries](#observability-investigate-save-queries)
+ [Datasets](observability-datasets.md)
+ [Explore Logs](observability-investigate-explore-logs.md)
+ [Discover Logs](observability-analyze-logs.md)
+ [Discover Traces](observability-analyze-traces.md)
+ [Discover Metrics](observability-metrics.md)
+ [Correlations](observability-correlations.md)

## Discover as an investigation starting point
<a name="observability-investigate-starting-point"></a>

Each Discover page is optimized for a specific telemetry type. The following table describes the available pages and their query languages.

| Page | Query language | More information |
| --- | --- | --- |
| Discover Logs | PPL | [Discover Logs](observability-analyze-logs.md) |
| Discover Traces | PPL | [Discover Traces](observability-analyze-traces.md) |
| Discover Metrics | PromQL | [Discover Metrics](observability-metrics.md) |

## Query languages at a glance
<a name="observability-investigate-query-languages"></a>

### PPL
<a name="observability-investigate-ppl"></a>

Piped processing language (PPL) uses pipe-based (`|`) syntax for chaining commands. You use PPL to query logs and traces data in Discover.

The following examples show common PPL queries.

Retrieve error logs for a specific service:

```
source = my-logs-dataset |
    where severityText = 'ERROR' and `resource.attributes.service.name` = 'order-service'
```

Count errors by service over time:

```
source = my-logs-dataset |
    where severityText = 'ERROR' |
    stats count() as error_count by `resource.attributes.service.name`, span(time, 1h)
```

Find the slowest trace spans:

```
source = my-traces-dataset |
    sort -durationInNanos |
    head 10
```

For more information about PPL, see the [PPL reference manual](https://observability.opensearch.org/docs/ppl/) on opensearch.org.

### PromQL
<a name="observability-investigate-promql"></a>

PromQL is a query language for Prometheus metrics. You use PromQL to query time-series metric data in the Discover Metrics page.

The following examples show common PromQL queries.

Query a specific metric:

```
up{job="prometheus"}
```

Calculate the rate of HTTP requests over 5 minutes:

```
rate(http_requests_total[5m])
```

For more information about PromQL, see the [PromQL documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/) on the Prometheus website.

## Autocomplete and query assistance
<a name="observability-investigate-autocomplete"></a>

The query editor in each Discover page provides autocomplete suggestions as you type. Autocomplete suggests field names, commands, and functions based on the selected dataset and query language. The Discover Logs page also provides natural language query assistance through the AI Assistant, which translates plain language questions into PPL queries. For prerequisites, see [AI Assistant in Amazon OpenSearch Service](application-ai-assistant.md).

## Visualizations in Discover
<a name="observability-investigate-visualizations"></a>

You can create visualizations directly from query results in Discover. The following table describes the available visualization types.

| Type | Use case |
| --- | --- |
| Line | Trends over time |
| Area | Volume over time |
| Bar | Comparing values across categories |
| Metric | Key performance indicators |
| State timeline | Status transitions over time |
| Heatmap | Density and patterns |
| Bar gauge | Progress toward a threshold |
| Pie | Composition and proportions |
| Scatter | Relationship between two numeric fields |
| Table | Detailed breakdowns |
| Gauge | A single value within a range |
| Histogram | Distribution of a numeric field |
| Sankey | Flows between two dimensions |

## Add to dashboard
<a name="observability-investigate-save-dashboard"></a>

After you create a visualization in Discover, you can save it to a dashboard for ongoing monitoring. Choose **Add to dashboard** in the results area, then select an existing dashboard or create a new one.

## Save and share queries
<a name="observability-investigate-save-queries"></a>

You can save frequently used queries for reuse and share them with other users in your workspace. To save a query, choose **Saved queries** > **Save query** and enter a name. Saved queries are available to all users with access to the workspace.
