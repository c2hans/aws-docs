---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConsolidatedPolicyAggregation.html
---

# ConsolidatedPolicyAggregation
<a name="API_ConsolidatedPolicyAggregation"></a>

 Controls on the analysis specifications that can be run on a configured table.

## Contents
<a name="API_ConsolidatedPolicyAggregation_Contents"></a>

 ** aggregateColumns **   <a name="API-Type-ConsolidatedPolicyAggregation-aggregateColumns"></a>
 Aggregate columns in consolidated policy aggregation.
Type: Array of [AggregateColumn](API_AggregateColumn.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** dimensionColumns **   <a name="API-Type-ConsolidatedPolicyAggregation-dimensionColumns"></a>
 The dimension columns of the consolidated policy aggregation.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** joinColumns **   <a name="API-Type-ConsolidatedPolicyAggregation-joinColumns"></a>
 The columns to join on.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** outputConstraints **   <a name="API-Type-ConsolidatedPolicyAggregation-outputConstraints"></a>
 The output constraints of the consolidated policy aggregation.
Type: Array of [AggregationConstraint](API_AggregationConstraint.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** scalarFunctions **   <a name="API-Type-ConsolidatedPolicyAggregation-scalarFunctions"></a>
 The scalar functions.
Type: Array of strings
Valid Values: `ABS | CAST | CEILING | COALESCE | CONVERT | CURRENT_DATE | DATEADD | EXTRACT | FLOOR | GETDATE | LN | LOG | LOWER | ROUND | RTRIM | SQRT | SUBSTRING | TO_CHAR | TO_DATE | TO_NUMBER | TO_TIMESTAMP | TRIM | TRUNC | UPPER`
Required: Yes

 ** additionalAnalyses **   <a name="API-Type-ConsolidatedPolicyAggregation-additionalAnalyses"></a>
 Additional analyses for the consolidated policy aggregation.
Type: String
Valid Values: `ALLOWED | REQUIRED | NOT_ALLOWED`
Required: No

 ** allowedAdditionalAnalyses **   <a name="API-Type-ConsolidatedPolicyAggregation-allowedAdditionalAnalyses"></a>
 The additional analyses allowed by the consolidated policy aggregation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
Required: No

 ** allowedJoinOperators **   <a name="API-Type-ConsolidatedPolicyAggregation-allowedJoinOperators"></a>
 The allowed join operators.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `OR | AND`
Required: No

 ** allowedResultReceivers **   <a name="API-Type-ConsolidatedPolicyAggregation-allowedResultReceivers"></a>
 The allowed result receivers.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** joinRequired **   <a name="API-Type-ConsolidatedPolicyAggregation-joinRequired"></a>
 Join required
Type: String
Valid Values: `QUERY_RUNNER`
Required: No

## See Also
<a name="API_ConsolidatedPolicyAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConsolidatedPolicyAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConsolidatedPolicyAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConsolidatedPolicyAggregation)
