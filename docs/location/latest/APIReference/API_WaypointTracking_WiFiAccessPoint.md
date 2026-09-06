---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_WiFiAccessPoint.html
---

# WiFiAccessPoint
<a name="API_WaypointTracking_WiFiAccessPoint"></a>

Wi-Fi access point.

## Contents
<a name="API_WaypointTracking_WiFiAccessPoint_Contents"></a>

 ** MacAddress **   <a name="location-Type-WaypointTracking_WiFiAccessPoint-MacAddress"></a>
Medium access control address (Mac).
Type: String
Length Constraints: Minimum length of 12. Maximum length of 17.
Pattern: `([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})`
Required: Yes

 ** Rss **   <a name="location-Type-WaypointTracking_WiFiAccessPoint-Rss"></a>
Received signal strength (dBm) of the WLAN measurement data.
Type: Integer
Valid Range: Minimum value of -128. Maximum value of 0.
Required: Yes

## See Also
<a name="API_WaypointTracking_WiFiAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/WiFiAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/WiFiAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/WiFiAccessPoint)
