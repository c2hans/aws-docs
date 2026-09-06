---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdsPersonalizationConcurrency.html
---

# AdsPersonalizationConcurrency
<a name="API_AdsPersonalizationConcurrency"></a>

The concurrency settings for ad decision server interactions during ad personalization.

## Contents
<a name="API_AdsPersonalizationConcurrency_Contents"></a>

 ** EnableVodVastParallelization **   <a name="mediatailor-Type-AdsPersonalizationConcurrency-EnableVodVastParallelization"></a>
Enables parallel processing of ad decision server requests in VOD workflows when the ADS returns VAST responses. The default is false.
Type: Boolean
Required: No

 ** MaxConcurrentAdsRequests **   <a name="mediatailor-Type-AdsPersonalizationConcurrency-MaxConcurrentAdsRequests"></a>
The maximum number of simultaneous requests that MediaTailor makes to the ad decision server per manifest request. The default is 1.
Type: Integer
Required: No

## See Also
<a name="API_AdsPersonalizationConcurrency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AdsPersonalizationConcurrency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AdsPersonalizationConcurrency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AdsPersonalizationConcurrency)
