---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/example-queries.html
---

# Example queries
<a name="example-queries"></a>

The behavior of metric collection depends on the metric type. `counter` type metrics are flushed each time they are reported on and must be calculated across an entire time range for each container. For `histogram`, `timer`, and `meter` type metrics, the values are a snapshot of the container’s lifetime at that particular timestamp. Athena views can be created to simplify pulling these tables in order to get the most up-to-date metrics across all containers. For more information about the various metrics types, see the [Metrics project](https://metrics.dropwizard.io/4.2.0/manual/core.html).

## Create views
<a name="create-views"></a>

Create views for the various metrics types. Set up the following views for the `histogram`, `timer`, and `meter` tables. Replace the ` <table-name> ` variable for each table.

```
CREATE VIEW <table-name>_current_data AS
WITH timestamp_ranking AS (
SELECT
*,
RANK() OVER(PARTITION BY "container_id", "name" ORDER BY "timestamp" DESC) AS "timestamp_rank"
FROM "prebid-server-us-east-1-metricsetl-database"."<table-name>"
)
SELECT *
FROM timestamp_ranking
WHERE "timestamp_rank" = 1
```

## Queries
<a name="queries"></a>

 **Bid-Adapter metrics**

1. Total number of bids received:

   ```
   SELECT
   "name",
   SUM("count") AS "total_bids_received"
   FROM "prebid-server-us-east-1-metricsetl-database"."counter"
   WHERE "name" LIKE 'adapter.%.bids_received'
   GROUP BY "name"
   ```

1. Average bid price:

   ```
   WITH timestamp_ranking AS (
   SELECT
   *,
   RANK() OVER(PARTITION BY "container_id", "name" ORDER BY "timestamp" DESC) AS "timestamp_rank"
   FROM "prebid-server-us-east-1-metricsetl-database"."histogram"
   ), current_data AS (
   SELECT
   "name",
   "count",
   "mean"
   FROM timestamp_ranking
   WHERE
   "name" LIKE 'adapter.%.prices'
   AND "timestamp_rank" = 1
   ), total_count AS (
   SELECT
   "name",
   SUM("count") AS "total"
   FROM current_data
   GROUP BY "name"
   ), weighted_values AS (
   SELECT
   current_data."name",
   current_data."mean" * (CAST(current_data."count" AS double) /
             total_count."total" ) AS "weighted_value"
   FROM current_data
   LEFT JOIN total_count
   ON current_data."name" = total_count."name"
   )
   SELECT
   "name",
   SUM("weighted_value") AS "average_bid_price"
   FROM weighted_values
   GROUP BY "name"
   ```

1. Win rate:

   ```
   WITH total_impressions AS (
       SELECT SUM("count") AS "total_impressions"
       FROM "prebid-server-us-east-1-metricsetl-database"."counter"
       WHERE "name" IN ('imps_banner', 'imps_video', 'imps_audio', 'imps_native')
   ), adaptor_bids_received AS (
       SELECT
           "name",
           SUM("count") AS "total_bids_received"
       FROM "prebid-server-us-east-1-metricsetl-database"."counter"
       WHERE "name" LIKE 'adapter.%.bids_received'
       GROUP BY "name"
   )
   SELECT
       adaptor_bids_received."name",
       CAST(total_impressions."total_impressions" AS double) /
       CAST(adaptor_bids_received."total_bids_received" AS double) AS "win_rate"
   FROM adaptor_bids_received
             CROSS JOIN total_impressions
   ```

1. Bid rate:

   ```
   WITH request_per_adapter AS (
   SELECT
   SPLIT("name", '.')[2] AS "bid_adapter",
   SUM("count") AS "count"
   FROM "prebid-server-us-east-1-metricsetl-database"."counter"
   WHERE
   "name" LIKE 'adapter.%.requests.gotbids'
   OR "name" LIKE 'adapter.%.requests.nobid'
   OR "name" LIKE 'adapter.%.requests.badinput'
   OR "name" LIKE 'adapter.%.requests.badserverresponse'
   OR "name" LIKE 'adapter.%.requests.timeout'
   OR "name" LIKE 'adapter.%.requests.unknown_error'
   GROUP BY SPLIT("name", '.')[2]
   ), gotbid_per_request AS (
   SELECT
   SPLIT("name", '.')[2] AS "bid_adapter",
   SUM("count") AS "gotbid_requests"
   FROM "prebid-server-us-east-1-metricsetl-database"."counter"
   WHERE
   "name" LIKE 'adapter.%.requests.gotbids'
   GROUP BY SPLIT("name", '.')[2]
   )
   SELECT
   request_per_adapter."bid_adapter",
   CAST(gotbid_per_request."gotbid_requests" AS double) / CAST(request_per_adapter."count" AS double) AS "bid_rate"
   FROM request_per_adapter
   LEFT JOIN gotbid_per_request
   ON request_per_adapter."bid_adapter" = gotbid_per_request."bid_adapter"
   ```

1. Bid request responses:

   ```
   WITH request_per_adapter AS (
   SELECT
   SPLIT("name", '.')[2] AS "bid_adapter",
   SPLIT("name", '.')[4] AS "response",
   SUM("count") AS "count"
   FROM "prebid-server-us-east-1-metricsetl-database"."counter"
   WHERE
   "name" LIKE 'adapter.%.requests.gotbids'
   OR "name" LIKE 'adapter.%.requests.nobid'
   OR "name" LIKE 'adapter.%.requests.badinput'
   OR "name" LIKE 'adapter.%.requests.badserverresponse'
   OR "name" LIKE 'adapter.%.requests.timeout'
   OR "name" LIKE 'adapter.%.requests.unknown_error'
   GROUP BY SPLIT("name", '.')[2], SPLIT("name", '.')[4]
   )
   SELECT
   request_per_adapter."bid_adapter",
   "response",
   "count"
   FROM request_per_adapter
   ```

## General auction metrics
<a name="general-auction-metrics"></a>

1. Fill rate:

   ```
   WITH total_impressions AS (
   SELECT SUM("count") AS "total_impressions"
   FROM "prebid-server-us-east-1-metricsetl-database"."counter"
   WHERE "name" IN ('imps_banner', 'imps_video', 'imps_audio', 'imps_native')
   ), total_requests AS (
   SELECT SUM("count") AS "total_requests"
   FROM "prebid-server-us-east-1-metricsetl-database"."counter"
   WHERE "name" = 'imps_requested'
   )
   SELECT CAST(total_impressions."total_impressions" AS double) / CAST(total_requests."total_requests" AS double) AS "fill_rate"
   FROM total_requests
   CROSS JOIN total_impressions
   ```

1. Average request time:

   ```
   WITH timestamp_ranking AS (
   SELECT
   *,
   RANK() OVER(PARTITION BY "container_id", "name" ORDER BY "timestamp" DESC) AS "timestamp_rank"
   FROM "prebid-server-us-east-1-metricsetl-database"."timer"
   ), current_data AS (
   SELECT
   "name",
   "count",
   "mean"
   FROM timestamp_ranking
   WHERE
   "name" LIKE 'request_time'
   AND "timestamp_rank" = 1
   ), total_count AS (
   SELECT SUM("count") AS "total"
   FROM current_data
   ), weighted_values AS (
   SELECT current_data."mean" * (
   CAST(current_data."count" AS double)/ total_count."total") AS "weighted_value"
   FROM current_data
   CROSS JOIN total_count
   )
   SELECT SUM("weighted_value") AS "average_request_time"
   FROM weighted_values
   ```

1. Sum of all impression types:

   ```
   SELECT
   "name",
   SUM("count")
   FROM "prebid-server-us-east-1-metricsetl-database"."counter"
   WHERE "name" IN ('imps_banner', 'imps_video', 'imps_audio', 'imps_native')
   GROUP BY "name"
   ```
