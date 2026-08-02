---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_Player.html
---

# Player
<a name="API_Player"></a>

Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.

## Contents
<a name="API_Player_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LatencyInMs **   <a name="gameliftservers-Type-Player-LatencyInMs"></a>
A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to a fleet location (AWS Regions or custom locations for Amazon GameLift Servers Anywhere fleets). If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.
If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.
To collect accurate latency data, use Amazon GameLift Servers's UDP ping beacons, which provide fixed endpoints in each Amazon GameLift Servers hosting location. These endpoints allow you to measure actual UDP network latency, which provides more accurate results than ICMP pings because UDP is the same protocol used by most game servers. For more information on using UDP ping beacons to measure latency, refer to [UDP ping beacons](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-udp-ping-beacons.html) in the Amazon GameLift Servers Developer Guide.
Type: String to integer map
Key Length Constraints: Minimum length of 1.
Valid Range: Minimum value of 1.
Required: No

 ** PlayerAttributes **   <a name="gameliftservers-Type-Player-PlayerAttributes"></a>
A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example: `"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}}`.
You can provide up to 10 `PlayerAttributes`.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PlayerId **   <a name="gameliftservers-Type-Player-PlayerId"></a>
A unique identifier for a player
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Team **   <a name="gameliftservers-Type-Player-Team"></a>
Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_Player_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/Player)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/Player)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/Player)
