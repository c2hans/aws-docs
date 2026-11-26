---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-analyze-logs.html
---

# Discover Logs

The Discover Logs page provides a dedicated interface for exploring and analyzing log data in your OpenSearch Service observability workspace. You can write PPL queries to filter and aggregate log data, create visualizations directly from query results, and add those visualizations to dashboards. The page also provides natural language query assistance through the AI Assistant. For prerequisites, see [AI Assistant in Amazon OpenSearch Service](application-ai-assistant.md).

The **Logs** page provides the following capabilities:
+ **Visual query building**: Build queries from menus with the [PPL Query Builder](#observability-logs-query-builder), writing no PPL.
+ **Automatic visualization**: When you use aggregation commands like `stats`, the interface automatically switches to a visualization view.
+ **Query management**: Save queries for reuse and access recent queries.

**Tip**
If you know a log index exists but haven't created a dataset to query it, start from [Explore Logs](observability-investigate-explore-logs.md). It shows the indexes and datasets in your data source with a live severity histogram and log preview. You can also use it to turn an index into a queryable dataset.

## To access the Logs page
<a name="observability-logs-access"></a>

In your observability workspace, expand **Discover** in the left navigation and choose **Logs**.

## Exploring log data
<a name="observability-logs-explore"></a>

The Discover Logs interface provides the following components for exploring your log data.

![Logs interface showing bar chart of log counts, field list, and table with timestamp, body, severity, and service columns.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/discover-logs/discover-logs-interface.png)

+ **Dataset selector** – Choose the logs dataset that you want to query. Each dataset maps to one or more indexes in your OpenSearch Service domain or collection.
+ **Query editor** – Write PPL queries to filter, aggregate, and transform your log data. The editor provides autocomplete suggestions and syntax highlighting.
+ **Time filter** – Specify the time range for your query results. You can choose a relative range or specify absolute start and end times.
+ **Results panel** – View query results as a table of log events. You can expand individual events to see all fields.

  Displays query results in tabs, including the following:
  + **Logs**: Shows individual log entries in a table format.
  + **Visualization**: Displays aggregated data as charts when using `stats` commands.
+ **Histogram** – View the distribution of log events over time. The histogram updates automatically based on your query and time filter.

  The **Log count** histogram shows the distribution of log entries over time. Use the **Interval** selector to adjust the time bucket size.
+ **Fields panel** – Browse available fields in your dataset and add them as columns to the results table.

  Located on the left side, the **Fields** panel displays available fields in the **Selected** and **Discovered** sections. A **Query** section also appears when the results of the current query contain fields that you haven't selected, and lists those fields.
+ **Recent queries**: Access previously run queries at the top of the page.
+ **Saved queries**: Access queries you have saved for reuse at the top of the page.

### Table settings
<a name="observability-logs-table-settings"></a>

Select the **Table settings** icon in the action bar above the **Logs** table to change how the table renders:
+ **Hide empty fields**: Hides columns that have no value in any row of the current results, and hides fields with no value when you expand a row. A column with a value in even one row stays visible, and `0`, `false`, and empty strings count as values. While columns are hidden, the hit count shows how many, for example **3 columns hidden**. Select it to show them again. The toggle is off by default, turns off when you change the dataset, and also applies to CSV exports.
+ **Wrap cell text**: Wraps long cell values onto multiple lines.

## Querying logs using PPL
<a name="observability-logs-query-ppl"></a>

Piped processing language (PPL) is a query language that uses pipe-based (`|`) syntax for chaining commands. You can use PPL to filter, aggregate, and transform your log data.

For the complete list of PPL commands and functions, see the [Piped Processing Language reference](https://observability.opensearch.org/docs/ppl/).

### Basic queries
<a name="observability-logs-basic-queries"></a>

To retrieve all log events from a dataset, use the `source` command:

```
source = my-logs-dataset
```

To limit the number of results, use the `head` command:

```
source = my-logs-dataset | head 20
```

The results appear in the **Logs** tab showing individual log entries.

### Filtering with WHERE
<a name="observability-logs-where-clause"></a>

Use the `where` clause to filter log events based on field values:

```
source = my-logs-dataset | where severityText = 'ERROR'
```

You can combine multiple conditions, either in one `where` clause or in several `where` clauses. The following examples show both forms:

```
source = my-logs-dataset |
    where severityText = 'ERROR' and `resource.attributes.service.name` = 'payment-service'
```

```
source = my-logs-dataset
| where `resource.attributes.service.name` = 'frontend-proxy'
| where `attributes.url.path` in ("/api/cart","/api/checkout")
```

### Managing queries
<a name="observability-logs-manage-queries"></a>

You can save frequently used queries for reuse.
+ **Recent queries**: Select **Recent queries** to view and rerun previously executed queries.
+ **Saved queries**: Select **Saved queries** to access queries you have saved. To save the current query, select **Saved queries** > **Save query**.

### Running and stopping queries
<a name="observability-logs-run-stop-queries"></a>

Select **Refresh** to run the query. The button reads **Update** when you've changed the query or time range since the last run.

While a query runs, the button changes to **Stop**. Select **Stop** to cancel the query. **Stop** stays available until every query in the run has finished, including the query behind the **Visualization** tab, which can run longer than the logs query. To run an edited query while another query is running, select **Stop** and then run the new query.

The same **Refresh**/**Stop** button appears on the **Traces** and **Metrics** pages and in the visualization editor.

### Time range and index pruning
<a name="observability-logs-index-pruning"></a>

Discover sends the time range you pick alongside the PPL query. OpenSearch uses it to skip indexes that can't contain data in that range, so a query over an index pattern that spans months of rollover indexes reads only the indexes it needs. The rows returned are the same either way, because the time filter in the query still does the filtering.

Skipping indexes narrows the merged field mapping, so a field that exists only in skipped indexes isn't available to the query. If a saved query depends on such a field, turn off the **Send the picked time range so the cluster can prune indices** advanced setting (`query:enhancements:indexPruning`, on by default).

## Building queries with the PPL Query Builder
<a name="observability-logs-query-builder"></a>

The **PPL Query Builder** gives you a visual editing surface for PPL on the Logs page. You pick fields and values from menus, and the builder compiles the PPL. It covers a subset of PPL: search, filter, aggregate, and sort. For anything outside that subset, switch to **Code** mode and write the PPL by hand.

The following image shows the builder with a **Where** filter on `severityText`, a **Count** aggregation, and a **Group by** of every 1h. The aggregations menu is open and lists Count, Sum, Average, Min, Max, and Percentile.

![PPL Query Builder with a Where filter on severityText, a Count aggregation, and a Group by of every 1h.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/obs-stack/ppl-ppl-query-builder.png)

### Builder mode and Code mode
<a name="observability-logs-builder-modes"></a>

You edit a logs query in one of two modes. The **Code** / **Builder** toggle at the upper right of the query panel switches between them.

| Mode | Description |
| --- | --- |
| Builder | The visual surface: a search box plus Where, Aggregations, Group by, and Sort by controls. |
| Code | The raw PPL editor, with syntax highlighting and autocomplete. Handles anything the builder cannot represent. |

The Logs page opens in Code mode, including when you load a saved search. To use the builder, choose **Builder**.

#### Switching between modes
<a name="observability-logs-builder-switch-modes"></a>

A query you build in Builder mode moves freely between the two modes. Switch **Builder → Code** and the editor opens with the PPL the builder generated, so you can build a query by clicking and then read the PPL behind it. Switch back and your builder controls return as they were.

When you write or edit PPL in Code mode, the page stays in Code mode. You can switch to **Builder** when the builder can represent the query, and the builder then shows the query as controls. When the builder can't represent the query, **Builder** greys out, and its tooltip reads *"This query cannot be represented in Builder mode. Simplify it or use Code mode."*

To make **Builder** available again, simplify the query or clear the query bar.

### Searching
<a name="observability-logs-builder-search"></a>

The **Search for** box at the top of the builder edits the PPL `search` expression. A dedicated search-expression grammar drives its autocomplete, so it offers what parses at your cursor:
+ **Field names** from the current dataset. Accepting one inserts `field=` and re-opens the suggestion list.
+ **Live field values** for the field you named, pulled from the index.
+ **Operators** `=`, `!=`, `>`, `>=`, `<`, `<=`.
+ **Keywords** `AND`, `OR`, `NOT`, and `IN`.

Two conditions side by side with no operator between them combine with `AND`. Precedence follows PPL: parentheses bind tightest, then `NOT`, then `OR`, then `AND`. This differs from SQL.

### Filtering with Where
<a name="observability-logs-builder-where"></a>

The **Where** row holds filter chips, and each chip compiles to one `where` command. Select **Where** to add a chip, then pick a field, an operator, and one or more values. The value menu lists live values from the index, so you filter on values you can see.

The field's mapped type determines which operators you get:

| Operator | Applies to | Compiles to |
| --- | --- | --- |
| is | any field | `field` = value |
| is not | any field | `field` \!= value |
| is one of | string, number, date, ip, geo | `field` = a OR `field` = b |
| is not one of | string, number, date, ip, geo | `field` \!= a AND `field` \!= b |
| is between | number, date, ip | `field` >= from AND `field` < to |
| is not between | number, date, ip | `field` < from OR `field` >= to |
| exists | any field | ISNOTNULL(`field`) |
| does not exist | any field | ISNULL(`field`) |

Ranges are half-open: `from` is inclusive, `to` is exclusive. Fill in one side and the chip emits that single comparison.

Hover a chip to see the predicate it emits. A chip with a field but no value yet contributes nothing to the query and shows *"Finish this condition"*.

### Aggregating
<a name="observability-logs-builder-aggregate"></a>

Select **Aggregation** to add a metric, then **Group by** to bucket it. Together they compile to a single `stats` command.

Metrics cover `count`, `sum`, `avg`, `min`, `max`, `median`, `percentile`, `distinct_count`, and the standard deviation and variance pairs. Each one that takes a field also offers a **Wrap in function** menu of math, string, and date functions to apply before aggregating.

Group by one or more fields, and add **Over time** for a `span()` time bucket on the dataset's time field. The builder sizes that interval to your current time range, and you can override it.

### Sorting
<a name="observability-logs-builder-sort"></a>

The **Sort** control adds a single `sort` command with a **Desc** or **Asc** direction. On a plain query you sort on any field; once the query aggregates, you sort on a column it emits, either a metric such as `count()` or one of the group-by fields.

### Running the query
<a name="observability-logs-builder-run"></a>

Select **Refresh**, or press `Cmd`/`Ctrl` \+ `Enter` from anywhere in the builder. While the query runs, you can cancel it with **Stop**. See [Running and stopping queries](#observability-logs-run-stop-queries).

Your edits do not run the query as you type. The builder holds the generated query as a draft until you run it, so the results table and histogram keep showing the last query you ran.

### Worked example
<a name="observability-logs-builder-example"></a>

This builder configuration:
+ **Search for**: ``resource.attributes.service.name`=frontend-proxy`
+ **Where**: `attributes.http.response.status_code` **is between** `500` and `600`
+ **Aggregations**: `Count`
+ **Group by**: `attributes.url.path`, over time every `1m`
+ **Sort by**: `count()`, `Desc`

generates:

```sql
`resource.attributes.service.name`=frontend-proxy
| WHERE `attributes.http.response.status_code` >= 500 AND `attributes.http.response.status_code` < 600
| stats count() by `attributes.url.path`, span(time, 1m)
| sort -`count()`
```

The builder writes `WHERE` in uppercase and doesn't add a `source` command, because the query runs on the dataset that you selected. PPL keywords are not case sensitive.

Because the query aggregates, the Logs page switches to the **Visualization** tab to chart the result.

## Creating visualizations from logs
<a name="observability-logs-visualizations"></a>

You can create visualizations directly from your PPL query results. Use the `stats` command to aggregate data for visualization:

```
source = my-logs-dataset |
    stats count() as error_count by `resource.attributes.service.name`, span(time, 1h)
```

After you run a `stats` query, the **Logs** page automatically switches to the **Visualization** tab to display the results as a chart.

The `stats` command aggregates data based on specified fields. For example, to count logs per minute grouped by URL path, use the following query:

```sql
source = my-logs-dataset
| where `resource.attributes.service.name` = 'frontend-proxy'
| where `attributes.url.path` in ("/api/cart","/api/checkout")
| stats count() by span(time, 1m), `attributes.url.path`
```

![Bar chart showing count of requests over time for two URL paths, /api/cart and /api/checkout.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/discover-logs/discover-logs-visualization.png)

### Visualization types
<a name="observability-logs-viz-types"></a>

To change the visualization type, go to **Settings** > **Visualization type** and select one of the available options.

The following table describes the visualization types that you can use.

| Type | Description |
| --- | --- |
| Line | Displays data points connected by lines, useful for showing trends over time. |
| Area | Similar to a line chart with the area under the line filled in, useful for showing volume over time. |
| Bar | Displays data as vertical or horizontal bars, useful for comparing values across categories. |
| Metric | Displays a single numeric value, useful for showing key performance indicators. |
| State timeline | Displays state changes over time as colored bands, useful for monitoring status transitions. |
| Heatmap | Displays data as a matrix of colored cells, useful for showing density and patterns. |
| Bar gauge | Displays a single value as a filled bar within a range, useful for showing progress toward a threshold. |
| Pie | Displays data as proportional slices of a circle, useful for showing composition. |
| Scatter | Displays individual data points on two axes, useful for showing how two numeric fields relate. |
| Table | Displays results as rows and columns, useful for detailed breakdowns. |
| Gauge | Displays a single value on a dial within a range, useful for showing how close a value is to a limit. |
| Histogram | Displays the distribution of a numeric field as bars, useful for showing how values are spread. |
| Sankey | Displays flows between two dimensions, useful for showing how volume moves from one category to another. |

![Area chart showing request counts over time for /api/cart and /api/checkout endpoints from 02:00 to 02:12.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/discover-logs/discover-logs-viz-types.png)

### Visualization settings
<a name="observability-logs-viz-settings"></a>

When the **Visualization** tab is active, a settings panel appears on the right side of the screen. Use this panel to configure the chart type, map fields to axes, and customize visual styles such as colors and legends.

To switch the axes of a visualization, use the **Fields** section of the settings panel.

![](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/discover-logs/discover-logs-switch-axes.png)

You can update the following options:
+ **Fields**: Configure the fields to display on the **X-Axis**, **Y-Axis**, and **Color** (for grouping data series by different values). For bar charts, you can switch the X and Y axes in the Fields section to change the chart orientation from vertical to horizontal.
+ **Bar/Bucket**: For bar charts, configure bar size (**Auto** or **Manual**) and bucket settings (**Type** and **Interval**).
+ **Thresholds**: Define value thresholds using custom colors.

  A threshold is a boundary value. When a data point reaches or exceeds it, the color changes, so you can see whether values are in the range that you treat as normal, warning, or critical. Each threshold has a color and a value. The base threshold sets the color for values below all other thresholds. On line and area charts, thresholds appear as horizontal reference lines.
+ **Axes**: Configure axes labels, scales, and formatting.
+ **Legend**: Control legend visibility and position.

## Adding visualizations to dashboards
<a name="observability-logs-add-to-dashboard"></a>

After you create a visualization, you can add it to a dashboard for ongoing monitoring. The visualization is saved with its underlying PPL query so that it refreshes automatically when you open the dashboard.

1. After creating a visualization, select **Add to dashboard** in the results area.

1. In the **Save and Add to Dashboard** dialog, choose one of the following options:
   + **Save to existing dashboard**: Select an existing dashboard from the dropdown.
   + **Save to new dashboard**: Enter a name for the new dashboard.

1. Enter a name for the saved search in the **Save search** field.

1. Select **Add** to save the visualization to the dashboard.
