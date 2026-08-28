---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ParameterControl.html
---

# ParameterControl
<a name="API_ParameterControl"></a>

The control of a parameter that users can interact with in a dashboard or an analysis.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_ParameterControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DateTimePicker **   <a name="QS-Type-ParameterControl-DateTimePicker"></a>
A control from a date parameter that specifies date and time.
Type: [ParameterDateTimePickerControl](API_ParameterDateTimePickerControl.md) object
Required: No

 ** Dropdown **   <a name="QS-Type-ParameterControl-Dropdown"></a>
A control to display a dropdown list with buttons that are used to select a single value.
Type: [ParameterDropDownControl](API_ParameterDropDownControl.md) object
Required: No

 ** List **   <a name="QS-Type-ParameterControl-List"></a>
A control to display a list with buttons or boxes that are used to select either a single value or multiple values.
Type: [ParameterListControl](API_ParameterListControl.md) object
Required: No

 ** Slider **   <a name="QS-Type-ParameterControl-Slider"></a>
A control to display a horizontal toggle bar. This is used to change a value by sliding the toggle.
Type: [ParameterSliderControl](API_ParameterSliderControl.md) object
Required: No

 ** TextArea **   <a name="QS-Type-ParameterControl-TextArea"></a>
A control to display a text box that is used to enter multiple entries.
Type: [ParameterTextAreaControl](API_ParameterTextAreaControl.md) object
Required: No

 ** TextField **   <a name="QS-Type-ParameterControl-TextField"></a>
A control to display a text box that is used to enter a single entry.
Type: [ParameterTextFieldControl](API_ParameterTextFieldControl.md) object
Required: No

## See Also
<a name="API_ParameterControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ParameterControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ParameterControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ParameterControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
