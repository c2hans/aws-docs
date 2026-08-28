---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CodeGenConfigurationNode.html
---

# CodeGenConfigurationNode
<a name="API_CodeGenConfigurationNode"></a>

 `CodeGenConfigurationNode` enumerates all valid Node types. One and only one of its member variables can be populated.

## Contents
<a name="API_CodeGenConfigurationNode_Contents"></a>

 ** Aggregate **   <a name="Glue-Type-CodeGenConfigurationNode-Aggregate"></a>
Specifies a transform that groups rows by chosen fields and computes the aggregated value by specified function.
Type: [Aggregate](API_Aggregate.md) object
Required: No

 ** AmazonRedshiftSource **   <a name="Glue-Type-CodeGenConfigurationNode-AmazonRedshiftSource"></a>
Specifies a target that writes to a data source in Amazon Redshift.
Type: [AmazonRedshiftSource](API_AmazonRedshiftSource.md) object
Required: No

 ** AmazonRedshiftTarget **   <a name="Glue-Type-CodeGenConfigurationNode-AmazonRedshiftTarget"></a>
Specifies a target that writes to a data target in Amazon Redshift.
Type: [AmazonRedshiftTarget](API_AmazonRedshiftTarget.md) object
Required: No

 ** ApplyMapping **   <a name="Glue-Type-CodeGenConfigurationNode-ApplyMapping"></a>
Specifies a transform that maps data property keys in the data source to data property keys in the data target. You can rename keys, modify the data types for keys, and choose which keys to drop from the dataset.
Type: [ApplyMapping](API_ApplyMapping.md) object
Required: No

 ** AthenaConnectorSource **   <a name="Glue-Type-CodeGenConfigurationNode-AthenaConnectorSource"></a>
Specifies a connector to an Amazon Athena data source.
Type: [AthenaConnectorSource](API_AthenaConnectorSource.md) object
Required: No

 ** CatalogDeltaSource **   <a name="Glue-Type-CodeGenConfigurationNode-CatalogDeltaSource"></a>
Specifies a Delta Lake data source that is registered in the AWS Glue Data Catalog.
Type: [CatalogDeltaSource](API_CatalogDeltaSource.md) object
Required: No

 ** CatalogHudiSource **   <a name="Glue-Type-CodeGenConfigurationNode-CatalogHudiSource"></a>
Specifies a Hudi data source that is registered in the AWS Glue Data Catalog.
Type: [CatalogHudiSource](API_CatalogHudiSource.md) object
Required: No

 ** CatalogIcebergSource **   <a name="Glue-Type-CodeGenConfigurationNode-CatalogIcebergSource"></a>
Specifies an Apache Iceberg data source that is registered in the AWS Glue Data Catalog.
Type: [CatalogIcebergSource](API_CatalogIcebergSource.md) object
Required: No

 ** CatalogKafkaSource **   <a name="Glue-Type-CodeGenConfigurationNode-CatalogKafkaSource"></a>
Specifies an Apache Kafka data store in the Data Catalog.
Type: [CatalogKafkaSource](API_CatalogKafkaSource.md) object
Required: No

 ** CatalogKinesisSource **   <a name="Glue-Type-CodeGenConfigurationNode-CatalogKinesisSource"></a>
Specifies a Kinesis data source in the AWS Glue Data Catalog.
Type: [CatalogKinesisSource](API_CatalogKinesisSource.md) object
Required: No

 ** CatalogSource **   <a name="Glue-Type-CodeGenConfigurationNode-CatalogSource"></a>
Specifies a data store in the AWS Glue Data Catalog.
Type: [CatalogSource](API_CatalogSource.md) object
Required: No

 ** CatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-CatalogTarget"></a>
Specifies a target that uses a AWS Glue Data Catalog table.
Type: [BasicCatalogTarget](API_BasicCatalogTarget.md) object
Required: No

 ** ConnectorDataSource **   <a name="Glue-Type-CodeGenConfigurationNode-ConnectorDataSource"></a>
Specifies a source generated with standard connection options.
Type: [ConnectorDataSource](API_ConnectorDataSource.md) object
Required: No

 ** ConnectorDataTarget **   <a name="Glue-Type-CodeGenConfigurationNode-ConnectorDataTarget"></a>
Specifies a target generated with standard connection options.
Type: [ConnectorDataTarget](API_ConnectorDataTarget.md) object
Required: No

 ** CustomCode **   <a name="Glue-Type-CodeGenConfigurationNode-CustomCode"></a>
