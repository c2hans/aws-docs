---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RowLevelPermissionTagConfiguration.html
---

# RowLevelPermissionTagConfiguration
<a name="API_RowLevelPermissionTagConfiguration"></a>

The configuration of tags on a dataset to set row-level security.

## Contents
<a name="API_RowLevelPermissionTagConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TagRules **   <a name="QS-Type-RowLevelPermissionTagConfiguration-TagRules"></a>
A set of rules associated with row-level security, such as the tag names and columns that they are assigned to.
Type: Array of [RowLevelPermissionTagRule](API_RowLevelPermissionTagRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** Status **   <a name="QS-Type-RowLevelPermissionTagConfiguration-Status"></a>
The status of row-level security tags. If enabled, the status is `ENABLED`. If disabled, the status is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** TagRuleConfigurations **   <a name="QS-Type-RowLevelPermissionTagConfiguration-TagRuleConfigurations"></a>
A list of tag configuration rules to apply to a dataset. All tag configurations have the OR condition. Tags within each tile will be joined (AND). At least one rule in this structure must have all tag values assigned to it to apply Row-level security (RLS) to the dataset.
Type: Array of arrays of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_RowLevelPermissionTagConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RowLevelPermissionTagConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RowLevelPermissionTagConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RowLevelPermissionTagConfiguration)
