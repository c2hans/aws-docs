---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameSessionQueue.html
---

# UpdateGameSessionQueue
<a name="API_UpdateGameSessionQueue"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Updates the configuration of a game session queue, which determines how the queue processes new game session requests. To update settings, specify the queue name to be updated and provide the new settings. When updating destinations, provide a complete list of destinations.

 **Learn more**

 [ Using Multi-Region Queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html)

## Request Syntax
<a name="API_UpdateGameSessionQueue_RequestSyntax"></a>

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
   "TimeoutInSeconds": {{number}}
}
```

## Request Parameters
<a name="API_UpdateGameSessionQueue_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_UpdateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-UpdateGameSessionQueue-request-Name"></a>
A descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]+|^arn:.*:gamesessionqueue\/[a-zA-Z0-9-]+`
Required: Yes

 ** [CustomEventData](#API_UpdateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-UpdateGameSessionQueue-request-CustomEventData"></a>
Information to be added to all events that are related to this game session queue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Destinations](#API_UpdateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-UpdateGameSessionQueue-request-Destinations"></a>
A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference. When updating this list, provide a complete list of destinations.
Type: Array of [GameSessionQueueDestination](API_GameSessionQueueDestination.md) objects
Required: No

 ** [FilterConfiguration](#API_UpdateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-UpdateGameSessionQueue-request-FilterConfiguration"></a>
A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of AWS Region codes, such as `us-west-2`. If this parameter is not set, game sessions can be placed in any queue location. To remove an existing filter configuration, pass in an empty set.
Type: [FilterConfiguration](API_FilterConfiguration.md) object
Required: No

 ** [NotificationTarget](#API_UpdateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-UpdateGameSessionQueue-request-NotificationTarget"></a>
An SNS topic ARN that is set up to receive game session placement notifications. See [ Setting up notifications for game session placement](https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `[a-zA-Z0-9:_-]*(\.fifo)?`
Required: No

 ** [PlayerLatencyPolicies](#API_UpdateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-UpdateGameSessionQueue-request-PlayerLatencyPolicies"></a>
A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value. When updating policies, provide a complete collection of policies.
Type: Array of [PlayerLatencyPolicy](API_PlayerLatencyPolicy.md) objects
Required: No

 ** [PriorityConfiguration](#API_UpdateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-UpdateGameSessionQueue-request-PriorityConfiguration"></a>
Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process. To remove an existing priority configuration, pass in an empty set.
Type: [PriorityConfiguration](API_PriorityConfiguration.md) object
Required: No

 ** [TimeoutInSeconds](#API_UpdateGameSessionQueue_RequestSyntax) **   <a name="gameliftservers-UpdateGameSessionQueue-request-TimeoutInSeconds"></a>
The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a `TIMED_OUT` status.
The minimum value is 10 and the maximum value is 600.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_UpdateGameSessionQueue_ResponseSyntax"></a>

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
<a name="API_UpdateGameSessionQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSessionQueue](#API_UpdateGameSessionQueue_ResponseSyntax) **   <a name="gameliftservers-UpdateGameSessionQueue-response-GameSessionQueue"></a>
An object that describes the newly updated game session queue.
Type: [GameSessionQueue](API_GameSessionQueue.md) object

## Errors
<a name="API_UpdateGameSessionQueue_Errors"></a>

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

## See Also
<a name="API_UpdateGameSessionQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateGameSessionQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateGameSessionQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateGameSessionQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateGameSessionQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateGameSessionQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateGameSessionQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateGameSessionQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateGameSessionQueue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateGameSessionQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateGameSessionQueue)
