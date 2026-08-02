---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameSessionQueue.html
---

# CreateGameSessionQueue
<a name="API_CreateGameSessionQueue"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Creates a placement queue that processes requests for new game sessions. A queue uses FleetIQ algorithms to locate the best available placement locations for a new game session, and then prompts the game server process to start a new game session.

A game session queue is configured with a set of destinations (Amazon GameLift Servers fleets or aliases) that determine where the queue can place new game sessions. These destinations can span multiple AWS Regions, can use different instance types, and can include both Spot and On-Demand fleets. If the queue includes multi-location fleets, the queue can place game sessions in any of a fleet's remote locations.

You can configure a queue to determine how it selects the best available placement for a new game session. Queues can prioritize placement decisions based on a combination of location, hosting cost, and player latency. You can set up the queue to use the default prioritization or provide alternate instructions using `PriorityConfiguration`.

 **Request options**

Use this operation to make these common types of requests.
+ Create a queue with the minimum required parameters.
  +  `Name`
  +  `Destinations` (This parameter isn't required, but a queue can't make placements without at least one destination.)
+ Create a queue with placement notification. Queues that have high placement activity must use a notification system, such as with Amazon Simple Notification Service (Amazon SNS) or Amazon CloudWatch.
  + Required parameters `Name` and `Destinations`
  +  `NotificationTarget`
+ Create a queue with custom prioritization settings. These custom settings replace the default prioritization configuration for a queue.
  + Required parameters `Name` and `Destinations`
  +  `PriorityConfiguration`
+ Create a queue with special rules for processing player latency data.
  + Required parameters `Name` and `Destinations`
  +  `PlayerLatencyPolicies`

 **Results**

