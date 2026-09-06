---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricSpecification.html
---

# MetricSpecification
<a name="API_MetricSpecification"></a>

An object containing information about a metric.

## Contents
<a name="API_MetricSpecification_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Customized **   <a name="sagemaker-Type-MetricSpecification-Customized"></a>
Information about a customized metric.
Type: [CustomizedMetricSpecification](API_CustomizedMetricSpecification.md) object
Required: No

 ** Predefined **   <a name="sagemaker-Type-MetricSpecification-Predefined"></a>
Information about a predefined metric.
Type: [PredefinedMetricSpecification](API_PredefinedMetricSpecification.md) object
Required: No

## See Also
<a name="API_MetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MetricSpecification)
