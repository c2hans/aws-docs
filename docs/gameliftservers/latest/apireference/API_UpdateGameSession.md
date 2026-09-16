---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameSession.html
---

# UpdateGameSession
<a name="API_UpdateGameSession"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Updates the mutable properties of a game session.

To update a game session, specify the game session ID and the values you want to change.

If successful, the updated `GameSession` object is returned.

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_UpdateGameSession_RequestSyntax"></a>

```
{
   "GameProperties": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "GameSessionId": "{{string}}",
   "MaximumPlayerSessionCount": {{number}},
   "Name": "{{string}}",
   "PlayerSessionCreationPolicy": "{{string}}",
   "ProtectionPolicy": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGameSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameSessionId](#API_UpdateGameSession_RequestSyntax) **   <a name="gameliftservers-UpdateGameSession-request-GameSessionId"></a>
An identifier for the game session that is unique across all regions to update. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: Yes

 ** [GameProperties](#API_UpdateGameSession_RequestSyntax) **   <a name="gameliftservers-UpdateGameSession-request-GameProperties"></a>
A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}`. You can use this parameter to modify game properties in an active game session. This action adds new properties and modifies existing properties. There is no way to delete properties. For an example, see [Update the value of a game property](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-update).
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
Type: Array of [GameProperty](API_GameProperty.md) objects
Array Members: Maximum number of 16 items.
Required: No

 ** [MaximumPlayerSessionCount](#API_UpdateGameSession_RequestSyntax) **   <a name="gameliftservers-UpdateGameSession-request-MaximumPlayerSessionCount"></a>
The maximum number of players that can be connected simultaneously to the game session.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [Name](#API_UpdateGameSession_RequestSyntax) **   <a name="gameliftservers-UpdateGameSession-request-Name"></a>
A descriptive label that is associated with a game session. Session names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [PlayerSessionCreationPolicy](#API_UpdateGameSession_RequestSyntax) **   <a name="gameliftservers-UpdateGameSession-request-PlayerSessionCreationPolicy"></a>
A policy that determines whether the game session is accepting new players.
Type: String
Valid Values: `ACCEPT_ALL | DENY_ALL`
Required: No

 ** [ProtectionPolicy](#API_UpdateGameSession_RequestSyntax) **   <a name="gameliftservers-UpdateGameSession-request-ProtectionPolicy"></a>
Game session protection policy to apply to this game session only.
+  `NoProtection` -- The game session can be terminated during a scale-down event.
+  `FullProtection` -- If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.
Type: String
Valid Values: `NoProtection | FullProtection`
Required: No

## Response Syntax
<a name="API_UpdateGameSession_ResponseSyntax"></a>

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
<a name="API_UpdateGameSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSession](#API_UpdateGameSession_ResponseSyntax) **   <a name="gameliftservers-UpdateGameSession-response-GameSession"></a>
The updated game session properties.
Type: [GameSession](API_GameSession.md) object

## Errors
<a name="API_UpdateGameSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

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

 ** NotReadyException **
 The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with [exponential backoffs and jitter](http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_UpdateGameSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateGameSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateGameSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateGameSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateGameSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateGameSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateGameSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateGameSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateGameSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateGameSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateGameSession)
