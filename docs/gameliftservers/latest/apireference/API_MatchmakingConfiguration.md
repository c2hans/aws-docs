---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_MatchmakingConfiguration.html
---

# MatchmakingConfiguration
<a name="API_MatchmakingConfiguration"></a>

Guidelines for use with FlexMatch to match players into games. All matchmaking requests must specify a matchmaking configuration.

## Contents
<a name="API_MatchmakingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AcceptanceRequired **   <a name="gameliftservers-Type-MatchmakingConfiguration-AcceptanceRequired"></a>
A flag that indicates whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE. When this option is enabled, matchmaking tickets use the status `REQUIRES_ACCEPTANCE` to indicate when a completed potential match is waiting for player acceptance.
Type: Boolean
Required: No

 ** AcceptanceTimeoutSeconds **   <a name="gameliftservers-Type-MatchmakingConfiguration-AcceptanceTimeoutSeconds"></a>
The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600.
Required: No

 ** AdditionalPlayerCount **   <a name="gameliftservers-Type-MatchmakingConfiguration-AdditionalPlayerCount"></a>
The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used when `FlexMatchMode` is set to `STANDALONE`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** BackfillMode **   <a name="gameliftservers-Type-MatchmakingConfiguration-BackfillMode"></a>
The method used to backfill game sessions created with this matchmaking configuration. MANUAL indicates that the game makes backfill requests or does not use the match backfill feature. AUTOMATIC indicates that GameLift creates backfill requests whenever a game session has one or more open slots. Learn more about manual and automatic backfill in [Backfill existing games with FlexMatch](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html). Automatic backfill is not available when `FlexMatchMode` is set to `STANDALONE`.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

 ** ConfigurationArn **   <a name="gameliftservers-Type-MatchmakingConfiguration-ConfigurationArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers matchmaking configuration resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::matchmakingconfiguration/<matchmaking configuration name>`. In a Amazon GameLift Servers configuration ARN, the resource ID matches the *Name* value.
Type: String
Pattern: `^arn:.*:matchmakingconfiguration\/[a-zA-Z0-9-\.]*`
Required: No

 ** CreationTime **   <a name="gameliftservers-Type-MatchmakingConfiguration-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** CustomEventData **   <a name="gameliftservers-Type-MatchmakingConfiguration-CustomEventData"></a>
Information to attach to all events related to the matchmaking configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** Description **   <a name="gameliftservers-Type-MatchmakingConfiguration-Description"></a>
A descriptive label that is associated with matchmaking configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** FlexMatchMode **   <a name="gameliftservers-Type-MatchmakingConfiguration-FlexMatchMode"></a>
Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution.
+  **STANDALONE** - FlexMatch forms matches and returns match information, including players and team assignments, in a [ MatchmakingSucceeded](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded) event.
+  **WITH\_QUEUE** - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match.
Type: String
Valid Values: `STANDALONE | WITH_QUEUE`
Required: No

 ** GameProperties **   <a name="gameliftservers-Type-MatchmakingConfiguration-GameProperties"></a>
A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}`. This information is added to the new `GameSession` object that is created for a successful match. This parameter is not used when `FlexMatchMode` is set to `STANDALONE`.
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
Type: Array of [GameProperty](API_GameProperty.md) objects
Array Members: Maximum number of 16 items.
Required: No

 ** GameSessionData **   <a name="gameliftservers-Type-MatchmakingConfiguration-GameSessionData"></a>
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession). This information is added to the new `GameSession` object that is created for a successful match. This parameter is not used when `FlexMatchMode` is set to `STANDALONE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** GameSessionQueueArns **   <a name="gameliftservers-Type-MatchmakingConfiguration-GameSessionQueueArns"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`. Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. This property is not set when `FlexMatchMode` is set to `STANDALONE`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** Name **   <a name="gameliftservers-Type-MatchmakingConfiguration-Name"></a>
A unique identifier for the matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: No

 ** NotificationTarget **   <a name="gameliftservers-Type-MatchmakingConfiguration-NotificationTarget"></a>
An SNS topic ARN that is set up to receive matchmaking notifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `[a-zA-Z0-9:_/-]*(.fifo)?`
Required: No

 ** RequestTimeoutSeconds **   <a name="gameliftservers-Type-MatchmakingConfiguration-RequestTimeoutSeconds"></a>
The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 43200.
Required: No

 ** RuleSetArn **   <a name="gameliftservers-Type-MatchmakingConfiguration-RuleSetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) associated with the GameLift matchmaking rule set resource that this configuration uses.
Type: String
Pattern: `^arn:.*:matchmakingruleset\/[a-zA-Z0-9-\.]*`
Required: No

 ** RuleSetName **   <a name="gameliftservers-Type-MatchmakingConfiguration-RuleSetName"></a>
A unique identifier for the matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same Region.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: No

## See Also
<a name="API_MatchmakingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/MatchmakingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/MatchmakingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/MatchmakingConfiguration)
