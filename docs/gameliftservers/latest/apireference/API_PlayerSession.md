---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PlayerSession.html
---

# PlayerSession
<a name="API_PlayerSession"></a>

Represents a player session. Player sessions are created either for a specific game session, or as part of a game session placement or matchmaking request. A player session can represents a reserved player slot in a game session (when status is `RESERVED`) or actual player activity in a game session (when status is `ACTIVE`). A player session object, including player data, is automatically passed to a game session when the player connects to the game session and is validated. After the game session ends, player sessions information is retained for 30 days and then removed.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Contents
<a name="API_PlayerSession_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreationTime **   <a name="gameliftservers-Type-PlayerSession-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** DnsName **   <a name="gameliftservers-Type-PlayerSession-DnsName"></a>
The DNS identifier assigned to the instance that is running the game session. Values have the following format:
+ TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com`.
+ Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com`. (See [Amazon EC2 Instance IP Addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses).)
When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.
Type: String
Required: No

 ** FleetArn **   <a name="gameliftservers-Type-PlayerSession-FleetArn"></a>
 The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) associated with the GameLift fleet that the player's game session is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** FleetId **   <a name="gameliftservers-Type-PlayerSession-FleetId"></a>
A unique identifier for the fleet that the player's game session is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** GameSessionId **   <a name="gameliftservers-Type-PlayerSession-GameSessionId"></a>
An identifier for the game session that is unique across all regions that the player session is connected to. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** IpAddress **   <a name="gameliftservers-Type-PlayerSession-IpAddress"></a>
The IP address of the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9A-Fa-f\:\.]+`
Required: No

 ** PlayerData **   <a name="gameliftservers-Type-PlayerSession-PlayerData"></a>
Developer-defined information related to a player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** PlayerId **   <a name="gameliftservers-Type-PlayerSession-PlayerId"></a>
A unique identifier for a player that is associated with this player session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PlayerSessionId **   <a name="gameliftservers-Type-PlayerSession-PlayerSessionId"></a>
A unique identifier for a player session.
Type: String
Pattern: `^psess-\S+`
Required: No

 ** Port **   <a name="gameliftservers-Type-PlayerSession-Port"></a>
Port number for the game session. To connect to a Amazon GameLift Servers server process, an app needs both the IP address and port number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: No

 ** Status **   <a name="gameliftservers-Type-PlayerSession-Status"></a>
Current status of the player session.
Possible player session statuses include the following:
+  **RESERVED** -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.
+  **ACTIVE** -- The player has been validated by the server process and is currently connected.
+  **COMPLETED** -- The player connection has been dropped.
+  **TIMEDOUT** -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).
Type: String
Valid Values: `RESERVED | ACTIVE | COMPLETED | TIMEDOUT`
Required: No

 ** TerminationTime **   <a name="gameliftservers-Type-PlayerSession-TerminationTime"></a>
A time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

## See Also
<a name="API_PlayerSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PlayerSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PlayerSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PlayerSession)
