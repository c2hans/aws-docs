---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_TrafficShapingTpsConfiguration.html
---

# TrafficShapingTpsConfiguration
<a name="API_TrafficShapingTpsConfiguration"></a>

The configuration for TPS-based traffic shaping. This approach limits requests to the ad decision server (ADS) based on transactions per second and concurrent users.

## Contents
<a name="API_TrafficShapingTpsConfiguration_Contents"></a>

 ** PeakConcurrentUsers **   <a name="mediatailor-Type-TrafficShapingTpsConfiguration-PeakConcurrentUsers"></a>
The expected peak number of concurrent viewers for your content. MediaTailor uses this value along with peak TPS to determine how to distribute prefetch requests across the available capacity without exceeding your ADS limits.
Type: Integer
Required: No

 ** PeakTps **   <a name="mediatailor-Type-TrafficShapingTpsConfiguration-PeakTps"></a>
The maximum number of transactions per second (TPS) that your ad decision server (ADS) can handle. MediaTailor uses this value along with concurrent users and headroom multiplier to calculate optimal traffic distribution and prevent ADS overload.
Type: Integer
Required: No

## See Also
<a name="API_TrafficShapingTpsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/TrafficShapingTpsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/TrafficShapingTpsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/TrafficShapingTpsConfiguration)
