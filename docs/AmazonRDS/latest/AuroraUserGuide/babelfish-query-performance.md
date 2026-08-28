---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-query-performance.html
---

# Improving Babelfish query performance
<a name="babelfish-query-performance"></a>

 You can achieve faster query processing in Babelfish using query hints and the PostgreSQL optimizer.

**Topics**
+ [Using explain plan to improve Babelfish query performance](working-with-babelfish-usage-notes-features.using.explain.md)
+ [Using T-SQL query hints to improve Babelfish query performance](babelfish-tsql-hints.md)

You can also improve the query performance using `sp_babelfish_volatility` procedure. For more information, see [sp\_babelfish\_volatility](sp_babelfish_volatility.md).

You can also improve the query performance using subquery transformation and subquery cache. For more information, see [Optimizing correlated subqueries in Aurora PostgreSQL](apg-correlated-subquery.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
