---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameSessionPlacement.html
---

# GameSessionPlacement
<a name="API_GameSessionPlacement"></a>

Represents a potential game session placement, including the full details of the original placement request and the current status.

**Note**
If the game session placement status is `PENDING`, the properties for game session ID/ARN, region, IP address/DNS, and port aren't final. A game session is not active and ready to accept players until placement status reaches `FULFILLED`. When the placement is in `PENDING` status, Amazon GameLift Servers may attempt to place a game session multiple times before succeeding. With each attempt it creates a [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameSession](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameSession) object and updates this placement object with the new game session properties.

## Contents
<a name="API_GameSessionPlacement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DnsName **   <a name="gameliftservers-Type-GameSessionPlacement-DnsName"></a>
The DNS identifier assigned to the instance that is running the game session. Values have the following format:
+ TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com`.
+ Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com`. (See [Amazon EC2 Instance IP Addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses).)
When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.
Type: String
Required: No

 ** EndTime **   <a name="gameliftservers-Type-GameSessionPlacement-EndTime"></a>
Time stamp indicating when this request was completed, canceled, or timed out.
Type: Timestamp
Required: No

 ** GameProperties **   <a name="gameliftservers-Type-GameSessionPlacement-GameProperties"></a>
A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}`.
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
Type: Array of [GameProperty](API_GameProperty.md) objects
Array Members: Maximum number of 16 items.
Required: No

 ** GameSessionArn **   <a name="gameliftservers-Type-GameSessionPlacement-GameSessionArn"></a>
An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`. This value is the same as `GameSessionId`. This value isn't final until placement status is `FULFILLED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** GameSessionData **   <a name="gameliftservers-Type-GameSessionPlacement-GameSessionData"></a>
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: No

 ** GameSessionId **   <a name="gameliftservers-Type-GameSessionPlacement-GameSessionId"></a>
An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`. This value is the same as `GameSessionArn`. This value isn't final until placement status is `FULFILLED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** GameSessionName **   <a name="gameliftservers-Type-GameSessionPlacement-GameSessionName"></a>
A descriptive label that is associated with a game session. Session names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** GameSessionQueueName **   <a name="gameliftservers-Type-GameSessionPlacement-GameSessionQueueName"></a>
A descriptive label that is associated with game session queue. Queue names must be unique within each Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** GameSessionRegion **   <a name="gameliftservers-Type-GameSessionPlacement-GameSessionRegion"></a>
Name of the Region where the game session created by this placement request is running. This value isn't final until placement status is `FULFILLED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** IpAddress **   <a name="gameliftservers-Type-GameSessionPlacement-IpAddress"></a>
The IP address of the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number. This value isn't final until placement status is `FULFILLED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9A-Fa-f\:\.]+`
Required: No

 ** MatchmakerData **   <a name="gameliftservers-Type-GameSessionPlacement-MatchmakerData"></a>
Information on the matchmaking process for this game. Data is in JSON syntax, formatted as a string. It identifies the matchmaking configuration used to create the match, and contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see [Match Data](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-server.html#match-server-data).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 390000.
Required: No

 ** MaximumPlayerSessionCount **   <a name="gameliftservers-Type-GameSessionPlacement-MaximumPlayerSessionCount"></a>
The maximum number of players that can be connected simultaneously to the game session.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PlacedPlayerSessions **   <a name="gameliftservers-Type-GameSessionPlacement-PlacedPlayerSessions"></a>
A collection of information on player sessions created in response to the game session placement request. These player sessions are created only after a new game session is successfully placed (placement status is `FULFILLED`). This information includes the player ID, provided in the placement request, and a corresponding player session ID.
Type: Array of [PlacedPlayerSession](API_PlacedPlayerSession.md) objects
Required: No

 ** PlacementId **   <a name="gameliftservers-Type-GameSessionPlacement-PlacementId"></a>
A unique identifier for a game session placement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** PlayerGatewayStatus **   <a name="gameliftservers-Type-GameSessionPlacement-PlayerGatewayStatus"></a>
The current status of player gateway for the game session placement. Note, even if a fleet has PlayerGatewayMode configured as `ENABLED`, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see [Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html).
Possible values include:
+  `ENABLED` -- Player gateway is available for this game session placement.
+  `DISABLED` -- Player gateway is not available for this game session placement.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** PlayerLatencies **   <a name="gameliftservers-Type-GameSessionPlacement-PlayerLatencies"></a>
A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to a fleet location (AWS Regions or custom locations for Amazon GameLift Servers Anywhere fleets).
Type: Array of [PlayerLatency](API_PlayerLatency.md) objects
Required: No

 ** Port **   <a name="gameliftservers-Type-GameSessionPlacement-Port"></a>
The port number for the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number. This value isn't final until placement status is `FULFILLED`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: No

 ** PriorityConfigurationOverride **   <a name="gameliftservers-Type-GameSessionPlacement-PriorityConfigurationOverride"></a>
An alternative priority list of locations that's included with a game session placement request. When provided, the list overrides a queue's location order list for this game session placement request only. The list might include AWS Regions, local zones, and custom locations (for Anywhere fleets). The fallback strategy tells Amazon GameLift Servers what action to take (if any) in the event that it failed to place a new game session.
Type: [PriorityConfigurationOverride](API_PriorityConfigurationOverride.md) object
Required: No

 ** StartTime **   <a name="gameliftservers-Type-GameSessionPlacement-StartTime"></a>
Time stamp indicating when this request was placed in the queue. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** Status **   <a name="gameliftservers-Type-GameSessionPlacement-Status"></a>
Current status of the game session placement request.
+  **PENDING** -- The placement request is in the queue waiting to be processed. Game session properties are not yet final.
+  **FULFILLED** -- A new game session has been successfully placed. Game session properties are now final.
+  **CANCELLED** -- The placement request was canceled.
+  **TIMED\_OUT** -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed.
+  **FAILED** -- Amazon GameLift Servers is not able to complete the process of placing the game session. Common reasons are the game session terminated before the placement process was completed, or an unexpected internal error.
Type: String
Valid Values: `PENDING | FULFILLED | CANCELLED | TIMED_OUT | FAILED`
Required: No

## See Also
<a name="API_GameSessionPlacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameSessionPlacement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameSessionPlacement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameSessionPlacement)
