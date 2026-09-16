---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateMatchmakingConfiguration.html
---

# CreateMatchmakingConfiguration
<a name="API_CreateMatchmakingConfiguration"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Defines a new matchmaking configuration for use with FlexMatch. Whether your are using FlexMatch with Amazon GameLift Servers hosting or as a standalone matchmaking service, the matchmaking configuration sets out rules for matching players and forming teams. If you're also using Amazon GameLift Servers hosting, it defines how to start game sessions for each match. Your matchmaking system can use multiple configurations to handle different game scenarios. All matchmaking requests identify the matchmaking configuration to use and provide player attributes consistent with that configuration.

To create a matchmaking configuration, you must provide the following: configuration name and FlexMatch mode (with or without Amazon GameLift Servers hosting); a rule set that specifies how to evaluate players and find acceptable matches; whether player acceptance is required; and the maximum time allowed for a matchmaking attempt. When using FlexMatch with Amazon GameLift Servers hosting, you also need to identify the game session queue to use when starting a game session for the match.

In addition, you must set up an Amazon Simple Notification Service topic to receive matchmaking notifications. Provide the topic ARN in the matchmaking configuration.

 **Learn more**

 [ Design a FlexMatch matchmaker](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html)

 [ Set up FlexMatch event notification](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html)

## Request Syntax
<a name="API_CreateMatchmakingConfiguration_RequestSyntax"></a>

