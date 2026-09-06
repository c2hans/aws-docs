---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterRelativeDateTimeControl.html
---

# FilterRelativeDateTimeControl
<a name="API_FilterRelativeDateTimeControl"></a>

A control from a date filter that is used to specify the relative date.

## Contents
<a name="API_FilterRelativeDateTimeControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterControlId **   <a name="QS-Type-FilterRelativeDateTimeControl-FilterControlId"></a>
The ID of the `FilterTextAreaControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceFilterId **   <a name="QS-Type-FilterRelativeDateTimeControl-SourceFilterId"></a>
The source filter ID of the `FilterTextAreaControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** CommitMode **   <a name="QS-Type-FilterRelativeDateTimeControl-CommitMode"></a>
The visibility configuration of the Apply button on a `FilterRelativeDateTimeControl`.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** ControlTitleFormatText **   <a name="QS-Type-FilterRelativeDateTimeControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-FilterRelativeDateTimeControl-DisplayOptions"></a>
The display options of a control.
Type: [RelativeDateTimeControlDisplayOptions](API_RelativeDateTimeControlDisplayOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-FilterRelativeDateTimeControl-Title"></a>
The title of the `FilterTextAreaControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_FilterRelativeDateTimeControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterRelativeDateTimeControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterRelativeDateTimeControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterRelativeDateTimeControl)
