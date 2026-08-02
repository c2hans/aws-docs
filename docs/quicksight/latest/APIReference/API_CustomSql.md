---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomSql.html
---

# CustomSql
<a name="API_CustomSql"></a>

A physical table type built from the results of the custom SQL query.

## Contents
<a name="API_CustomSql_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSourceArn **   <a name="QS-Type-CustomSql-DataSourceArn"></a>
The Amazon Resource Name (ARN) of the data source.
Type: String
Required: Yes

 ** Name **   <a name="QS-Type-CustomSql-Name"></a>
A display name for the SQL query result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** SqlQuery **   <a name="QS-Type-CustomSql-SqlQuery"></a>
The SQL query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 168000.
Required: Yes

 ** Columns **   <a name="QS-Type-CustomSql-Columns"></a>
The column schema from the SQL query result set.
Type: Array of [InputColumn](API_InputColumn.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: No

## See Also
<a name="API_CustomSql_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomSql)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomSql)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomSql)