Specifies a transform that uses custom code you provide to perform the data transformation. The output is a collection of DynamicFrames.
Type: [CustomCode](API_CustomCode.md) object
Required: No

 ** DirectJDBCSource **   <a name="Glue-Type-CodeGenConfigurationNode-DirectJDBCSource"></a>
Specifies the direct JDBC source connection.
Type: [DirectJDBCSource](API_DirectJDBCSource.md) object
Required: No

 ** DirectKafkaSource **   <a name="Glue-Type-CodeGenConfigurationNode-DirectKafkaSource"></a>
Specifies an Apache Kafka data store.
Type: [DirectKafkaSource](API_DirectKafkaSource.md) object
Required: No

 ** DirectKinesisSource **   <a name="Glue-Type-CodeGenConfigurationNode-DirectKinesisSource"></a>
Specifies a direct Amazon Kinesis data source.
Type: [DirectKinesisSource](API_DirectKinesisSource.md) object
Required: No

 ** DropDuplicates **   <a name="Glue-Type-CodeGenConfigurationNode-DropDuplicates"></a>
Specifies a transform that removes rows of repeating data from a data set.
Type: [DropDuplicates](API_DropDuplicates.md) object
Required: No

 ** DropFields **   <a name="Glue-Type-CodeGenConfigurationNode-DropFields"></a>
Specifies a transform that chooses the data property keys that you want to drop.
Type: [DropFields](API_DropFields.md) object
Required: No

 ** DropNullFields **   <a name="Glue-Type-CodeGenConfigurationNode-DropNullFields"></a>
Specifies a transform that removes columns from the dataset if all values in the column are 'null'. By default, AWS Glue Studio will recognize null objects, but some values such as empty strings, strings that are "null", -1 integers or other placeholders such as zeros, are not automatically recognized as nulls.
Type: [DropNullFields](API_DropNullFields.md) object
Required: No

 ** DynamicTransform **   <a name="Glue-Type-CodeGenConfigurationNode-DynamicTransform"></a>
Specifies a custom visual transform created by a user.
Type: [DynamicTransform](API_DynamicTransform.md) object
Required: No

 ** DynamoDBCatalogSource **   <a name="Glue-Type-CodeGenConfigurationNode-DynamoDBCatalogSource"></a>
Specifies a DynamoDBC Catalog data store in the AWS Glue Data Catalog.
Type: [DynamoDBCatalogSource](API_DynamoDBCatalogSource.md) object
Required: No

 ** DynamoDBELTConnectorSource **   <a name="Glue-Type-CodeGenConfigurationNode-DynamoDBELTConnectorSource"></a>
Specifies a DynamoDB ELT connector source for extracting data from DynamoDB tables.
Type: [DynamoDBELTConnectorSource](API_DynamoDBELTConnectorSource.md) object
Required: No

 ** EvaluateDataQuality **   <a name="Glue-Type-CodeGenConfigurationNode-EvaluateDataQuality"></a>
Specifies your data quality evaluation criteria.
Type: [EvaluateDataQuality](API_EvaluateDataQuality.md) object
Required: No

 ** EvaluateDataQualityMultiFrame **   <a name="Glue-Type-CodeGenConfigurationNode-EvaluateDataQualityMultiFrame"></a>
Specifies your data quality evaluation criteria. Allows multiple input data and returns a collection of Dynamic Frames.
Type: [EvaluateDataQualityMultiFrame](API_EvaluateDataQualityMultiFrame.md) object
Required: No

 ** FillMissingValues **   <a name="Glue-Type-CodeGenConfigurationNode-FillMissingValues"></a>
Specifies a transform that locates records in the dataset that have missing values and adds a new field with a value determined by imputation. The input data set is used to train the machine learning model that determines what the missing value should be.
Type: [FillMissingValues](API_FillMissingValues.md) object
Required: No

 ** Filter **   <a name="Glue-Type-CodeGenConfigurationNode-Filter"></a>
Specifies a transform that splits a dataset into two, based on a filter condition.
Type: [Filter](API_Filter.md) object
Required: No

 ** GovernedCatalogSource **   <a name="Glue-Type-CodeGenConfigurationNode-GovernedCatalogSource"></a>
Specifies a data source in a goverened Data Catalog.
Type: [GovernedCatalogSource](API_GovernedCatalogSource.md) object
Required: No

 ** GovernedCatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-GovernedCatalogTarget"></a>
