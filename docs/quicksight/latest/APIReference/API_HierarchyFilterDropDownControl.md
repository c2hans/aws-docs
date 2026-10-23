---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_HierarchyFilterDropDownControl.html
---

# HierarchyFilterDropDownControl
<a name="API_HierarchyFilterDropDownControl"></a>

A control from a hierarchy filter that displays the hierarchy as a dropdown list. You can expand a value to see and select the values beneath it, and select either a single value or multiple values.

## Contents
<a name="API_HierarchyFilterDropDownControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterControlId **   <a name="QS-Type-HierarchyFilterDropDownControl-FilterControlId"></a>
The ID of the `HierarchyFilterDropDownControl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** SourceFilterId **   <a name="QS-Type-HierarchyFilterDropDownControl-SourceFilterId"></a>
The source filter ID of the `HierarchyFilterDropDownControl`. This must be the `FilterId` of a `HierarchyFilter`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** CommitMode **   <a name="QS-Type-HierarchyFilterDropDownControl-CommitMode"></a>
The visibility configuration of the Apply button on a `HierarchyFilterDropDownControl`.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** ControlSortConfigurations **   <a name="QS-Type-HierarchyFilterDropDownControl-ControlSortConfigurations"></a>
The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.
Type: Array of [ControlSortConfiguration](API_ControlSortConfiguration.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** ControlTitleFormatText **   <a name="QS-Type-HierarchyFilterDropDownControl-ControlTitleFormatText"></a>
The title text format configuration for the control.
Type: [ControlTitleFormatText](API_ControlTitleFormatText.md) object
Required: No

 ** DisplayOptions **   <a name="QS-Type-HierarchyFilterDropDownControl-DisplayOptions"></a>
The display options of a control.
Type: [HierarchyFilterDropDownControlDisplayOptions](API_HierarchyFilterDropDownControlDisplayOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-HierarchyFilterDropDownControl-Title"></a>
The title of the `HierarchyFilterDropDownControl`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Type **   <a name="QS-Type-HierarchyFilterDropDownControl-Type"></a>
The type of the `HierarchyFilterDropDownControl`. Choose one of the following options:
+  `MULTI_SELECT`: The user can select multiple entries from a dropdown menu.
+  `SINGLE_SELECT`: The user can select a single entry from a dropdown menu.
Type: String
Valid Values: `MULTI_SELECT | SINGLE_SELECT`
Required: No

## See Also
<a name="API_HierarchyFilterDropDownControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/HierarchyFilterDropDownControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/HierarchyFilterDropDownControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/HierarchyFilterDropDownControl)
