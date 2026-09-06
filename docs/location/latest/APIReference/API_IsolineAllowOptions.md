---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineAllowOptions.html
---

# IsolineAllowOptions
<a name="API_IsolineAllowOptions"></a>

Special road types or features that should be considered available for routing. For example, this attribute can be used to allow the use of HOV (high-occupancy vehicle) or HOT (high-occupancy toll) lanes, even if they would otherwise not be.

## Contents
<a name="API_IsolineAllowOptions_Contents"></a>

 ** Hot **   <a name="location-Type-IsolineAllowOptions-Hot"></a>
When true, allows the use of HOT (high-occupancy toll) lanes, which may affect travel times and reachable areas.
Default value: `false`
Type: Boolean
Required: No

 ** Hov **   <a name="location-Type-IsolineAllowOptions-Hov"></a>
When true, allows the use of HOV (high-occupancy vehicle) lanes, which may affect travel times and reachable areas.
Default value: `false`
Type: Boolean
Required: No

## See Also
<a name="API_IsolineAllowOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineAllowOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineAllowOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineAllowOptions)
