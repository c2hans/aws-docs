---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TagColumnOperation.html
---

# TagColumnOperation
<a name="API_TagColumnOperation"></a>

A transform operation that tags a column with additional information.

## Contents
<a name="API_TagColumnOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-TagColumnOperation-ColumnName"></a>
The column that this operation acts on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Tags **   <a name="QS-Type-TagColumnOperation-Tags"></a>
The dataset column tag, currently only used for geospatial type tagging.
This is not tags for the AWS tagging feature.
Type: Array of [ColumnTag](API_ColumnTag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Required: Yes

## See Also
<a name="API_TagColumnOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TagColumnOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TagColumnOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TagColumnOperation)