Specifies a data target that writes to a goverened catalog.
Type: [GovernedCatalogTarget](API_GovernedCatalogTarget.md) object
Required: No

 ** JDBCConnectorSource **   <a name="Glue-Type-CodeGenConfigurationNode-JDBCConnectorSource"></a>
Specifies a connector to a JDBC data source.
Type: [JDBCConnectorSource](API_JDBCConnectorSource.md) object
Required: No

 ** JDBCConnectorTarget **   <a name="Glue-Type-CodeGenConfigurationNode-JDBCConnectorTarget"></a>
Specifies a data target that writes to Amazon S3 in Apache Parquet columnar storage.
Type: [JDBCConnectorTarget](API_JDBCConnectorTarget.md) object
Required: No

 ** Join **   <a name="Glue-Type-CodeGenConfigurationNode-Join"></a>
Specifies a transform that joins two datasets into one dataset using a comparison phrase on the specified data property keys. You can use inner, outer, left, right, left semi, and left anti joins.
Type: [Join](API_Join.md) object
Required: No

 ** Merge **   <a name="Glue-Type-CodeGenConfigurationNode-Merge"></a>
Specifies a transform that merges a `DynamicFrame` with a staging `DynamicFrame` based on the specified primary keys to identify records. Duplicate records (records with the same primary keys) are not de-duplicated.
Type: [Merge](API_Merge.md) object
Required: No

 ** MicrosoftSQLServerCatalogSource **   <a name="Glue-Type-CodeGenConfigurationNode-MicrosoftSQLServerCatalogSource"></a>
Specifies a Microsoft SQL server data source in the AWS Glue Data Catalog.
Type: [MicrosoftSQLServerCatalogSource](API_MicrosoftSQLServerCatalogSource.md) object
Required: No

 ** MicrosoftSQLServerCatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-MicrosoftSQLServerCatalogTarget"></a>
Specifies a target that uses Microsoft SQL.
Type: [MicrosoftSQLServerCatalogTarget](API_MicrosoftSQLServerCatalogTarget.md) object
Required: No

 ** MySQLCatalogSource **   <a name="Glue-Type-CodeGenConfigurationNode-MySQLCatalogSource"></a>
Specifies a MySQL data source in the AWS Glue Data Catalog.
Type: [MySQLCatalogSource](API_MySQLCatalogSource.md) object
Required: No

 ** MySQLCatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-MySQLCatalogTarget"></a>
Specifies a target that uses MySQL.
Type: [MySQLCatalogTarget](API_MySQLCatalogTarget.md) object
Required: No

 ** OracleSQLCatalogSource **   <a name="Glue-Type-CodeGenConfigurationNode-OracleSQLCatalogSource"></a>
Specifies an Oracle data source in the AWS Glue Data Catalog.
Type: [OracleSQLCatalogSource](API_OracleSQLCatalogSource.md) object
Required: No

 ** OracleSQLCatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-OracleSQLCatalogTarget"></a>
Specifies a target that uses Oracle SQL.
Type: [OracleSQLCatalogTarget](API_OracleSQLCatalogTarget.md) object
Required: No

 ** PIIDetection **   <a name="Glue-Type-CodeGenConfigurationNode-PIIDetection"></a>
Specifies a transform that identifies, removes or masks PII data.
Type: [PIIDetection](API_PIIDetection.md) object
Required: No

 ** PostgreSQLCatalogSource **   <a name="Glue-Type-CodeGenConfigurationNode-PostgreSQLCatalogSource"></a>
Specifies a PostgresSQL data source in the AWS Glue Data Catalog.
Type: [PostgreSQLCatalogSource](API_PostgreSQLCatalogSource.md) object
Required: No

 ** PostgreSQLCatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-PostgreSQLCatalogTarget"></a>
Specifies a target that uses Postgres SQL.
Type: [PostgreSQLCatalogTarget](API_PostgreSQLCatalogTarget.md) object
Required: No

 ** Recipe **   <a name="Glue-Type-CodeGenConfigurationNode-Recipe"></a>
Specifies a AWS Glue DataBrew recipe node.
Type: [Recipe](API_Recipe.md) object
Required: No

 ** RedshiftSource **   <a name="Glue-Type-CodeGenConfigurationNode-RedshiftSource"></a>
