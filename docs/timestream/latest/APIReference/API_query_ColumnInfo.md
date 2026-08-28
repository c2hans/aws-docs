---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ColumnInfo.html
---

# ColumnInfo
<a name="API_query_ColumnInfo"></a>

 Contains the metadata for query results such as the column names, data types, and other attributes.

## Contents
<a name="API_query_ColumnInfo_Contents"></a>

 ** Type **   <a name="timestream-Type-query_ColumnInfo-Type"></a>
The data type of the result set column. The data type can be a scalar or complex. Scalar data types are integers, strings, doubles, Booleans, and others. Complex data types are types such as arrays, rows, and others.
Type: [Type](API_query_Type.md) object
Required: Yes

 ** Name **   <a name="timestream-Type-query_ColumnInfo-Name"></a>
 The name of the result set column. The name of the result set is available for columns of all data types except for arrays.
Type: String
Required: No

## See Also
<a name="API_query_ColumnInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ColumnInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ColumnInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ColumnInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
