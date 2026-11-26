---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-dashboards-build.html
---

# Building dashboards

## Visualization types
<a name="observability-dashboards-build-viz-types"></a>

The following table describes the visualization types available for dashboard panels.

| Type | Use case |
| --- | --- |
| Line | Trends over time, such as request rates or latency |
| Area | Volume over time with stacked breakdowns |
| Bar | Comparing values across categories |
| Horizontal bar | Ranked comparisons, such as top services by error count |
| Data table | Tabular data with sorting and pagination |
| Metric value | Single key performance indicators, such as total requests |
| Gauge | Progress toward a threshold, such as CPU utilization |
| Pie | Composition and proportions, such as traffic by region |
| Heat map | Density and distribution patterns over two dimensions |
| Tag cloud | Relative frequency of terms, such as common error messages |

Panels that you create from Discover use a different set of visualization types. For that list, see [Visualization types in Discover Logs](observability-analyze-logs.md#observability-logs-viz-types).

## Configuring panels
<a name="observability-dashboards-build-configure"></a>

Each panel has a query editor where you write PPL or PromQL queries. The following examples show common panel queries.

Error count by service (PPL):

```
source = logs-dataset |
    where severityText = 'ERROR' |
    stats count() as error_count by `resource.attributes.service.name`, span(time, 5m)
```

CPU utilization rate (PromQL):

```
rate(container_cpu_usage_seconds_total{namespace="production"}[5m])
```

You can also configure the following panel options.
+ **Axes** – Set axis labels, scales (linear or logarithmic), and value ranges.
+ **Legends** – Control legend position and which series to display.
+ **Thresholds** – Add horizontal threshold lines to highlight warning or critical levels.

## Layout tips
<a name="observability-dashboards-build-layout"></a>

Use the following tips to organize your dashboard panels effectively.
+ Place high-level summary panels (metric values, gauges) at the top of the dashboard.
+ Group related panels together, such as all panels for a single service.
+ Use consistent widths for panels in the same row.
+ Drag panel edges to resize, and drag panel headers to reposition.

## Recommended layouts
<a name="observability-dashboards-build-recommended"></a>

The following tables describe recommended panel layouts for common dashboard types.

**Service health dashboard**

| Panel | Visualization type |
| --- | --- |
| Request rate | Line |
| Error rate | Line |
| P99 latency | Line |
| Active alerts | Metric value |
| Top errors by service | Horizontal bar |

**Incident response dashboard**

| Panel | Visualization type |
| --- | --- |
| Error logs | Data table |
| Error count over time | Area |
| Affected services | Pie |
| Latency spikes | Line |

**Resource utilization dashboard**

| Panel | Visualization type |
| --- | --- |
| CPU utilization | Gauge |
| Memory usage over time | Area |
| Disk I/O | Line |
| Network throughput | Line |

## Time range controls
<a name="observability-dashboards-build-time-range"></a>

The time range picker at the top of the dashboard controls the time window for all panels. You can select a preset range (such as **Last 15 minutes** or **Last 24 hours**) or specify a custom absolute range.

To enable auto-refresh, choose the refresh interval dropdown next to the time range picker and select an interval. Auto-refresh re-runs all panel queries at the specified interval so that your dashboard displays the latest data.