Specifies an Amazon Redshift data store.
Type: [RedshiftSource](API_RedshiftSource.md) object
Required: No

 ** RedshiftTarget **   <a name="Glue-Type-CodeGenConfigurationNode-RedshiftTarget"></a>
Specifies a target that uses Amazon Redshift.
Type: [RedshiftTarget](API_RedshiftTarget.md) object
Required: No

 ** RelationalCatalogSource **   <a name="Glue-Type-CodeGenConfigurationNode-RelationalCatalogSource"></a>
Specifies a relational catalog data store in the AWS Glue Data Catalog.
Type: [RelationalCatalogSource](API_RelationalCatalogSource.md) object
Required: No

 ** RenameField **   <a name="Glue-Type-CodeGenConfigurationNode-RenameField"></a>
Specifies a transform that renames a single data property key.
Type: [RenameField](API_RenameField.md) object
Required: No

 ** Route **   <a name="Glue-Type-CodeGenConfigurationNode-Route"></a>
Specifies a route node that directs data to different output paths based on defined filtering conditions.
Type: [Route](API_Route.md) object
Required: No

 ** S3CatalogDeltaSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3CatalogDeltaSource"></a>
Specifies a Delta Lake data source that is registered in the AWS Glue Data Catalog. The data source must be stored in Amazon S3.
Type: [S3CatalogDeltaSource](API_S3CatalogDeltaSource.md) object
Required: No

 ** S3CatalogHudiSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3CatalogHudiSource"></a>
Specifies a Hudi data source that is registered in the AWS Glue Data Catalog. The data source must be stored in Amazon S3.
Type: [S3CatalogHudiSource](API_S3CatalogHudiSource.md) object
Required: No

 ** S3CatalogIcebergSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3CatalogIcebergSource"></a>
Specifies an Apache Iceberg data source that is registered in the AWS Glue Data Catalog. The Iceberg data source must be stored in Amazon S3.
Type: [S3CatalogIcebergSource](API_S3CatalogIcebergSource.md) object
Required: No

 ** S3CatalogSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3CatalogSource"></a>
Specifies an Amazon S3 data store in the AWS Glue Data Catalog.
Type: [S3CatalogSource](API_S3CatalogSource.md) object
Required: No

 ** S3CatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3CatalogTarget"></a>
Specifies a data target that writes to Amazon S3 using the AWS Glue Data Catalog.
Type: [S3CatalogTarget](API_S3CatalogTarget.md) object
Required: No

 ** S3CsvSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3CsvSource"></a>
Specifies a command-separated value (CSV) data store stored in Amazon S3.
Type: [S3CsvSource](API_S3CsvSource.md) object
Required: No

 ** S3DeltaCatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3DeltaCatalogTarget"></a>
Specifies a target that writes to a Delta Lake data source in the AWS Glue Data Catalog.
Type: [S3DeltaCatalogTarget](API_S3DeltaCatalogTarget.md) object
Required: No

 ** S3DeltaDirectTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3DeltaDirectTarget"></a>
Specifies a target that writes to a Delta Lake data source in Amazon S3.
Type: [S3DeltaDirectTarget](API_S3DeltaDirectTarget.md) object
Required: No

 ** S3DeltaSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3DeltaSource"></a>
Specifies a Delta Lake data source stored in Amazon S3.
Type: [S3DeltaSource](API_S3DeltaSource.md) object
Required: No

 ** S3DirectTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3DirectTarget"></a>
Specifies a data target that writes to Amazon S3.
Type: [S3DirectTarget](API_S3DirectTarget.md) object
Required: No

 ** S3ExcelSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3ExcelSource"></a>
Defines configuration parameters for reading Excel files from Amazon S3.
Type: [S3ExcelSource](API_S3ExcelSource.md) object
Required: No

 ** S3GlueParquetTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3GlueParquetTarget"></a>
Specifies a data target that writes to Amazon S3 in Apache Parquet columnar storage.
Type: [S3GlueParquetTarget](API_S3GlueParquetTarget.md) object
Required: No

 ** S3HudiCatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3HudiCatalogTarget"></a>
Specifies a target that writes to a Hudi data source in the AWS Glue Data Catalog.
Type: [S3HudiCatalogTarget](API_S3HudiCatalogTarget.md) object
Required: No

 ** S3HudiDirectTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3HudiDirectTarget"></a>
Specifies a target that writes to a Hudi data source in Amazon S3.
Type: [S3HudiDirectTarget](API_S3HudiDirectTarget.md) object
Required: No

 ** S3HudiSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3HudiSource"></a>
