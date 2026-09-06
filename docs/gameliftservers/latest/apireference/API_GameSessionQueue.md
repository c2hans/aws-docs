---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameSessionQueue.html
---

# GameSessionQueue
<a name="API_GameSessionQueue"></a>

Configuration for a game session placement mechanism that processes requests for new game sessions. A queue can be used on its own or as part of a matchmaking solution.

## Contents
<a name="API_GameSessionQueue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomEventData **   <a name="gameliftservers-Type-GameSessionQueue-CustomEventData"></a>
 Information that is added to all events that are related to this game session queue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Destinations **   <a name="gameliftservers-Type-GameSessionQueue-Destinations"></a>
A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.
Type: Array of [GameSessionQueueDestination](API_GameSessionQueueDestination.md) objects
Required: No

 ** FilterConfiguration **   <a name="gameliftservers-Type-GameSessionQueue-FilterConfiguration"></a>
A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of AWS Region codes, such as `us-west-2`. If this parameter is not set, game sessions can be placed in any queue location.
Type: [FilterConfiguration](API_FilterConfiguration.md) object
Required: No

 ** GameSessionQueueArn **   <a name="gameliftservers-Type-GameSessionQueue-GameSessionQueueArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`. In a Amazon GameLift Servers game session queue ARN, the resource ID matches the *Name* value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:.*:gamesessionqueue\/[a-zA-Z0-9-]+`
Required: No

 ** Name **   <a name="gameliftservers-Type-GameSessionQueue-Name"></a>
A descriptive label that is associated with game session queue. Queue names must be unique within each Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** NotificationTarget **   <a name="gameliftservers-Type-GameSessionQueue-NotificationTarget"></a>
An SNS topic ARN that is set up to receive game session placement notifications. See [ Setting up notifications for game session placement](https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `[a-zA-Z0-9:_-]*(\.fifo)?`
Required: No

 ** PlayerLatencyPolicies **   <a name="gameliftservers-Type-GameSessionQueue-PlayerLatencyPolicies"></a>
A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value.
Type: Array of [PlayerLatencyPolicy](API_PlayerLatencyPolicy.md) objects
Required: No

 ** PriorityConfiguration **   <a name="gameliftservers-Type-GameSessionQueue-PriorityConfiguration"></a>
Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.
Type: [PriorityConfiguration](API_PriorityConfiguration.md) object
Required: No

 ** TimeoutInSeconds **   <a name="gameliftservers-Type-GameSessionQueue-TimeoutInSeconds"></a>
The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a `TIMED_OUT` status.
The minimum value is 10 and the maximum value is 600.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_GameSessionQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameSessionQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameSessionQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameSessionQueue)
