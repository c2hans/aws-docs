---
source_url: https://docs.aws.amazon.com/athena/latest/ug/updates-removing-columns.html
---

# Remove columns
<a name="updates-removing-columns"></a>

You may need to remove columns from tables if they no longer contain data, or to restrict access to the data in them.
+ You can remove columns from tables in JSON, Avro, and in Parquet and ORC if they are read by name. For information, see [Understand index access for Apache ORC and Apache Parquet](handling-schema-updates-chapter.md#index-access).
+ We do not recommend removing columns from tables in CSV and TSV if you want to retain the tables you have already created in Athena. Removing a column breaks the schema and requires that you recreate the table without the removed column.

In this example, remove a column ``totalprice`` from a table in Parquet and run a query. In Athena, Parquet is read by name by default, this is why we omit the SERDEPROPERTIES configuration that specifies reading by name. Notice that the following query succeeds, even though you changed the schema:

```
CREATE EXTERNAL TABLE orders_parquet_column_removed (
   `o_orderkey` int,
   `o_custkey` int,
   `o_orderstatus` string,
   `o_orderdate` string,
   `o_orderpriority` string,
   `o_clerk` string,
   `o_shippriority` int,
   `o_comment` string
)
STORED AS PARQUET
LOCATION 's3://amzn-s3-demo-bucket/orders_parquet/';
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
