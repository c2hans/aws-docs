---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ParameterTextAreaControl.html
---

# ParameterTextAreaControl
<a name="API_ParameterTextAreaControl"></a>

A control to display a text box that is used to enter multiple entries.

## Contents
<a name="API_ParameterTextAreaControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ParameterControlId **   <a name="QS-Type-ParameterTextAreaControl-ParameterControlId"></a>
The ID of the `ParameterTextAreaControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceParameterName **   <a name="QS-Type-ParameterTextAreaControl-SourceParameterName"></a>
The source parameter name of the `ParameterTextAreaControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** ControlTitleFormatText **   <a name="QS-Type-ParameterTextAreaControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** Delimiter **   <a name="QS-Type-ParameterTextAreaControl-Delimiter"></a>
The delimiter that is used to separate the lines in text.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** DisplayOptions **   <a name="QS-Type-ParameterTextAreaControl-DisplayOptions"></a>
The display options of a control.
Type: [TextAreaControlDisplayOptions](API_TextAreaControlDisplayOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-ParameterTextAreaControl-Title"></a>
The title of the `ParameterTextAreaControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_ParameterTextAreaControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ParameterTextAreaControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ParameterTextAreaControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ParameterTextAreaControl)
