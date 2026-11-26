---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-metrics.html
---

# Discover Metrics

The Discover Metrics page in OpenSearch UI provides a dedicated interface for discovering, querying, and visualizing time-series metric data. This page is optimized for working with Prometheus metrics using PromQL.

![Line graph showing CPU usage metrics by mode over time with a tooltip displaying values for different modes at 14:02:29.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/dashboards/prometheus.png)

The page has two modes, switched with the radio toggle at the top:
+ **Explore** – a no-code metric browser for finding metrics and filtering by labels.
+ **Query** – a PromQL editor for authoring and visualizing expressions.

Both modes share the same time range picker and data source selector; switch at any time.

The Discover Metrics page is available in Observability workspaces. To access it, navigate to an Observability workspace, expand **Discover** in the left navigation, and select **Metrics**.

## Configuring a Prometheus data source
<a name="observability-metrics-data-source"></a>

Before you start, configure a Prometheus data source using one of the following methods:
+ [Creating an Amazon Managed Service for Prometheus data source](direct-query-prometheus-creating.md) in the AWS Management Console
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/opensearch/add-direct-query-data-source.html)

For the permissions that the data source needs, see [Creating an Amazon Managed Service for Prometheus data source](direct-query-prometheus-creating.md).

## Explore mode
<a name="observability-metrics-explore"></a>

Browse and discover metrics without writing PromQL. Use it to find a metric when you don't yet know what to query.

The following image shows Explore mode after a search for `mem`. Each matching metric appears on a card with a sparkline and a metric type badge.

![Metrics Explore mode with a search for mem and metric cards that each show a sparkline and a metric type badge.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/obs-stack/discover-metrics-explore.png)

The interface includes:
+ A **metric browser** that lists all metrics from the data source as cards, each with a small sparkline preview.
+ A **search box** with debounced server-side filtering by metric name.
+ **Label filters** that narrow the metric list to only those carrying matching labels. Each filter row uses a Prometheus operator: `=`, `!=`, `=~` (regex match), or `!~` (regex not match).
+ **Grouping** options that organize metric cards by **Prefix** (the namespace prefix of the metric name) or **A-Z** (alphabetical, in a single group).
+ **Layout** options for **Grid** or **Rows**.
+ **Metric type** badges (Counter, Gauge, Histogram, Summary, or Unknown) taken from Prometheus metric metadata, with a fallback that infers Counter and Histogram from name suffixes (`_total`, `_count`, `_sum`, `_created`, `_bucket`) when metadata is missing.

Click a metric card to open the **metric detail** view, which previews the time series broken down by label and lets you drill into a specific label combination. Or select one or more metric cards and select **Query Metrics** to send them into Query mode as a multi-query execution.

## Query panel
<a name="observability-metrics-query"></a>

You can write and run metric queries in the query panel at the top of the Discover Metrics page. The query editor provides autocomplete suggestions and syntax highlighting for PromQL.

Author one or more PromQL expressions and render them in a chart. Use it when you know what you want to compute.

Each query lives in its own row.

**Writing queries**
Write queries using PromQL syntax. For example:

```
up{job="prometheus"}
```

**Running queries**
To run a query, enter your query in the query editor and select **Refresh**.

To run several queries together in a single execution, add a row for each one or, in Code mode, separate them with a semicolon (`;`):

```
up{job="prometheus"};
node_cpu_seconds_total{mode="idle"};
```

Each query runs independently, and the results are rendered side by side on the visualization.

### Builder versus Code
<a name="observability-metrics-query-builder-code"></a>

Each query row has two editor styles, toggled per row:
+ **Builder** – a structured UI for selecting a metric, adding label filters with operators (`=`, `!=`, `=~`, `!~`), and chaining operations (aggregations, range functions, math). Useful when you're learning PromQL or want fewer typos.
+ **Code** – a raw PromQL editor with autocomplete and syntax highlighting. Suggestions are fetched from the Prometheus data source and trigger on space, `(`, `{`, `[`, `,`, `=`, `~`, `'`, and `"`.

