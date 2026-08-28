---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreatePlayerSession.html
---

# CreatePlayerSession
<a name="API_CreatePlayerSession"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Reserves an open player slot in a game session for a player. New player sessions can be created in any game session with an open slot that is in `ACTIVE` status and has a player creation policy of `ACCEPT_ALL`. You can add a group of players to a game session with [CreatePlayerSessions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreatePlayerSessions.html) .

To create a player session, specify a game session ID, player ID, and optionally a set of player data.

If successful, a slot is reserved in the game session for the player and a new `PlayerSessions` object is returned with a player session ID. The player references the player session ID when sending a connection request to the game session, and the game server can use it to validate the player reservation with the Amazon GameLift Servers service. Player sessions cannot be updated.

The maximum number of players per game session is 200. It is not adjustable.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_CreatePlayerSession_RequestSyntax"></a>

```
{
   "GameSessionId": "{{string}}",
   "PlayerData": "{{string}}",
   "PlayerId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePlayerSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameSessionId](#API_CreatePlayerSession_RequestSyntax) **   <a name="gameliftservers-CreatePlayerSession-request-GameSessionId"></a>
An identifier for the game session that is unique across all regions to add a player to. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: Yes

 ** [PlayerId](#API_CreatePlayerSession_RequestSyntax) **   <a name="gameliftservers-CreatePlayerSession-request-PlayerId"></a>
A unique identifier for a player. Player IDs are developer-defined.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [PlayerData](#API_CreatePlayerSession_RequestSyntax) **   <a name="gameliftservers-CreatePlayerSession-request-PlayerData"></a>
Developer-defined information related to a player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_CreatePlayerSession_ResponseSyntax"></a>

```
{
   "PlayerSession": {
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
}
```

## Response Elements
<a name="API_CreatePlayerSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PlayerSession](#API_CreatePlayerSession_ResponseSyntax) **   <a name="gameliftservers-CreatePlayerSession-response-PlayerSession"></a>
Object that describes the newly created player session record.
Type: [PlayerSession](API_PlayerSession.md) object

## Errors
<a name="API_CreatePlayerSession_Errors"></a>

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
<a name="API_CreatePlayerSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreatePlayerSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreatePlayerSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreatePlayerSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreatePlayerSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreatePlayerSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreatePlayerSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreatePlayerSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreatePlayerSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreatePlayerSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreatePlayerSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
