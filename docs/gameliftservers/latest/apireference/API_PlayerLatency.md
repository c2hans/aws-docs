---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PlayerLatency.html
---

# PlayerLatency
<a name="API_PlayerLatency"></a>

Regional latency information for a player, used when requesting a new game session. This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified location (an AWS Region or a custom location for Amazon GameLift Servers Anywhere fleets). The relative difference between a player's latency values for multiple locations are used to determine which fleets are best suited to place a new game session for the player.

## Contents
<a name="API_PlayerLatency_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LatencyInMilliseconds **   <a name="gameliftservers-Type-PlayerLatency-LatencyInMilliseconds"></a>
Amount of time that represents the time lag experienced by the player when connected to the specified Region.
Type: Float
Required: No

 ** PlayerId **   <a name="gameliftservers-Type-PlayerLatency-PlayerId"></a>
A unique identifier for a player associated with the latency data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** RegionIdentifier **   <a name="gameliftservers-Type-PlayerLatency-RegionIdentifier"></a>
Name of the Region or custom location that is associated with the latency value. For Amazon GameLift Servers Anywhere fleets, use the custom location name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_PlayerLatency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PlayerLatency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PlayerLatency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PlayerLatency)
