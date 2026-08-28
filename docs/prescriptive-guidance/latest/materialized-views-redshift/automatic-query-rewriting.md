---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/automatic-query-rewriting.html
---

# Automatic query rewriting
<a name="automatic-query-rewriting"></a>

Amazon Redshift can automatically rewrite SQL queries that don't explicitly reference existing materialized views that are used for performance improvements. Directly querying a materialized view reduces the query processing time, but the query statement must be modified. If you use materialized views to accelerate queries, it's important to consider how to systematically and automatically use materialized views to respond to queries. You can use transparent rewriting to add or delete materialized views in the same way as an index, without affecting existing SQL statements. Amazon Redshift uses only up-to-date materialized views when it automatically rewrites queries.

## How query rewriting works
<a name="query-rewriting-works"></a>

Consider the following SQL query. The query joins two tables: customer (10\+ million rows) and order (10\+ billion rows):

```
SELECT c.cust_id,
       c.first_name,
       sum(o.amount) as total_amount
FROM orders o
JOIN customer c
  ON c.cust_id = o.customer_id
GROUP BY c.cust_id,
         c.first_name
HAVING sum(o.amount) > 500;
```

This query joins two large tables, applies a sum aggregation on the `o.amount` column, and then filters the results to display only the customers who ordered more than $500. This query could consume a lot of resources.

As an example, consider the `mv_total_orders` materialized view from the [Creating materialized views](creating-materialized-views.md) section of this guide. After this view is created, then Amazon Redshift automatically rewrites the preceding query as follows:

```
SELECT cust_id,
       first_name,
       total_amount
FROM mv_total_orders
WHERE total_amount > 500;
```

This new query runs much faster because it uses a materialized view instead of joining two large tables.

Query rewriting has led to the wider adoption of materialized views for the following reasons:

1. Materialized views support the transparent rewriting of queries. The query rewrite transforms a SQL statement expressed in terms of tables into a statement accessing one or more materialized views. This transformation is transparent to the end user, requiring no intervention and no reference to the materialized view in the SQL statement.

1. Materialized views simplify the application of cached common result sets and support cross-query optimizations such as precomputing.

1. In data warehouses and data integration scenarios, materialized views can materialize foreign table results to hide the differences among multiple data sources, implementing local replicas or read/write splitting.

1. The query rewriting feature combined with automatic materialized view creation accelerates database autonomy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
