---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MetricCategory.html
---

# MetricCategory
<a name="API_MetricCategory"></a>

Describes a metric category. A metric category is a set of additional metrics that you can associate with an instance that has detailed monitoring enabled.

## Contents
<a name="API_MetricCategory_Contents"></a>

 ** metricCategoryId **
The ID of the metric category.
Type: String
Required: No

 ** MetricSet.N **
The names of the metrics in the metric category.
Type: Array of strings
Required: No

 ** TagSet.N **
Any tags assigned to the metric category.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_MetricCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/MetricCategory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/MetricCategory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/MetricCategory)
