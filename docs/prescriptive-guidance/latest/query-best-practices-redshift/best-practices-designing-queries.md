---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-best-practices-redshift/best-practices-designing-queries.html
---

# Best practices for designing Amazon Redshift queries
<a name="best-practices-designing-queries"></a>

This section provides an overview of best practices for designing queries. We recommend that you follow the best practices in this section to achieve optimal query performance and efficiency.

## Avoid using the SELECT \* FROM statement
<a name="select-from-statement"></a>

We recommend that you avoid using the `SELECT * FROM` statement. Instead, always list out columns for analysis. This reduces query execution time and scans costs for Amazon Redshift Spectrum queries.

**Example of what to avoid**

```
select *
from sales;
```

**Best practice example**

```
select sales_date, sales_amt
from sales;
```

## Identify query issues
<a name="query-issues"></a>

We recommend that you check the [STL\_ALERT\_EVENT\_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_ALERT_EVENT_LOG.html) view to identify and correct possible issues with your query.

## Get summary information on your query
<a name="summary-info"></a>

We recommend that you use the [SVL\_QUERY\_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_SUMMARY.html) and [SVL\_QUERY\_REPORT](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_REPORT.html) views to get summary information on your queries. You can use this information to optimize your queries.

## Avoid cross-joins
<a name="cross-joins"></a>

We recommend that you avoid using cross-joins unless absolutely necessary. Without a join condition, cross-joins result in the Cartesian product of two tables. Cross-joins are typically run as nested-loop joins (the slowest of the possible join types).

**Example of what to avoid**

```
select c.c_name,
          n.n_name
from tpch.customer c,
        tpch.nation n;
```

**Best practice example**

```
select c.c_name,
           n.n_name
from tpch.customer c,
join tpch.nation n
  on n.n_nationkey = c.c_nationkey;
```

## Avoid functions in query predicates
<a name="functions-query-predicates"></a>

We recommend that you avoid using functions in query predicates. Using functions in query predicates can negatively impact performance because functions typically add extra processing overhead to each row and slow down the overall execution of the query.

**Example of what to avoid**

```
select sum(o_totalprice)
from tpch.orders
where datepart(year, o_orderdate) = 1992;
```

**Best practice example**

```
select sum(o_totalprice)
from tpch.orders
where o_orderdate between '1992-01-01' and '1992-12-31';
```

## Avoid unnecessary cast conversions
<a name="cast-conversions"></a>

We recommend that you avoid using unnecessary cast conversion on the queries because casting data types takes time and resources and slows down query execution.

**Example of what to avoid**

```
select sum(o_totalprice)
from tpch.orders
where o_ordertime::date = '1992-01-01';
```

**Best practice example**

```
select sum(o_totalprice)
from tpch.orders
where o_ordertime between '1992-01-01 00:00:00' and '1992-12-31 23:59:59';
```

## Use CASE expressions for complex aggregations
<a name="case-expressions"></a>

We recommend that you use a [CASE expression](https://docs.aws.amazon.com/redshift/latest/dg/r_CASE_function.html) to perform complex aggregations instead of selecting from the same table multiple times.

**Example of what to avoid**

```
select sum(sales_amt) as us_sales
from sales
where country = 'US';

select sum(sales_amt) as ca_sales
from sales
where country = 'CA';
```

**Best practice example**

```
select sum(case when country = 'US' then sales_amt end) as us_sales,
           sum(case when country = 'CA' then sales_amt end) as ca_sales
from sales;
```

## Use subqueries
<a name="subqueries"></a>

We recommend that you use subqueries in cases where one table in the query is used only for predicate conditions and the subquery returns a small number of rows (less than about 200).

**Example of what to avoid**

If a subquery returns less than 200 rows:

```
select sum(order_amt) as total_sales
from sales
where region_key IN
        (select region_key
         from regions
         where state = 'CA');
```

**Best practice example**

If a subquery returns greater than or equal to 200 rows:

```
select sum(o.order_amt) as total_sales
from sales o
join regions r
  on r.region_key = o.region_key
  and r.state = 'CA';
```

## Use predicates
<a name="predicates"></a>

We recommend that you use predicates to restrict the dataset as much as possible. Predicates are used in SQL to filter and restrict the data that's returned in a query. By specifying conditions in a predicate, you can specify which rows must be included in the query results based on specified conditions. This allows you to retrieve only the data that you're interested in and improves the efficiency and accuracy of your queries. For more information, see [Conditions](https://docs.aws.amazon.com/redshift/latest/dg/r_conditions.html) in the Amazon Redshift documentation.

## Add predicates to filter tables with joins
<a name="filter-tables-joins"></a>

We recommend that you add predicates to filter tables that participate in joins, even if the predicates apply the same filters. Using predicates to filter tables with joins in SQL can improve query performance by reducing the amount of data that must be processed and reducing the size of the intermediate result set. By specifying the conditions for the join operation in the `WHERE` clause, the query execution engine can eliminate rows that don't match the conditions before they are joined. This results in a smaller result set and faster query execution.

**Example of what to avoid**

```
select p.product_name, sum(o.order_amt)
from sales o
join product p
   on r.product_key = o.product_key
where o.order_date > '2022-01-01';
```

**Best practice example**

```
select p.product_name, sum(o.order_amt)
from sales o
join product p
  on p.product_key = o.product_key
  and p.added_date > '2022-01-01'
where o.order_date > '2022-01-01';
```

## Use the least expensive operators for predicates
<a name="least-expensive-operators"></a>

In the predicate, use the least expensive operators that you can. [Comparison condition](https://docs.aws.amazon.com/redshift/latest/dg/r_comparison_condition.html) operators are preferable to [LIKE](https://docs.aws.amazon.com/redshift/latest/dg/r_patternmatching_condition_like.html) operators. `LIKE` operators are still preferable to [SIMILAR TO](https://docs.aws.amazon.com/redshift/latest/dg/pattern-matching-conditions-similar-to.html) or [POSIX](https://docs.aws.amazon.com/redshift/latest/dg/pattern-matching-conditions-posix.html) operators.

## Use sort keys in GROUP BY clauses
<a name="group-by-clauses"></a>

Use sort keys in the `GROUP BY` clause so that the query planner can use more efficient aggregation. A query might qualify for one-phase aggregation when its `GROUP BY` list contains only sort key columns, one of which is also the distribution key. The sort key columns in the `GROUP BY` list must include the first sort key, followed by other sort keys that you want to use in sort key order.

## Take advantage of materialized views
<a name="materialized-views"></a>

If possible, rewrite the query by replacing the complex code with a materialized view, which will significantly improve the performance of the query. For more information, see [Creating materialized views in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html) in the Amazon Redshift documentation.

## Be careful with columns in GROUP BY and ORDER BY clauses
<a name="group-by-order-by"></a>

If you use both `GROUP BY` and `ORDER BY` clauses, make sure that you put the columns in the same order in both `GROUP BY` and `ORDER BY` clauses. `GROUP BY` implicitly requires the data to be sorted. If your `ORDER BY` clause is different, then the data must be sorted twice.

**Example of what to avoid**

```
select a, b, c, sum(d)
from a_table
group by b, c, a
order by a, b, c
```

**Best practice example**

```
select a, b, c, sum(d)
from a_table
group by a, b, c
order by a, b, c
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