You can switch between Builder and Code at any time. Switching from Builder to Code reveals the underlying PromQL; the reverse parses your PromQL back into Builder controls when possible.

### Per-row query options
<a name="observability-metrics-query-options"></a>

Each query row has a gear popover for options that apply to that row only:
+ **Min step** – a lower bound on the resolved step, in seconds. It is also treated as the assumed scrape interval when sizing the `rate()` window.
+ **Series name** – a `{{label}}` template that renames the returned series in the legend. For example, `{{job}} - {{instance}}` formats each series using the values of its `job` and `instance` labels.

Each row also displays the resolved step (`$__interval`) and rate window (`$__rate_interval`) it actually ran with.

### Interval macros
<a name="observability-metrics-interval-macros"></a>

Queries can reference interval macros that are interpolated per query segment at execution time. Autocomplete suggests them in Code mode:
+ `$__interval`, `$__interval_ms` – the resolved step, in seconds or milliseconds.
+ `$__rate_interval` – the rate window sized for the resolved step and assumed scrape interval.
+ `$__range`, `$__range_s`, `$__range_ms` – the active time range, as a duration string, seconds, or milliseconds.

For example, `rate(node_cpu_seconds_total[$__rate_interval])` sizes the rate window automatically as you zoom in and out.

### Step and resolution
<a name="observability-metrics-step-resolution"></a>

The step is derived from the active time range, targeting a number of datapoints with a 15-second floor. The `rate()` window is sized to be at least four times the assumed scrape interval and at least one scrape interval larger than the step, so zoomed-out views don't show gaps.

In Query mode, a **Query options** popover on the panel exposes **Max data points**: the datapoint target the step is derived from (default 1440), shared across all query rows. Leave it blank to auto-resolve; the placeholder then reports the resolution used in the last run. Combine it with a row's **Min step** to control resolution precisely.

In Explore mode, sparkline and detail queries are generated using the same resolver, with a 60-second assumed scrape interval.

## Time filter
<a name="observability-metrics-time-filter"></a>

Use the time filter to specify the time range for your metric data:
+ **Quick select** – Choose a relative time range (for example, the last 15 minutes or the last 1 hour).
+ **Commonly used** – Select from predefined time ranges.
+ **Custom** – Specify absolute start and end times.
+ **Auto-refresh** – Set an automatic refresh interval.

## Viewing results
<a name="observability-metrics-results"></a>

After running a query, the results are displayed in a tabbed interface:
+ **Table** – Displays the latest data point for each series in a table format, with a banner if the response was truncated for performance.
+ **Visualization** – Provides interactive charts for your metric data.

### Series limit
<a name="observability-metrics-series-limit"></a>

To keep the browser responsive, the visualization renders up to **20 series** by default. If a query returns more, a banner appears with a **Show {count}** button to render all of them. Tighten label filters or aggregate (for example, `sum by (...)`) to bring the count down rather than rendering hundreds of series.

## Configuring visualizations
<a name="observability-metrics-visualizations"></a>

When the **Visualization** tab is selected, a settings panel appears on the right side of the screen. Use this panel to:
+ **Select a chart type** – Choose from line, bar, area, scatter, pie, heatmap, table, metric, gauge, bar gauge, state timeline, histogram, or sankey visualizations.
+ **Map axes** – Assign fields to the X and Y axes.
+ **Customize styles** – Adjust colors, legends, gridlines, thresholds, units, and other visual options.

When you modify the settings, the visualization is updated automatically.

For a description of each visualization type, see [Visualization types](observability-analyze-logs.md#observability-logs-viz-types).

## Saving and reusing
<a name="observability-metrics-saving"></a>

Metrics explorations are saved as **Explore** saved objects. Save a query from the page actions to revisit it later, or add a metrics view as a panel on a new or existing dashboard to track it alongside logs and traces. From the global **Visualize** application, choosing **Create visualization → Visualize with Metrics** also opens a fresh metrics canvas in Query mode.
