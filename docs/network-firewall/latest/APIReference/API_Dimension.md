---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Dimension.html
---

# Dimension
<a name="API_Dimension"></a>

The value to use in an Amazon CloudWatch custom metric dimension. This is used in the `PublishMetrics` [CustomAction](API_CustomAction.md). A CloudWatch custom metric dimension is a name/value pair that's part of the identity of a metric.

 AWS Network Firewall sets the dimension name to `CustomAction` and you provide the dimension value.

For more information about CloudWatch custom metric dimensions, see [Publishing Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#usingDimensions) in the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

## Contents
<a name="API_Dimension_Contents"></a>

 ** Value **   <a name="networkfirewall-Type-Dimension-Value"></a>
The value to use in the custom metric dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_ ]+$`
Required: Yes

## See Also
<a name="API_Dimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Dimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Dimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Dimension)
