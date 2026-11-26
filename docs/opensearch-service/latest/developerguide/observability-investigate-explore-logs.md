---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-investigate-explore-logs.html
---

# Explore Logs

**Explore logs** is a guided onboarding canvas for the **Logs** experience in an observability workspace of OpenSearch UI. You can use it to browse the log data in a data source before you write a query. A data source is an Amazon OpenSearch Service domain or an Amazon OpenSearch Serverless collection that is associated with the workspace.

For each index and dataset, the canvas shows a live severity histogram and a preview of the latest raw log lines. From the canvas, you can open an existing dataset to query it. You can also turn one or more indexes into a saved dataset.

Use **Explore logs** when you know that an index exists, but you don't yet have a dataset to query. For example, the index might be `otel-frontend` or `nginx-access-logs`. The canvas shows which logs you have, whether they are arriving now, and how to start. You don't need to write Piped Processing Language (PPL) or create a dataset first.

## Prerequisites
<a name="observability-explore-logs-prerequisites"></a>

Before you open **Explore logs**, make sure that you meet the following requirements:
+ You're in an observability workspace.
+ The workspace has at least one associated data source.

## Open Explore logs
<a name="observability-explore-logs-open"></a>

**Explore logs** is available alongside the **Logs** experience. You can open it from any of the following places:
+ **Discover Logs query bar** – On the Discover Logs page, choose **Explore logs** at the right side of the query bar.
+ **Discover Logs page with no dataset selected** – When you open the Discover Logs page without a dataset selected, the page offers **Explore logs** alongside **Create dataset**. Browsing your logs is the suggested first step.
+ ****Logs** navigation popover** – In the left navigation, pause on **Logs**, and then choose **Explore logs** in the popover.

The following image shows the Discover Logs query bar. The dataset selector, **Recent queries**, and **Saved queries** appear at the left, and the **Explore logs** action appears at the right.

![The Discover Logs query bar with the dataset selector, Recent queries, Saved queries, and the Explore logs action.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/obs-stack/explore-logs-entry-point.png)

## The Explore logs canvas
<a name="observability-explore-logs-canvas"></a>

The **Explore logs** canvas is a full-width vertical stack of cards. Each dataset and each index has one card.

A toolbar at the top of the canvas has the following controls:
+ **Data source picker** – Limits the card list to one data source. To see the indexes and datasets of a data source, select it.
+ **Search** – Filters both datasets and indexes by name as you enter text.
+ **Create dataset** – Turns the selected indexes into a dataset. The button shows a count, such as **Create dataset (2)**. The button is unavailable until you select at least one index. If an existing dataset already covers every selected index, the button reads **Query** instead and opens that dataset.
+ **Time range** – Sets the time window for the histogram and log preview on every card.

The canvas shows the cards in groups. The **Datasets** group comes first, and then the **Indexes** group, with the newest indexes first. The canvas loads the first set of cards. When more indexes are available, the canvas shows a **Load more** control.

## Read a card
<a name="observability-explore-logs-card"></a>

Each card previews one index or dataset. The following image shows a dataset card with its severity histogram, log-line preview, time field, and the **Query** and **Manage** actions.

![An Explore logs dataset card with a severity histogram, log-line preview, time field, and the Query and Manage actions.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/obs-stack/explore-logs-card-anatomy.png)

A card includes the following elements:
+ **Severity histogram** – A stacked bar chart of log volume over the selected time range, with one series for each severity level. Examples of severity levels are info, warn, error, debug, trace, and fatal. The chart legend names each severity level and shows its total in a human-readable form. Documents with no recognized severity field count as a single **logs** series.
+ **Log-line preview** – The latest raw log lines. Each line shows a timestamp, the name of the severity level, and the remaining fields.
+ **Time field** – The date field that the card uses for the histogram and for sorting. When an index has more than one date field, you can use this control to switch the field.
+ **Index health** (indexes only) – A status indicator that shows one of the following values: **Healthy** (all shards are allocated), **Degraded** (replica shards are unassigned), or **Unhealthy** (primary shards are unassigned). To see the store size and shard layout, pause on the indicator.
+ **Actions** – A dataset card has two actions. **Query** opens the dataset on the Discover Logs page, and **Manage** opens the dataset settings. When you choose the name of an index card, the workflow to create a dataset starts. If an existing dataset already covers the index, that dataset opens on the Discover Logs page instead.

