---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RowLevelPermissionTagRule.html
---

# RowLevelPermissionTagRule
<a name="API_RowLevelPermissionTagRule"></a>

A set of rules associated with a tag.

## Contents
<a name="API_RowLevelPermissionTagRule_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-RowLevelPermissionTagRule-ColumnName"></a>
The column name that a tag key is assigned to.
Type: String
Required: Yes

 ** TagKey **   <a name="QS-Type-RowLevelPermissionTagRule-TagKey"></a>
The unique key for a tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** MatchAllValue **   <a name="QS-Type-RowLevelPermissionTagRule-MatchAllValue"></a>
A string that you want to use to filter by all the values in a column in the dataset and don’t want to list the values one by one. For example, you can use an asterisk as your match all value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** TagMultiValueDelimiter **   <a name="QS-Type-RowLevelPermissionTagRule-TagMultiValueDelimiter"></a>
A string that you want to use to delimit the values when you pass the values at run time. For example, you can delimit the values with a comma.
Type: String
Length Constraints: Maximum length of 10.
Required: No

## See Also
<a name="API_RowLevelPermissionTagRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RowLevelPermissionTagRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RowLevelPermissionTagRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RowLevelPermissionTagRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
