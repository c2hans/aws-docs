---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterDateTimePickerControl.html
---

# FilterDateTimePickerControl
<a name="API_FilterDateTimePickerControl"></a>

A control from a date filter that is used to specify date and time.

## Contents
<a name="API_FilterDateTimePickerControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterControlId **   <a name="QS-Type-FilterDateTimePickerControl-FilterControlId"></a>
The ID of the `FilterDateTimePickerControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceFilterId **   <a name="QS-Type-FilterDateTimePickerControl-SourceFilterId"></a>
The source filter ID of the `FilterDateTimePickerControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** CommitMode **   <a name="QS-Type-FilterDateTimePickerControl-CommitMode"></a>
The visibility configurationof the Apply button on a `DateTimePickerControl`.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** ControlTitleFormatText **   <a name="QS-Type-FilterDateTimePickerControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-FilterDateTimePickerControl-DisplayOptions"></a>
The display options of a control.
Type: [DateTimePickerControlDisplayOptions](API_DateTimePickerControlDisplayOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-FilterDateTimePickerControl-Title"></a>
The title of the `FilterDateTimePickerControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Type **   <a name="QS-Type-FilterDateTimePickerControl-Type"></a>
The type of the `FilterDropDownControl`. Choose one of the following options:
+  `MULTI_SELECT`: The user can select multiple entries from a dropdown menu.
+  `SINGLE_SELECT`: The user can select a single entry from a dropdown menu.
Type: String
Valid Values: `SINGLE_VALUED | DATE_RANGE`
Required: No

## See Also
<a name="API_FilterDateTimePickerControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterDateTimePickerControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterDateTimePickerControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterDateTimePickerControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
