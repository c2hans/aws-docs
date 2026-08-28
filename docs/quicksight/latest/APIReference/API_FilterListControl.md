---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterListControl.html
---

# FilterListControl
<a name="API_FilterListControl"></a>

A control to display a list of buttons or boxes. This is used to select either a single value or multiple values.

## Contents
<a name="API_FilterListControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterControlId **   <a name="QS-Type-FilterListControl-FilterControlId"></a>
The ID of the `FilterListControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceFilterId **   <a name="QS-Type-FilterListControl-SourceFilterId"></a>
The source filter ID of the `FilterListControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** CascadingControlConfiguration **   <a name="QS-Type-FilterListControl-CascadingControlConfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
Type: [CascadingControlConfiguration](API_CascadingControlConfiguration.md) object
Required: No

 ** ControlSortConfigurations **   <a name="QS-Type-FilterListControl-ControlSortConfigurations"></a>
The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.
Type: Array of [ControlSortConfiguration](API_ControlSortConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** ControlTitleFormatText **   <a name="QS-Type-FilterListControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-FilterListControl-DisplayOptions"></a>
The display options of a control.
Type: [ListControlDisplayOptions](API_ListControlDisplayOptions.md) object
Required: No

 ** SelectableValues **   <a name="QS-Type-FilterListControl-SelectableValues"></a>
A list of selectable values that are used in a control.
Type: [FilterSelectableValues](API_FilterSelectableValues.md) object
Required: No

 ** Title **   <a name="QS-Type-FilterListControl-Title"></a>
The title of the `FilterListControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Type **   <a name="QS-Type-FilterListControl-Type"></a>
The type of the `FilterListControl`. Choose one of the following options:
+  `MULTI_SELECT`: The user can select multiple entries from the list.
+  `SINGLE_SELECT`: The user can select a single entry from the list.
Type: String
Valid Values: `MULTI_SELECT | SINGLE_SELECT`
Required: No

## See Also
<a name="API_FilterListControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterListControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterListControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterListControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
