---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SameSheetTargetVisualConfiguration.html
---

# SameSheetTargetVisualConfiguration
<a name="API_SameSheetTargetVisualConfiguration"></a>

The configuration of the same-sheet target visuals that you want to be filtered.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_SameSheetTargetVisualConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TargetVisualOptions **   <a name="QS-Type-SameSheetTargetVisualConfiguration-TargetVisualOptions"></a>
The options that choose the target visual in the same sheet.
Valid values are defined as follows:
+  `ALL_VISUALS`: Applies the filter operation to all visuals in the same sheet.
Type: String
Valid Values: `ALL_VISUALS`
Required: No

 ** TargetVisuals **   <a name="QS-Type-SameSheetTargetVisualConfiguration-TargetVisuals"></a>
A list of the target visual IDs that are located in the same sheet of the analysis.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 75 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

## See Also
<a name="API_SameSheetTargetVisualConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SameSheetTargetVisualConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SameSheetTargetVisualConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SameSheetTargetVisualConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
