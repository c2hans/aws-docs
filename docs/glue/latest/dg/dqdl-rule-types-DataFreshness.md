---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-DataFreshness.html
---

# DataFreshness
<a name="dqdl-rule-types-DataFreshness"></a>

Checks the freshness of data in a column by evaluating the difference between the current time and the values of a date column. You can specify a time-based expression for this rule type to make sure that column values are up to date.

**Syntax**

```
DataFreshness {{<COL_NAME>}} {{<EXPRESSION>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Date
+ **EXPRESSION** – A numeric expression in hours or days. You must specify the time unit in your expression.

**Example: Data freshness**

The following example rules check for data freshness.

```
DataFreshness "Order_Date" <= 24 hours
DataFreshness "Order_Date" between 2 days and 5 days
```

**Null behavior**

 The `DataFreshness` rules will fail for rows with `NULL` values. If the rule fails due to a null value, the failure reason will display the following:

```
80.00 % of rows passed the threshold
```

 where 20% of the rows that failed include the rows with `NULL`.

 The following example compound rule provides a way to explicitly allow for `NULL` values:

```
(DataFreshness "Order_Date" <= 24 hours) OR (ColumnValues "Order_Date" = NULL)
```

**Data Freshness for Amazon S3 objects**

 Sometimes you will need to validate the freshness of data based on the Amazon S3 file creating time. To do this, you can use the following code to get the timestamp and add it to your dataframe, and then apply Data Freshness checks.

```
df = glueContext.create_data_frame.from_catalog(database = "default", table_name = "mytable")
df = df.withColumn("file_ts", df["_metadata.file_modification_time"])

Rules = [
 DataFreshness "file_ts" < 24 hours
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
