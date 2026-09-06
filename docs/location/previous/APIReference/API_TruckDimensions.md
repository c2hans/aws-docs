---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_TruckDimensions.html
---

# TruckDimensions
<a name="API_TruckDimensions"></a>

Contains details about the truck dimensions in the unit of measurement that you specify. Used to filter out roads that can't support or allow the specified dimensions for requests that specify `TravelMode` as `Truck`.

## Contents
<a name="API_TruckDimensions_Contents"></a>

 ** Height **   <a name="location-Type-TruckDimensions-Height"></a>
The height of the truck.
+ For example, `4.5`.
 For routes calculated with a HERE resource, this value must be between 0 and 50 meters.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** Length **   <a name="location-Type-TruckDimensions-Length"></a>
The length of the truck.
+ For example, `15.5`.
 For routes calculated with a HERE resource, this value must be between 0 and 300 meters.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** Unit **   <a name="location-Type-TruckDimensions-Unit"></a>
 Specifies the unit of measurement for the truck dimensions.
Default Value: `Meters`
Type: String
Valid Values: `Meters | Feet`
Required: No

 ** Width **   <a name="location-Type-TruckDimensions-Width"></a>
The width of the truck.
+ For example, `4.5`.
 For routes calculated with a HERE resource, this value must be between 0 and 50 meters.
Type: Double
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_TruckDimensions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/TruckDimensions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/TruckDimensions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/TruckDimensions)
