---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_InputColumn.html
---

# InputColumn
<a name="API_InputColumn"></a>

Metadata for a column that is used as the input of a transform operation.

## Contents
<a name="API_InputColumn_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-InputColumn-Name"></a>
The name of this column in the underlying data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Type **   <a name="QS-Type-InputColumn-Type"></a>
The data type of the column.
 **Note:** `SEMISTRUCT` represents Athena's map, row, and struct data types. It is supported when using the new data preparation experience.
Type: String
Valid Values: `STRING | INTEGER | DECIMAL | DATETIME | BIT | BOOLEAN | JSON | SEMISTRUCT`
Required: Yes

 ** Id **   <a name="QS-Type-InputColumn-Id"></a>
A unique identifier for the input column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** SubType **   <a name="QS-Type-InputColumn-SubType"></a>
The sub data type of the column. Sub types are only available for decimal columns that are part of a SPICE dataset.
Type: String
Valid Values: `FLOAT | FIXED`
Required: No

## See Also
<a name="API_InputColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/InputColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/InputColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/InputColumn)
