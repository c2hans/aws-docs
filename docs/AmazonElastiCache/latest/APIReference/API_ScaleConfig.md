---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ScaleConfig.html
---

# ScaleConfig
<a name="API_ScaleConfig"></a>

Configuration settings for horizontal or vertical scaling operations on Memcached clusters.

## Contents
<a name="API_ScaleConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ScaleIntervalMinutes **
The time interval in seconds between scaling operations when performing gradual scaling for a Memcached cluster.
Type: Integer
Required: No

 ** ScalePercentage **
The percentage by which to scale the Memcached cluster, either horizontally by adding nodes or vertically by increasing resources.
Type: Integer
Required: No

## See Also
<a name="API_ScaleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ScaleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ScaleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ScaleConfig)
