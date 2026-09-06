---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterCrossSheetControl.html
---

# FilterCrossSheetControl
<a name="API_FilterCrossSheetControl"></a>

A control from a filter that is scoped across more than one sheet. This represents your filter control on a sheet

## Contents
<a name="API_FilterCrossSheetControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterControlId **   <a name="QS-Type-FilterCrossSheetControl-FilterControlId"></a>
The ID of the `FilterCrossSheetControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceFilterId **   <a name="QS-Type-FilterCrossSheetControl-SourceFilterId"></a>
The source filter ID of the `FilterCrossSheetControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** CascadingControlConfiguration **   <a name="QS-Type-FilterCrossSheetControl-CascadingControlConfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
Type: [CascadingControlConfiguration](API_CascadingControlConfiguration.md) object
Required: No

## See Also
<a name="API_FilterCrossSheetControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterCrossSheetControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterCrossSheetControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterCrossSheetControl)
