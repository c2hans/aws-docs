---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameSessionConnectionInfo.html
---

# GameSessionConnectionInfo
<a name="API_GameSessionConnectionInfo"></a>

Connection information for a new game session that is created in response to a start matchmaking request. Once a match is made, the FlexMatch engine creates a new game session for it. This information, including the game session endpoint and player sessions for each player in the original matchmaking request, is added to the matchmaking ticket.

## Contents
<a name="API_GameSessionConnectionInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DnsName **   <a name="gameliftservers-Type-GameSessionConnectionInfo-DnsName"></a>
The DNS identifier assigned to the instance that is running the game session. Values have the following format:
+ TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com`.
+ Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com`. (See [Amazon EC2 Instance IP Addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses).)
When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.
Type: String
Required: No

 ** GameSessionArn **   <a name="gameliftservers-Type-GameSessionConnectionInfo-GameSessionArn"></a>
An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** IpAddress **   <a name="gameliftservers-Type-GameSessionConnectionInfo-IpAddress"></a>
The IP address of the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9A-Fa-f\:\.]+`
Required: No

 ** MatchedPlayerSessions **   <a name="gameliftservers-Type-GameSessionConnectionInfo-MatchedPlayerSessions"></a>
A collection of player session IDs, one for each player ID that was included in the original matchmaking request.
Type: Array of [MatchedPlayerSession](API_MatchedPlayerSession.md) objects
Required: No

 ** PlayerGatewayStatus **   <a name="gameliftservers-Type-GameSessionConnectionInfo-PlayerGatewayStatus"></a>
The current status of player gateway for the game session. Note, even if a fleet has PlayerGatewayMode configured as `ENABLED`, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see [supported locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html).
Possible values include:
+  `ENABLED` -- Player gateway is available for this game session.
+  `DISABLED` -- Player gateway is not available for this game session.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** Port **   <a name="gameliftservers-Type-GameSessionConnectionInfo-Port"></a>
The port number for the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_GameSessionConnectionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameSessionConnectionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameSessionConnectionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameSessionConnectionInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
