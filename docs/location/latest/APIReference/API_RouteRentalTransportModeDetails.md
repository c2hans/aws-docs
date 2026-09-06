---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRentalTransportModeDetails.html
---

# RouteRentalTransportModeDetails
<a name="API_RouteRentalTransportModeDetails"></a>

Transport mode details for the rental leg.

## Contents
<a name="API_RouteRentalTransportModeDetails_Contents"></a>

 ** Mode **   <a name="location-Type-RouteRentalTransportModeDetails-Mode"></a>
Mode of the rental transport.
Type: String
Valid Values: `All | Car`
Required: Yes

 ** AvailableSeats **   <a name="location-Type-RouteRentalTransportModeDetails-AvailableSeats"></a>
Number of available seats in the vehicle.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Category **   <a name="location-Type-RouteRentalTransportModeDetails-Category"></a>
Human readable transport category.
Type: String
Required: No

 ** Color **   <a name="location-Type-RouteRentalTransportModeDetails-Color"></a>
Color of the transport polyline and background for the transport name.
Type: String
Required: No

 ** Engine **   <a name="location-Type-RouteRentalTransportModeDetails-Engine"></a>
Vehicle engine type.
Type: String
Valid Values: `Electric | InternalCombustion | PluginHybrid`
Required: No

 ** LicensePlate **   <a name="location-Type-RouteRentalTransportModeDetails-LicensePlate"></a>
Vehicle license plate number.
Type: String
Required: No

 ** Model **   <a name="location-Type-RouteRentalTransportModeDetails-Model"></a>
Vehicle model.
Type: String
Required: No

 ** Name **   <a name="location-Type-RouteRentalTransportModeDetails-Name"></a>
Vehicle name or mobility provider name.
Type: String
Required: No

 ** TextColor **   <a name="location-Type-RouteRentalTransportModeDetails-TextColor"></a>
Color of the transport name text.
Type: String
Required: No

## See Also
<a name="API_RouteRentalTransportModeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteRentalTransportModeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteRentalTransportModeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteRentalTransportModeDetails)
