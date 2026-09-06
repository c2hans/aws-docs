---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AggregationConstraint.html
---

# AggregationConstraint
<a name="API_AggregationConstraint"></a>

Constraint on query output removing output rows that do not meet a minimum number of distinct values of a specified column.

## Contents
<a name="API_AggregationConstraint_Contents"></a>

 ** columnName **   <a name="API-Type-AggregationConstraint-columnName"></a>
Column in aggregation constraint for which there must be a minimum number of distinct values in an output row for it to be in the query output.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** minimum **   <a name="API-Type-AggregationConstraint-minimum"></a>
The minimum number of distinct values that an output row must be an aggregation of. Minimum threshold of distinct values for a specified column that must exist in an output row for it to be in the query output.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 100000.
Required: Yes

 ** type **   <a name="API-Type-AggregationConstraint-type"></a>
The type of aggregation the constraint allows. The only valid value is currently `COUNT\_DISTINCT`.
Type: String
Valid Values: `COUNT_DISTINCT`
Required: Yes

## See Also
<a name="API_AggregationConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AggregationConstraint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AggregationConstraint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AggregationConstraint)
