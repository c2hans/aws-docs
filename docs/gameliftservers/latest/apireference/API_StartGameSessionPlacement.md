---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartGameSessionPlacement.html
---

# StartGameSessionPlacement
<a name="API_StartGameSessionPlacement"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Makes a request to start a new game session using a game session queue. When processing a placement request, Amazon GameLift Servers looks for the best possible available resource to host the game session, based on how the queue is configured to prioritize factors such as resource cost, latency, and location. After selecting an available resource, Amazon GameLift Servers prompts the resource to start a game session. A placement request can include a list of players to create a set of player sessions. The request can also include information to pass to the new game session, such as to specify a game map or other options.

 **Request options**

Use this operation to make the following types of requests.
+ Request a placement using the queue's default prioritization process (see the default prioritization described in [PriorityConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_PriorityConfiguration.html)). Include these required parameters:
  +  `GameSessionQueueName`
  +  `MaximumPlayerSessionCount`
  +  `PlacementID`
+ Request a placement and prioritize based on latency. Include these parameters:
  + Required parameters `GameSessionQueueName`, `MaximumPlayerSessionCount`, `PlacementID`.
  +  `PlayerLatencies`. Include a set of latency values for destinations in the queue. When a request includes latency data, Amazon GameLift Servers automatically reorder the queue's locations priority list based on lowest available latency values. If a request includes latency data for multiple players, Amazon GameLift Servers calculates each location's average latency for all players and reorders to find the lowest latency across all players. To obtain accurate latency measurements, use Amazon GameLift Servers's UDP ping beacons. These endpoints allow you to measure actual UDP network latency between player devices and potential hosting locations, resulting in more accurate placement decisions than using ICMP pings. For more information on using UDP ping beacons to measure latency, refer to [UDP ping beacons](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-udp-ping-beacons.html) in the Amazon GameLift Servers Developer Guide.
  + Don't include `PriorityConfigurationOverride`.
  + Prioritize based on a custom list of locations. If you're using a queue that's configured to prioritize location first (see [PriorityConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_PriorityConfiguration.html) for game session queues), you can optionally use the *PriorityConfigurationOverride* parameter to substitute a different location priority list for this placement request. Amazon GameLift Servers searches each location on the priority override list to find an available hosting resource for the new game session. Specify a fallback strategy to use in the event that Amazon GameLift Servers fails to place the game session in any of the locations on the override list.
+ Request a placement and prioritized based on a custom list of locations.
+ You can request new player sessions for a group of players. Include the *DesiredPlayerSessions* parameter and include at minimum a unique player ID for each. You can also include player-specific data to pass to the new game session.

 **Result**

If successful, this operation generates a new game session placement request and adds it to the game session queue for processing. You can track the status of individual placement requests by calling [DescribeGameSessionPlacement](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessionPlacement.html) or by monitoring queue notifications. When the request status is `FULFILLED`, a new game session has started and the placement request is updated with connection information for the game session (IP address and port). If the request included player session data, Amazon GameLift Servers creates a player session for each player ID in the request.

The request results in a `InvalidRequestException` in the following situations:
+ If the request includes both *PlayerLatencies* and *PriorityConfigurationOverride* parameters.
+ If the request includes the *PriorityConfigurationOverride* parameter and specifies a queue that doesn't prioritize locations.

Amazon GameLift Servers continues to retry each placement request until it reaches the queue's timeout setting. If a request times out, you can resubmit the request to the same queue or try a different queue.

## Request Syntax
<a name="API_StartGameSessionPlacement_RequestSyntax"></a>

