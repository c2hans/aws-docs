---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SnowflakeNodeData.html
---

# SnowflakeNodeData
<a name="API_SnowflakeNodeData"></a>

Specifies configuration for Snowflake nodes in AWS Glue Studio.

## Contents
<a name="API_SnowflakeNodeData_Contents"></a>

 ** Action **   <a name="Glue-Type-SnowflakeNodeData-Action"></a>
Specifies what action to take when writing to a table with preexisting data. Valid values: ` append`, `merge`, `truncate`, `drop`.
Type: String
Required: No

 ** AdditionalOptions **   <a name="Glue-Type-SnowflakeNodeData-AdditionalOptions"></a>
Specifies additional options passed to the Snowflake connector. If options are specified elsewhere in this node, this will take precedence.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** AutoPushdown **   <a name="Glue-Type-SnowflakeNodeData-AutoPushdown"></a>
Specifies whether automatic query pushdown is enabled. If pushdown is enabled, then when a query is run on Spark, if part of the query can be "pushed down" to the Snowflake server, it is pushed down. This improves performance of some queries.
Type: Boolean
Required: No

 ** Connection **   <a name="Glue-Type-SnowflakeNodeData-Connection"></a>
Specifies a AWS Glue Data Catalog Connection to a Snowflake endpoint.
Type: [Option](API_Option.md) object
Required: No

 ** Database **   <a name="Glue-Type-SnowflakeNodeData-Database"></a>
Specifies a Snowflake database for your node to use.
Type: String
Required: No

 ** IamRole **   <a name="Glue-Type-SnowflakeNodeData-IamRole"></a>
Not currently used.
Type: [Option](API_Option.md) object
Required: No

 ** MergeAction **   <a name="Glue-Type-SnowflakeNodeData-MergeAction"></a>
Specifies a merge action. Valid values: `simple`, `custom`. If simple, merge behavior is defined by `MergeWhenMatched` and ` MergeWhenNotMatched`. If custom, defined by `MergeClause`.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** MergeClause **   <a name="Glue-Type-SnowflakeNodeData-MergeClause"></a>
A SQL statement that specifies a custom merge behavior.
Type: String
Required: No

 ** MergeWhenMatched **   <a name="Glue-Type-SnowflakeNodeData-MergeWhenMatched"></a>
Specifies how to resolve records that match preexisting data when merging. Valid values: ` update`, `delete`.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** MergeWhenNotMatched **   <a name="Glue-Type-SnowflakeNodeData-MergeWhenNotMatched"></a>
Specifies how to process records that do not match preexisting data when merging. Valid values: `insert`, `none`.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** PostAction **   <a name="Glue-Type-SnowflakeNodeData-PostAction"></a>
A SQL string run after the Snowflake connector performs its standard actions.
Type: String
Required: No

 ** PreAction **   <a name="Glue-Type-SnowflakeNodeData-PreAction"></a>
A SQL string run before the Snowflake connector performs its standard actions.
Type: String
Required: No

 ** SampleQuery **   <a name="Glue-Type-SnowflakeNodeData-SampleQuery"></a>
A SQL string used to retrieve data with the `query` sourcetype.
Type: String
Required: No

 ** Schema **   <a name="Glue-Type-SnowflakeNodeData-Schema"></a>
Specifies a Snowflake database schema for your node to use.
Type: String
Required: No

 ** SelectedColumns **   <a name="Glue-Type-SnowflakeNodeData-SelectedColumns"></a>
Specifies the columns combined to identify a record when detecting matches for merges and upserts. A list of structures with `value`, `label` and ` description` keys. Each structure describes a column.
Type: Array of [Option](API_Option.md) objects
Required: No

 ** SourceType **   <a name="Glue-Type-SnowflakeNodeData-SourceType"></a>
Specifies how retrieved data is specified. Valid values: `"table"`, ` "query"`.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** StagingTable **   <a name="Glue-Type-SnowflakeNodeData-StagingTable"></a>
The name of a staging table used when performing `merge` or upsert `append` actions. Data is written to this table, then moved to `table` by a generated postaction.
Type: String
Required: No

 ** Table **   <a name="Glue-Type-SnowflakeNodeData-Table"></a>
Specifies a Snowflake table for your node to use.
Type: String
Required: No

 ** TableSchema **   <a name="Glue-Type-SnowflakeNodeData-TableSchema"></a>
Manually defines the target schema for the node. A list of structures with `value` , `label` and `description` keys. Each structure defines a column.
Type: Array of [Option](API_Option.md) objects
Required: No

 ** TempDir **   <a name="Glue-Type-SnowflakeNodeData-TempDir"></a>
Not currently used.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** Upsert **   <a name="Glue-Type-SnowflakeNodeData-Upsert"></a>
Used when Action is `append`. Specifies the resolution behavior when a row already exists. If true, preexisting rows will be updated. If false, those rows will be inserted.
Type: Boolean
Required: No

## See Also
<a name="API_SnowflakeNodeData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SnowflakeNodeData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SnowflakeNodeData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SnowflakeNodeData)
