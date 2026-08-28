---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterControl.html
---

# FilterControl
<a name="API_FilterControl"></a>

The control of a filter that is used to interact with a dashboard or an analysis.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_FilterControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CrossSheet **   <a name="QS-Type-FilterControl-CrossSheet"></a>
A control from a filter that is scoped across more than one sheet. This represents your filter control on a sheet
Type: [FilterCrossSheetControl](API_FilterCrossSheetControl.md) object
Required: No

 ** DateTimePicker **   <a name="QS-Type-FilterControl-DateTimePicker"></a>
A control from a date filter that is used to specify date and time.
Type: [FilterDateTimePickerControl](API_FilterDateTimePickerControl.md) object
Required: No

 ** Dropdown **   <a name="QS-Type-FilterControl-Dropdown"></a>
A control to display a dropdown list with buttons that are used to select a single value.
Type: [FilterDropDownControl](API_FilterDropDownControl.md) object
Required: No

 ** List **   <a name="QS-Type-FilterControl-List"></a>
A control to display a list of buttons or boxes. This is used to select either a single value or multiple values.
Type: [FilterListControl](API_FilterListControl.md) object
Required: No

 ** RelativeDateTime **   <a name="QS-Type-FilterControl-RelativeDateTime"></a>
A control from a date filter that is used to specify the relative date.
Type: [FilterRelativeDateTimeControl](API_FilterRelativeDateTimeControl.md) object
Required: No

 ** Slider **   <a name="QS-Type-FilterControl-Slider"></a>
A control to display a horizontal toggle bar. This is used to change a value by sliding the toggle.
Type: [FilterSliderControl](API_FilterSliderControl.md) object
Required: No

 ** TextArea **   <a name="QS-Type-FilterControl-TextArea"></a>
A control to display a text box that is used to enter multiple entries.
Type: [FilterTextAreaControl](API_FilterTextAreaControl.md) object
Required: No

 ** TextField **   <a name="QS-Type-FilterControl-TextField"></a>
A control to display a text box that is used to enter a single entry.
Type: [FilterTextFieldControl](API_FilterTextFieldControl.md) object
Required: No

## See Also
<a name="API_FilterControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
