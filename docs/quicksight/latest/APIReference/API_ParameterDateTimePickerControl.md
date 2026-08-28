---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ParameterDateTimePickerControl.html
---

# ParameterDateTimePickerControl
<a name="API_ParameterDateTimePickerControl"></a>

A control from a date parameter that specifies date and time.

## Contents
<a name="API_ParameterDateTimePickerControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ParameterControlId **   <a name="QS-Type-ParameterDateTimePickerControl-ParameterControlId"></a>
The ID of the `ParameterDateTimePickerControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceParameterName **   <a name="QS-Type-ParameterDateTimePickerControl-SourceParameterName"></a>
The name of the `ParameterDateTimePickerControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** ControlTitleFormatText **   <a name="QS-Type-ParameterDateTimePickerControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-ParameterDateTimePickerControl-DisplayOptions"></a>
The display options of a control.
Type: [DateTimePickerControlDisplayOptions](API_DateTimePickerControlDisplayOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-ParameterDateTimePickerControl-Title"></a>
The title of the `ParameterDateTimePickerControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_ParameterDateTimePickerControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ParameterDateTimePickerControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ParameterDateTimePickerControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ParameterDateTimePickerControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
