---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/advantages-materialized-views.html
---

# Advantages of materialized views
<a name="advantages-materialized-views"></a>

There are several advantages to using materialized views:
+ **Fewer updates** – A standard view isn't physically materialized, which means that the query that defines a standard view runs every time the view is referenced in a query. In contrast, a materialized view is precomputed and stored on disk (similar to an object) as a result of a query expression like regular views. Unlike standard views, materialized views are not updated each time they are used.
+ **Faster response times** – A materialized view responds faster in comparison to a view. This is because the materialized view is precomputed and therefore doesn't waste time resolving the query or joins in the query that create the materialized view.
+ **Stored SQL statement** – You can use a rollup, or aggregation, table instead of a materialized view. Rollup tables are precomputed and stored on disk (similar to materialized views), but they don't store their SQL statements in the database. Materialized views do store their SQL statements.
+ **Easy to refresh** – Materialized views are easy to refresh. Simply run the `REFRESH MATERIALIZED VIEW` command.
+ **Automatic query rewriting** – The query optimizer can rewrite your SQL statement to fetch data from an existing materialized view, even if the materialized view isn't explicitly used in your SQL statement.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