If successful, this operation returns a new `GameSessionQueue` object with an assigned queue ARN. Use the queue's name or ARN when submitting new game session requests with [StartGameSessionPlacement](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartGameSessionPlacement.html) or [StartMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartMatchmaking.html).

 **Learn more**

 [ Design a game session queue](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-design.html)

 [ Create a game session queue](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-creating.html)

 **Related actions**

 [CreateGameSessionQueue](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateGameSessionQueue.html) \| [DescribeGameSessionQueues](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessionQueues.html) \| [UpdateGameSessionQueue](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSessionQueue.html) \| [DeleteGameSessionQueue](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeleteGameSessionQueue.html) \| [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_CreateGameSessionQueue_RequestSyntax"></a>

```
{
   "CustomEventData": "{{string}}",
   "Destinations": [
      {
         "DestinationArn": "{{string}}"
      }
   ],
   "FilterConfiguration": {
      "AllowedLocations": [ "{{string}}" ]
   },
   "Name": "{{string}}",
   "NotificationTarget": "{{string}}",
   "PlayerLatencyPolicies": [
      {
         "MaximumIndividualPlayerLatencyMilliseconds": {{number}},
         "PolicyDurationSeconds": {{number}}
      }
   ],
   "PriorityConfiguration": {
      "LocationOrder": [ "{{string}}" ],
      "PriorityOrder": [ "{{string}}" ]
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TimeoutInSeconds": {{number}}
}
```

## Request Parameters
<a name="API_CreateGameSessionQueue_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_CreateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-request-Name"></a>
A descriptive label that is associated with game session queue. Queue names must be unique within each Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [CustomEventData](#API_CreateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-request-CustomEventData"></a>
Information to be added to all events that are related to this game session queue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Destinations](#API_CreateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-request-Destinations"></a>
A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.
Type: Array of [GameSessionQueueDestination](API_GameSessionQueueDestination.md) objects
Required: No

 ** [FilterConfiguration](#API_CreateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-request-FilterConfiguration"></a>
A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of AWS Region codes, such as `us-west-2`. If this parameter is not set, game sessions can be placed in any queue location.
Type: [FilterConfiguration](API_FilterConfiguration.md) object
Required: No

 ** [NotificationTarget](#API_CreateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-request-NotificationTarget"></a>
An SNS topic ARN that is set up to receive game session placement notifications. See [ Setting up notifications for game session placement](https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `[a-zA-Z0-9:_-]*(\.fifo)?`
Required: No

 ** [PlayerLatencyPolicies](#API_CreateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-request-PlayerLatencyPolicies"></a>
A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value.
Type: Array of [PlayerLatencyPolicy](API_PlayerLatencyPolicy.md) objects
Required: No

 ** [PriorityConfiguration](#API_CreateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-request-PriorityConfiguration"></a>
Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.
Type: [PriorityConfiguration](API_PriorityConfiguration.md) object
Required: No

 ** [Tags](#API_CreateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-request-Tags"></a>
A list of labels to assign to the new game session queue resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [TimeoutInSeconds](#API_CreateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-request-TimeoutInSeconds"></a>
The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a `TIMED_OUT` status. If you don't specify a request timeout, the queue uses a default value.
The minimum value is 10 and the maximum value is 600.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_CreateGameSessionQueue_ResponseSyntax"></a>

```
{
   "GameSessionQueue": {
      "CustomEventData": "string",
      "Destinations": [
         {
            "DestinationArn": "string"
         }
      ],
      "FilterConfiguration": {
         "AllowedLocations": [ "string" ]
      },
      "GameSessionQueueArn": "string",
      "Name": "string",
      "NotificationTarget": "string",
      "PlayerLatencyPolicies": [
         {
            "MaximumIndividualPlayerLatencyMilliseconds": number,
            "PolicyDurationSeconds": number
         }
      ],
      "PriorityConfiguration": {
         "LocationOrder": [ "string" ],
         "PriorityOrder": [ "string" ]
      },
      "TimeoutInSeconds": number
   }
}
```

## Response Elements
<a name="API_CreateGameSessionQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSessionQueue](#API_CreateGameSessionQueue_ResponseSyntax) **   <a name="gameliftservers-CreateGameSessionQueue-response-GameSessionQueue"></a>
An object that describes the newly created game session queue.
Type: [GameSessionQueue](API_GameSessionQueue.md) object

## Errors
<a name="API_CreateGameSessionQueue_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** TaggingFailedException **
The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_CreateGameSessionQueue_Examples"></a>

### Create and configure a game session queue
<a name="API_CreateGameSessionQueue_Example_1"></a>

In this example, we want to create a game session queue with two single-location destinations, each residing in different Regions. We configure the queue so that requests for new game sessions expire after 10 minutes. The queue will process game session requests with player latency data, so we provide a set of latency cap polices that initially start at 100mm and then relax to 200ms after one minute. We opt to use the default sort approach for FleetIQ.

#### Sample Request
<a name="API_CreateGameSessionQueue_Example_1_Request"></a>

```
{
    "Name": "matchmaker-queue",
    "Destinations": [
        { "DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d" },
        { "DestinationArn": "arn:aws:gamelift:sa-east-1::fleet/fleet-5c6d3c4d-5e6f-7a8b-9a0b-1e2f3a4b5a2b" }
    ],
    "NotificationTarget": "arn:aws:sns:us-west-2:111122223333:My_Placement_SNS_Topic",
    "PlayerLatencyPolicies": [
        { "MaximumIndividualPlayerLatencyMilliseconds": 200 },
        { "MaximumIndividualPlayerLatencyMilliseconds": 100, "PolicyDurationSeconds": 60 }
    ],
    "TimeoutInSeconds": 600
}
```

#### Sample Response
<a name="API_CreateGameSessionQueue_Example_1_Response"></a>

```
{
    "GameSessionQueue": {
        "Name": "matchmaker-queue",
        "GameSessionQueueArn": "arn:aws:gamelift:us-west-2:111122223333:gamesessionqueue/matchmaker-queue",
        "TimeoutInSeconds": 600,
        "NotificationTarget": "arn:aws:sns:us-west-2:111122223333:My_Placement_SNS_Topic",
        "PlayerLatencyPolicies": [
            {
                "MaximumIndividualPlayerLatencyMilliseconds": 100,
                "PolicyDurationSeconds": 60
            },
            {
                "MaximumIndividualPlayerLatencyMilliseconds": 200
            }
        ],
        "Destinations": [
            {"DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"},
            {"DestinationArn": "arn:aws:gamelift:us-east-1::fleet/fleet-5c6d3c4d-5e6f-7a8b-9c0d-1e2f3a4b5a2b"}
        ]
    }
}
```

### Create a game session queue with multi-location fleets
<a name="API_CreateGameSessionQueue_Example_2"></a>

In this example, we want to create a game session queue to place game sessions with two multi-location Spot fleets and one single-location On-Demand fleet. The multi-location fleets have remote locations in (`us-west-1`, `us-east-2`, `sa-east-1`).

We also want to change how FleetIQ prioritizes destinations and locations for placement. We opt to have FleetIQ prioritize by location first (with a custom location order provided), and then by destination list order. Based on our priority configuration, the queue will always try to place game sessions in the `us-west-1` remote location of the first listed destination fleet. If no game servers are available there, the queue will try to place in the `us-west-1` home Region of the second listed destination fleet, and so on.

#### Sample Request
<a name="API_CreateGameSessionQueue_Example_2_Request"></a>

```
{
    "Name": "matchmaker-queue",
    "Destinations": [
        { "DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d" },
        { "DestinationArn": "arn:aws:gamelift:us-west-1::fleet/fleet-2a3b4c5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d" },
        { "DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-5c6d3c4d-5e6f-7a8b-9a0b-1e2f3a4b5a2b" }
    ],
    "NotificationTarget": "arn:aws:sns:us-west-2:111122223333:My_Placement_SNS_Topic",
    "PriorityConfiguration": {
        "PriorityOrder": "LOCATION,DESTINATION",
        "LocationOrder": "us-west-1,us-west-2,us-east-2, sa-east-1"
    },
    "TimeoutInSeconds": 600
}
```

#### Sample Response
<a name="API_CreateGameSessionQueue_Example_2_Response"></a>

```
{
    "GameSessionQueue": {
        "Name": "matchmaker-queue",
        "GameSessionQueueArn": "arn:aws:gamelift:us-west-2:111122223333:gamesessionqueue/matchmaker-queue",
        "TimeoutInSeconds": 600,
        "Destinations": [
            { "DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d" },
            { "DestinationArn": "arn:aws:gamelift:us-west-1::fleet/fleet-2a3b4c5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d" },
            { "DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-5c6d3c4d-5e6f-7a8b-9a0b-1e2f3a4b5a2b" }
        ],
        "PriorityConfiguration": {
            "PriorityOrder": "LOCATION,DESTINATION",
            "LocationOrder": "us-west-1,us-west-2,us-east-2, sa-east-1"
        },
        "NotificationTarget": "arn:aws:sns:us-west-2:111122223333:My_Placement_SNS_Topic",
    }
}
```

## See Also
<a name="API_CreateGameSessionQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateGameSessionQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateGameSessionQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateGameSessionQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateGameSessionQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateGameSessionQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateGameSessionQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateGameSessionQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateGameSessionQueue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateGameSessionQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateGameSessionQueue)
