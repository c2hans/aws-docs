---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UntagColumnOperation.html
---

# UntagColumnOperation
<a name="API_UntagColumnOperation"></a>

A transform operation that removes tags associated with a column.

## Contents
<a name="API_UntagColumnOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-UntagColumnOperation-ColumnName"></a>
The column that this operation acts on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** TagNames **   <a name="QS-Type-UntagColumnOperation-TagNames"></a>
The column tags to remove from this column.
Type: Array of strings
Valid Values: `COLUMN_GEOGRAPHIC_ROLE | COLUMN_DESCRIPTION`
Required: Yes

## See Also
<a name="API_UntagColumnOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UntagColumnOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UntagColumnOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UntagColumnOperation)
