---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UnmaterializedCalculatedColumn.html
---

# UnmaterializedCalculatedColumn

A calculated column that is not materialized in the prepared data. The column is computed at analysis time and can use aggregate expressions.

## Contents
<a name="API_UnmaterializedCalculatedColumn_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnId **   <a name="QS-Type-UnmaterializedCalculatedColumn-ColumnId"></a>
A unique ID to identify the unmaterialized calculated column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ColumnName **   <a name="QS-Type-UnmaterializedCalculatedColumn-ColumnName"></a>
The name of the unmaterialized calculated column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Expression **   <a name="QS-Type-UnmaterializedCalculatedColumn-Expression"></a>
An expression that defines the unmaterialized calculated column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250000.
Required: Yes

 ** SubType **   <a name="QS-Type-UnmaterializedCalculatedColumn-SubType"></a>
The sub data type of the unmaterialized calculated column.
Type: String
Valid Values: `FLOAT | FIXED`
Required: No

 ** Type **   <a name="QS-Type-UnmaterializedCalculatedColumn-Type"></a>
The data type of the unmaterialized calculated column.
Type: String
Valid Values: `STRING | INTEGER | DECIMAL | DATETIME`
Required: No

## See Also
<a name="API_UnmaterializedCalculatedColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UnmaterializedCalculatedColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UnmaterializedCalculatedColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UnmaterializedCalculatedColumn)
