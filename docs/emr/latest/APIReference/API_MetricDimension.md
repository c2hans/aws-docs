---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_MetricDimension.html
---

# MetricDimension
<a name="API_MetricDimension"></a>

A CloudWatch dimension, which is specified using a `Key` (known as a `Name` in CloudWatch), `Value` pair. By default, Amazon EMR uses one dimension whose `Key` is `JobFlowID` and `Value` is a variable representing the cluster ID, which is `${emr.clusterId}`. This enables the rule to bootstrap when the cluster ID becomes available.

## Contents
<a name="API_MetricDimension_Contents"></a>

 ** Key **   <a name="EMR-Type-MetricDimension-Key"></a>
The dimension name.
Type: String
Required: No

 ** Value **   <a name="EMR-Type-MetricDimension-Value"></a>
The dimension value.
Type: String
Required: No

## See Also
<a name="API_MetricDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/MetricDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/MetricDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/MetricDimension)
