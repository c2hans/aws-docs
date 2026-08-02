---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationConnection.html
---

# WaypointOptimizationConnection
<a name="API_WaypointOptimizationConnection"></a>

This contains information such as distance and duration from one waypoint to the next waypoint in the sequence.

## Contents
<a name="API_WaypointOptimizationConnection_Contents"></a>

 ** Distance **   <a name="location-Type-WaypointOptimizationConnection-Distance"></a>
Distance of the step.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** From **   <a name="location-Type-WaypointOptimizationConnection-From"></a>
contains the ID of the starting waypoint in this connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^,;!]+`
Required: Yes

 ** RestDuration **   <a name="location-Type-WaypointOptimizationConnection-RestDuration"></a>
Resting time before the driver can continue driving.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** To **   <a name="location-Type-WaypointOptimizationConnection-To"></a>
Contains the ID of the ending waypoint in this connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^,;!]+`
Required: Yes

 ** TravelDuration **   <a name="location-Type-WaypointOptimizationConnection-TravelDuration"></a>
Total duration.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** WaitDuration **   <a name="location-Type-WaypointOptimizationConnection-WaitDuration"></a>
Duration of a wait step.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

## See Also
<a name="API_WaypointOptimizationConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationConnection)
