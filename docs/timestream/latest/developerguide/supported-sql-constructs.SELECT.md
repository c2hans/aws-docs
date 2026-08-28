---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/supported-sql-constructs.SELECT.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# SELECT
<a name="supported-sql-constructs.SELECT"></a>

**SELECT** statements can be used to retrieve data from one or more tables. Timestream's query language supports the following syntax for **SELECT** statements:

```
[ WITH with_query [, ...] ]
            SELECT [ ALL | DISTINCT ] select_expr [, ...]
            [ function (expression) OVER (
            [ PARTITION BY partition_expr_list ]
            [ ORDER BY order_list ]
            [ frame_clause ] )
            [ FROM from_item [, ...] ]
            [ WHERE condition ]
            [ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
            [ HAVING condition]
            [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
            [ ORDER BY order_list ]
            [ LIMIT [ count | ALL ] ]
```

where
+ `function (expression)` is one of the supported [window functions](window-functions.md).
+ `partition_expr_list` is:

  ```
  expression | column_name [, expr_list ]
  ```
+ `order_list` is:

  ```
  expression | column_name [ ASC | DESC ]
  [ NULLS FIRST | NULLS LAST ]
  [, order_list ]
  ```
+ `frame_clause` is:

  ```
  ROWS | RANGE
  { UNBOUNDED PRECEDING | expression PRECEDING | CURRENT ROW } |
  {BETWEEN
  { UNBOUNDED PRECEDING | expression { PRECEDING | FOLLOWING } |
  CURRENT ROW}
  AND
  { UNBOUNDED FOLLOWING | expression { PRECEDING | FOLLOWING } |
  CURRENT ROW }}
  ```
+ `from_item` is one of:

  ```
  table_name [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
  from_item join_type from_item [ ON join_condition | USING ( join_column [, ...] ) ]
  ```
+ `join_type` is one of:

  ```
  [ INNER ] JOIN
  LEFT [ OUTER ] JOIN
  RIGHT [ OUTER ] JOIN
  FULL [ OUTER ] JOIN
  ```
+ `grouping_element` is one of:

  ```
  ()
  expression
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
