---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameServer.html
---

# GameServer
<a name="API_GameServer"></a>

Properties describing a game server that is running on an instance in a game server group.

A game server is created by a successful call to `RegisterGameServer` and deleted by calling `DeregisterGameServer`. A game server is claimed to host a game session by calling `ClaimGameServer`.

## Contents
<a name="API_GameServer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClaimStatus **   <a name="gameliftservers-Type-GameServer-ClaimStatus"></a>
Indicates when an available game server has been reserved for gameplay but has not yet started hosting a game. Once it is claimed, the game server remains in `CLAIMED` status for a maximum of one minute. During this time, game clients connect to the game server to start the game and trigger the game server to update its utilization status. After one minute, the game server claim status reverts to null.
Type: String
Valid Values: `CLAIMED`
Required: No

 ** ConnectionInfo **   <a name="gameliftservers-Type-GameServer-ConnectionInfo"></a>
The port and IP address that must be used to establish a client connection to the game server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*\S.*`
Required: No

 ** GameServerData **   <a name="gameliftservers-Type-GameServer-GameServerData"></a>
A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** GameServerGroupArn **   <a name="gameliftservers-Type-GameServer-GameServerGroupArn"></a>
The ARN identifier for the game server group where the game server is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]*`
Required: No

 ** GameServerGroupName **   <a name="gameliftservers-Type-GameServer-GameServerGroupName"></a>
A unique identifier for the game server group where the game server is running.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]+`
Required: No

 ** GameServerId **   <a name="gameliftservers-Type-GameServer-GameServerId"></a>
A custom string that uniquely identifies the game server. Game server IDs are developer-defined and are unique across all game server groups in an AWS account.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]+`
Required: No

 ** InstanceId **   <a name="gameliftservers-Type-GameServer-InstanceId"></a>
The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: `i-1234567890abcdef0`.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `^i-[0-9a-zA-Z]{17}$`
Required: No

 ** LastClaimTime **   <a name="gameliftservers-Type-GameServer-LastClaimTime"></a>
Timestamp that indicates the last time the game server was claimed. The format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`). This value is used to calculate when a claimed game server's status should revert to null.
Type: Timestamp
Required: No

 ** LastHealthCheckTime **   <a name="gameliftservers-Type-GameServer-LastHealthCheckTime"></a>
Timestamp that indicates the last time the game server was updated with health status. The format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`). After game server registration, this property is only changed when a game server update specifies a health check value.
Type: Timestamp
Required: No

 ** RegistrationTime **   <a name="gameliftservers-Type-GameServer-RegistrationTime"></a>
Timestamp that indicates when the game server registered. The format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** UtilizationStatus **   <a name="gameliftservers-Type-GameServer-UtilizationStatus"></a>
Indicates whether the game server is currently available for new games or is busy. Possible statuses include:
+  `AVAILABLE` - The game server is available to be claimed. A game server that has been claimed remains in this status until it reports game hosting activity.
+  `UTILIZED` - The game server is currently hosting a game session with players.
Type: String
Valid Values: `AVAILABLE | UTILIZED`
Required: No

## See Also
<a name="API_GameServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
