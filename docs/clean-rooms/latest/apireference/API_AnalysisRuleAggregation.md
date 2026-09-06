---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisRuleAggregation.html
---

# AnalysisRuleAggregation
<a name="API_AnalysisRuleAggregation"></a>

A type of analysis rule that enables query structure and specified queries that produce aggregate statistics.

## Contents
<a name="API_AnalysisRuleAggregation_Contents"></a>

 ** aggregateColumns **   <a name="API-Type-AnalysisRuleAggregation-aggregateColumns"></a>
The columns that query runners are allowed to use in aggregation queries.
Type: Array of [AggregateColumn](API_AggregateColumn.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** dimensionColumns **   <a name="API-Type-AnalysisRuleAggregation-dimensionColumns"></a>
The columns that query runners are allowed to select, group by, or filter by.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** joinColumns **   <a name="API-Type-AnalysisRuleAggregation-joinColumns"></a>
Columns in configured table that can be used in join statements and/or as aggregate columns. They can never be outputted directly.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** outputConstraints **   <a name="API-Type-AnalysisRuleAggregation-outputConstraints"></a>
Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.
Type: Array of [AggregationConstraint](API_AggregationConstraint.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** scalarFunctions **   <a name="API-Type-AnalysisRuleAggregation-scalarFunctions"></a>
Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.
Type: Array of strings
Valid Values: `ABS | CAST | CEILING | COALESCE | CONVERT | CURRENT_DATE | DATEADD | EXTRACT | FLOOR | GETDATE | LN | LOG | LOWER | ROUND | RTRIM | SQRT | SUBSTRING | TO_CHAR | TO_DATE | TO_NUMBER | TO_TIMESTAMP | TRIM | TRUNC | UPPER`
Required: Yes

 ** additionalAnalyses **   <a name="API-Type-AnalysisRuleAggregation-additionalAnalyses"></a>
 An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.
The `additionalAnalyses` parameter is currently supported for the list analysis rule (`AnalysisRuleList`) and the custom analysis rule (`AnalysisRuleCustom`).
Type: String
Valid Values: `ALLOWED | REQUIRED | NOT_ALLOWED`
Required: No

 ** allowedJoinOperators **   <a name="API-Type-AnalysisRuleAggregation-allowedJoinOperators"></a>
Which logical operators (if any) are to be used in an INNER JOIN match condition. Default is `AND`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `OR | AND`
Required: No

 ** joinRequired **   <a name="API-Type-AnalysisRuleAggregation-joinRequired"></a>
Control that requires member who runs query to do a join with their configured table and/or other configured table in query.
Type: String
Valid Values: `QUERY_RUNNER`
Required: No

## See Also
<a name="API_AnalysisRuleAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisRuleAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisRuleAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisRuleAggregation)
