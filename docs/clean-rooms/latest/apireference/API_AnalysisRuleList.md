---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisRuleList.html
---

# AnalysisRuleList
<a name="API_AnalysisRuleList"></a>

A type of analysis rule that enables row-level analysis.

## Contents
<a name="API_AnalysisRuleList_Contents"></a>

 ** joinColumns **   <a name="API-Type-AnalysisRuleList-joinColumns"></a>
Columns that can be used to join a configured table with the table of the member who can query and other members' configured tables.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** listColumns **   <a name="API-Type-AnalysisRuleList-listColumns"></a>
Columns that can be listed in the output.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** additionalAnalyses **   <a name="API-Type-AnalysisRuleList-additionalAnalyses"></a>
 An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.
Type: String
Valid Values: `ALLOWED | REQUIRED | NOT_ALLOWED`
Required: No

 ** allowedJoinOperators **   <a name="API-Type-AnalysisRuleList-allowedJoinOperators"></a>
The logical operators (if any) that are to be used in an INNER JOIN match condition. Default is `AND`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `OR | AND`
Required: No

## See Also
<a name="API_AnalysisRuleList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisRuleList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisRuleList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisRuleList)
