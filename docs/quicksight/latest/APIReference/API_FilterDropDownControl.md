---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterDropDownControl.html
---

# FilterDropDownControl
<a name="API_FilterDropDownControl"></a>

A control to display a dropdown list with buttons that are used to select a single value.

## Contents
<a name="API_FilterDropDownControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterControlId **   <a name="QS-Type-FilterDropDownControl-FilterControlId"></a>
The ID of the `FilterDropDownControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceFilterId **   <a name="QS-Type-FilterDropDownControl-SourceFilterId"></a>
The source filter ID of the `FilterDropDownControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** CascadingControlConfiguration **   <a name="QS-Type-FilterDropDownControl-CascadingControlConfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
Type: [CascadingControlConfiguration](API_CascadingControlConfiguration.md) object
Required: No

 ** CommitMode **   <a name="QS-Type-FilterDropDownControl-CommitMode"></a>
The visibility configuration of the Apply button on a `FilterDropDownControl`.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** ControlSortConfigurations **   <a name="QS-Type-FilterDropDownControl-ControlSortConfigurations"></a>
The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.
Type: Array of [ControlSortConfiguration](API_ControlSortConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** ControlTitleFormatText **   <a name="QS-Type-FilterDropDownControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-FilterDropDownControl-DisplayOptions"></a>
The display options of the `FilterDropDownControl`.
Type: [DropDownControlDisplayOptions](API_DropDownControlDisplayOptions.md) object
Required: No

 ** SelectableValues **   <a name="QS-Type-FilterDropDownControl-SelectableValues"></a>
A list of selectable values that are used in a control.
Type: [FilterSelectableValues](API_FilterSelectableValues.md) object
Required: No

 ** Title **   <a name="QS-Type-FilterDropDownControl-Title"></a>
The title of the `FilterDropDownControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Type **   <a name="QS-Type-FilterDropDownControl-Type"></a>
The type of the `FilterDropDownControl`. Choose one of the following options:
+  `MULTI_SELECT`: The user can select multiple entries from a dropdown menu.
+  `SINGLE_SELECT`: The user can select a single entry from a dropdown menu.
Type: String
Valid Values: `MULTI_SELECT | SINGLE_SELECT`
Required: No

## See Also
<a name="API_FilterDropDownControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterDropDownControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterDropDownControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterDropDownControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
