---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineTravelModeOptions.html
---

# IsolineTravelModeOptions
<a name="API_IsolineTravelModeOptions"></a>

Mode-specific routing options that further refine how reachable areas are calculated. Options are only considered when they match the selected travel mode.

## Contents
<a name="API_IsolineTravelModeOptions_Contents"></a>

 ** Car **   <a name="location-Type-IsolineTravelModeOptions-Car"></a>
Options specific to passenger vehicle routing (`Car`, such as vehicle characteristics and license plate restrictions.
Type: [IsolineCarOptions](API_IsolineCarOptions.md) object
Required: No

 ** Scooter **   <a name="location-Type-IsolineTravelModeOptions-Scooter"></a>
Options specific to scooter routing (`Scooter`, such as vehicle characteristics and license plate restrictions.
When using the `Scooter` travel mode, controlled-access highways are automatically avoided unless explicitly allowed.
Type: [IsolineScooterOptions](API_IsolineScooterOptions.md) object
Required: No

 ** Truck **   <a name="location-Type-IsolineTravelModeOptions-Truck"></a>
Options specific to commercial truck routing (`Truck`, including vehicle dimensions, weight limits, and hazardous cargo specifications.
Type: [IsolineTruckOptions](API_IsolineTruckOptions.md) object
Required: No

## See Also
<a name="API_IsolineTravelModeOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineTravelModeOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineTravelModeOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineTravelModeOptions)
