---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ParameterListControl.html
---

# ParameterListControl
<a name="API_ParameterListControl"></a>

A control to display a list with buttons or boxes that are used to select either a single value or multiple values.

## Contents
<a name="API_ParameterListControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ParameterControlId **   <a name="QS-Type-ParameterListControl-ParameterControlId"></a>
The ID of the `ParameterListControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceParameterName **   <a name="QS-Type-ParameterListControl-SourceParameterName"></a>
The source parameter name of the `ParameterListControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** CascadingControlConfiguration **   <a name="QS-Type-ParameterListControl-CascadingControlConfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
Type: [CascadingControlConfiguration](API_CascadingControlConfiguration.md) object
Required: No

 ** ControlSortConfigurations **   <a name="QS-Type-ParameterListControl-ControlSortConfigurations"></a>
The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.
Type: Array of [ControlSortConfiguration](API_ControlSortConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** ControlTitleFormatText **   <a name="QS-Type-ParameterListControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-ParameterListControl-DisplayOptions"></a>
The display options of a control.
Type: [ListControlDisplayOptions](API_ListControlDisplayOptions.md) object
Required: No

 ** SelectableValues **   <a name="QS-Type-ParameterListControl-SelectableValues"></a>
A list of selectable values that are used in a control.
Type: [ParameterSelectableValues](API_ParameterSelectableValues.md) object
Required: No

 ** Title **   <a name="QS-Type-ParameterListControl-Title"></a>
The title of the `ParameterListControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Type **   <a name="QS-Type-ParameterListControl-Type"></a>
The type of `ParameterListControl`.
Type: String
Valid Values: `MULTI_SELECT | SINGLE_SELECT`
Required: No

## See Also
<a name="API_ParameterListControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ParameterListControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ParameterListControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ParameterListControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
