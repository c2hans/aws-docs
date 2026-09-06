---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-best-practices-redshift/best-practices-tables.html
---

# Best practices for designing Amazon Redshift tables
<a name="best-practices-tables"></a>

This section provides an overview of best practices for designing database tables. We recommend that you follow these best practices to achieve optimal query performance and efficiency.

## Understand how sort keys work
<a name="sort-keys"></a>

Amazon Redshift stores your data on disk in sorted order according to the sort key. The Amazon Redshift query optimizer uses sort order when it determines optimal query plans. To use sort keys effectively, we recommend that you do the following:
+ Keep the table sorted as much as possible.
+ Use `VACUUM` sort to restore optimal performance.
+ Avoid compressing the sort key column.
+ If the sort key is compressed and if the `sortkey1_skew` ratio is significantly high, then recreate the table without enabling compression on the sort key.
+ Avoid applying a function to the sort key columns. For example, in the following query, the `trans_dt : TIMESTAMPTZ` sort key column isn't used if you cast it to `DATE`:

  ```
  select order_id, order_amt
  from sales
  where trans_dt::date = '2021-01-08'::date
  ```
+ Perform `INSERT` operations in sort key order.
+ Use sort keys in the `GROUP BY` clause when possible.

### Query tuning tips
<a name="query-tuning-tips.002031f0-df13-5525-bfb6-918f88e3b9bd"></a>

We recommend that you do the following to tune your queries:
+ Always order compound sort keys from lowest-cardinality to highest-cardinality for optimal effectiveness.
+ If the leading key in a compound sort key is relatively unique (that is, it has high cardinality), then avoid adding additional columns to your sort key. Adding additional columns has little impact on query performance but does add maintenance costs.

## Evaluate sort key effectiveness
<a name="sort-key-effectiveness"></a>

To optimize your queries, you must be able to evaluate the effectiveness of your queries. We recommend that you use the [SVL\_QUERY\_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_SUMMARY.html) view to find general information about the execution of a query. In this view, you can use the attribute `IS_RRSCAN` to determine if an `EXPLAIN` plan step uses a range-restricted scan. You can also use the attribute `rows_pre_filter` to determine the selectivity the of a sort key.

You can also use an admin view from GitHub called [v\_my\_last\_query\_summary](https://github.com/awslabs/amazon-redshift-utils/blob/master/src/AdminViews/v_my_last_query_summary.sql). The view displays information for the last query that ran.

The following statement shows how to find general information about the execution of a query.

```
select lpad(' ',stm+seg+step) || label as label,
       rows,
       bytes,
       is_diskbased,
       is_rrscan,
       rows_pre_filter
from svl_query_summary
where query = pg_last_query_id()
order by stm, seg, step;
```

The preceding query returns the following sample output.

![Sample output of the previous query.](http://docs.aws.amazon.com/prescriptive-guidance/latest/query-best-practices-redshift/images/guide-img/0ed1f977-d92c-4ac8-bf6e-781c9fd51a62/images/ab652299-58f5-4100-94fb-47a0d69d3cf0.png)

## Know your table
<a name="know-table"></a>

It's important to understand the critical properties of your table. To learn more about your table, do the following:
+ Use [PG\_TABLE\_DEF](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_TABLE_DEF.html) to view information about table columns.
+ Use [SVV\_TABLE\_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html) to view more comprehensive information about a table, including data distribution skew, key distribution skew, table size, and statistics.

## Choose the right table distribution style
<a name="distribution-style"></a>

When you run a query, the query optimizer redistributes the rows to the compute nodes as needed to perform any joins and aggregations. The goal in selecting a table distribution style is to minimize the impact of the redistribution step by locating the data where it needs to be before you run the query.

We recommend the following approach to choosing the right table distribution style:
+ Avoid broadcasting and redistribution in a query execution plan by collocating the rows within the same node. For example, by selecting a `DISTKEY`, you can distribute the fact table and one-dimension table on their common columns. Choose the largest dimension based on the size of the filtered dataset. Only the rows that are used in the join must be distributed, so consider the size of the dataset after filtering, not the size of the table.
+ Make sure there is no skewness on the column where the distribution key is created. Otherwise, one compute node could perform more heavy lifting than others. If you notice skewness, then consider changing the distribution key column. A column can be considered as a candidate for a distribution key if its values are uniformly distributed or high cardinal values.
+ If the table used in the join condition is small (less than 1 GB), then consider the distribution style `ALL`.
+ You can compress the distribution key, but you must avoid compressing the sort key column (especially the first column of the sort key).

|
|
| Note: If you use automatic table optimization, you don't need to choose the distribution style of your table. For more information, see [Working with automatic table optimization](https://docs.aws.amazon.com/redshift/latest/dg/t_Creating_tables.html) in the Amazon Redshift documentation. To have Amazon Redshift choose the appropriate distribution style, specify `AUTO` for the distribution style. |
| --- |
