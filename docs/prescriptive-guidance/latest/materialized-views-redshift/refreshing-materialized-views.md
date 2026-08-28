---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/refreshing-materialized-views.html
---

# Refreshing materialized views
<a name="refreshing-materialized-views"></a>

A materialized view contains a snapshot of the query result. Materialized views are not updated periodically, unless you configure Amazon Redshift to make periodic updates. To manually refresh and update the data in a materialized view, you can use the `REFRESH MATERIALIZED VIEW` statement at any time. This command identifies changes that take place in the base tables and applies those changes to the materialized view.

There are two ways to refresh a materialized view: a manual refresh and an automatic refresh (called [autorefreshing](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-refresh.html#materialized-view-auto-refresh)). The following example query shows how to manually refresh a materialized view:

```
REFRESH MATERIALIZED VIEW mv_total_orders;
```

To autorefresh a materialized view, add the `AUTO REFRESH YES` clause to the `CREATE MATERIALIZED VIEW` statement as the following example demonstrates:

```
CREATE MATERIALIZED VIEW mv_total_orders
AUTO REFRESH YES -- Add this clause to auto refresh the MV
AS
 SELECT c.cust_id,
        c.first_name,
        sum(o.amount) as total_amount
 FROM orders o
 JOIN customer c
    ON c.cust_id = o.customer_id
 GROUP BY c.cust_id,
          c.first_name;
```

Amazon Redshift autorefreshes materialized views as soon as possible after a base table changes. To minimize the impact of active workloads in your cluster when processing the refresh, Amazon Redshift considers the following factors:
+ Current system load
+ The resources required for a refresh
+ Available cluster resources
+ How often the materialized views are used

Amazon Redshift prioritizes your workloads over autorefresh and could stop autorefreshing to preserve the performance of the user workload. Keep in mind that this approach can delay the refreshes of some materialized views. For refresh status, you can check the [SVL\_MV\_REFRESH\_STATUS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_MV_REFRESH_STATUS.html) view. This view records queries that are user-initiated or autorefreshed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
