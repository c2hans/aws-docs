---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdMarkerPassthrough.html
---

# AdMarkerPassthrough
<a name="API_AdMarkerPassthrough"></a>

For HLS, when set to `true`, MediaTailor passes through `EXT-X-CUE-IN`, `EXT-X-CUE-OUT`, and `EXT-X-SPLICEPOINT-SCTE35` ad markers from the origin manifest to the MediaTailor personalized manifest.

No logic is applied to these ad markers. For example, if `EXT-X-CUE-OUT` has a value of `60`, but no ads are filled for that ad break, MediaTailor will not set the value to `0`.

## Contents
<a name="API_AdMarkerPassthrough_Contents"></a>

 ** Enabled **   <a name="mediatailor-Type-AdMarkerPassthrough-Enabled"></a>
Enables ad marker passthrough for your configuration.
Type: Boolean
Required: No

## See Also
<a name="API_AdMarkerPassthrough_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AdMarkerPassthrough)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AdMarkerPassthrough)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AdMarkerPassthrough)
