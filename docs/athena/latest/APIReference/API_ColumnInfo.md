---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ColumnInfo.html
---

# ColumnInfo
<a name="API_ColumnInfo"></a>

Information about the columns in a query execution result.

## Contents
<a name="API_ColumnInfo_Contents"></a>

 ** Name **   <a name="athena-Type-ColumnInfo-Name"></a>
The name of the column.
Type: String
Required: Yes

 ** Type **   <a name="athena-Type-ColumnInfo-Type"></a>
The data type of the column.
Type: String
Required: Yes

 ** CaseSensitive **   <a name="athena-Type-ColumnInfo-CaseSensitive"></a>
Indicates whether values in the column are case-sensitive.
Type: Boolean
Required: No

 ** CatalogName **   <a name="athena-Type-ColumnInfo-CatalogName"></a>
The catalog to which the query results belong.
Type: String
Required: No

 ** Label **   <a name="athena-Type-ColumnInfo-Label"></a>
A column label.
Type: String
Required: No

 ** Nullable **   <a name="athena-Type-ColumnInfo-Nullable"></a>
Unsupported constraint. This value always shows as `UNKNOWN`.
Type: String
Valid Values: `NOT_NULL | NULLABLE | UNKNOWN`
Required: No

 ** Precision **   <a name="athena-Type-ColumnInfo-Precision"></a>
For `DECIMAL` data types, specifies the total number of digits, up to 38. For performance reasons, we recommend up to 18 digits.
Type: Integer
Required: No

 ** Scale **   <a name="athena-Type-ColumnInfo-Scale"></a>
For `DECIMAL` data types, specifies the total number of digits in the fractional part of the value. Defaults to 0.
Type: Integer
Required: No

 ** SchemaName **   <a name="athena-Type-ColumnInfo-SchemaName"></a>
The schema name (database name) to which the query results belong.
Type: String
Required: No

 ** TableName **   <a name="athena-Type-ColumnInfo-TableName"></a>
The table name for the query results.
Type: String
Required: No

## See Also
<a name="API_ColumnInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ColumnInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ColumnInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ColumnInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
