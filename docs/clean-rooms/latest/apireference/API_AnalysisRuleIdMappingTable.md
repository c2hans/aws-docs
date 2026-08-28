---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisRuleIdMappingTable.html
---

# AnalysisRuleIdMappingTable
<a name="API_AnalysisRuleIdMappingTable"></a>

Defines details for the analysis rule ID mapping table.

## Contents
<a name="API_AnalysisRuleIdMappingTable_Contents"></a>

 ** joinColumns **   <a name="API-Type-AnalysisRuleIdMappingTable-joinColumns"></a>
The columns that query runners are allowed to use in an INNER JOIN statement.
Type: Array of strings
Array Members: Fixed number of 2 items.
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** queryConstraints **   <a name="API-Type-AnalysisRuleIdMappingTable-queryConstraints"></a>
The query constraints of the analysis rule ID mapping table.
Type: Array of [QueryConstraint](API_QueryConstraint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: Yes

 ** dimensionColumns **   <a name="API-Type-AnalysisRuleIdMappingTable-dimensionColumns"></a>
The columns that query runners are allowed to select, group by, or filter by.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: No

## See Also
<a name="API_AnalysisRuleIdMappingTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisRuleIdMappingTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisRuleIdMappingTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisRuleIdMappingTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
