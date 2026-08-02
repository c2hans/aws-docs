---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollPass.html
---

# RouteTollPass
<a name="API_RouteTollPass"></a>

Details if the toll rate can be a pass that supports multiple trips.

## Contents
<a name="API_RouteTollPass_Contents"></a>

 ** IncludesReturnTrip **   <a name="location-Type-RouteTollPass-IncludesReturnTrip"></a>
If the pass includes the rate for the return leg of the trip.
Type: Boolean
Required: No

 ** SeniorPass **   <a name="location-Type-RouteTollPass-SeniorPass"></a>
If the pass is only valid for senior persons.
Type: Boolean
Required: No

 ** TransferCount **   <a name="location-Type-RouteTollPass-TransferCount"></a>
If the toll pass can be transferred, and how many times.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TripCount **   <a name="location-Type-RouteTollPass-TripCount"></a>
Number of trips the pass is valid for.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ValidityPeriod **   <a name="location-Type-RouteTollPass-ValidityPeriod"></a>
Period for which the pass is valid.
Type: [RouteTollPassValidityPeriod](API_RouteTollPassValidityPeriod.md) object
Required: No

## See Also
<a name="API_RouteTollPass_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTollPass)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTollPass)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTollPass)
