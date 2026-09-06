---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteLeg.html
---

# RouteLeg
<a name="API_RouteLeg"></a>

A leg is a section of a route from one waypoint to the next. A leg could be of type Vehicle, Pedestrian or Ferry. Legs of different types could occur together within a single route. For example, a car employing the use of a Ferry will contain Vehicle legs corresponding to journey on land, and Ferry legs corresponding to the journey via Ferry.

## Contents
<a name="API_RouteLeg_Contents"></a>

 ** Geometry **   <a name="location-Type-RouteLeg-Geometry"></a>
Geometry of the area to be avoided.
Type: [RouteLegGeometry](API_RouteLegGeometry.md) object
Required: Yes

 ** TravelMode **   <a name="location-Type-RouteLeg-TravelMode"></a>
Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.
Default value: `Car`
Type: String
Valid Values: `Car | Ferry | Pedestrian | Scooter | Truck | CarShuttleTrain | AerialTramway | Airplane | Bus | BusRapidTransit | CityTrain | FunicularRailway | HighSpeedTrain | IntercityTrain | InterregionalTrain | LightRail | Monorail | PrivateBus | RegionalTrain | Subway`
Required: Yes

 ** Type **   <a name="location-Type-RouteLeg-Type"></a>
Type of the leg.
Type: String
Valid Values: `Ferry | Pedestrian | Vehicle | Rental | Taxi | Transit`
Required: Yes

 ** FerryLegDetails **   <a name="location-Type-RouteLeg-FerryLegDetails"></a>
 FerryLegDetails is populated when the Leg type is Ferry, and provides additional information that is specific to ferry travel. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteFerryLegDetails](API_RouteFerryLegDetails.md) object
Required: No

 ** Language **   <a name="location-Type-RouteLeg-Language"></a>
 List of languages for instructions within steps in the response. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** PedestrianLegDetails **   <a name="location-Type-RouteLeg-PedestrianLegDetails"></a>
Details related to the pedestrian leg.
Type: [RoutePedestrianLegDetails](API_RoutePedestrianLegDetails.md) object
Required: No

 ** RentalLegDetails **   <a name="location-Type-RouteLeg-RentalLegDetails"></a>
Details related to the rental leg.
Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteRentalLegDetails](API_RouteRentalLegDetails.md) object
Required: No

 ** TaxiLegDetails **   <a name="location-Type-RouteLeg-TaxiLegDetails"></a>
Details related to the taxi leg.
Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteTaxiLegDetails](API_RouteTaxiLegDetails.md) object
Required: No

 ** TransitLegDetails **   <a name="location-Type-RouteLeg-TransitLegDetails"></a>
Details related to the transit leg.
Type: [RouteTransitLegDetails](API_RouteTransitLegDetails.md) object
Required: No

 ** VehicleLegDetails **   <a name="location-Type-RouteLeg-VehicleLegDetails"></a>
Details related to the vehicle leg.
Type: [RouteVehicleLegDetails](API_RouteVehicleLegDetails.md) object
Required: No

## See Also
<a name="API_RouteLeg_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteLeg)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteLeg)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteLeg)
