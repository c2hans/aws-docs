---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hyperscale-aurora-mysql/query-tuning-guidance.html
---

# Guidance for query tuning
<a name="query-tuning-guidance"></a>

After you identify problematic queries in your workload, each query should be tuned. Use the following guidelines on tuning to help your workload to run more efficiently.

## Minimize the number of rows scanned
<a name="rows-scanned"></a>

Basic as it seems, this is a great piece of advice to use when you tune queries. Use the EXPLAIN statement, and review the rows column to see how many rows the optimizer scans at each join. Try to reduce the number of rows scanned by creating an optimal index, and then re-explain your query to confirm your work. For more information, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html).

If you use partitioned tables, always query them with the WHERE clause that enables partition pruning so that the optimizer doesn't have to scan each partition. If your WHERE clause contains a constant for the partitioned column, the optimizer knows which partition to look for, and this makes your query more efficient.

Another facet to this advice is the design of your database. The fewer tables in your query, the faster your query will be. If you can denormalize your database design, you can get the optimizer to scan fewer rows, resulting in faster query performance.

## Minimize temporary table usage and temporary tables on disk
<a name="temporary-tables"></a>

The Aurora MySQL-Compatible optimizer creates temporary tables both on RAM and on disk if it cannot get the desired results of your query directly from indexes. Consequently, a large part of tuning is to have the right indexes that serve your workload. However, there might be queries in your workload that cannot rely only on indexes, so some operations might be performed in a temporary file. This is fine as long as you keep these to a minimum, and you ensure that very few tables are created on disk. MySQL creates disk tables when the size of the temporary table is too large to be housed in memory. The logic that MySQL uses to check the size of the internal temporary table is the smaller of the two variable values tmp\_table\_size and max-heap-table-size. You can tune these variables to an optimal value based on your workload so that in cases where you can't prevent temporary tables, you push them to disk only on rare occasions.

## Avoid file sorts
<a name="avoid-file-sorts"></a>

If your workload has a lot of `ORDER BY` queries, the best way to solve them is to use the right indexes on your tables. Ensure your multicolumn indexes are designed well to avoid sorting in files. Sorting can't happen on a column if the preceding columns are not scanned with constants (`in`, `>`, `<`, `!=`, and `BETWEEN` will not allow sorting on the next column to the right). The optimal way to sort in MySQL is to place a multicolumn index that positions columns that contain constant values supplied in the query to the left of the sorting column in a contiguous structure. If in the last resort, your query is unable to return results without a file sort, move the sorting to the application.

## Avoid running aggregation queries at high concurrency
<a name="avoid-aggregation"></a>

Your workload might have a small number of aggregation queries to cater to some functionality within your application. This use case calls for a lot of caution. The InnoDB engine is geared for proper online transaction processing (OLTP) loads, but even a few group-by queries on high concurrency can be very heavy on the CPU and can rapidly degrade the performance of your cluster. To solve use cases where you require aggregated result sets, pre-aggregate the data in ready to read tables so that you can avoid group by queries altogether.

## Test your queries for concurrency
<a name="concurrency"></a>

When tuning individual queries, remember that these queries run concurrently on several vCPUs in Aurora MySQL-Compatible. Your query might run in a few milliseconds in your test environment on single runs. But this is not the whole picture. Be sure to test your query with the expected level of concurrency on your production cluster and benchmark its performance. Release the query to production only when it meets your concurrency goals. Ensure that you use the optimizer `hint sql_no_cache` in your test scripts so that you avoid fetching results from the cache. You can use tools such as mysqlslap to perform the test at concurrency and benchmark the results.