```
{
   "AcceptanceRequired": {{boolean}},
   "AcceptanceTimeoutSeconds": {{number}},
   "AdditionalPlayerCount": {{number}},
   "BackfillMode": "{{string}}",
   "CustomEventData": "{{string}}",
   "Description": "{{string}}",
   "FlexMatchMode": "{{string}}",
   "GameProperties": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "GameSessionData": "{{string}}",
   "GameSessionQueueArns": [ "{{string}}" ],
   "Name": "{{string}}",
   "NotificationTarget": "{{string}}",
   "RequestTimeoutSeconds": {{number}},
   "RuleSetName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateMatchmakingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AcceptanceRequired](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-AcceptanceRequired"></a>
A flag that determines whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to `TRUE`. With this option enabled, matchmaking tickets use the status `REQUIRES_ACCEPTANCE` to indicate when a completed potential match is waiting for player acceptance.
Type: Boolean
Required: Yes

 ** [Name](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-Name"></a>
A unique identifier for the matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: Yes

 ** [RequestTimeoutSeconds](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-RequestTimeoutSeconds"></a>
The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 43200.
Required: Yes

 ** [RuleSetName](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-RuleSetName"></a>
A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingruleset\/[a-zA-Z0-9-\.]*`
Required: Yes

 ** [AcceptanceTimeoutSeconds](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-AcceptanceTimeoutSeconds"></a>
The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600.
Required: No

 ** [AdditionalPlayerCount](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-AdditionalPlayerCount"></a>
The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used if `FlexMatchMode` is set to `STANDALONE`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [BackfillMode](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-BackfillMode"></a>
The method used to backfill game sessions that are created with this matchmaking configuration. Specify `MANUAL` when your game manages backfill requests manually or does not use the match backfill feature. Specify `AUTOMATIC` to have Amazon GameLift Servers create a backfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in [ Backfill Existing Games with FlexMatch](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html). Automatic backfill is not available when `FlexMatchMode` is set to `STANDALONE`.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

 ** [CustomEventData](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-CustomEventData"></a>
Information to be added to all events related to this matchmaking configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Description](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-Description"></a>
A human-readable description of the matchmaking configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [FlexMatchMode](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-FlexMatchMode"></a>
Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution.
+  **STANDALONE** - FlexMatch forms matches and returns match information, including players and team assignments, in a [ MatchmakingSucceeded](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded) event.
+  **WITH\_QUEUE** - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match.
Type: String
Valid Values: `STANDALONE | WITH_QUEUE`
Required: No

 ** [GameProperties](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-GameProperties"></a>
A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}`. This information is added to the new `GameSession` object that is created for a successful match. This parameter is not used if `FlexMatchMode` is set to `STANDALONE`.
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
Type: Array of [GameProperty](API_GameProperty.md) objects
Array Members: Maximum number of 16 items.
Required: No

 ** [GameSessionData](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-GameSessionData"></a>
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession). This information is added to the new `GameSession` object that is created for a successful match. This parameter is not used if `FlexMatchMode` is set to `STANDALONE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [GameSessionQueueArns](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-GameSessionQueueArns"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`. Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. If `FlexMatchMode` is set to `STANDALONE`, do not set this parameter.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** [NotificationTarget](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-NotificationTarget"></a>
An SNS topic ARN that is set up to receive matchmaking notifications. See [ Setting up notifications for matchmaking](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html) for more information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `[a-zA-Z0-9:_/-]*(.fifo)?`
Required: No

 ** [Tags](#API_CreateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-request-Tags"></a>
A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateMatchmakingConfiguration_ResponseSyntax"></a>

```
{
   "Configuration": {
      "AcceptanceRequired": boolean,
      "AcceptanceTimeoutSeconds": number,
      "AdditionalPlayerCount": number,
      "BackfillMode": "string",
      "ConfigurationArn": "string",
      "CreationTime": number,
      "CustomEventData": "string",
      "Description": "string",
      "FlexMatchMode": "string",
      "GameProperties": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "GameSessionData": "string",
      "GameSessionQueueArns": [ "string" ],
      "Name": "string",
      "NotificationTarget": "string",
      "RequestTimeoutSeconds": number,
      "RuleSetArn": "string",
      "RuleSetName": "string"
   }
}
```

## Response Elements
<a name="API_CreateMatchmakingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Configuration](#API_CreateMatchmakingConfiguration_ResponseSyntax) **   <a name="gameliftservers-CreateMatchmakingConfiguration-response-Configuration"></a>
Object that describes the newly created matchmaking configuration.
Type: [MatchmakingConfiguration](API_MatchmakingConfiguration.md) object

## Errors
<a name="API_CreateMatchmakingConfiguration_Errors"></a>

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

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_CreateMatchmakingConfiguration_Examples"></a>

### Create a matchmaking configuration for use with GameLift managed hosting
<a name="API_CreateMatchmakingConfiguration_Example_1"></a>

The following example creates a matchmaking configuration for a game that is being hosted on Amazon GameLift Servers servers, identifying a game session queue and providing a set of game properties to be passed on to new game sessions. Player acceptance is required, with a 60-second timeout, and auto-backfill is enabled.

#### Sample Request
<a name="API_CreateMatchmakingConfiguration_Example_1_Request"></a>

```
{
    "Name": "MM-1v1",
    "Description": "Head-to-head sprint format",
    "RequestTimeoutSeconds": 120,
    "RuleSetName": "mm_one_v_one",
    "NotificationTarget": "arn:aws:sns:us-west-2:111122223333:My_Matchmaking_SNS_Topic",
    "FlexMatchMode": "WITH_QUEUE",
    "GameSessionQueueArns": "arn:aws:gamelift:us-west-2:111122223333:gamesessionqueue/My_Game_Session_Queue_One",
    "AcceptanceRequired": true,
    "AcceptanceTimeoutSeconds": 60,
    "BackfillMode": "AUTOMATIC",
    "AdditionalPlayerCount": 8,
    "GameProperties": [
      {
          "Key": "level",
          "Value": "10"
      },
      {
          "Key": "difficulty",
          "Value": "hard"
      }
    ]
}
```

#### Sample Response
<a name="API_CreateMatchmakingConfiguration_Example_1_Response"></a>

```
{
   "Configuration": {
      "AcceptanceRequired": true,
      "AcceptanceTimeoutSeconds": 60,
      "AdditionalPlayerCount": 8,
      "BackfillMode": "AUTOMATIC",
      "ConfigurationArn": "arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MM-1v1",
      "CreationTime": 1496365885.44,
      "Description": "Head-to-head sprint format",
      "FlexMatchMode": "WITH_QUEUE",
      "GameProperties": [
        {
            "Key": "level",
            "Value": "10"
        },
        {
            "Key": "difficulty",
            "Value": "hard"
        }
      ],
      "GameSessionQueueArns": "arn:aws:gamelift:us-west-2:111122223333:gamesessionqueue/My_Game_Session_Queue_One",
      "Name": "MM-1v1",
      "NotificationTarget": "arn:aws:sns:us-west-2:111122223333:My_Matchmaking_SNS_Topic",
      "RequestTimeoutSeconds": 120,
      "RuleSetArn": "arn:aws:gamelift:us-west-2:111122223333:matchmakingruleset/mm_one_v_one",
      "RuleSetName": "mm_one_v_one"
   }
}
}
```

### Create a matchmaking configuration for a standalone FlexMatch system
<a name="API_CreateMatchmakingConfiguration_Example_2"></a>

The following example creates a matchmaking configuration for a game that is hosted on resources other than Amazon GameLift Servers game servers. This includes games that are hosted on Amazon EC2 with Amazon GameLift Servers FleetIQ. This configuration omits the game session queue, game properties, and additional player count. Player acceptance is required, with a 60-second timeout.

#### Sample Request
<a name="API_CreateMatchmakingConfiguration_Example_2_Request"></a>

```
{
    "Name": "MM-1v1",
    "Description": "Head-to-head sprint format",
    "RequestTimeoutSeconds": 120,
    "RuleSetName": "mm_one_v_one",
    "NotificationTarget": "arn:aws:sns:us-west-2:111122223333:My_Matchmaking_SNS_Topic",
    "FlexMatchMode": "STANDALONE",
    "AcceptanceRequired": true,
    "AcceptanceTimeoutSeconds": 60,
    "BackfillMode": "MANUAL"
}
```

#### Sample Response
<a name="API_CreateMatchmakingConfiguration_Example_2_Response"></a>

```
{
   "Configuration": {
      "AcceptanceRequired": true,
      "AcceptanceTimeoutSeconds": 60,
      "AdditionalPlayerCount": 0,
      "BackfillMode": "MANUAL",
      "ConfigurationArn": "arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MM-1v1",
      "CreationTime": 1496365885.44,
      "Description": "Head-to-head sprint format",
      "FlexMatchMode": "STANDALONE",
      "GameSessionQueueArns": "",
      "Name": "MM-1v1",
      "NotificationTarget": "arn:aws:sns:us-west-2:111122223333:My_Matchmaking_SNS_Topic",
      "RequestTimeoutSeconds": 120,
      "RuleSetArn": "arn:aws:gamelift:us-west-2:111122223333:matchmakingruleset/mm_one_v_one",
      "RuleSetName": "mm_one_v_one"
   }
}
}
```

## See Also
<a name="API_CreateMatchmakingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateMatchmakingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateMatchmakingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateMatchmakingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateMatchmakingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateMatchmakingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateMatchmakingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateMatchmakingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateMatchmakingConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateMatchmakingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateMatchmakingConfiguration)
