---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SatelliteListItem.html
---

# SatelliteListItem
<a name="API_SatelliteListItem"></a>

Item in a list of satellites.

## Contents
<a name="API_SatelliteListItem_Contents"></a>

 ** currentEphemeris **   <a name="groundstation-Type-SatelliteListItem-currentEphemeris"></a>
The current ephemeris being used to compute the trajectory of the satellite.
Type: [EphemerisMetaData](API_EphemerisMetaData.md) object
Required: No

 ** groundStations **   <a name="groundstation-Type-SatelliteListItem-groundStations"></a>
A list of ground stations to which the satellite is on-boarded.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: No

 ** noradSatelliteID **   <a name="groundstation-Type-SatelliteListItem-noradSatelliteID"></a>
NORAD satellite ID number.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 339999.
Required: No

 ** satelliteArn **   <a name="groundstation-Type-SatelliteListItem-satelliteArn"></a>
ARN of a satellite.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 132.
Pattern: `arn:aws:groundstation:([-a-z0-9]{1,50})?:[0-9]{12}:satellite/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** satelliteId **   <a name="groundstation-Type-SatelliteListItem-satelliteId"></a>
UUID of a satellite.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_SatelliteListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/SatelliteListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/SatelliteListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/SatelliteListItem)
