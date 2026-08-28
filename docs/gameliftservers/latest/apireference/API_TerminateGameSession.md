---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_TerminateGameSession.html
---

# TerminateGameSession
<a name="API_TerminateGameSession"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Ends a game session that's currently in progress. Use this action to terminate any game session that isn't in `ERROR` status. Terminating a game session is the most efficient way to free up a server process when it's hosting a game session that's in a bad state or not ending properly. You can use this action to terminate a game session that's being hosted on any type of Amazon GameLift Servers fleet compute, including computes for managed EC2, managed container, and Anywhere fleets. The game server must be integrated with Amazon GameLift Servers server SDK 5.x or greater.

 **Request options**

Request termination for a single game session. Provide the game session ID and the termination mode. There are two potential methods for terminating a game session:
+ Initiate a graceful termination using the normal game session shutdown sequence. With this mode, the Amazon GameLift Servers service prompts the server process that's hosting the game session by calling the server SDK callback method `OnProcessTerminate()`. The callback implementation is part of the custom game server code. It might involve a variety of actions to gracefully end a game session, such as notifying players, before stopping the server process.
+ Force an immediate game session termination. With this mode, the Amazon GameLift Servers service takes action to stop the server process, which ends the game session without the normal game session shutdown sequence.

 **Results**

If successful, game session termination is initiated. During this activity, the game session status is changed to `TERMINATING`. When completed, the server process that was hosting the game session has been stopped and replaced with a new server process that's ready to host a new game session. The old game session's status is changed to `TERMINATED` with a status reason that indicates the termination method used.

 **Learn more**

 [Add Amazon GameLift Servers to your game server](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html)

Amazon GameLift Servers server SDK 5 reference guide for `OnProcessTerminate()` ([C\+\+](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-cpp-initsdk.html)) ([C\#](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-csharp-initsdk.html)) ([Unreal](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-unreal-initsdk.html)) ([Go](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk-go-initsdk.html))

## Request Syntax
<a name="API_TerminateGameSession_RequestSyntax"></a>

```
{
   "GameSessionId": "{{string}}",
   "TerminationMode": "{{string}}"
}
```

## Request Parameters
<a name="API_TerminateGameSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameSessionId](#API_TerminateGameSession_RequestSyntax) **   <a name="gameliftservers-TerminateGameSession-request-GameSessionId"></a>
An identifier for the game session that is unique across all regions to be terminated. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: Yes

 ** [TerminationMode](#API_TerminateGameSession_RequestSyntax) **   <a name="gameliftservers-TerminateGameSession-request-TerminationMode"></a>
The method to use to terminate the game session. Available methods include:
+  `TRIGGER_ON_PROCESS_TERMINATE` – Prompts the Amazon GameLift Servers service to send an `OnProcessTerminate()` callback to the server process and initiate the normal game session shutdown sequence. The `OnProcessTerminate` method, which is implemented in the game server code, must include a call to the server SDK action `ProcessEnding()`, which is how the server process signals to Amazon GameLift Servers that a game session is ending. If the server process doesn't call `ProcessEnding()`, the game session termination won't conclude successfully.
+  `FORCE_TERMINATE` – Prompts the Amazon GameLift Servers service to stop the server process immediately. Amazon GameLift Servers takes action (depending on the type of fleet) to shut down the server process without the normal game session shutdown sequence.
**Note**
This method is not available for game sessions that are running on Anywhere fleets unless the fleet is deployed with the Amazon GameLift Servers Agent. In this scenario, a force terminate request results in an invalid or bad request exception.
Type: String
Valid Values: `TRIGGER_ON_PROCESS_TERMINATE | FORCE_TERMINATE`
Required: Yes

## Response Syntax
<a name="API_TerminateGameSession_ResponseSyntax"></a>

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
<a name="API_TerminateGameSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSession](#API_TerminateGameSession_ResponseSyntax) **   <a name="gameliftservers-TerminateGameSession-response-GameSession"></a>
Properties describing a game session.
A game session in ACTIVE status can host players. When a game session ends, its status is set to `TERMINATED`.
Amazon GameLift Servers retains a game session resource for 30 days after the game session ends. You can reuse idempotency token values after this time. Game session logs are retained for 14 days.
 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)
Type: [GameSession](API_GameSession.md) object

## Errors
<a name="API_TerminateGameSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** NotReadyException **
 The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with [exponential backoffs and jitter](http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_TerminateGameSession_Examples"></a>

### Terminate a game session
<a name="API_TerminateGameSession_Example_1"></a>

In this example, we want to gracefully end a game session that's entered a bad state. The game session is being hosted on a managed EC2 fleet.

#### Sample Request
<a name="API_TerminateGameSession_Example_1_Request"></a>

```
{
  "GameSessionId": "arn:aws:gamelift:us-west-2::gamesession/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa/gsess-4444dddd-55ee-66ff-77aa-8888bbbb99cc",
  "TerminationMode": "TRIGGER_ON_PROCESS_TERMINATE"
}

CLI syntax:
    aws gamelift terminate-game-session --game-session-id "arn:aws:gamelift:us-west-2::gamesession/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa/gsess-4444dddd-55ee-66ff-77aa-8888bbbb99cc" --termination-mode "TRIGGER_ON_PROCESS_TERMINATE"
```

#### Sample Response
<a name="API_TerminateGameSession_Example_1_Response"></a>

```
{
  "GameSession": {
    "CreationTime": 1469498468.057,
    "CurrentPlayerSessionCount": 5,
    "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "GameProperties": [
      {"Key": "difficulty","Value": "easy"},
      {"Key": "gameMap","Value": "Snowfall"},
      {"Key": "gameMode","Value": "Explore"}
    ],
    "GameSessionId": "arn:aws:gamelift:us-west-2::gamesession/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa/gsess-4444dddd-55ee-66ff-77aa-8888bbbb99cc",
    "IpAddress": "192.0.2.0",
    "Location": "us-west-2",
    "MaximumPlayerSessionCount": 10,
    "Name": "Matt's Awesome Game win123",
    "PlayerSessionCreationPolicy": "ACCEPT_ALL",
    "Port": "8080",
    "Status": "ACTIVE",
    "ComputeName": "i-9999aaaabbbbcccc0"
  }
}
```

## See Also
<a name="API_TerminateGameSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/TerminateGameSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/TerminateGameSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/TerminateGameSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/TerminateGameSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/TerminateGameSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/TerminateGameSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/TerminateGameSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/TerminateGameSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/TerminateGameSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/TerminateGameSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
