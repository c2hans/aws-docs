---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityObservation.html
---

# DataQualityObservation
<a name="API_DataQualityObservation"></a>

Describes the observation generated after evaluating the rules and analyzers.

## Contents
<a name="API_DataQualityObservation_Contents"></a>

 ** Description **   <a name="Glue-Type-DataQualityObservation-Description"></a>
A description of the data quality observation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MetricBasedObservation **   <a name="Glue-Type-DataQualityObservation-MetricBasedObservation"></a>
An object of type `MetricBasedObservation` representing the observation that is based on evaluated data quality metrics.
Type: [MetricBasedObservation](API_MetricBasedObservation.md) object
Required: No

## See Also
<a name="API_DataQualityObservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityObservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityObservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityObservation)
