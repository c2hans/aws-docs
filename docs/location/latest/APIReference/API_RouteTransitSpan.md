---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransitSpan.html
---

# RouteTransitSpan
<a name="API_RouteTransitSpan"></a>

Span computed for the requested SpanAdditionalFeatures.

## Contents
<a name="API_RouteTransitSpan_Contents"></a>

 ** Country **   <a name="location-Type-RouteTransitSpan-Country"></a>
3 letter Country code corresponding to the Span.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

 ** Distance **   <a name="location-Type-RouteTransitSpan-Distance"></a>
Distance of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.
 **Unit**: `meters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Duration **   <a name="location-Type-RouteTransitSpan-Duration"></a>
Duration of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** GeometryOffset **   <a name="location-Type-RouteTransitSpan-GeometryOffset"></a>
Offset in the leg geometry corresponding to the start of this span.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Names **   <a name="location-Type-RouteTransitSpan-Names"></a>
Names of the transit span in available languages.
Type: Array of [LocalizedString](API_LocalizedString.md) objects
Required: No

 ** Region **   <a name="location-Type-RouteTransitSpan-Region"></a>
2-3 letter Region code corresponding to the Span. This is either a province or a state.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3.
Required: No

## See Also
<a name="API_RouteTransitSpan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTransitSpan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTransitSpan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTransitSpan)
