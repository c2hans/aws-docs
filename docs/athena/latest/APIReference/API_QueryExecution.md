---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_QueryExecution.html
---

# QueryExecution
<a name="API_QueryExecution"></a>

Information about a single instance of a query execution.

## Contents
<a name="API_QueryExecution_Contents"></a>

 ** EngineVersion **   <a name="athena-Type-QueryExecution-EngineVersion"></a>
The engine version that executed the query.
Type: [EngineVersion](API_EngineVersion.md) object
Required: No

 ** ExecutionParameters **   <a name="athena-Type-QueryExecution-ExecutionParameters"></a>
A list of values for the parameters in a query. The values are applied sequentially to the parameters in the query in the order in which the parameters occur. The list of parameters is not returned in the response.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ManagedQueryResultsConfiguration **   <a name="athena-Type-QueryExecution-ManagedQueryResultsConfiguration"></a>
 The configuration for storing results in Athena owned storage, which includes whether this feature is enabled; whether encryption configuration, if any, is used for encrypting query results.
Type: [ManagedQueryResultsConfiguration](API_ManagedQueryResultsConfiguration.md) object
Required: No

 ** Query **   <a name="athena-Type-QueryExecution-Query"></a>
The SQL query statements which the query execution ran.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: No

 ** QueryExecutionContext **   <a name="athena-Type-QueryExecution-QueryExecutionContext"></a>
The database in which the query execution occurred.
Type: [QueryExecutionContext](API_QueryExecutionContext.md) object
Required: No

 ** QueryExecutionId **   <a name="athena-Type-QueryExecution-QueryExecutionId"></a>
The unique identifier for each query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S+`
Required: No

 ** QueryResultsS3AccessGrantsConfiguration **   <a name="athena-Type-QueryExecution-QueryResultsS3AccessGrantsConfiguration"></a>
Specifies whether Amazon S3 access grants are enabled for query results.
Type: [QueryResultsS3AccessGrantsConfiguration](API_QueryResultsS3AccessGrantsConfiguration.md) object
Required: No

 ** ResultConfiguration **   <a name="athena-Type-QueryExecution-ResultConfiguration"></a>
The location in Amazon S3 where query and calculation results are stored and the encryption option, if any, used for query results. These are known as "client-side settings". If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup.
Type: [ResultConfiguration](API_ResultConfiguration.md) object
Required: No

 ** ResultReuseConfiguration **   <a name="athena-Type-QueryExecution-ResultReuseConfiguration"></a>
Specifies the query result reuse behavior that was used for the query.
Type: [ResultReuseConfiguration](API_ResultReuseConfiguration.md) object
Required: No

 ** StatementType **   <a name="athena-Type-QueryExecution-StatementType"></a>
The type of query statement that was run. `DDL` indicates DDL query statements. `DML` indicates DML (Data Manipulation Language) query statements, such as `CREATE TABLE AS SELECT`. `UTILITY` indicates query statements other than DDL and DML, such as `SHOW CREATE TABLE`, `EXPLAIN`, `DESCRIBE`, or `SHOW TABLES`.
Type: String
Valid Values: `DDL | DML | UTILITY`
Required: No

 ** Statistics **   <a name="athena-Type-QueryExecution-Statistics"></a>
Query execution statistics, such as the amount of data scanned, the amount of time that the query took to process, and the type of statement that was run.
Type: [QueryExecutionStatistics](API_QueryExecutionStatistics.md) object
Required: No

 ** Status **   <a name="athena-Type-QueryExecution-Status"></a>
The completion date, current state, submission time, and state change reason (if applicable) for the query execution.
Type: [QueryExecutionStatus](API_QueryExecutionStatus.md) object
Required: No

 ** SubstatementType **   <a name="athena-Type-QueryExecution-SubstatementType"></a>
The kind of query statement that was run.
Type: String
Required: No

 ** WorkGroup **   <a name="athena-Type-QueryExecution-WorkGroup"></a>
The name of the workgroup in which the query ran.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: No

## See Also
<a name="API_QueryExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/QueryExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/QueryExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/QueryExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
