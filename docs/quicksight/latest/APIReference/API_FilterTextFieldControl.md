---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterTextFieldControl.html
---

# FilterTextFieldControl
<a name="API_FilterTextFieldControl"></a>

A control to display a text box that is used to enter a single entry.

## Contents
<a name="API_FilterTextFieldControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterControlId **   <a name="QS-Type-FilterTextFieldControl-FilterControlId"></a>
The ID of the `FilterTextFieldControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceFilterId **   <a name="QS-Type-FilterTextFieldControl-SourceFilterId"></a>
The source filter ID of the `FilterTextFieldControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** ControlTitleFormatText **   <a name="QS-Type-FilterTextFieldControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-FilterTextFieldControl-DisplayOptions"></a>
The display options of a control.
Type: [TextFieldControlDisplayOptions](API_TextFieldControlDisplayOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-FilterTextFieldControl-Title"></a>
The title of the `FilterTextFieldControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_FilterTextFieldControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterTextFieldControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterTextFieldControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterTextFieldControl)
