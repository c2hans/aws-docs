---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateMatchmakingConfiguration.html
---

# UpdateMatchmakingConfiguration
<a name="API_UpdateMatchmakingConfiguration"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Updates settings for a FlexMatch matchmaking configuration. These changes affect all matches and game sessions that are created after the update. To update settings, specify the configuration name to be updated and provide the new settings.

 **Learn more**

 [ Design a FlexMatch matchmaker](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html)

## Request Syntax
<a name="API_UpdateMatchmakingConfiguration_RequestSyntax"></a>

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
   "RuleSetName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMatchmakingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-Name"></a>
A unique identifier for the matchmaking configuration to update. You can use either the configuration name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingconfiguration\/[a-zA-Z0-9-\.]*`
Required: Yes

 ** [AcceptanceRequired](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-AcceptanceRequired"></a>
A flag that indicates whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE. With this option enabled, matchmaking tickets use the status `REQUIRES_ACCEPTANCE` to indicate when a completed potential match is waiting for player acceptance.
Type: Boolean
Required: No

 ** [AcceptanceTimeoutSeconds](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-AcceptanceTimeoutSeconds"></a>
The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600.
Required: No

 ** [AdditionalPlayerCount](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-AdditionalPlayerCount"></a>
The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used if `FlexMatchMode` is set to `STANDALONE`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [BackfillMode](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-BackfillMode"></a>
The method that is used to backfill game sessions created with this matchmaking configuration. Specify MANUAL when your game manages backfill requests manually or does not use the match backfill feature. Specify AUTOMATIC to have GameLift create a match backfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in [Backfill Existing Games with FlexMatch](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html). Automatic backfill is not available when `FlexMatchMode` is set to `STANDALONE`.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

 ** [CustomEventData](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-CustomEventData"></a>
Information to add to all events related to the matchmaking configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Description](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-Description"></a>
A description for the matchmaking configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [FlexMatchMode](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-FlexMatchMode"></a>
Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution.
+  **STANDALONE** - FlexMatch forms matches and returns match information, including players and team assignments, in a [ MatchmakingSucceeded](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded) event.
+  **WITH\_QUEUE** - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match.
Type: String
Valid Values: `STANDALONE | WITH_QUEUE`
Required: No

 ** [GameProperties](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-GameProperties"></a>
A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}`. This information is added to the new `GameSession` object that is created for a successful match. This parameter is not used if `FlexMatchMode` is set to `STANDALONE`.
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
Type: Array of [GameProperty](API_GameProperty.md) objects
Array Members: Maximum number of 16 items.
Required: No

 ** [GameSessionData](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-GameSessionData"></a>
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession). This information is added to the game session that is created for a successful match. This parameter is not used if `FlexMatchMode` is set to `STANDALONE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [GameSessionQueueArns](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-GameSessionQueueArns"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`. Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. If `FlexMatchMode` is set to `STANDALONE`, do not set this parameter.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** [NotificationTarget](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-NotificationTarget"></a>
An SNS topic ARN that is set up to receive matchmaking notifications. See [ Setting up notifications for matchmaking](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html) for more information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `[a-zA-Z0-9:_/-]*(.fifo)?`
Required: No

 ** [RequestTimeoutSeconds](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-RequestTimeoutSeconds"></a>
The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 43200.
Required: No

 ** [RuleSetName](#API_UpdateMatchmakingConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-request-RuleSetName"></a>
A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingruleset\/[a-zA-Z0-9-\.]*`
Required: No

## Response Syntax
<a name="API_UpdateMatchmakingConfiguration_ResponseSyntax"></a>

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
<a name="API_UpdateMatchmakingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Configuration](#API_UpdateMatchmakingConfiguration_ResponseSyntax) **   <a name="gameliftservers-UpdateMatchmakingConfiguration-response-Configuration"></a>
The updated matchmaking configuration.
Type: [MatchmakingConfiguration](API_MatchmakingConfiguration.md) object

## Errors
<a name="API_UpdateMatchmakingConfiguration_Errors"></a>

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
<a name="API_UpdateMatchmakingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateMatchmakingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateMatchmakingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateMatchmakingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateMatchmakingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateMatchmakingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateMatchmakingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateMatchmakingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateMatchmakingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateMatchmakingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateMatchmakingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
