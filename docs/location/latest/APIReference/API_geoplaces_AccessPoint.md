---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AccessPoint.html
---

# AccessPoint
<a name="API_geoplaces_AccessPoint"></a>

Position of the access point represented by longitude and latitude for a vehicle.

## Contents
<a name="API_geoplaces_AccessPoint_Contents"></a>

 ** Label **   <a name="location-Type-geoplaces_AccessPoint-Label"></a>
A short textual description of the access point, such as `"North Entrance"`.
Type: String
Required: No

 ** Position **   <a name="location-Type-geoplaces_AccessPoint-Position"></a>
The position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** Primary **   <a name="location-Type-geoplaces_AccessPoint-Primary"></a>
Set to `true` for the primary access position when the place has more than one access point.
Type: Boolean
Required: No

 ** Type **   <a name="location-Type-geoplaces_AccessPoint-Type"></a>
The type of access point, indicating its intended use. Only applies to results of type place.
Type: String
Valid Values: `Delivery | Emergency | Entrance | Loading | Other | Parking | Taxi`
Required: No

## See Also
<a name="API_geoplaces_AccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/AccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/AccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/AccessPoint)
