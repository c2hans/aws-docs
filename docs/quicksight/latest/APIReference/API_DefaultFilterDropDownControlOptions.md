---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DefaultFilterDropDownControlOptions.html
---

# DefaultFilterDropDownControlOptions
<a name="API_DefaultFilterDropDownControlOptions"></a>

The default options that correspond to the `Dropdown` filter control type.

## Contents
<a name="API_DefaultFilterDropDownControlOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CommitMode **   <a name="QS-Type-DefaultFilterDropDownControlOptions-CommitMode"></a>
The visibility configuration of the Apply button on a `FilterDropDownControl`.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** ControlSortConfigurations **   <a name="QS-Type-DefaultFilterDropDownControlOptions-ControlSortConfigurations"></a>
The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.
Type: Array of [ControlSortConfiguration](API_ControlSortConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** DisplayOptions **   <a name="QS-Type-DefaultFilterDropDownControlOptions-DisplayOptions"></a>
The display options of a control.
Type: [DropDownControlDisplayOptions](API_DropDownControlDisplayOptions.md) object
Required: No

 ** SelectableValues **   <a name="QS-Type-DefaultFilterDropDownControlOptions-SelectableValues"></a>
A list of selectable values that are used in a control.
Type: [FilterSelectableValues](API_FilterSelectableValues.md) object
Required: No

 ** Type **   <a name="QS-Type-DefaultFilterDropDownControlOptions-Type"></a>
The type of the `FilterDropDownControl`. Choose one of the following options:
+  `MULTI_SELECT`: The user can select multiple entries from a dropdown menu.
+  `SINGLE_SELECT`: The user can select a single entry from a dropdown menu.
Type: String
Valid Values: `MULTI_SELECT | SINGLE_SELECT`
Required: No

## See Also
<a name="API_DefaultFilterDropDownControlOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DefaultFilterDropDownControlOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DefaultFilterDropDownControlOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DefaultFilterDropDownControlOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
