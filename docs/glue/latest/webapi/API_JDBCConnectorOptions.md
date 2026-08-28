---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JDBCConnectorOptions.html
---

# JDBCConnectorOptions
<a name="API_JDBCConnectorOptions"></a>

Additional connection options for the connector.

## Contents
<a name="API_JDBCConnectorOptions_Contents"></a>

 ** DataTypeMapping **   <a name="Glue-Type-JDBCConnectorOptions-DataTypeMapping"></a>
Custom data type mapping that builds a mapping from a JDBC data type to an AWS Glue data type. For example, the option `"dataTypeMapping":{"FLOAT":"STRING"}` maps data fields of JDBC type `FLOAT` into the Java `String` type by calling the `ResultSet.getString()` method of the driver, and uses it to build the AWS Glue record. The `ResultSet` object is implemented by each driver, so the behavior is specific to the driver you use. Refer to the documentation for your JDBC driver to understand how the driver performs the conversions.
Type: String to string map
Valid Keys: `ARRAY | BIGINT | BINARY | BIT | BLOB | BOOLEAN | CHAR | CLOB | DATALINK | DATE | DECIMAL | DISTINCT | DOUBLE | FLOAT | INTEGER | JAVA_OBJECT | LONGNVARCHAR | LONGVARBINARY | LONGVARCHAR | NCHAR | NCLOB | NULL | NUMERIC | NVARCHAR | OTHER | REAL | REF | REF_CURSOR | ROWID | SMALLINT | SQLXML | STRUCT | TIME | TIME_WITH_TIMEZONE | TIMESTAMP | TIMESTAMP_WITH_TIMEZONE | TINYINT | VARBINARY | VARCHAR`
Valid Values: `DATE | STRING | TIMESTAMP | INT | FLOAT | LONG | BIGDECIMAL | BYTE | SHORT | DOUBLE`
Required: No

 ** FilterPredicate **   <a name="Glue-Type-JDBCConnectorOptions-FilterPredicate"></a>
Extra condition clause to filter data from source. For example:
 `BillingCity='Mountain View'`
When using a query instead of a table name, you should validate that the query works with the specified `filterPredicate`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** JobBookmarkKeys **   <a name="Glue-Type-JDBCConnectorOptions-JobBookmarkKeys"></a>
The name of the job bookmark keys on which to sort.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** JobBookmarkKeysSortOrder **   <a name="Glue-Type-JDBCConnectorOptions-JobBookmarkKeysSortOrder"></a>
Specifies an ascending or descending sort order.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** LowerBound **   <a name="Glue-Type-JDBCConnectorOptions-LowerBound"></a>
The minimum value of `partitionColumn` that is used to decide partition stride.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** NumPartitions **   <a name="Glue-Type-JDBCConnectorOptions-NumPartitions"></a>
The number of partitions. This value, along with `lowerBound` (inclusive) and `upperBound` (exclusive), form partition strides for generated `WHERE` clause expressions that are used to split the `partitionColumn`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** PartitionColumn **   <a name="Glue-Type-JDBCConnectorOptions-PartitionColumn"></a>
The name of an integer column that is used for partitioning. This option works only when it's included with `lowerBound`, `upperBound`, and `numPartitions`. This option works the same way as in the Spark SQL JDBC reader.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** UpperBound **   <a name="Glue-Type-JDBCConnectorOptions-UpperBound"></a>
The maximum value of `partitionColumn` that is used to decide partition stride.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_JDBCConnectorOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JDBCConnectorOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JDBCConnectorOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JDBCConnectorOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