```
{
   "DesiredPlayerSessions": [
      {
         "PlayerData": "{{string}}",
         "PlayerId": "{{string}}"
      }
   ],
   "GameProperties": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "GameSessionData": "{{string}}",
   "GameSessionName": "{{string}}",
   "GameSessionQueueName": "{{string}}",
   "MaximumPlayerSessionCount": {{number}},
   "PlacementId": "{{string}}",
   "PlayerLatencies": [
      {
         "LatencyInMilliseconds": {{number}},
         "PlayerId": "{{string}}",
         "RegionIdentifier": "{{string}}"
      }
   ],
   "PriorityConfigurationOverride": {
      "LocationOrder": [ "{{string}}" ],
      "PlacementFallbackStrategy": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_StartGameSessionPlacement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameSessionQueueName](#API_StartGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-request-GameSessionQueueName"></a>
Name of the queue to use to place the new game session. You can use either the queue name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]+|^arn:.*:gamesessionqueue\/[a-zA-Z0-9-]+`
Required: Yes

 ** [MaximumPlayerSessionCount](#API_StartGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-request-MaximumPlayerSessionCount"></a>
The maximum number of players that can be connected simultaneously to the game session.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** [PlacementId](#API_StartGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-request-PlacementId"></a>
A unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all Regions and cannot be reused.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [DesiredPlayerSessions](#API_StartGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-request-DesiredPlayerSessions"></a>
Set of information on each player to create a player session for.
Type: Array of [DesiredPlayerSession](API_DesiredPlayerSession.md) objects
Required: No

 ** [GameProperties](#API_StartGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-request-GameProperties"></a>
A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}`.
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
Type: Array of [GameProperty](API_GameProperty.md) objects
Array Members: Maximum number of 16 items.
Required: No

 ** [GameSessionData](#API_StartGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-request-GameSessionData"></a>
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: No

 ** [GameSessionName](#API_StartGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-request-GameSessionName"></a>
A descriptive label that is associated with a game session. Session names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [PlayerLatencies](#API_StartGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-request-PlayerLatencies"></a>
A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to a fleet location (AWS Regions or custom locations for Amazon GameLift Servers Anywhere fleets). This information is used to try to place the new game session where it can offer the best possible gameplay experience for the players. To obtain accurate latency measurements, use Amazon GameLift Servers's UDP ping beacons. These endpoints allow you to measure actual UDP network latency between player devices and potential hosting locations, resulting in more accurate placement decisions than using ICMP pings. For more information on using UDP ping beacons to measure latency, refer to [UDP ping beacons](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-udp-ping-beacons.html) in the Amazon GameLift Servers Developer Guide.
Type: Array of [PlayerLatency](API_PlayerLatency.md) objects
Required: No

 ** [PriorityConfigurationOverride](#API_StartGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-request-PriorityConfigurationOverride"></a>
A prioritized list of locations to use for the game session placement and instructions on how to use it. This list overrides a queue's prioritized location list for this game session placement request only. You can include AWS Regions, local zones, and custom locations (for Anywhere fleets). You can choose to limit placements to locations on the override list only, or you can prioritize locations on the override list first and then fall back to the queue's other locations if needed. Choose a fallback strategy to use in the event that Amazon GameLift Servers fails to place a game session in any of the locations on the priority override list.
Type: [PriorityConfigurationOverride](API_PriorityConfigurationOverride.md) object
Required: No

## Response Syntax
<a name="API_StartGameSessionPlacement_ResponseSyntax"></a>

```
{
   "GameSessionPlacement": {
      "DnsName": "string",
      "EndTime": number,
      "GameProperties": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "GameSessionArn": "string",
      "GameSessionData": "string",
      "GameSessionId": "string",
      "GameSessionName": "string",
      "GameSessionQueueName": "string",
      "GameSessionRegion": "string",
      "IpAddress": "string",
      "MatchmakerData": "string",
      "MaximumPlayerSessionCount": number,
      "PlacedPlayerSessions": [
         {
            "PlayerId": "string",
            "PlayerSessionId": "string"
         }
      ],
      "PlacementId": "string",
      "PlayerGatewayStatus": "string",
      "PlayerLatencies": [
         {
            "LatencyInMilliseconds": number,
            "PlayerId": "string",
            "RegionIdentifier": "string"
         }
      ],
      "Port": number,
      "PriorityConfigurationOverride": {
         "LocationOrder": [ "string" ],
         "PlacementFallbackStrategy": "string"
      },
      "StartTime": number,
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_StartGameSessionPlacement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSessionPlacement](#API_StartGameSessionPlacement_ResponseSyntax) **   <a name="gameliftservers-StartGameSessionPlacement-response-GameSessionPlacement"></a>
Object that describes the newly created game session placement. This object includes all the information provided in the request, as well as start/end time stamps and placement status.
Type: [GameSessionPlacement](API_GameSessionPlacement.md) object

## Errors
<a name="API_StartGameSessionPlacement_Errors"></a>

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

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_StartGameSessionPlacement_Examples"></a>

### Request a new game session placement with player latency data
<a name="API_StartGameSessionPlacement_Example_1"></a>

This example starts a new game session placement. The request calls for player sessions for two players, and provides each player's latency data for two Regions.

Amazon GameLift Servers uses the latency data provided to determine what order to use when looking for a fleet to host the new game session. It does this by calculating the average player latency for each Region and ordering the queue's destinations starting with the lowest average latency. If the queue "matchmaker-queue" has a latency policy, however, things may change. For example, let's say matchmaker-queue has a policy that caps latency at 130 milliseconds for 60 seconds, followed by no cap. In this scenario, using the sample request below, the following sequence plays out:

1. Amazon GameLift Servers calculates average latency for each Region: `us-east-1` = 110 and `us-west-2` = 100.

1. Amazon GameLift Servers reorders the queue's destinations based on lowest average latency, and prioritizes destinations in Region `us-west-2`.

1. The queue has a latency cap of 130 ms in force for the first 60 seconds of a placement. Amazon GameLift Servers looks for any individual latency values that are greater than 130 ms. There is one: Player 2 reports a 150 ms latency when connected to Region `us-west-2`. As a result, Amazon GameLift Servers temporarily drops all `us-west-2` fleets as valid destinations.

1. Amazon GameLift Servers tries to place the new game session on fleets in Region `us-east-1`, followed by fleets in Regions with no latency information (if any). If available resources are found, the game session is placed and the request fulfilled.

1. If no available resources are found, Amazon GameLift Servers starts a new round of placement attempts, restarting at step 3. If 60 seconds have passed and the latency policy is no longer in force, then fleets in Region `us-west-2` are once more valid destinations -- and are preferred based on their low average latency.

1. Amazon GameLift Servers continues to attempt to place the new game session until it is successful or until the queue's timeout limit is reached.

#### Sample Request
<a name="API_StartGameSessionPlacement_Example_1_Request"></a>

```
{
   "DesiredPlayerSessions": [
      { "PlayerData": "level:10", "PlayerId": "player1" },
      { "PlayerData": "level:11", "PlayerId": "player2" }
   ],
   "GameProperties": [
      { "Key": "map", "Value": "winter" }
   ],
   "GameSessionName": "matchmaker-1234567890",
   "GameSessionQueueName": "matchmaker-queue",
   "MaximumPlayerSessionCount": 4,
   "PlacementId": "Place-12345",
   "PlayerLatencies": [
      { "LatencyInMilliseconds": 100, "PlayerId": "player1", "RegionIdentifier": "us-east-1" },
      { "LatencyInMilliseconds":  50, "PlayerId": "player1", "RegionIdentifier": "us-west-2" },
      { "LatencyInMilliseconds": 120, "PlayerId": "player2", "RegionIdentifier": "us-east-1" },
      { "LatencyInMilliseconds": 150, "PlayerId": "player2", "RegionIdentifier": "us-west-2" }
   ]
}
```

### Request a game session placement with priority configuration override
<a name="API_StartGameSessionPlacement_Example_2"></a>

This example requests a game session placement using an alternate list of location priorities.

Amazon GameLift Servers uses the priority configuration override to change how it searches a queue's destinations when looking for a resource to host the new game session. The queue "custom-locations" has a `PriorityConfiguration` setting that prioritizes locations first and includes a prioritized location list. For this one placement request only, that list is overridden with the list in *PriorityConfigurationOverride*. The following sequence plays out:

1. Amazon GameLift Servers looks for the first location on the override list (`us-west-2`) in each destination in the queue, using the queue's destination priority order. In each fleet location, it searches for an available hosting resource. When one is found, the game session is placed and the request fulfilled.

1. If no available resources are found in the first location, Amazon GameLift Servers looks at destinations for the next location on the override list. and so on. As soon as an available resource is found, the game session is placed and the search stops.

1. If Amazon GameLift Servers searches all locations on the override list and finds no available resources, the first placement pass has failed. Because this placement request specified no fallback strategy, Amazon GameLift Servers doesn't look at any additional queue locations. The placement request remains in the queue and is processed again in turn until a placement succeeds or until the queue's timeout limit is reached.

#### Sample Request
<a name="API_StartGameSessionPlacement_Example_2_Request"></a>

```
{
   "GameSessionName": "customlocations-1234567890",
   "GameSessionQueueName": "custom-locations",
   "MaximumPlayerSessionCount": 4,
   "PlacementId": "Place-12345",
   "PriorityConfigurationOverride": {
      "LocationOrder": ["us-west-2", "us-east-1"],
      "PlacementFallbackStrategy":  "NONE"
   }
}
```

## See Also
<a name="API_StartGameSessionPlacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/StartGameSessionPlacement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/StartGameSessionPlacement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/StartGameSessionPlacement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/StartGameSessionPlacement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/StartGameSessionPlacement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/StartGameSessionPlacement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/StartGameSessionPlacement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/StartGameSessionPlacement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/StartGameSessionPlacement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/StartGameSessionPlacement)
