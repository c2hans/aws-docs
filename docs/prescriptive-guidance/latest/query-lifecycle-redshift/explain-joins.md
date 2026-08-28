---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/explain-joins.html
---

# EXPLAIN joins for Amazon Redshift query plans
<a name="explain-joins"></a>

Amazon Redshift uses different join operators to retrieve data based on the following:
+ The physical design of the tables that are being joined
+ The structure of the query
+ The location of the data required by the join
+ The specific requirements of the query itself

The following join types are commonly used in Amazon Redshift:
+ **Nested loop** – A nested loop occurs when a hash table can't be created between the two tables. Nested loops are used mainly for cross-joins (Cartesian products) and some inequality joins. This will require the database to check every value in the left table against every value in the right table. The complexity of a nested loop join is "quadratic" in that you must perform approximately N\*N (or N²) different operations to process the join. The nested loop is the least optimal join type.
+ **Hash join** – In a hash join, the join conditions aren't perfect for each other, but Amazon Redshift can manage using hash joins with a bit of work. A hash join is typically faster than a nested loop join. Amazon Redshift looks at both tables and between them creates a hash table, which is like a lookup table that sits in the middle of the tables. For example, hash join and hash operators are used when joining tables where the join columns are not both distribution keys and sort keys.
+ **Merge join** – A merge join is typically the fastest join and is used for inner joins and outer joins. In a merge join, both tables are perfect for each other. This means that the join condition on each side is the distribution key and the sort key. Both tables perfectly line up without any need for adjustment. Note that the unsorted rows in the tables should be less than 20 percent of the joining tables. To view the percent of unsorted rows, query the [SVV\_TABLE\_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html) system table. The merge join is not used for full joins.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
