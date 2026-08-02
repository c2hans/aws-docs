---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreatePlayerSessions.html
---

# CreatePlayerSessions
<a name="API_CreatePlayerSessions"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Reserves open slots in a game session for a group of players. New player sessions can be created in any game session with an open slot that is in `ACTIVE` status and has a player creation policy of `ACCEPT_ALL`. To add a single player to a game session, use [CreatePlayerSession](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreatePlayerSession.html)

To create player sessions, specify a game session ID and a list of player IDs. Optionally, provide a set of player data for each player ID.

If successful, a slot is reserved in the game session for each player, and new `PlayerSession` objects are returned with player session IDs. Each player references their player session ID when sending a connection request to the game session, and the game server can use it to validate the player reservation with the Amazon GameLift Servers service. Player sessions cannot be updated.

The maximum number of players per game session is 200. It is not adjustable.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_CreatePlayerSessions_RequestSyntax"></a>

```
{
   "GameSessionId": "{{string}}",
   "PlayerDataMap": {
      "{{string}}" : "{{string}}"
   },
   "PlayerIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreatePlayerSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameSessionId](#API_CreatePlayerSessions_RequestSyntax) **   <a name="gameliftservers-CreatePlayerSessions-request-GameSessionId"></a>
An identifier for the game session that is unique across all regions to add players to. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: Yes

 ** [PlayerIds](#API_CreatePlayerSessions_RequestSyntax) **   <a name="gameliftservers-CreatePlayerSessions-request-PlayerIds"></a>
List of unique identifiers for the players to be added.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [PlayerDataMap](#API_CreatePlayerSessions_RequestSyntax) **   <a name="gameliftservers-CreatePlayerSessions-request-PlayerDataMap"></a>
Map of string pairs, each specifying a player ID and a set of developer-defined information related to the player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game. Any player data strings for player IDs that are not included in the `PlayerIds` parameter are ignored.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_CreatePlayerSessions_ResponseSyntax"></a>

```
{
   "PlayerSessions": [
      {
         "CreationTime": number,
         "DnsName": "string",
         "FleetArn": "string",
         "FleetId": "string",
         "GameSessionId": "string",
         "IpAddress": "string",
         "PlayerData": "string",
         "PlayerId": "string",
         "PlayerSessionId": "string",
         "Port": number,
         "Status": "string",
         "TerminationTime": number
      }
   ]
}
```

## Response Elements
<a name="API_CreatePlayerSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PlayerSessions](#API_CreatePlayerSessions_ResponseSyntax) **   <a name="gameliftservers-CreatePlayerSessions-response-PlayerSessions"></a>
A collection of player session objects created for the added players.
Type: Array of [PlayerSession](API_PlayerSession.md) objects

## Errors
<a name="API_CreatePlayerSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GameSessionFullException **
The game instance is currently full and cannot allow the requested player(s) to join. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidGameSessionStatusException **
The requested operation would cause a conflict with the current state of a resource associated with the request and/or the game instance. Resolve the conflict before retrying.
HTTP Status Code: 400

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** TerminalRoutingStrategyException **
The service is unable to resolve the routing for a particular alias because it has a terminal `RoutingStrategy` associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_CreatePlayerSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreatePlayerSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreatePlayerSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreatePlayerSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreatePlayerSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreatePlayerSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreatePlayerSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreatePlayerSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreatePlayerSessions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreatePlayerSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreatePlayerSessions)
