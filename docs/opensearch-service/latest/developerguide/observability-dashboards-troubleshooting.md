---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-dashboards-troubleshooting.html
---

# Troubleshooting dashboards

This section describes common dashboard issues and how to resolve them.

## No data in a panel
<a name="observability-dashboards-troubleshooting-no-data"></a>

If a panel displays no data, check the following common causes.

| Cause | Check | Fix |
| --- | --- | --- |
| Time range too narrow | Verify that the dashboard time range covers the period when data was ingested. | Expand the time range or select Last 24 hours. |
| Active filter excluding data | Review the filter bar for filters that might exclude all matching documents. | Remove or adjust the filter, then verify that data appears. |
| Incorrect index pattern | Confirm that the panel data source points to an index that contains data. | Update the data source to the correct index pattern in the panel editor. |
| Query syntax error | Look for error messages in the panel header or query editor. | Correct the PPL or PromQL syntax and re-run the query. |

## Wrong data in a panel
<a name="observability-dashboards-troubleshooting-wrong-data"></a>

If a panel displays unexpected results, try the following steps.
+ Verify that the query returns the expected fields by running it in Discover first.
+ Check that the visualization type matches the data shape (for example, use a line chart for time-series data).
+ Confirm that the correct data source is selected in the panel editor.

## Stale data
<a name="observability-dashboards-troubleshooting-stale-data"></a>

If dashboard panels display outdated information, try the following steps.
+ Choose the refresh icon in the toolbar to manually refresh all panels.
+ Verify that auto-refresh is enabled and set to an appropriate interval.
+ Confirm that your ingestion pipeline is actively sending data to the configured indexes.

## Performance issues
<a name="observability-dashboards-troubleshooting-performance"></a>

The following tips can help you resolve common performance issues.
+ **Slow dashboard** – Reduce the number of panels or narrow the time range. Dashboards with many panels run multiple queries simultaneously, which can increase load times.
+ **Slow panel** – Simplify the panel query. Avoid using wildcard patterns in PPL `where` clauses and limit the number of aggregation buckets.
+ **Browser lag** – Reduce the data density in visualizations. For example, increase the time span interval in `stats` commands to produce fewer data points.

## Filter issues
<a name="observability-dashboards-troubleshooting-filters"></a>

If filters do not behave as expected, try the following steps.
+ Verify that the field name in the filter matches the field name in the index mapping.
+ Check whether a pinned filter from another dashboard is affecting results.
+ Remove all filters and add them back one at a time to isolate the issue.

## Inspect a panel
<a name="observability-dashboards-troubleshooting-inspect"></a>

The panel inspector helps you debug data and query issues. To open the inspector, choose the panel menu (three dots) and select **Inspect**. The inspector provides the following views.
+ **Data** – Displays the raw data returned by the query in tabular format.
+ **Requests** – Shows the requests that the panel sent to the data source. For each request, this view shows the following:
  + **Statistics** – Shows statistics about the request.
  + **Request** – Shows the query sent to the data source, including the full PPL or PromQL statement.
  + **Response** – Shows the raw response from the data source, including timing and status information.

## Browser developer tools
<a name="observability-dashboards-troubleshooting-browser"></a>

For advanced troubleshooting, use your browser developer tools to inspect network requests. Open the **Network** tab, filter for API calls, and look for failed requests or slow responses. Check the response body for error messages that can help you identify the root cause.