Cards adapt to the state of the underlying data. The following table describes the card states.

| Card state | Description |
| --- | --- |
| Full | The index or dataset has documents in the selected time range. The card shows the full histogram and log preview. |
| No recent data | The index or dataset has documents, but none in the selected time range. These indexes collapse into a drawer at the end of the card list. The drawer label is {{N}} indexes with no recent data. To see these indexes, widen the time range. |
| No documents yet | The index has never received a document. You can't create a dataset over it. |
| No time field | The index has no date field. The card can't chart the index, and you can't turn the index into a logs dataset. |
| Couldn't load preview | The preview query failed. To try again, choose Retry. |

## Select the time range
<a name="observability-explore-logs-time-range"></a>

The time range defaults to the last 15 minutes. This default keeps the canvas from running heavy queries for every card when it loads. To widen or shift the time window, use the time range picker. You can also drag across a region of the histogram on any card. The canvas then uses that region as the time range for all cards.

## Create a dataset from indexes
<a name="observability-explore-logs-create-dataset"></a>

Turning indexes into a dataset is the core workflow of **Explore logs**.

**To create a dataset from indexes**

1. Select the checkbox on one or more index cards.

   A selection bar appears under the toolbar. It shows **{{N}} index selected**, a **New dataset** label, and the proposed dataset name. To reset the selection, choose **Clear all**.

1. Review the proposed dataset name in the selection bar.

   The selection bar proposes a wildcard dataset name that it derives from the selected indexes. For example, if you select `nginx-access-logs-2026.08.03`, the proposed name is `nginx-access-logs-*`. The dataset then covers the whole family of indexes rather than a single day.

1. Choose **Create dataset**.

   A short wizard opens on **Step 1: Select data source**. The wizard starts with the active data source, and the proposed wildcard is already in the **Selected** list.

1. (Optional) Add more indexes or wildcard patterns.

1. Choose **Next**.

1. Confirm the time field and the remaining settings.

1. To save the dataset, choose **Create Dataset**.

   The Discover Logs page opens with the new dataset ready to query.

**Note**
If the indexes that you select don't share a common date field, **Explore logs** shows a warning. A single dataset needs one time field across all of its indexes.

## Query an existing dataset
<a name="observability-explore-logs-query-dataset"></a>

Datasets that you already created appear first on the canvas. To open a dataset directly on the Discover Logs page, choose the name of its card or choose **Query**. For more information about how to query and visualize logs on that page, see [Discover Logs](observability-analyze-logs.md).

## Data requirements
<a name="observability-explore-logs-data-requirements"></a>

An index needs a date field to appear as a full card with a chart and to become a logs dataset. **Explore logs** looks for the following field names, in order. If none of them is present, it uses the first date field on the index.

`@timestamp`, `time`, `startTime`, `endTime`, `timestamp`, `observedTimestamp`

The severity breakdown in the histogram uses the first of the following fields that is present. The field names follow the OpenTelemetry log record convention.

`severityText`, `severity`, `level`, `log.level`, `severityNumber`

If none of these fields is present, the histogram still renders as a single **logs** series without a severity breakdown.

## Related topics
<a name="observability-explore-logs-related"></a>

For more information, see the following topics:
+ [Discover Logs](observability-analyze-logs.md) – Query and visualize logs with PPL.
+ [Datasets](observability-datasets.md) – Create and manage datasets.
