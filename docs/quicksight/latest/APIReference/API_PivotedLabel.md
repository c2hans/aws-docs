---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PivotedLabel.html
---

# PivotedLabel
<a name="API_PivotedLabel"></a>

Specifies a label value to be pivoted into a separate column, including the new column name and identifier.

## Contents
<a name="API_PivotedLabel_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LabelName **   <a name="QS-Type-PivotedLabel-LabelName"></a>
The label value from the source data to be pivoted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2047.
Required: Yes

 ** NewColumnId **   <a name="QS-Type-PivotedLabel-NewColumnId"></a>
A unique identifier for the new column created from this pivoted label.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** NewColumnName **   <a name="QS-Type-PivotedLabel-NewColumnName"></a>
The name for the new column created from this pivoted label.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_PivotedLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PivotedLabel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PivotedLabel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PivotedLabel)
