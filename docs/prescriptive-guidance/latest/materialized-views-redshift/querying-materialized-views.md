---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/querying-materialized-views.html
---

# Querying materialized views
<a name="querying-materialized-views"></a>

When you query a materialized view, you directly access the precomputed data in the materialized view. You can use a materialized view in any SQL query by referencing the materialized view name as the data source, as in a table or standard view.

For example, consider the `mv_total_orders` materialized view example illustration from the [Creating materialized views ](creating-materialized-views.md)section of this guide. If you want to build a query for `mv_total_orders` (which returns a list of customers who have orders totaling more than $500), then you could run the following standard query:

```
statement. SELECT c.cust_id,
       c.first_name,
       sum(o.amount) as total_amount
FROM orders o
JOIN customer c
  ON c.cust_id = o.customer_id
GROUP BY c.cust_id,
         c.first_name
HAVING sum(o.amount) > 500;
```

However, the preceding query isn't optimized for speed. We recommend that you run the following query instead:

```
SELECT cust_id,
       first_name,
       total_amount
FROM mv_total_orders
WHERE total_amount > 500;
```

The recommended query runs much faster because the query results are precomputed, and there's no need to access the underlying tables (customer and order). Amazon Redshift can return the results directly from `mv_total_orders`.

**Important**
When a query accesses a materialized view, the query sees only the data stored in the materialized view as of its most recent refresh. Therefore, the query might not see all the latest changes from the corresponding base tables of the materialized view.
