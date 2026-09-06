---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ParameterDropDownControl.html
---

# ParameterDropDownControl
<a name="API_ParameterDropDownControl"></a>

A control to display a dropdown list with buttons that are used to select a single value.

## Contents
<a name="API_ParameterDropDownControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ParameterControlId **   <a name="QS-Type-ParameterDropDownControl-ParameterControlId"></a>
The ID of the `ParameterDropDownControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceParameterName **   <a name="QS-Type-ParameterDropDownControl-SourceParameterName"></a>
The source parameter name of the `ParameterDropDownControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** CascadingControlConfiguration **   <a name="QS-Type-ParameterDropDownControl-CascadingControlConfiguration"></a>
The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.
Type: [CascadingControlConfiguration](API_CascadingControlConfiguration.md) object
Required: No

 ** CommitMode **   <a name="QS-Type-ParameterDropDownControl-CommitMode"></a>
The visibility configuration of the Apply button on a `ParameterDropDownControl`.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** ControlSortConfigurations **   <a name="QS-Type-ParameterDropDownControl-ControlSortConfigurations"></a>
The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.
Type: Array of [ControlSortConfiguration](API_ControlSortConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** ControlTitleFormatText **   <a name="QS-Type-ParameterDropDownControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-ParameterDropDownControl-DisplayOptions"></a>
The display options of a control.
Type: [DropDownControlDisplayOptions](API_DropDownControlDisplayOptions.md) object
Required: No

 ** SelectableValues **   <a name="QS-Type-ParameterDropDownControl-SelectableValues"></a>
A list of selectable values that are used in a control.
Type: [ParameterSelectableValues](API_ParameterSelectableValues.md) object
Required: No

 ** Title **   <a name="QS-Type-ParameterDropDownControl-Title"></a>
The title of the `ParameterDropDownControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Type **   <a name="QS-Type-ParameterDropDownControl-Type"></a>
The type parameter name of the `ParameterDropDownControl`.
Type: String
Valid Values: `MULTI_SELECT | SINGLE_SELECT`
Required: No

## See Also
<a name="API_ParameterDropDownControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ParameterDropDownControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ParameterDropDownControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ParameterDropDownControl)