Specifies a Hudi data source stored in Amazon S3.
Type: [S3HudiSource](API_S3HudiSource.md) object
Required: No

 ** S3HyperDirectTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3HyperDirectTarget"></a>
Defines configuration parameters for writing data to Amazon S3 using HyperDirect optimization.
Type: [S3HyperDirectTarget](API_S3HyperDirectTarget.md) object
Required: No

 ** S3IcebergCatalogTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3IcebergCatalogTarget"></a>
Specifies an Apache Iceberg catalog target that writes data to Amazon S3 and registers the table in the AWS Glue Data Catalog.
Type: [S3IcebergCatalogTarget](API_S3IcebergCatalogTarget.md) object
Required: No

 ** S3IcebergDirectTarget **   <a name="Glue-Type-CodeGenConfigurationNode-S3IcebergDirectTarget"></a>
Defines configuration parameters for writing data to Amazon S3 as an Apache Iceberg table.
Type: [S3IcebergDirectTarget](API_S3IcebergDirectTarget.md) object
Required: No

 ** S3JsonSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3JsonSource"></a>
Specifies a JSON data store stored in Amazon S3.
Type: [S3JsonSource](API_S3JsonSource.md) object
Required: No

 ** S3ParquetSource **   <a name="Glue-Type-CodeGenConfigurationNode-S3ParquetSource"></a>
Specifies an Apache Parquet data store stored in Amazon S3.
Type: [S3ParquetSource](API_S3ParquetSource.md) object
Required: No

 ** SelectFields **   <a name="Glue-Type-CodeGenConfigurationNode-SelectFields"></a>
Specifies a transform that chooses the data property keys that you want to keep.
Type: [SelectFields](API_SelectFields.md) object
Required: No

 ** SelectFromCollection **   <a name="Glue-Type-CodeGenConfigurationNode-SelectFromCollection"></a>
Specifies a transform that chooses one `DynamicFrame` from a collection of `DynamicFrames`. The output is the selected `DynamicFrame`
Type: [SelectFromCollection](API_SelectFromCollection.md) object
Required: No

 ** SnowflakeSource **   <a name="Glue-Type-CodeGenConfigurationNode-SnowflakeSource"></a>
Specifies a Snowflake data source.
Type: [SnowflakeSource](API_SnowflakeSource.md) object
Required: No

 ** SnowflakeTarget **   <a name="Glue-Type-CodeGenConfigurationNode-SnowflakeTarget"></a>
Specifies a target that writes to a Snowflake data source.
Type: [SnowflakeTarget](API_SnowflakeTarget.md) object
Required: No

 ** SparkConnectorSource **   <a name="Glue-Type-CodeGenConfigurationNode-SparkConnectorSource"></a>
Specifies a connector to an Apache Spark data source.
Type: [SparkConnectorSource](API_SparkConnectorSource.md) object
Required: No

 ** SparkConnectorTarget **   <a name="Glue-Type-CodeGenConfigurationNode-SparkConnectorTarget"></a>
Specifies a target that uses an Apache Spark connector.
Type: [SparkConnectorTarget](API_SparkConnectorTarget.md) object
Required: No

 ** SparkSQL **   <a name="Glue-Type-CodeGenConfigurationNode-SparkSQL"></a>
Specifies a transform where you enter a SQL query using Spark SQL syntax to transform the data. The output is a single `DynamicFrame`.
Type: [SparkSQL](API_SparkSQL.md) object
Required: No

 ** Spigot **   <a name="Glue-Type-CodeGenConfigurationNode-Spigot"></a>
Specifies a transform that writes samples of the data to an Amazon S3 bucket.
Type: [Spigot](API_Spigot.md) object
Required: No

 ** SplitFields **   <a name="Glue-Type-CodeGenConfigurationNode-SplitFields"></a>
Specifies a transform that splits data property keys into two `DynamicFrames`. The output is a collection of `DynamicFrames`: one with selected data property keys, and one with the remaining data property keys.
Type: [SplitFields](API_SplitFields.md) object
Required: No

 ** Union **   <a name="Glue-Type-CodeGenConfigurationNode-Union"></a>
Specifies a transform that combines the rows from two or more datasets into a single result.
Type: [Union](API_Union.md) object
Required: No

## See Also
<a name="API_CodeGenConfigurationNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CodeGenConfigurationNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CodeGenConfigurationNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CodeGenConfigurationNode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
