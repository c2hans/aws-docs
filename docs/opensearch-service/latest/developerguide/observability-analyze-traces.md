---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-analyze-traces.html
---

# Discover Traces

The Discover Traces page provides a dedicated interface for exploring distributed trace data in your OpenSearch Service observability workspace. You can view RED metrics (rate, error rate, duration) for your services, browse trace spans with faceted filtering, and drill into individual spans and traces to diagnose performance issues. The page also supports correlating traces with related log data.

## To access the Traces page
<a name="observability-traces-access"></a>

In your observability workspace, expand **Discover** in the left navigation and choose **Traces**.

![Traces interface showing request count, error count, and latency charts with a table of trace results below.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/discover-traces/discover-traces.png)

## Configuring trace datasets
<a name="observability-traces-configure-datasets"></a>

Before you can explore trace data, you must configure a traces dataset. You can create a dataset automatically or manually.

### Automatic dataset creation
<a name="observability-traces-auto-create"></a>

When you navigate to the Discover Traces page for the first time and trace data exists in your domain or collection, the page prompts you to create a dataset automatically. Choose **Create Trace Datasets** to accept the default configuration.

![Dialog box prompting to create trace datasets for a data source in which otel-v1-apm-span traces are detected.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/discover-traces/trace-auto-create.png)

### Manual dataset creation
<a name="observability-traces-manual-create"></a>

If your indexes use different naming conventions, you must manually create the datasets and configure the correlation relationships between traces and logs.

