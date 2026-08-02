---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NamedEntityDefinitionMetric.html
---

# NamedEntityDefinitionMetric
<a name="API_NamedEntityDefinitionMetric"></a>

A structure that represents a metric.

## Contents
<a name="API_NamedEntityDefinitionMetric_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Aggregation **   <a name="QS-Type-NamedEntityDefinitionMetric-Aggregation"></a>
The aggregation of a named entity. Valid values for this structure are `SUM`, `MIN`, `MAX`, `COUNT`, `AVERAGE`, `DISTINCT_COUNT`, `STDEV`, `STDEVP`, `VAR`, `VARP`, `PERCENTILE`, `MEDIAN`, and `CUSTOM`.
Type: String
Valid Values: `SUM | MIN | MAX | COUNT | AVERAGE | DISTINCT_COUNT | STDEV | STDEVP | VAR | VARP | PERCENTILE | MEDIAN | CUSTOM`
Required: No

 ** AggregationFunctionParameters **   <a name="QS-Type-NamedEntityDefinitionMetric-AggregationFunctionParameters"></a>
The additional parameters for an aggregation function.
Type: String to string map
Key Length Constraints: Maximum length of 256.
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_NamedEntityDefinitionMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NamedEntityDefinitionMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NamedEntityDefinitionMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NamedEntityDefinitionMetric)
