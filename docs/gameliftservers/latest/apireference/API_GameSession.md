---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameSession.html
---

# GameSession
<a name="API_GameSession"></a>

Properties describing a game session.

A game session in ACTIVE status can host players. When a game session ends, its status is set to `TERMINATED`.

Amazon GameLift Servers retains a game session resource for 30 days after the game session ends. You can reuse idempotency token values after this time. Game session logs are retained for 14 days.

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Contents
<a name="API_GameSession_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputeName **   <a name="gameliftservers-Type-GameSession-ComputeName"></a>
A descriptive label for the compute resource. The compute resource that is hosting the game session. For EC2 fleets, this is the EC2 instance ID. For Container fleets, each game server container group on a fleet instance is assigned a compute name. For Anywhere fleets, this is the custom compute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
Required: No

 ** CreationTime **   <a name="gameliftservers-Type-GameSession-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** CreatorId **   <a name="gameliftservers-Type-GameSession-CreatorId"></a>
A unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** CurrentPlayerSessionCount **   <a name="gameliftservers-Type-GameSession-CurrentPlayerSessionCount"></a>
Number of players currently in the game session.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** DnsName **   <a name="gameliftservers-Type-GameSession-DnsName"></a>
The DNS identifier assigned to the instance that is running the game session. Values have the following format:
+ TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com`.
+ Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com`. (See [Amazon EC2 Instance IP Addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses).)
When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.
Type: String
Required: No

 ** FleetArn **   <a name="gameliftservers-Type-GameSession-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) associated with the GameLift fleet that this game session is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** FleetId **   <a name="gameliftservers-Type-GameSession-FleetId"></a>
A unique identifier for the fleet that the game session is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** GameProperties **   <a name="gameliftservers-Type-GameSession-GameProperties"></a>
A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}`.
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
Type: Array of [GameProperty](API_GameProperty.md) objects
Array Members: Maximum number of 16 items.
Required: No

 ** GameSessionData **   <a name="gameliftservers-Type-GameSession-GameSessionData"></a>
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: No

 ** GameSessionId **   <a name="gameliftservers-Type-GameSession-GameSessionId"></a>
An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** IpAddress **   <a name="gameliftservers-Type-GameSession-IpAddress"></a>
The IP address of the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9A-Fa-f\:\.]+`
Required: No

 ** Location **   <a name="gameliftservers-Type-GameSession-Location"></a>
The fleet location where the game session is running. This value might specify the fleet's home Region or a remote location. Location is expressed as an AWS Region code such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** MatchmakerData **   <a name="gameliftservers-Type-GameSession-MatchmakerData"></a>
Information about the matchmaking process that resulted in the game session, if matchmaking was used. Data is in JSON syntax, formatted as a string. Information includes the matchmaker ID as well as player attributes and team assignments. For more details on matchmaker data, see [Match Data](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-server.html#match-server-data). Matchmaker data is updated whenever new players are added during a successful backfill (see [StartMatchBackfill](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartMatchBackfill.html)).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 390000.
Required: No

 ** MaximumPlayerSessionCount **   <a name="gameliftservers-Type-GameSession-MaximumPlayerSessionCount"></a>
The maximum number of players that can be connected simultaneously to the game session.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Name **   <a name="gameliftservers-Type-GameSession-Name"></a>
A descriptive label that is associated with a game session. Session names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PlayerGatewayStatus **   <a name="gameliftservers-Type-GameSession-PlayerGatewayStatus"></a>
Indicates whether player gateway is available for use for this game session. Note, even if a fleet has PlayerGatewayMode configured as `ENABLED`, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see [Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html).
Possible values include:
+  `ENABLED` -- Player gateway is available for routing player connections for this game session.
+  `DISABLED` -- Player gateway is not available for this game session.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** PlayerSessionCreationPolicy **   <a name="gameliftservers-Type-GameSession-PlayerSessionCreationPolicy"></a>
Indicates whether the game session is accepting new players.
Type: String
Valid Values: `ACCEPT_ALL | DENY_ALL`
Required: No

 ** Port **   <a name="gameliftservers-Type-GameSession-Port"></a>
The port number for the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: No

 ** Status **   <a name="gameliftservers-Type-GameSession-Status"></a>
Current status of the game session. A game session must have an `ACTIVE` status to have player sessions.
Type: String
Valid Values: `ACTIVE | ACTIVATING | TERMINATED | TERMINATING | ERROR`
Required: No

 ** StatusReason **   <a name="gameliftservers-Type-GameSession-StatusReason"></a>
Provides additional information about game session status.
+  `INTERRUPTED` -- The game session was hosted on an EC2 Spot instance that was reclaimed, causing the active game session to be stopped.
+  `TRIGGERED_ON_PROCESS_TERMINATE` – The game session was stopped by calling `TerminateGameSession` with the termination mode `TRIGGER_ON_PROCESS_TERMINATE`.
+  `FORCE_TERMINATED` – The game session was stopped by calling `TerminateGameSession` with the termination mode `FORCE_TERMINATE`.

Type: String
Valid Values: `INTERRUPTED | TRIGGERED_ON_PROCESS_TERMINATE | FORCE_TERMINATED`
Required: No

 ** TerminationTime **   <a name="gameliftservers-Type-GameSession-TerminationTime"></a>
A time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

## See Also
<a name="API_GameSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
