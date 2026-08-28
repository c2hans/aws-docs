---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AmazonRedshiftNodeData.html
---

# AmazonRedshiftNodeData
<a name="API_AmazonRedshiftNodeData"></a>

Specifies an Amazon Redshift node.

## Contents
<a name="API_AmazonRedshiftNodeData_Contents"></a>

 ** AccessType **   <a name="Glue-Type-AmazonRedshiftNodeData-AccessType"></a>
The access type for the Redshift connection. Can be a direct connection or catalog connections.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** Action **   <a name="Glue-Type-AmazonRedshiftNodeData-Action"></a>
Specifies how writing to a Redshift cluser will occur.
Type: String
Required: No

 ** AdvancedOptions **   <a name="Glue-Type-AmazonRedshiftNodeData-AdvancedOptions"></a>
Optional values when connecting to the Redshift cluster.
Type: Array of [AmazonRedshiftAdvancedOption](API_AmazonRedshiftAdvancedOption.md) objects
Required: No

 ** CatalogDatabase **   <a name="Glue-Type-AmazonRedshiftNodeData-CatalogDatabase"></a>
The name of the AWS Glue Data Catalog database when working with a data catalog.
Type: [Option](API_Option.md) object
Required: No

 ** CatalogRedshiftSchema **   <a name="Glue-Type-AmazonRedshiftNodeData-CatalogRedshiftSchema"></a>
The Redshift schema name when working with a data catalog.
Type: String
Required: No

 ** CatalogRedshiftTable **   <a name="Glue-Type-AmazonRedshiftNodeData-CatalogRedshiftTable"></a>
The database table to read from.
Type: String
Required: No

 ** CatalogTable **   <a name="Glue-Type-AmazonRedshiftNodeData-CatalogTable"></a>
The AWS Glue Data Catalog table name when working with a data catalog.
Type: [Option](API_Option.md) object
Required: No

 ** Connection **   <a name="Glue-Type-AmazonRedshiftNodeData-Connection"></a>
The AWS Glue connection to the Redshift cluster.
Type: [Option](API_Option.md) object
Required: No

 ** CrawlerConnection **   <a name="Glue-Type-AmazonRedshiftNodeData-CrawlerConnection"></a>
Specifies the name of the connection that is associated with the catalog table used.
Type: String
Required: No

 ** IamRole **   <a name="Glue-Type-AmazonRedshiftNodeData-IamRole"></a>
Optional. The role name use when connection to S3. The IAM role ill default to the role on the job when left blank.
Type: [Option](API_Option.md) object
Required: No

 ** MergeAction **   <a name="Glue-Type-AmazonRedshiftNodeData-MergeAction"></a>
The action used when to detemine how a MERGE in a Redshift sink will be handled.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** MergeClause **   <a name="Glue-Type-AmazonRedshiftNodeData-MergeClause"></a>
The SQL used in a custom merge to deal with matching records.
Type: String
Required: No

 ** MergeWhenMatched **   <a name="Glue-Type-AmazonRedshiftNodeData-MergeWhenMatched"></a>
The action used when to detemine how a MERGE in a Redshift sink will be handled when an existing record matches a new record.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** MergeWhenNotMatched **   <a name="Glue-Type-AmazonRedshiftNodeData-MergeWhenNotMatched"></a>
The action used when to detemine how a MERGE in a Redshift sink will be handled when an existing record doesn't match a new record.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** PostAction **   <a name="Glue-Type-AmazonRedshiftNodeData-PostAction"></a>
The SQL used before a MERGE or APPEND with upsert is run.
Type: String
Required: No

 ** PreAction **   <a name="Glue-Type-AmazonRedshiftNodeData-PreAction"></a>
The SQL used before a MERGE or APPEND with upsert is run.
Type: String
Required: No

 ** SampleQuery **   <a name="Glue-Type-AmazonRedshiftNodeData-SampleQuery"></a>
The SQL used to fetch the data from a Redshift sources when the SourceType is 'query'.
Type: String
Required: No

 ** Schema **   <a name="Glue-Type-AmazonRedshiftNodeData-Schema"></a>
The Redshift schema name when working with a direct connection.
Type: [Option](API_Option.md) object
Required: No

 ** SelectedColumns **   <a name="Glue-Type-AmazonRedshiftNodeData-SelectedColumns"></a>
The list of column names used to determine a matching record when doing a MERGE or APPEND with upsert.
Type: Array of [Option](API_Option.md) objects
Required: No

 ** SourceType **   <a name="Glue-Type-AmazonRedshiftNodeData-SourceType"></a>
The source type to specify whether a specific table is the source or a custom query.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** StagingTable **   <a name="Glue-Type-AmazonRedshiftNodeData-StagingTable"></a>
The name of the temporary staging table that is used when doing a MERGE or APPEND with upsert.
Type: String
Required: No

 ** Table **   <a name="Glue-Type-AmazonRedshiftNodeData-Table"></a>
The Redshift table name when working with a direct connection.
Type: [Option](API_Option.md) object
Required: No

 ** TablePrefix **   <a name="Glue-Type-AmazonRedshiftNodeData-TablePrefix"></a>
Specifies the prefix to a table.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** TableSchema **   <a name="Glue-Type-AmazonRedshiftNodeData-TableSchema"></a>
The array of schema output for a given node.
Type: Array of [Option](API_Option.md) objects
Required: No

 ** TempDir **   <a name="Glue-Type-AmazonRedshiftNodeData-TempDir"></a>
The Amazon S3 path where temporary data can be staged when copying out of the database.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** Upsert **   <a name="Glue-Type-AmazonRedshiftNodeData-Upsert"></a>
The action used on Redshift sinks when doing an APPEND.
Type: Boolean
Required: No

## See Also
<a name="API_AmazonRedshiftNodeData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AmazonRedshiftNodeData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AmazonRedshiftNodeData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AmazonRedshiftNodeData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
