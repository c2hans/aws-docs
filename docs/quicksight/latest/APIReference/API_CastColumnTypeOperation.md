---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CastColumnTypeOperation.html
---

# CastColumnTypeOperation
<a name="API_CastColumnTypeOperation"></a>

A transform operation that casts a column to a different type.

## Contents
<a name="API_CastColumnTypeOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-CastColumnTypeOperation-ColumnName"></a>
Column name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** NewColumnType **   <a name="QS-Type-CastColumnTypeOperation-NewColumnType"></a>
New column data type.
Type: String
Valid Values: `STRING | INTEGER | DECIMAL | DATETIME`
Required: Yes

 ** Format **   <a name="QS-Type-CastColumnTypeOperation-Format"></a>
When casting a column from string to datetime type, you can supply a string in a format supported by Quick Sight to denote the source data format.
Type: String
Length Constraints: Maximum length of 32.
Required: No

 ** SubType **   <a name="QS-Type-CastColumnTypeOperation-SubType"></a>
The sub data type of the new column. Sub types are only available for decimal columns that are part of a SPICE dataset.
Type: String
Valid Values: `FLOAT | FIXED`
Required: No

## See Also
<a name="API_CastColumnTypeOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CastColumnTypeOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CastColumnTypeOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CastColumnTypeOperation)
