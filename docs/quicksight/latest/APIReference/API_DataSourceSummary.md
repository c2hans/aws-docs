---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSourceSummary.html
---

# DataSourceSummary
<a name="API_DataSourceSummary"></a>

A `DataSourceSummary` object that returns a summary of a data source.

## Contents
<a name="API_DataSourceSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-DataSourceSummary-Arn"></a>
The arn of the datasource.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-DataSourceSummary-CreatedTime"></a>
The date and time that the data source was created. This value is expressed in MM-DD-YYYY HH:MM:SS format.
Type: Timestamp
Required: No

 ** DataSourceId **   <a name="QS-Type-DataSourceSummary-DataSourceId"></a>
The unique ID of the data source.
Type: String
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-DataSourceSummary-LastUpdatedTime"></a>
The date and time the data source was last updated. This value is expressed in MM-DD-YYYY HH:MM:SS format.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-DataSourceSummary-Name"></a>
The name of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Type **   <a name="QS-Type-DataSourceSummary-Type"></a>
The type of the data source.
Type: String
Valid Values: `ADOBE_ANALYTICS | AMAZON_ELASTICSEARCH | ATHENA | AURORA | AURORA_POSTGRESQL | AWS_IOT_ANALYTICS | GITHUB | JIRA | MARIADB | MYSQL | ORACLE | POSTGRESQL | PRESTO | REDSHIFT | S3 | S3_TABLES | SALESFORCE | SERVICENOW | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | TWITTER | TIMESTREAM | AMAZON_OPENSEARCH | EXASOL | DATABRICKS | STARBURST | TRINO | BIGQUERY | GOOGLESHEETS | GOOGLE_DRIVE | CONFLUENCE | SHAREPOINT | ONE_DRIVE | WEB_CRAWLER | S3_KNOWLEDGE_BASE | QBUSINESS`
Required: No

## See Also
<a name="API_DataSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSourceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
