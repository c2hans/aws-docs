---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_TrafficShapingRetrievalWindow.html
---

# TrafficShapingRetrievalWindow
<a name="API_TrafficShapingRetrievalWindow"></a>

The configuration that tells AWS Elemental MediaTailor how many seconds to spread out requests to the ad decision server (ADS). Instead of sending ADS requests for all sessions at the same time, MediaTailor spreads the requests across the amount of time specified in the retrieval window.

## Contents
<a name="API_TrafficShapingRetrievalWindow_Contents"></a>

 ** RetrievalWindowDurationSeconds **   <a name="mediatailor-Type-TrafficShapingRetrievalWindow-RetrievalWindowDurationSeconds"></a>
The amount of time, in seconds, that MediaTailor spreads prefetch requests to the ADS.
Type: Integer
Required: No

## See Also
<a name="API_TrafficShapingRetrievalWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/TrafficShapingRetrievalWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/TrafficShapingRetrievalWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/TrafficShapingRetrievalWindow)
