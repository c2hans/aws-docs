---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSourceParameters.html
---

# DataSourceParameters
<a name="API_DataSourceParameters"></a>

The parameters that Quick Sight uses to connect to your underlying data source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

## Contents
<a name="API_DataSourceParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AmazonElasticsearchParameters **   <a name="QS-Type-DataSourceParameters-AmazonElasticsearchParameters"></a>
The parameters for OpenSearch.
Type: [AmazonElasticsearchParameters](API_AmazonElasticsearchParameters.md) object
Required: No

 ** AmazonOpenSearchParameters **   <a name="QS-Type-DataSourceParameters-AmazonOpenSearchParameters"></a>
The parameters for OpenSearch.
Type: [AmazonOpenSearchParameters](API_AmazonOpenSearchParameters.md) object
Required: No

 ** AthenaParameters **   <a name="QS-Type-DataSourceParameters-AthenaParameters"></a>
The parameters for Amazon Athena.
Type: [AthenaParameters](API_AthenaParameters.md) object
Required: No

 ** AuroraParameters **   <a name="QS-Type-DataSourceParameters-AuroraParameters"></a>
The parameters for Amazon Aurora MySQL.
Type: [AuroraParameters](API_AuroraParameters.md) object
Required: No

 ** AuroraPostgreSqlParameters **   <a name="QS-Type-DataSourceParameters-AuroraPostgreSqlParameters"></a>
The parameters for Amazon Aurora.
Type: [AuroraPostgreSqlParameters](API_AuroraPostgreSqlParameters.md) object
Required: No

 ** AwsIotAnalyticsParameters **   <a name="QS-Type-DataSourceParameters-AwsIotAnalyticsParameters"></a>
The parameters for AWS IoT Analytics.
Type: [AwsIotAnalyticsParameters](API_AwsIotAnalyticsParameters.md) object
Required: No

 ** BigQueryParameters **   <a name="QS-Type-DataSourceParameters-BigQueryParameters"></a>
The parameters that are required to connect to a Google BigQuery data source.
Type: [BigQueryParameters](API_BigQueryParameters.md) object
Required: No

 ** ConfluenceParameters **   <a name="QS-Type-DataSourceParameters-ConfluenceParameters"></a>
The parameters for Confluence.
Type: [ConfluenceParameters](API_ConfluenceParameters.md) object
Required: No

 ** CustomConnectionParameters **   <a name="QS-Type-DataSourceParameters-CustomConnectionParameters"></a>
The parameters for custom connectors.
Type: [CustomConnectionParameters](API_CustomConnectionParameters.md) object
Required: No

 ** DatabricksParameters **   <a name="QS-Type-DataSourceParameters-DatabricksParameters"></a>
The parameters that are required to connect to a Databricks data source.
Type: [DatabricksParameters](API_DatabricksParameters.md) object
Required: No

 ** ExasolParameters **   <a name="QS-Type-DataSourceParameters-ExasolParameters"></a>
The parameters for Exasol.
Type: [ExasolParameters](API_ExasolParameters.md) object
Required: No

 ** FMKBParameters **   <a name="QS-Type-DataSourceParameters-FMKBParameters"></a>
The parameters for a fully managed knowledge base data source.
Type: [FMKBParameters](API_FMKBParameters.md) object
Required: No

 ** GoogleDriveParameters **   <a name="QS-Type-DataSourceParameters-GoogleDriveParameters"></a>
The parameters for a Google Drive data source.
Type: [GoogleDriveParameters](API_GoogleDriveParameters.md) object
Required: No

 ** ImpalaParameters **   <a name="QS-Type-DataSourceParameters-ImpalaParameters"></a>
The parameters for Impala.
Type: [ImpalaParameters](API_ImpalaParameters.md) object
Required: No

 ** JiraParameters **   <a name="QS-Type-DataSourceParameters-JiraParameters"></a>
The parameters for Jira.
Type: [JiraParameters](API_JiraParameters.md) object
Required: No

 ** MariaDbParameters **   <a name="QS-Type-DataSourceParameters-MariaDbParameters"></a>
The parameters for MariaDB.
Type: [MariaDbParameters](API_MariaDbParameters.md) object
Required: No

 ** MySqlParameters **   <a name="QS-Type-DataSourceParameters-MySqlParameters"></a>
The parameters for MySQL.
Type: [MySqlParameters](API_MySqlParameters.md) object
Required: No

 ** OneDriveParameters **   <a name="QS-Type-DataSourceParameters-OneDriveParameters"></a>
