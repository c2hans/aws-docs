---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixScooterOptions.html
---

# RouteMatrixScooterOptions
<a name="API_RouteMatrixScooterOptions"></a>

Travel mode options when the provided travel mode is `Scooter`.

## Contents
<a name="API_RouteMatrixScooterOptions_Contents"></a>

 ** LicensePlate **   <a name="location-Type-RouteMatrixScooterOptions-LicensePlate"></a>
The vehicle License Plate.
Type: [RouteMatrixVehicleLicensePlate](API_RouteMatrixVehicleLicensePlate.md) object
Required: No

 ** MaxSpeed **   <a name="location-Type-RouteMatrixScooterOptions-MaxSpeed"></a>
Maximum speed.
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 3.6. Maximum value of 252.0.
Required: No

 ** Occupancy **   <a name="location-Type-RouteMatrixScooterOptions-Occupancy"></a>
The number of occupants in the vehicle.
Default value: `1`
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_RouteMatrixScooterOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixScooterOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixScooterOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixScooterOptions)
