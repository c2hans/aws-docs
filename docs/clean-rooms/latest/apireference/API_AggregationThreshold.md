---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AggregationThreshold.html
---

# AggregationThreshold
<a name="API_AggregationThreshold"></a>

Specifies the minimum number of distinct identities that each query output group must represent.

## Contents
<a name="API_AggregationThreshold_Contents"></a>

 ** allowedAggregateExpressionType **   <a name="API-Type-AggregationThreshold-allowedAggregateExpressionType"></a>
Specifies whether a query can aggregate a transformed column. This applies to the arguments of both aggregate and window functions. Valid values are:
 `COLUMNS_ONLY` – A query can aggregate only a direct column reference, such as `SUM(amount)`, or a constant. AWS Clean Rooms rejects a query that transforms a column and then aggregates it, such as `SUM(amount * 2)` or `SUM(ROUND(amount))`.
 `ANY_EXPRESSION` – A query can aggregate any expression. This includes arithmetic, such as `SUM(price * quantity)`; a cast, such as `SUM(CAST(amount AS DECIMAL))`; a nested function call, such as `SUM(COALESCE(amount, 0))`; and a conditional, such as `SUM(CASE WHEN region = 'EU' THEN amount ELSE 0 END)`.
Type: String
Valid Values: `COLUMNS_ONLY | ANY_EXPRESSION`
Required: Yes

 ** identityColumns **   <a name="API-Type-AggregationThreshold-identityColumns"></a>
The identity column, such as `user_id`, whose distinct values AWS Clean Rooms counts to enforce minimum aggregation thresholds. Currently, you can specify only one column, and its data type must be string, varchar, or char.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** minimumIdentityCount **   <a name="API-Type-AggregationThreshold-minimumIdentityCount"></a>
The minimum number of distinct identities that each query output group must represent. This threshold applies to all output columns in the table. To override this threshold for a specific column, use `outputColumnThresholds`.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 100000.
Required: Yes

 ** type **   <a name="API-Type-AggregationThreshold-type"></a>
The type of aggregation that the threshold enforces. Currently, the only supported value is `COUNT_DISTINCT`, which counts the distinct values in the identity column.
Type: String
Valid Values: `COUNT_DISTINCT`
Required: Yes

 ** outputColumnThresholds **   <a name="API-Type-AggregationThreshold-outputColumnThresholds"></a>
The per-column overrides of `minimumIdentityCount`. An output column without an override uses `minimumIdentityCount`.
Type: Array of [OutputColumnThreshold](API_OutputColumnThreshold.md) objects
Required: No

## See Also
<a name="API_AggregationThreshold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AggregationThreshold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AggregationThreshold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AggregationThreshold)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
