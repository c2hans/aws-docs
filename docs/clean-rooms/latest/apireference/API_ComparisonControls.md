---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ComparisonControls.html
---

# ComparisonControls
<a name="API_ComparisonControls"></a>

Specifies how a query can compare the columns in a table, including literal comparisons and column-to-column comparisons.

## Contents
<a name="API_ComparisonControls_Contents"></a>

 ** allowedColumnComparisonColumns **   <a name="API-Type-ComparisonControls-allowedColumnComparisonColumns"></a>
The columns that a query can compare to another column, for example, in a join, a WHERE clause, a GROUP BY clause, or a window function. AWS Clean Rooms rejects a query that uses any other column in a column-to-column comparison. Specify an empty list to block column-to-column comparison on every column.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** allowedLiteralComparisonColumns **   <a name="API-Type-ComparisonControls-allowedLiteralComparisonColumns"></a>
The columns that a query can compare to literal values, for example, in a WHERE clause. AWS Clean Rooms rejects a query that compares any other column to a literal value. Specify an empty list to block literal comparison on every column. You can't specify a column that you also use as an identity column in an aggregation threshold.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

## See Also
<a name="API_ComparisonControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ComparisonControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ComparisonControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ComparisonControls)
