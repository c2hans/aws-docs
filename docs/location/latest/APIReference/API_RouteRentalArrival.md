---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRentalArrival.html
---

# RouteRentalArrival
<a name="API_RouteRentalArrival"></a>

Details corresponding to the arrival for the leg.

## Contents
<a name="API_RouteRentalArrival_Contents"></a>

 ** Place **   <a name="location-Type-RouteRentalArrival-Place"></a>
Place details corresponding to the arrival.
Type: [RouteRentalPlace](API_RouteRentalPlace.md) object
Required: Yes

 ** Time **   <a name="location-Type-RouteRentalArrival-Time"></a>
The arrival time.
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

## See Also
<a name="API_RouteRentalArrival_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteRentalArrival)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteRentalArrival)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteRentalArrival)