To manually create a traces dataset, follow the steps in [To create a traces dataset](observability-datasets.md#observability-datasets-create-traces). Manual creation gives you control over the index pattern, timestamp field, and dataset name.

## Exploring trace data
<a name="observability-traces-explore"></a>

The Discover Traces page provides the following components for exploring your trace data.
+ **RED metrics** – View rate (requests per second), error rate (percentage of failed requests), and duration (latency percentiles) for the selected dataset. These metrics update based on your time filter.
+ **Faceted fields** – Filter trace spans by service name, operation, status code, and other span attributes. Select values in the faceted fields panel to narrow your results.
+ **Span table** – Browse individual spans with columns for trace ID, span ID, service name, operation, duration, and status. You can sort by any column and expand rows to see span details.

## Viewing a specific span
<a name="observability-traces-view-span"></a>

To view details for a specific span, choose the timestamp in the span table. A flyout panel opens with the span attributes, resource attributes, and event information.

![Span details panel showing service identifier, span ID, start time, and span status for user_get_recommendations.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/discover-traces/trace-details-flyout.png)

The **Trace Details** flyout displays the following information:
+ The relationship of the selected span within its parent trace.
+ The hierarchical structure showing how the span relates to other spans in the same trace.

## Trace detail page
<a name="observability-traces-detail-page"></a>

To view the complete trace, choose the span ID in the span table or choose **Full page** in the flyout panel. The trace detail page displays a waterfall chart showing all spans in the trace, their timing relationships, and the overall trace duration. You can select individual spans to view their attributes and identify bottlenecks.

The full page view provides an expanded interface for deeper trace analysis, featuring a timeline visualization that shows the hierarchical span relationships and durations, along with detailed span information in a side panel. The page has four tabs: **Timeline**, **Span list**, **Trace map**, and **Related logs**.

![Trace detail page showing the timeline waterfall with service-colored bars, inline span durations, and error markers](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/obs-stack/discover-traces-trace-details-timeline.png)

### Reading the timeline
<a name="observability-traces-timeline"></a>

The **Timeline** tab shows the trace as a waterfall:
+ Each bar is colored by service. Select **Service legend** to see which color maps to which service.
+ Each span's duration appears at the end of its bar.
+ Error spans are outlined in red and marked with a warning icon.
+ Light vertical guides show nesting depth. The service name appears only when it changes from the row above.
+ Spans that call a database, message broker, or external service show the dependency's icon, such as PostgreSQL or Kafka. Hover over the icon to see the dependency type and system, for example `Database: postgresql`. For more information, see [External dependencies](#observability-traces-dependencies).

Use the toolbar above the waterfall to control the view:

| Control | What it does |
| --- | --- |
| Expand all / Collapse all | Expands or collapses the entire span tree. |
| Expand one level / Collapse one level | Moves the whole tree one level at a time. Disabled at the top and bottom levels. |
| Full screen | Opens the timeline in full screen. |
| Density | Switches row density between Compact, Normal, and Expanded. |
| Reset zoom | Restores the full trace duration after you zoom. |

To zoom, drag the slider under the time ruler. The bars and ruler rescale to the selected window, and spans outside it are dimmed.

### Filtering spans
<a name="observability-traces-filter-spans"></a>

The **Filters** bar above the tabs narrows the timeline, span list, and trace map at the same time:
+ **Status**: Show only spans with the **Error**, **OK**, or **Unset** status.
+ **Duration**: Show only spans at least as long as a minimum duration. Enter a value in milliseconds, or select a **p90** or **p99** preset calculated from the current trace.
+ **Attributes**: Filter on any span field with `=` or `!=`. Choose the field from the dataset's field list, then pick a value from the loaded spans or type one.

Each applied filter appears as a pill, such as `status = Error`. Select a pill to edit its value, select its **x** to remove it, or select **Clear all** to remove every filter. **Status** and **Duration** filters apply instantly without querying the cluster again.

![Filters bar with a status = Error pill applied and the Duration popover showing p90 and p99 presets](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/obs-stack/discover-traces-trace-details-filters.png)

### Viewing the trace map
<a name="observability-traces-trace-map"></a>

The **Trace map** tab shows how the services in the trace call each other:
+ Each service is a card with **Requests**, **Errors**, and **Duration** bars. Services with errors show an error marker.
+ Edges get thicker as call volume increases and are labeled with the call count.
+ Select a service card to add a `serviceName` filter that scopes the whole page to that service.

You can drag cards, zoom, and fit the map to the view. A minimap appears on the full page but not in the flyout.

![Trace map tab showing service cards with request, error, and duration bars connected by call-count edges](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/obs-stack/discover-traces-trace-details-trace-map.png)

### External dependencies
<a name="observability-traces-dependencies"></a>

Calls from your services to databases, message brokers, and external services appear as dependencies in the trace map and the timeline, even though those systems don't emit spans of their own. Dependencies are detected from the OpenTelemetry attributes on the calling spans, so they need no extra ingestion configuration.

In the **Trace map** tab:
+ Each dependency is a card labeled **Database**, **Messaging**, or **External**, with the system's icon (for example PostgreSQL, Redis, or Kafka) or a generic icon for the type. Like service cards, dependency cards show **Requests**, **Errors**, and **Duration** bars.
+ Dependencies are named from the span attributes, for example `redis:valkey-cart` for a database, `kafka:orders` for a message broker topic, or `api.openai.com` for an external service.
+ Edges point from the calling service to the dependency. For messages a service consumes, the edge points from the broker to the service.
+ Select a dependency card to filter the trace to the spans that call it, for example `attributes.server.address = valkey-cart`. Select it again to remove the filter. If no single attribute identifies the dependency, selecting the card doesn't add a filter.

In the span details, attributes that describe the dependency, such as `db.*`, `messaging.*`, and `peer.service`, are grouped under **Dependency** on the **Metadata** tab.

## Correlating traces with logs
<a name="observability-traces-correlate-logs"></a>

When you configure a correlation between a traces dataset and a logs dataset, you can view related log entries directly from the Discover Traces page. For information about creating correlations, see [Correlations](observability-correlations.md).

### Viewing related logs
<a name="observability-traces-related-logs"></a>

In the span details flyout or trace detail page, choose the **Related logs** tab to view log entries that match the span's trace ID, service name, and time range. This correlation helps you understand what happened in your application during the span execution.

![Related logs tab showing log entries filtered by trace ID with timestamps, levels, and span IDs.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/discover-traces/related-logs.png)

### Log redirection with context
<a name="observability-traces-log-redirection"></a>

You can navigate from a trace span directly to the Discover Logs page with the relevant context preserved. Choose **View in Discover Logs** from the related logs panel to open the Discover Logs page with the query pre-populated to filter by the span's trace ID and time range.

![Logs page showing 8 query results filtered by trace ID with log entries from various services.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/discover-traces/logs-redirection.png)

## Querying traces using PPL
<a name="observability-traces-querying"></a>

You can use PPL to query trace data directly. PPL chains commands using the pipe character to filter, transform, and aggregate span data.

**Note**
The following examples query the `otel-v1-apm-span*` indexes. On a domain with the engine optimized for log analytics, an observability stack stores spans in `otel-v2-apm-span*`, so use that index name instead. The field names that these examples use are the same in both indexes.

The following example finds the 10 slowest traces that take longer than 5 seconds (5,000,000,000 nanoseconds):

```
source = otel-v1-apm-span*
| where durationInNanos > 5000000000
| fields traceId, serviceName, name, durationInNanos
| sort - durationInNanos
| head 10
```

The following example counts errors by service:

```
source = otel-v1-apm-span*
| where status.code = 2
| stats count() as errorCount by serviceName
| sort - errorCount
```

The following example finds traces for a specific service:

```
source = otel-v1-apm-span*
| where serviceName = 'checkout-service'
| where parentSpanId = ''
| sort - startTime
| head 20
```
