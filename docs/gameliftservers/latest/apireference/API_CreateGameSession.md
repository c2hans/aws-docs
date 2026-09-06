---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameSession.html
---

# CreateGameSession
<a name="API_CreateGameSession"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Creates a multiplayer game session for players in a specific fleet location. This operation prompts an available server process to start a game session and retrieves connection information for the new game session. As an alternative, consider using the Amazon GameLift Servers game session placement feature with [StartGameSessionPlacement](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartGameSessionPlacement.html), which uses the FleetIQ algorithm and queues to optimize the placement process.

When creating a game session, you specify exactly where you want to place it and provide a set of game session configuration settings. The target fleet must be in `ACTIVE` status.

You can use this operation in the following ways:
+ To create a game session on an instance in a fleet's home Region, provide a fleet or alias ID along with your game session configuration.
+ To create a game session on an instance in a fleet's remote location, provide a fleet or alias ID and a location name, along with your game session configuration.
+ To create a game session on an instance in an Anywhere fleet, specify the fleet's custom location.

If successful, Amazon GameLift Servers initiates a workflow to start a new game session and returns a `GameSession` object containing the game session configuration and status. When the game session status is `ACTIVE`, it is updated with connection information and you can create player sessions for the game session. By default, newly created game sessions are open to new players. You can restrict new player access by using [UpdateGameSession](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html) to change the game session's player session creation policy.

Amazon GameLift Servers retains logs for active for 14 days. To access the logs, call [GetGameSessionLogUrl](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetGameSessionLogUrl.html) to download the log files.

 *Available in Amazon GameLift Servers Local.*

 **Learn more**

 [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession)

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_CreateGameSession_RequestSyntax"></a>

```
{
   "AliasId": "{{string}}",
   "CreatorId": "{{string}}",
   "FleetId": "{{string}}",
   "GameProperties": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "GameSessionData": "{{string}}",
   "GameSessionId": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "Location": "{{string}}",
   "MaximumPlayerSessionCount": {{number}},
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateGameSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [MaximumPlayerSessionCount](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-MaximumPlayerSessionCount"></a>
The maximum number of players that can be connected simultaneously to the game session.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** [AliasId](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-AliasId"></a>
A unique identifier for the alias associated with the fleet to create a game session in. You can use either the alias ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.
Type: String
Pattern: `^alias-\S+|^arn:.*:alias\/alias-\S+`
Required: No

 ** [CreatorId](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-CreatorId"></a>
A unique identifier for a player or entity creating the game session.
If you add a resource creation limit policy to a fleet, the `CreateGameSession` operation requires a `CreatorId`. Amazon GameLift Servers limits the number of game session creation requests with the same `CreatorId` in a specified time period.
If you your fleet doesn't have a resource creation limit policy and you provide a `CreatorId` in your `CreateGameSession` requests, Amazon GameLift Servers limits requests to one request per `CreatorId` per second.
To not limit `CreateGameSession` requests with the same `CreatorId`, don't provide a `CreatorId` in your `CreateGameSession` request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [FleetId](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-FleetId"></a>
A unique identifier for the fleet to create a game session in. You can use either the fleet ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** [GameProperties](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-GameProperties"></a>
A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}`. For an example, see [Create a game session with custom properties](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-create).
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
Type: Array of [GameProperty](API_GameProperty.md) objects
Array Members: Maximum number of 16 items.
Required: No

 ** [GameSessionData](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-GameSessionData"></a>
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: No

 ** [GameSessionId](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-GameSessionId"></a>
 *This parameter is deprecated. Use `IdempotencyToken` instead.*
Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [IdempotencyToken](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-IdempotencyToken"></a>
Custom string that uniquely identifies the new game session request. This is useful for ensuring that game session requests with the same idempotency token are processed only once. Subsequent requests with the same string return the original `GameSession` object, with an updated status. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`. Idempotency tokens remain in use for 30 days after a game session has ended; game session objects are retained for this time period and then deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [Location](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-Location"></a>
A fleet's remote location to place the new game session in. If this parameter is not set, the new game session is placed in the fleet's home Region. Specify a remote location with an AWS Region code such as `us-west-2`. When using an Anywhere fleet, this parameter is required and must be set to the Anywhere fleet's custom location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** [Name](#API_CreateGameSession_RequestSyntax) **   <a name="gameliftservers-CreateGameSession-request-Name"></a>
A descriptive label that is associated with a game session. Session names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_CreateGameSession_ResponseSyntax"></a>

```
{
   "GameSession": {
      "ComputeName": "string",
      "CreationTime": number,
      "CreatorId": "string",
      "CurrentPlayerSessionCount": number,
      "DnsName": "string",
      "FleetArn": "string",
      "FleetId": "string",
      "GameProperties": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "GameSessionData": "string",
      "GameSessionId": "string",
      "IpAddress": "string",
      "Location": "string",
      "MatchmakerData": "string",
      "MaximumPlayerSessionCount": number,
      "Name": "string",
      "PlayerGatewayStatus": "string",
      "PlayerSessionCreationPolicy": "string",
      "Port": number,
      "Status": "string",
      "StatusReason": "string",
      "TerminationTime": number
   }
}
```

## Response Elements
<a name="API_CreateGameSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSession](#API_CreateGameSession_ResponseSyntax) **   <a name="gameliftservers-CreateGameSession-response-GameSession"></a>
Object that describes the newly created game session record.
Type: [GameSession](API_GameSession.md) object

## Errors
<a name="API_CreateGameSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** FleetCapacityExceededException **
The specified fleet has no available instances to fulfill a `CreateGameSession` request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
A game session with this custom ID string already exists in this fleet. Resolve this conflict before retrying this request.
HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidFleetStatusException **
The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.
HTTP Status Code: 400

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
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

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_CreateGameSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateGameSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateGameSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateGameSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateGameSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateGameSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateGameSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateGameSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateGameSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateGameSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateGameSession)
