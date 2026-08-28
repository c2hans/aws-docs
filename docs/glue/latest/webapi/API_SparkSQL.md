---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SparkSQL.html
---

# SparkSQL
<a name="API_SparkSQL"></a>

Specifies a transform where you enter a SQL query using Spark SQL syntax to transform the data. The output is a single `DynamicFrame`.

## Contents
<a name="API_SparkSQL_Contents"></a>

 ** Inputs **   <a name="Glue-Type-SparkSQL-Inputs"></a>
The data inputs identified by their node names. You can associate a table name with each input node to use in the SQL query. The name you choose must meet the Spark SQL naming restrictions.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-SparkSQL-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** SqlAliases **   <a name="Glue-Type-SparkSQL-SqlAliases"></a>
A list of aliases. An alias allows you to specify what name to use in the SQL for a given input. For example, you have a datasource named "MyDataSource". If you specify `From` as MyDataSource, and `Alias` as SqlName, then in your SQL you can do:
 `select * from SqlName`
and that gets data from MyDataSource.
Type: Array of [SqlAlias](API_SqlAlias.md) objects
Required: Yes

 ** SqlQuery **   <a name="Glue-Type-SparkSQL-SqlQuery"></a>
A SQL query that must use Spark SQL syntax and return a single data set.
Type: String
Pattern: `([\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\s])*`
Required: Yes

 ** OutputSchemas **   <a name="Glue-Type-SparkSQL-OutputSchemas"></a>
Specifies the data schema for the SparkSQL transform.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_SparkSQL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SparkSQL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SparkSQL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SparkSQL)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
