---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_SearchGameSessions.html
---

# SearchGameSessions
<a name="API_SearchGameSessions"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves all active game sessions that match a set of search criteria and sorts them into a specified order.

This operation is not designed to continually track game session status because that practice can cause you to exceed your API limit and generate errors. Instead, configure an Amazon Simple Notification Service (Amazon SNS) topic to receive notifications from a matchmaker or a game session placement queue.

When searching for game sessions, you specify exactly where you want to search and provide a search filter expression, a sort expression, or both. A search request can search only one fleet, but it can search all of a fleet's locations.

This operation can be used in the following ways:
+ To search all game sessions that are currently running on all locations in a fleet, provide a fleet or alias ID. This approach returns game sessions in the fleet's home Region and all remote locations that fit the search criteria.
+ To search all game sessions that are currently running on a specific fleet location, provide a fleet or alias ID and a location name. For location, you can specify a fleet's home Region or any remote location.

Use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a `GameSession` object is returned for each game session that matches the request. Search finds game sessions that are in `ACTIVE` status only. To retrieve information on game sessions in other statuses, use [DescribeGameSessions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessions.html).

To set search and sort criteria, create a filter expression using the following game session attributes. For game session search examples, see the Examples section of this topic.
+  **gameSessionId** -- An identifier for the game session that is unique across all regions. You must use the full ARN value.
+  **gameSessionName** -- Name assigned to a game session. Game session names do not need to be unique to a game session.
+  **gameSessionProperties** -- A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}`. The filter expression must specify the [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameProperty](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameProperty) -- a `Key` and a string `Value` to search for the game sessions.

  For example, to search for the above key-value pair, specify the following search filter: `gameSessionProperties.difficulty = "novice"`. All game property values are searched as strings.

   For examples of searching game sessions, see the ones below, and also see [Search game sessions by game property](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-search).
**Note**
Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
+  **maximumSessions** -- Maximum number of player sessions allowed for a game session.
+  **creationTimeMillis** -- Value indicating when a game session was created. It is expressed in Unix time as milliseconds.
+  **playerSessionCount** -- Number of players currently connected to a game session. This value changes rapidly as players join the session or drop out.
+  **hasAvailablePlayerSessions** -- Boolean value indicating whether a game session has reached its maximum number of players. It is highly recommended that all search requests include this filter attribute to optimize search performance and return only sessions that players can join.

**Note**
Returned values for `playerSessionCount` and `hasAvailablePlayerSessions` change quickly as players join sessions and others drop out. Results should be considered a snapshot in time. Be sure to refresh search results often, and handle sessions that fill up before a player can join.

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_SearchGameSessions_RequestSyntax"></a>

```
{
   "AliasId": "{{string}}",
   "FilterExpression": "{{string}}",
   "FleetId": "{{string}}",
   "Limit": {{number}},
   "Location": "{{string}}",
   "NextToken": "{{string}}",
   "SortExpression": "{{string}}"
}
```

## Request Parameters
<a name="API_SearchGameSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AliasId](#API_SearchGameSessions_RequestSyntax) **   <a name="gameliftservers-SearchGameSessions-request-AliasId"></a>
A unique identifier for the alias associated with the fleet to search for active game sessions. You can use either the alias ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.
Type: String
Pattern: `^alias-\S+|^arn:.*:alias\/alias-\S+`
Required: No

 ** [FilterExpression](#API_SearchGameSessions_RequestSyntax) **   <a name="gameliftservers-SearchGameSessions-request-FilterExpression"></a>
String containing the search criteria for the session search. If no filter expression is included, the request returns results for all game sessions in the fleet that are in `ACTIVE` status.
A filter expression can contain one or multiple conditions. Each condition consists of the following:
+  **Operand** -- Name of a game session attribute. Valid values are `gameSessionName`, `gameSessionId`, `gameSessionProperties`, `maximumSessions`, `creationTimeMillis`, `playerSessionCount`, `hasAvailablePlayerSessions`.
+  **Comparator** -- Valid comparators are: `=`, `<>`, `<`, `>`, `<=`, `>=`.
+  **Value** -- Value to be searched for. Values may be numbers, boolean values (true/false) or strings depending on the operand. String values are case sensitive and must be enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators `=` and `<>`. For example, the following filter expression searches on `gameSessionName`: "`FilterExpression": "gameSessionName = 'Matt\\'s Awesome Game 1'"`.
To chain multiple conditions in a single expression, use the logical keywords `AND`, `OR`, and `NOT` and parentheses as needed. For example: `x AND y AND NOT z`, `NOT (x OR y)`.
Session search evaluates conditions from left to right using the following precedence rules:

