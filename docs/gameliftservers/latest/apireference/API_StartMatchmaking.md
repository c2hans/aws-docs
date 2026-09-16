---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartMatchmaking.html
---

# StartMatchmaking
<a name="API_StartMatchmaking"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Uses FlexMatch to create a game match for a group of players based on custom matchmaking rules. With games that use Amazon GameLift Servers managed hosting, this operation also triggers Amazon GameLift Servers to find hosting resources and start a new game session for the new match. Each matchmaking request includes information on one or more players and specifies the FlexMatch matchmaker to use. When a request is for multiple players, FlexMatch attempts to build a match that includes all players in the request, placing them in the same team and finding additional players as needed to fill the match.

To start matchmaking, provide a unique ticket ID, specify a matchmaking configuration, and include the players to be matched. You must also include any player attributes that are required by the matchmaking configuration's rule set. If successful, a matchmaking ticket is returned with status set to `QUEUED`.

Track matchmaking events to respond as needed and acquire game session connection information for successfully completed matches. Ticket status updates are tracked using event notification through Amazon Simple Notification Service, which is defined in the matchmaking configuration.

 **Learn more**

 [ Add FlexMatch to a game client](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html)

 [ Set Up FlexMatch event notification](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html)

 [ How Amazon GameLift Servers FlexMatch works](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/gamelift-match.html)

## Request Syntax
<a name="API_StartMatchmaking_RequestSyntax"></a>

```
{
   "ConfigurationName": "{{string}}",
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
<a name="API_StartMatchmaking_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ConfigurationName](#API_StartMatchmaking_RequestSyntax) **   <a name="gameliftservers-StartMatchmaking-request-ConfigurationName"></a>
Name of the matchmaking configuration to use for this request. Matchmaking configurations must exist in the same Region as this request. You can use either the configuration name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingconfiguration\/[a-zA-Z0-9-\.]*`
Required: Yes

 ** [Players](#API_StartMatchmaking_RequestSyntax) **   <a name="gameliftservers-StartMatchmaking-request-Players"></a>
Information on each player to be matched. This information must include a player ID, and may contain player attributes and latency data to be used in the matchmaking process. After a successful match, `Player` objects contain the name of the team the player is assigned to.
You can include up to 10 `Players` in a `StartMatchmaking` request.
For accurate player latency data, use Amazon GameLift Servers's UDP ping beacons to measure network latency between player devices and potential hosting locations. UDP ping beacons provide more accurate measurements than ICMP pings because they use the same protocol (UDP) that most game servers use. For more information on using UDP ping beacons to measure latency, refer to [UDP ping beacons](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-udp-ping-beacons.html) in the Amazon GameLift Servers Developer Guide.
Type: Array of [Player](API_Player.md) objects
Required: Yes

 ** [TicketId](#API_StartMatchmaking_RequestSyntax) **   <a name="gameliftservers-StartMatchmaking-request-TicketId"></a>
A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift Servers will generate one in the form of a UUID. Use this identifier to track the matchmaking ticket status and retrieve match results.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: No

## Response Syntax
<a name="API_StartMatchmaking_ResponseSyntax"></a>

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
<a name="API_StartMatchmaking_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MatchmakingTicket](#API_StartMatchmaking_ResponseSyntax) **   <a name="gameliftservers-StartMatchmaking-response-MatchmakingTicket"></a>
Ticket representing the matchmaking request. This object include the information included in the request, ticket status, and match results as generated during the matchmaking process.
Type: [MatchmakingTicket](API_MatchmakingTicket.md) object

## Errors
<a name="API_StartMatchmaking_Errors"></a>

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
<a name="API_StartMatchmaking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/StartMatchmaking)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/StartMatchmaking)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/StartMatchmaking)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/StartMatchmaking)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/StartMatchmaking)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/StartMatchmaking)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/StartMatchmaking)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/StartMatchmaking)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/StartMatchmaking)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/StartMatchmaking)
