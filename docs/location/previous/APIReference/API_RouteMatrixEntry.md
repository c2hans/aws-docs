---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_RouteMatrixEntry.html
---

# RouteMatrixEntry
<a name="API_RouteMatrixEntry"></a>

The result for the calculated route of one `DeparturePosition` `DestinationPosition` pair.

## Contents
<a name="API_RouteMatrixEntry_Contents"></a>

 ** Distance **   <a name="location-Type-RouteMatrixEntry-Distance"></a>
The total distance of travel for the route.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** DurationSeconds **   <a name="location-Type-RouteMatrixEntry-DurationSeconds"></a>
The expected duration of travel for the route.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** Error **   <a name="location-Type-RouteMatrixEntry-Error"></a>
An error corresponding to the calculation of a route between the `DeparturePosition` and `DestinationPosition`.
Type: [RouteMatrixEntryError](API_RouteMatrixEntryError.md) object
Required: No

## See Also
<a name="API_RouteMatrixEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/RouteMatrixEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/RouteMatrixEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/RouteMatrixEntry)