The parameters for an OneDrive data source.
Type: [OneDriveParameters](API_OneDriveParameters.md) object
Required: No

 ** OracleParameters **   <a name="QS-Type-DataSourceParameters-OracleParameters"></a>
The parameters for Oracle.
Type: [OracleParameters](API_OracleParameters.md) object
Required: No

 ** PostgreSqlParameters **   <a name="QS-Type-DataSourceParameters-PostgreSqlParameters"></a>
The parameters for PostgreSQL.
Type: [PostgreSqlParameters](API_PostgreSqlParameters.md) object
Required: No

 ** PrestoParameters **   <a name="QS-Type-DataSourceParameters-PrestoParameters"></a>
The parameters for Presto.
Type: [PrestoParameters](API_PrestoParameters.md) object
Required: No

 ** QBusinessParameters **   <a name="QS-Type-DataSourceParameters-QBusinessParameters"></a>
The parameters for Amazon Q Business.
Type: [QBusinessParameters](API_QBusinessParameters.md) object
Required: No

 ** RdsParameters **   <a name="QS-Type-DataSourceParameters-RdsParameters"></a>
The parameters for Amazon RDS.
Type: [RdsParameters](API_RdsParameters.md) object
Required: No

 ** RedshiftParameters **   <a name="QS-Type-DataSourceParameters-RedshiftParameters"></a>
The parameters for Amazon Redshift.
Type: [RedshiftParameters](API_RedshiftParameters.md) object
Required: No

 ** S3KnowledgeBaseParameters **   <a name="QS-Type-DataSourceParameters-S3KnowledgeBaseParameters"></a>
The parameters for S3 Knowledge Base.
Type: [S3KnowledgeBaseParameters](API_S3KnowledgeBaseParameters.md) object
Required: No

 ** S3Parameters **   <a name="QS-Type-DataSourceParameters-S3Parameters"></a>
The parameters for S3.
Type: [S3Parameters](API_S3Parameters.md) object
Required: No

 ** S3TablesParameters **   <a name="QS-Type-DataSourceParameters-S3TablesParameters"></a>
The parameters for S3 Tables.
Type: [S3TablesParameters](API_S3TablesParameters.md) object
Required: No

 ** ServiceNowParameters **   <a name="QS-Type-DataSourceParameters-ServiceNowParameters"></a>
The parameters for ServiceNow.
Type: [ServiceNowParameters](API_ServiceNowParameters.md) object
Required: No

 ** SharePointParameters **   <a name="QS-Type-DataSourceParameters-SharePointParameters"></a>
The parameters for a SharePoint data source.
Type: [SharePointParameters](API_SharePointParameters.md) object
Required: No

 ** SnowflakeParameters **   <a name="QS-Type-DataSourceParameters-SnowflakeParameters"></a>
The parameters for Snowflake.
Type: [SnowflakeParameters](API_SnowflakeParameters.md) object
Required: No

 ** SparkParameters **   <a name="QS-Type-DataSourceParameters-SparkParameters"></a>
The parameters for Spark.
Type: [SparkParameters](API_SparkParameters.md) object
Required: No

 ** SqlServerParameters **   <a name="QS-Type-DataSourceParameters-SqlServerParameters"></a>
The parameters for SQL Server.
Type: [SqlServerParameters](API_SqlServerParameters.md) object
Required: No

 ** StarburstParameters **   <a name="QS-Type-DataSourceParameters-StarburstParameters"></a>
The parameters that are required to connect to a Starburst data source.
Type: [StarburstParameters](API_StarburstParameters.md) object
Required: No

 ** TeradataParameters **   <a name="QS-Type-DataSourceParameters-TeradataParameters"></a>
The parameters for Teradata.
Type: [TeradataParameters](API_TeradataParameters.md) object
Required: No

 ** TrinoParameters **   <a name="QS-Type-DataSourceParameters-TrinoParameters"></a>
The parameters that are required to connect to a Trino data source.
Type: [TrinoParameters](API_TrinoParameters.md) object
Required: No

 ** TwitterParameters **   <a name="QS-Type-DataSourceParameters-TwitterParameters"></a>
The parameters for Twitter.
Type: [TwitterParameters](API_TwitterParameters.md) object
Required: No

 ** WebCrawlerParameters **   <a name="QS-Type-DataSourceParameters-WebCrawlerParameters"></a>
The parameters for Web Crawler.
Type: [WebCrawlerParameters](API_WebCrawlerParameters.md) object
Required: No

## See Also
<a name="API_DataSourceParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSourceParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSourceParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSourceParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
