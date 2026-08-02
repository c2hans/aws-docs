---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ManifestProcessingRules.html
---

# ManifestProcessingRules
<a name="API_ManifestProcessingRules"></a>

The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.

## Contents
<a name="API_ManifestProcessingRules_Contents"></a>

 ** AdMarkerPassthrough **   <a name="mediatailor-Type-ManifestProcessingRules-AdMarkerPassthrough"></a>
For HLS, when set to `true`, MediaTailor passes through `EXT-X-CUE-IN`, `EXT-X-CUE-OUT`, and `EXT-X-SPLICEPOINT-SCTE35` ad markers from the origin manifest to the MediaTailor personalized manifest.
No logic is applied to these ad markers. For example, if `EXT-X-CUE-OUT` has a value of `60`, but no ads are filled for that ad break, MediaTailor will not set the value to `0`.
Type: [AdMarkerPassthrough](API_AdMarkerPassthrough.md) object
Required: No

## See Also
<a name="API_ManifestProcessingRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ManifestProcessingRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ManifestProcessingRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ManifestProcessingRules)
