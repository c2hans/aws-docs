---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdsPersonalizationTimeouts.html
---

# AdsPersonalizationTimeouts
<a name="API_AdsPersonalizationTimeouts"></a>

The timeout settings for ad decision server interactions during ad personalization.

## Contents
<a name="API_AdsPersonalizationTimeouts_Contents"></a>

 ** AdsRequestTimeoutMilliseconds **   <a name="mediatailor-Type-AdsPersonalizationTimeouts-AdsRequestTimeoutMilliseconds"></a>
The maximum time, in milliseconds, that MediaTailor waits for a single ad decision server response during live or VOD playback. The default is 3000.
Type: Integer
Required: No

 ** LiveMaximumAdsPersonalizationTimeMilliseconds **   <a name="mediatailor-Type-AdsPersonalizationTimeouts-LiveMaximumAdsPersonalizationTimeMilliseconds"></a>
The maximum total time, in milliseconds, that MediaTailor spends on ad decision server activity for live manifests, including making requests, waiting for responses, and following VAST wrapper redirects. The default is 10000.
Type: Integer
Required: No

 ** PrefetchAdsRequestTimeoutMilliseconds **   <a name="mediatailor-Type-AdsPersonalizationTimeouts-PrefetchAdsRequestTimeoutMilliseconds"></a>
The maximum time, in milliseconds, that MediaTailor waits for a single ad decision server response during prefetch retrieval. If not set, the value of AdsRequestTimeoutMilliseconds is used.
Type: Integer
Required: No

 ** PrefetchMaximumAdsPersonalizationTimeMilliseconds **   <a name="mediatailor-Type-AdsPersonalizationTimeouts-PrefetchMaximumAdsPersonalizationTimeMilliseconds"></a>
The maximum total time, in milliseconds, that MediaTailor spends on ad decision server activity during prefetch retrieval, including making requests, waiting for responses, and following VAST wrapper redirects.
Type: Integer
Required: No

 ** VodMaximumAdsPersonalizationTimeMilliseconds **   <a name="mediatailor-Type-AdsPersonalizationTimeouts-VodMaximumAdsPersonalizationTimeMilliseconds"></a>
The maximum total time, in milliseconds, that MediaTailor spends on ad decision server activity for VOD manifests, including making requests, waiting for responses, and following VAST wrapper redirects. The default is 10000.
Type: Integer
Required: No

## See Also
<a name="API_AdsPersonalizationTimeouts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AdsPersonalizationTimeouts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AdsPersonalizationTimeouts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AdsPersonalizationTimeouts)
