---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/query-processing.html
---

# SQL query processing in Amazon Redshift
<a name="query-processing"></a>

Amazon Redshift routes a submitted SQL query through the parser and optimizer to develop a query plan. The execution engine then translates the query plan into code and sends that code to the compute nodes for execution. Before you design a query plan, it's critical to understand how query processing works.

## Query planning and execution workflow
<a name="query-planning-and-execution-workflow"></a>

The following diagram provides a high-level view of the query planning and execution workflow.

![Query planning and execution workflow between the client, leader node, and compute nodes.](http://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/images/guide-img/84453e49-6013-472a-b5b1-062248897e49/images/2766303e-53bb-4085-ba79-a0e2731b7a92.png)

The diagram shows the following workflow:

1. The leader node in the Amazon Redshift cluster receives the query and parses the SQL statement.

1. The parser produces an initial query tree that's a logical representation of the original query.

1. The query optimizer takes the initial query tree and evaluates it, analyzes table statistics to determine join order and predicate selectivity, and, if necessary, rewrites the query to maximize its efficiency. Sometimes a single query can be written as several dependent statements in the background.

1. The optimizer generates a query plan (or several, if the previous step resulted in multiple queries) for the execution with the best performance. The query plan specifies execution options such as execution order, network operations, join types, join order, aggregation options, and data distributions.

1. A query plan contains information on the individual operations required to run a query. You can use the `EXPLAIN` command to view the query plan. The query plan is a fundamental tool for analyzing and tuning complex queries.

1. The query optimizer sends the query plan to the execution engine. The execution engine checks the compiled plan cache for a query plan match and uses the compiled cache (if found). Otherwise, the execution engine translates the query plan into steps, segments, and streams:
   + *Steps* are individual operations that take place during query execution. Steps are identified by a label (for example, `scan`, `dist`, `hjoin`, or `merge`). A step is the smallest unit. You can combine steps so that compute nodes can perform a query, join, or another database operation.
   + A *segment* refers to a segment of a query and combines several steps that can be done by a single process. A segment is the smallest compilation unit executable by a compute node slice. A slice is the unit of parallel processing in Amazon Redshift.
   + A *stream* is a collection of segments to be parceled out over the available compute node slices. The segments in a stream run in parallel across node slices. Therefore, the same step from the same segment is also executed in parallel in multiple slices.

1. The code generator receives the translated plan and generates a C\+\+ function for each segment.

1. The generated C\+\+ function gets compiled by the GNU Compiler Collection and converted to an O (`.o`) file.

1. The compiled code (O file) runs. Compiled code runs faster than interpreted code and uses less compute capacity.

1. The compiled O file is then broadcasted to the compute nodes.

1. Each compute node consists of several compute slices. The compute slices run the query segments in parallel. Amazon Redshift takes advantage of optimized network communication, memory, and disk management to pass intermediate results from one query plan step to the next. This also helps to speed up query execution. Consider the following:
   + Steps 6, 7, 8, 9, 10, and 11 happen once for each stream.
   + The engine creates the executable segments for one stream and sends these segments to the compute nodes.
   + After the segments of a prior stream are completed, the engine generates the segments for the next stream. In this way, the engine can analyze what happened in the prior stream (for example, whether operations were disk-based) to influence the generation of segments in the next stream.

1. After the compute nodes are done, they return the query results to the leader node for final processing. The leader node merges the data into a single result set and addresses any required sorting or aggregation.

1. The leader node returns the results to the client.

The following diagram shows the execution workflow of streams, segments, steps, and compute node slices. Keep in mind the following:
+ Steps in a segment run sequentially.
+ Segments in a stream run in parallel.
+ Streams run sequentially.
+ Compute node slices run in parallel.

The following diagram shows a visual representation of streams, segments, and steps. Each segment contains multiple steps, and each stream contains multiple segments.

![Each stream contains multiple segments, which contain multiple steps.](http://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/images/guide-img/84453e49-6013-472a-b5b1-062248897e49/images/a0bac1f4-2b7e-4738-bbe9-8c64d9d4e08a.png)

The following diagram shows a visual representation of query executions and compute node slices. Each compute node contains multiple slices, streams, segments, and steps.

![Slices, streams, segments, and steps in each compute node.](http://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/images/guide-img/84453e49-6013-472a-b5b1-062248897e49/images/c18be91a-fe4e-4ba8-a82b-8c0c0b73bc81.png)

## Additional considerations
<a name="additional-considerations"></a>

We recommend that you consider the following in regard to query processing:
+ Cached compiled code is shared across sessions on the same cluster, so subsequent executions of the same query will be faster, often even with different parameters.
+ When you benchmark your queries, we recommend that you always compare the times for the second execution of a query, because the first execution time includes the overhead of compiling the code. For more information, see [Query performance factors](https://docs.aws.amazon.com/prescriptive-guidance/latest/query-best-practices-redshift/query-performance-factors.html) in the *Query best practices for Amazon Redshift* guide.
+ The compute nodes could return some data to the leader node during query execution if necessary. For example, if you have a subquery with a `LIMIT` clause, the limit is applied on the leader node before data is redistributed across the cluster for further processing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
