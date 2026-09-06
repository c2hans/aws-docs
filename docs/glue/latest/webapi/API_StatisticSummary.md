---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StatisticSummary.html
---

# StatisticSummary
<a name="API_StatisticSummary"></a>

Summary information about a statistic.

## Contents
<a name="API_StatisticSummary_Contents"></a>

 ** ColumnsReferenced **   <a name="Glue-Type-StatisticSummary-ColumnsReferenced"></a>
The list of columns referenced by the statistic.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** DoubleValue **   <a name="Glue-Type-StatisticSummary-DoubleValue"></a>
The value of the statistic.
Type: Double
Required: No

 ** EvaluationLevel **   <a name="Glue-Type-StatisticSummary-EvaluationLevel"></a>
The evaluation level of the statistic. Possible values: `Dataset`, `Column`, `Multicolumn`.
Type: String
Valid Values: `Dataset | Column | Multicolumn`
Required: No

 ** InclusionAnnotation **   <a name="Glue-Type-StatisticSummary-InclusionAnnotation"></a>
The inclusion annotation for the statistic.
Type: [TimestampedInclusionAnnotation](API_TimestampedInclusionAnnotation.md) object
Required: No

 ** ProfileId **   <a name="Glue-Type-StatisticSummary-ProfileId"></a>
The Profile ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RecordedOn **   <a name="Glue-Type-StatisticSummary-RecordedOn"></a>
The timestamp when the statistic was recorded.
Type: Timestamp
Required: No

 ** ReferencedDatasets **   <a name="Glue-Type-StatisticSummary-ReferencedDatasets"></a>
The list of datasets referenced by the statistic.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RunIdentifier **   <a name="Glue-Type-StatisticSummary-RunIdentifier"></a>
The Run Identifier
Type: [RunIdentifier](API_RunIdentifier.md) object
Required: No

 ** StatisticId **   <a name="Glue-Type-StatisticSummary-StatisticId"></a>
The Statistic ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StatisticName **   <a name="Glue-Type-StatisticSummary-StatisticName"></a>
The name of the statistic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Z][A-Za-z\.]+`
Required: No

 ** StatisticProperties **   <a name="Glue-Type-StatisticSummary-StatisticProperties"></a>
A `StatisticPropertiesMap`, which contains a `NameString` and `DescriptionString`
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_StatisticSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StatisticSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StatisticSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StatisticSummary)
