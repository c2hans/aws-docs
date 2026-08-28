---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartMatchBackfill.html
---

# StartMatchBackfill
<a name="API_StartMatchBackfill"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Finds new players to fill open slots in currently running game sessions. The backfill match process is essentially identical to the process of forming new matches. Backfill requests use the same matchmaker that was used to make the original match, and they provide matchmaking data for all players currently in the game session. FlexMatch uses this information to select new players so that backfilled match continues to meet the original match requirements.

When including player latency data in backfill requests, you can use Amazon GameLift Servers's UDP ping beacons to obtain accurate measurements of network latency between player devices and the game session's hosting location. For more information on using UDP ping beacons to measure latency, refer to [UDP ping beacons](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-udp-ping-beacons.html) in the Amazon GameLift Servers Developer Guide.

When using FlexMatch with Amazon GameLift Servers managed hosting, you can request a backfill match from a client service by calling this operation with a `GameSessions` ID. You also have the option of making backfill requests directly from your game server. In response to a request, FlexMatch creates player sessions for the new players, updates the `GameSession` resource, and sends updated matchmaking data to the game server. You can request a backfill match at any point after a game session is started. Each game session can have only one active backfill request at a time; a subsequent request automatically replaces the earlier request.

When using FlexMatch as a standalone component, request a backfill match by calling this operation without a game session identifier. As with newly formed matches, matchmaking results are returned in a matchmaking event so that your game can update the game session that is being backfilled.

To request a backfill match, specify a unique ticket ID, the original matchmaking configuration, and matchmaking data for all current players in the game session being backfilled. Optionally, specify the `GameSession` ARN. If successful, a match backfill ticket is created and returned with status set to QUEUED. Track the status of backfill tickets using the same method for tracking tickets for new matches.

Only game sessions created by FlexMatch are supported for match backfill.

 **Learn more**

 [ Backfill existing games with FlexMatch](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html)

 [ Matchmaking events](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html) (reference)

 [ How Amazon GameLift Servers FlexMatch works](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/gamelift-match.html)

## Request Syntax
<a name="API_StartMatchBackfill_RequestSyntax"></a>

```
{
   "ConfigurationName": "{{string}}",
   "GameSessionArn": "{{string}}",
   "Players": [
      {
         "LatencyInMs": {
            "{{string}}" : {{number}}
         },
         "PlayerAttributes": {
            "{{string}}" : {
               "N": {{number}},
               "S": "{{string}}",
               "SDM": {
                  "{{string}}" : {{number}}
               },
               "SL": [ "{{string}}" ]
            }
         },
         "PlayerId": "{{string}}",
         "Team": "{{string}}"
      }
   ],
   "TicketId": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMatchBackfill_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ConfigurationName](#API_StartMatchBackfill_RequestSyntax) **   <a name="gameliftservers-StartMatchBackfill-request-ConfigurationName"></a>
Name of the matchmaker to use for this request. You can use either the configuration name or ARN value. The ARN of the matchmaker that was used with the original game session is listed in the `GameSession` object, `MatchmakerData` property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingconfiguration\/[a-zA-Z0-9-\.]*`
Required: Yes

 ** [Players](#API_StartMatchBackfill_RequestSyntax) **   <a name="gameliftservers-StartMatchBackfill-request-Players"></a>
Match information on all players that are currently assigned to the game session. This information is used by the matchmaker to find new players and add them to the existing game.
You can include up to 199 `Players` in a `StartMatchBackfill` request.
+ PlayerID, PlayerAttributes, Team -- This information is maintained in the `GameSession` object, `MatchmakerData` property, for all players who are currently assigned to the game session. The matchmaker data is in JSON syntax, formatted as a string. For more details, see [ Match Data](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-server.html#match-server-data).

  The backfill request must specify the team membership for every player. Do not specify team if you are not using backfill.
+ LatencyInMs -- If the matchmaker uses player latency, include a latency value, in milliseconds, for the Region that the game session is currently in. Do not include latency values for any other Region.
Type: Array of [Player](API_Player.md) objects
Required: Yes

 ** [GameSessionArn](#API_StartMatchBackfill_RequestSyntax) **   <a name="gameliftservers-StartMatchBackfill-request-GameSessionArn"></a>
An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`. When using FlexMatch as a standalone matchmaking solution, this parameter is not needed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** [TicketId](#API_StartMatchBackfill_RequestSyntax) **   <a name="gameliftservers-StartMatchBackfill-request-TicketId"></a>
A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift Servers will generate one in the form of a UUID. Use this identifier to track the match backfill ticket status and retrieve match results.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: No

## Response Syntax
<a name="API_StartMatchBackfill_ResponseSyntax"></a>

```
{
   "MatchmakingTicket": {
      "ConfigurationArn": "string",
      "ConfigurationName": "string",
      "EndTime": number,
      "EstimatedWaitTime": number,
      "GameSessionConnectionInfo": {
         "DnsName": "string",
         "GameSessionArn": "string",
         "IpAddress": "string",
         "MatchedPlayerSessions": [
            {
               "PlayerId": "string",
               "PlayerSessionId": "string"
            }
         ],
         "PlayerGatewayStatus": "string",
         "Port": number
      },
      "Players": [
         {
            "LatencyInMs": {
               "string" : number
            },
            "PlayerAttributes": {
               "string" : {
                  "N": number,
                  "S": "string",
                  "SDM": {
                     "string" : number
                  },
                  "SL": [ "string" ]
               }
            },
            "PlayerId": "string",
            "Team": "string"
         }
      ],
      "StartTime": number,
      "Status": "string",
      "StatusMessage": "string",
      "StatusReason": "string",
      "TicketId": "string"
   }
}
```

## Response Elements
<a name="API_StartMatchBackfill_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MatchmakingTicket](#API_StartMatchBackfill_ResponseSyntax) **   <a name="gameliftservers-StartMatchBackfill-response-MatchmakingTicket"></a>
Ticket representing the backfill matchmaking request. This object includes the information in the request, ticket status, and match results as generated during the matchmaking process.
Type: [MatchmakingTicket](API_MatchmakingTicket.md) object

## Errors
<a name="API_StartMatchBackfill_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_StartMatchBackfill_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/StartMatchBackfill)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/StartMatchBackfill)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/StartMatchBackfill)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/StartMatchBackfill)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/StartMatchBackfill)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/StartMatchBackfill)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/StartMatchBackfill)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/StartMatchBackfill)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/StartMatchBackfill)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/StartMatchBackfill)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