1.  `=`, `<>`, `<`, `>`, `<=`, `>=`

1. Parentheses

1. NOT

1. AND

1. OR
For example, this filter expression retrieves game sessions hosting at least ten players that have an open player slot: `"maximumSessions>=10 AND hasAvailablePlayerSessions=true"`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [FleetId](#API_SearchGameSessions_RequestSyntax) **   <a name="gameliftservers-SearchGameSessions-request-FleetId"></a>
A unique identifier for the fleet to search for active game sessions. You can use either the fleet ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** [Limit](#API_SearchGameSessions_RequestSyntax) **   <a name="gameliftservers-SearchGameSessions-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages. The maximum number of results returned is 20, even if this value is not set or is set higher than 20.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Location](#API_SearchGameSessions_RequestSyntax) **   <a name="gameliftservers-SearchGameSessions-request-Location"></a>
A fleet location to search for game sessions. You can specify a fleet's home Region or a remote location. Use the AWS Region code format, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** [NextToken](#API_SearchGameSessions_RequestSyntax) **   <a name="gameliftservers-SearchGameSessions-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [SortExpression](#API_SearchGameSessions_RequestSyntax) **   <a name="gameliftservers-SearchGameSessions-request-SortExpression"></a>
Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:
+  **Operand** -- Name of a game session attribute. Valid values are `gameSessionName`, `gameSessionId`, `gameSessionProperties`, `maximumSessions`, `creationTimeMillis`, `playerSessionCount`, `hasAvailablePlayerSessions`.
+  **Order** -- Valid sort orders are `ASC` (ascending) and `DESC` (descending).
For example, this sort expression returns the oldest active sessions first: `"SortExpression": "creationTimeMillis ASC"`. Results with a null value for the sort operand are returned at the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_SearchGameSessions_ResponseSyntax"></a>

```
{
   "GameSessions": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchGameSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSessions](#API_SearchGameSessions_ResponseSyntax) **   <a name="gameliftservers-SearchGameSessions-response-GameSessions"></a>
A collection of objects containing game session properties for each session that matches the request.
Type: Array of [GameSession](API_GameSession.md) objects

 ** [NextToken](#API_SearchGameSessions_ResponseSyntax) **   <a name="gameliftservers-SearchGameSessions-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_SearchGameSessions_Errors"></a>

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

 ** TerminalRoutingStrategyException **
The service is unable to resolve the routing for a particular alias because it has a terminal `RoutingStrategy` associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_SearchGameSessions_Examples"></a>

### Search game sessions
<a name="API_SearchGameSessions_Example_1"></a>

In this example, we want to find all game sessions that have at least two players already connected. We also want to filter out active game sessions that are not accepting new players.

This example illustrates a search that includes all of the fleet's locations. The results include a matching game session in the fleet's home Region (`us-west-2`) and another in a remote location (`ca-central-1`).

#### Sample Request
<a name="API_SearchGameSessions_Example_1_Request"></a>

```
    {"AliasId": "MOG-base",
    "FilterExpression": "playerSessionCount>=2 AND hasAvailablePlayerSessions=true",
    "Limit": 2
    }

CLI syntax:
    aws gamelift search-game-sessions --alias-id "MOG-base" --filter-expression "playerSessionCount>=2 AND hasAvailablePlayerSessions=true" --limit 2
```

#### Sample Response
<a name="API_SearchGameSessions_Example_1_Response"></a>

```
{
  "GameSessions": [
    {
        "CreationTime": 1469498468.057,
        "CurrentPlayerSessionCount": 5,
        "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
        "GameProperties": [
            {"Key": "difficulty","Value": "easy"},
            {"Key": "gameMap","Value": "Snowfall"},
            {"Key": "gameMode","Value": "Explore"}
        ],
        "GameSessionId": "arn:aws:gamelift:us-west-2::gamesession/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa/gsess-4444dddd-55ee-66ff-77aa-8888bbbb99cc",
        "IpAddress": "192.0.2.0",
        "MaximumPlayerSessionCount": 10,
        "Name": "Matt's Awesome Game win123",
        "Port": "8080",
        "Status": "ACTIVE",
        "Location": "us-west-2",
        "ComputeName": "i-1234567890abcdef0"
    },
    {
        "CreationTime": 1469498497.792,
        "CurrentPlayerSessionCount": 3,
        "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
        "GameProperties": [
            {"Key": "difficulty","Value": "insane"},
            {"Key": "gameMap","Value": "Dystopia"},
            {"Key": "gameMode","Value": "FFA"}
        ],
        "GameSessionId": "arn:aws:gamelift:ca-central-1::gamesession/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa/gsess-7777dddd-55ee-66ff-44aa-8888bbbb99cc",
        "IpAddress": "192.0.2.0",
        "MaximumPlayerSessionCount": 10,
        "Name": "Matt's Awesome Game  win456",
        "Port": "8080",
        "Status": "ACTIVE",
        "Location": "ca-central-1",
        "ComputeName": "i-0987654321fedcba0"
    }
  ]
}
```

### Search and sort game sessions
<a name="API_SearchGameSessions_Example_2"></a>

In this example, we want to find all game sessions that allow 20 or more players and are currently accepting new players. We want the results to be sorted so that the newest game sessions are returned first.

This example illustrates a search of a single fleet location. The requested fleet, which resides in us-west-2, also has game sessions in remote locations, including `ap-southeast-2`. As shown, the results are limited to the requested fleet location.

#### Sample Request
<a name="API_SearchGameSessions_Example_2_Request"></a>

```
{
    "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "Location": "ap-southeast-2",
    "FilterExpression": "maximumSessions>=20 AND hasAvailablePlayerSessions=true",
    "SortExpression": "creationTimeMillis DESC"
    "Limit": 2
}

CLI syntax:
    aws gamelift search-game-sessions --fleet-id "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa" --location "ap-southeast-2" --filter-expression "maximumSessions=20 AND hasAvailablePlayerSessions=true" --sort-expression "creationTimeMillis DESC"
```

#### Sample Response
<a name="API_SearchGameSessions_Example_2_Response"></a>

```
{
  "GameSessions": [
    {
        "CreationTime": 1469498497.792,
        "CurrentPlayerSessionCount": 3,
        "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
        "GameProperties": [
            {"Key": "difficulty","Value": "hard"},
            {"Key": "gameMap","Value": "Dystopia"},
            {"Key": "gameMode","Value": "Brawl"}
        ],
        "GameSessionId": "arn:aws:gamelift:ap-southeast-2::gamesession/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa/gsess-7777dddd-55ee-66ff-44aa-8888bbbb99cc",
        "IpAddress": "192.0.2.0",
        "MaximumPlayerSessionCount": 20,
        "Name": "Matt's Awesome Game  win456",
        "Port": "8080",
        "Status": "ACTIVE",
        "Location": "ap-southeast-2",
        "ComputeName": "i-abcdef1234567890a"
    },
    {
        "CreationTime": 1469498468.057,
        "CurrentPlayerSessionCount": ,
        "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
        "GameProperties": [
            {"Key": "difficulty","Value": "easy"},
            {"Key": "gameMap","Value": "Snowfall"},
            {"Key": "gameMode","Value": "Explore"}
        ],
        "GameSessionId": "arn:aws:gamelift:ap-southeast-2::gamesession/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa/gsess-4444dddd-55ee-66ff-77aa-8888bbbb99cc",
        "IpAddress": "192.0.2.0",
        "MaximumPlayerSessionCount": 50,
        "Name": "Matt's Awesome Game win123",
        "Port": "8080",
        "Status": "ACTIVE",
        "Location": "ap-southeast-2",
        "ComputeName": "i-fedcba0987654321f"
    }
  ]
}
```

### Search game sessions by custom game properties
<a name="API_SearchGameSessions_Example_3"></a>

This example searches for game sessions based on game map and game mode information, which is stored as key-value pairs in the `GameProperties` of a `GameSession`. In this example, we want to find all game sessions where `gameMode` is `Ffa` (free-for-all), and `gameMap` is either `"Suzuka"` or `"Silverstone"`. We are sorting our results by `gameSessionProperties.difficulty` (with possible values of "novice", "easy", "normal", "hard", or "insane"). Note: `"Value` is evaluated as a string, so the sorted results will be listed by the alphabetic order of the difficulty values.

#### Sample Request
<a name="API_SearchGameSessions_Example_3_Request"></a>

```
{
    "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "Location": "us-west-2",
    "FilterExpression": "gameSessionProperties.gameMode = 'Ffa' AND gameSessionProperties.gameMap = 'Suzuka' OR gameSessionProperties.gameMap = 'Silverstone'",
    "SortExpression": "gameSessionProperties.difficulty ASC"
    "Limit": 2
}

CLI syntax:
    aws gamelift search-game-sessions --fleet-id "9999ffff-88ee-77dd-66cc-5555bbbb44aa" --filter-expression "gameSessionProperties.gameMode = 'Ffa' AND gameSessionProperties.gameMap = 'Suzuka' OR gameSessionProperties.gameMap = 'Silverstone'" --sort-expression "gameSessionProperties.difficulty DESC"
```

#### Sample Response
<a name="API_SearchGameSessions_Example_3_Response"></a>

```
{
  "GameSessions": [
    {
        "CreationTime": 1469498468.057,
        "CurrentPlayerSessionCount": 5,
        "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
        "GameProperties": [
            {"Key": "difficulty","Value": "easy"},
            {"Key": "gameMap","Value": "Suzuka"},
            {"Key": "gameMode","Value": "Ffa"}
        ],
        "GameSessionId": "arn:aws:gamelift:us-west-2::gamesession/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa/gsess-4444dddd-55ee-66ff-77aa-8888bbbb99cc",
        "IpAddress": "192.0.2.0",
        "MaximumPlayerSessionCount": 10,
        "Name": "Matt's Awesome Game win123",
        "Port": "8080",
        "Status": "ACTIVE",
        "Location": "us-west-2",
        "ComputeName": "i-1111222233334444a"
    },
    {
        "CreationTime": 1469498497.792,
        "CurrentPlayerSessionCount": 3,
        "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
        "GameProperties": [
            {"Key": "difficulty","Value": "normal"},
            {"Key": "gameMap","Value": "Silverstone"},
            {"Key": "gameMode","Value": "Ffa"}
        ],
        "GameSessionId": "arn:aws:gamelift:us-west-2::gamesession/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa/gsess-7777dddd-55ee-66ff-44aa-8888bbbb99cc",
        "IpAddress": "192.0.2.0",
        "MaximumPlayerSessionCount": 10,
        "Name": "Matt's Awesome Game  win456",
        "Port": "8080",
        "Status": "ACTIVE",
        "Location": "us-west-2",
        "ComputeName": "i-5555666677778888b"
    }
  ]
}
```

## See Also
<a name="API_SearchGameSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/SearchGameSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/SearchGameSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/SearchGameSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/SearchGameSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/SearchGameSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/SearchGameSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/SearchGameSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/SearchGameSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/SearchGameSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/SearchGameSessions)
