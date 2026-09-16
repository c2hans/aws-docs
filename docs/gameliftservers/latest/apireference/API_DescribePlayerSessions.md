---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribePlayerSessions.html
---

# DescribePlayerSessions
<a name="API_DescribePlayerSessions"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves properties for one or more player sessions.

This action can be used in the following ways:
+ To retrieve a specific player session, provide the player session ID only.
+ To retrieve all player sessions in a game session, provide the game session ID only.
+ To retrieve all player sessions for a specific player, provide a player ID only.

To request player sessions, specify either a player session ID, game session ID, or player ID. You can filter this request by player session status. If you provide a specific `PlayerSessionId` or `PlayerId`, Amazon GameLift Servers ignores the filter criteria. Use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a `PlayerSession` object is returned for each session that matches the request.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_DescribePlayerSessions_RequestSyntax"></a>

```
{
   "GameSessionId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "PlayerId": "{{string}}",
   "PlayerSessionId": "{{string}}",
   "PlayerSessionStatusFilter": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePlayerSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameSessionId](#API_DescribePlayerSessions_RequestSyntax) **   <a name="gameliftservers-DescribePlayerSessions-request-GameSessionId"></a>
An identifier for the game session that is unique across all regions to retrieve player sessions for. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** [Limit](#API_DescribePlayerSessions_RequestSyntax) **   <a name="gameliftservers-DescribePlayerSessions-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_DescribePlayerSessions_RequestSyntax) **   <a name="gameliftservers-DescribePlayerSessions-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [PlayerId](#API_DescribePlayerSessions_RequestSyntax) **   <a name="gameliftservers-DescribePlayerSessions-request-PlayerId"></a>
A unique identifier for a player to retrieve player sessions for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [PlayerSessionId](#API_DescribePlayerSessions_RequestSyntax) **   <a name="gameliftservers-DescribePlayerSessions-request-PlayerSessionId"></a>
A unique identifier for a player session to retrieve.
Type: String
Pattern: `^psess-\S+`
Required: No

 ** [PlayerSessionStatusFilter](#API_DescribePlayerSessions_RequestSyntax) **   <a name="gameliftservers-DescribePlayerSessions-request-PlayerSessionStatusFilter"></a>
Player session status to filter results on. Note that when a PlayerSessionId or PlayerId is provided in a DescribePlayerSessions request, then the PlayerSessionStatusFilter has no effect on the response.
Possible player session statuses include the following:
+  **RESERVED** -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.
+  **ACTIVE** -- The player has been validated by the server process and is currently connected.
+  **COMPLETED** -- The player connection has been dropped.
+  **TIMEDOUT** -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribePlayerSessions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PlayerSessions": [
      {
         "CreationTime": number,
         "DnsName": "string",
         "FleetArn": "string",
         "FleetId": "string",
         "GameSessionId": "string",
         "IpAddress": "string",
         "PlayerData": "string",
         "PlayerId": "string",
         "PlayerSessionId": "string",
         "Port": number,
         "Status": "string",
         "TerminationTime": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribePlayerSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribePlayerSessions_ResponseSyntax) **   <a name="gameliftservers-DescribePlayerSessions-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [PlayerSessions](#API_DescribePlayerSessions_ResponseSyntax) **   <a name="gameliftservers-DescribePlayerSessions-response-PlayerSessions"></a>
A collection of objects containing properties for each player session that matches the request.
Type: Array of [PlayerSession](API_PlayerSession.md) objects

## Errors
<a name="API_DescribePlayerSessions_Errors"></a>

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
<a name="API_DescribePlayerSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribePlayerSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribePlayerSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribePlayerSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribePlayerSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribePlayerSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribePlayerSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribePlayerSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribePlayerSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribePlayerSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribePlayerSessions)
