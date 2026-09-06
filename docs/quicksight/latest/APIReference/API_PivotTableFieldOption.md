---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PivotTableFieldOption.html
---

# PivotTableFieldOption
<a name="API_PivotTableFieldOption"></a>

The selected field options for the pivot table field options.

## Contents
<a name="API_PivotTableFieldOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FieldId **   <a name="QS-Type-PivotTableFieldOption-FieldId"></a>
The field ID of the pivot table field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** CustomLabel **   <a name="QS-Type-PivotTableFieldOption-CustomLabel"></a>
The custom label of the pivot table field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Visibility **   <a name="QS-Type-PivotTableFieldOption-Visibility"></a>
The visibility of the pivot table field.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_PivotTableFieldOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PivotTableFieldOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PivotTableFieldOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PivotTableFieldOption)
