---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_InferredState.html
---

# InferredState
<a name="API_InferredState"></a>

The inferred state of the device, given the provided position, IP address, cellular signals, and Wi-Fi- access points.

## Contents
<a name="API_InferredState_Contents"></a>

 ** ProxyDetected **   <a name="location-Type-InferredState-ProxyDetected"></a>
Indicates if a proxy was used.
Type: Boolean
Required: Yes

 ** Accuracy **   <a name="location-Type-InferredState-Accuracy"></a>
The level of certainty of the inferred position.
Type: [PositionalAccuracy](API_PositionalAccuracy.md) object
Required: No

 ** DeviationDistance **   <a name="location-Type-InferredState-DeviationDistance"></a>
The distance between the inferred position and the device's self-reported position.
Type: Double
Required: No

 ** Position **   <a name="location-Type-InferredState-Position"></a>
The device position inferred by the provided position, IP address, cellular signals, and Wi-Fi- access points.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

## See Also
<a name="API_InferredState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/InferredState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/InferredState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/InferredState)
