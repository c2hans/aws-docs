---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CalculatedColumn.html
---

# CalculatedColumn
<a name="API_CalculatedColumn"></a>

A calculated column for a dataset.

## Contents
<a name="API_CalculatedColumn_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnId **   <a name="QS-Type-CalculatedColumn-ColumnId"></a>
A unique ID to identify a calculated column. During a dataset update, if the column ID of a calculated column matches that of an existing calculated column, Quick Sight preserves the existing calculated column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** ColumnName **   <a name="QS-Type-CalculatedColumn-ColumnName"></a>
Column name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Expression **   <a name="QS-Type-CalculatedColumn-Expression"></a>
An expression that defines the calculated column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250000.
Required: Yes

## See Also
<a name="API_CalculatedColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CalculatedColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CalculatedColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CalculatedColumn)
