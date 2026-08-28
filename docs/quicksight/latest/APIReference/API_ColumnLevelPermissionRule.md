---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnLevelPermissionRule.html
---

# ColumnLevelPermissionRule
<a name="API_ColumnLevelPermissionRule"></a>

A rule defined to grant access on one or more restricted columns. Each dataset can have multiple rules. To create a restricted column, you add it to one or more rules. Each rule must contain at least one column and at least one user or group. To be able to see a restricted column, a user or group needs to be added to a rule for that column.

## Contents
<a name="API_ColumnLevelPermissionRule_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnNames **   <a name="QS-Type-ColumnLevelPermissionRule-ColumnNames"></a>
An array of column names.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** Principals **   <a name="QS-Type-ColumnLevelPermissionRule-Principals"></a>
An array of Amazon Resource Names (ARNs) for Quick Sight users or groups.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_ColumnLevelPermissionRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ColumnLevelPermissionRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ColumnLevelPermissionRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ColumnLevelPermissionRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
