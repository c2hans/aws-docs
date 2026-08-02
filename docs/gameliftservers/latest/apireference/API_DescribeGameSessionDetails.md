---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessionDetails.html
---

# DescribeGameSessionDetails
<a name="API_DescribeGameSessionDetails"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves additional game session properties, including the game session protection policy in force, a set of one or more game sessions in a specific fleet location. You can optionally filter the results by current game session status.

This operation can be used in the following ways:
+ To retrieve details for all game sessions that are currently running on all locations in a fleet, provide a fleet or alias ID, with an optional status filter. This approach returns details from the fleet's home Region and all remote locations.
+ To retrieve details for all game sessions that are currently running on a specific fleet location, provide a fleet or alias ID and a location name, with optional status filter. The location can be the fleet's home Region or any remote location.
+ To retrieve details for a specific game session, provide the game session ID. This approach looks for the game session ID in all fleets that reside in the AWS Region defined in the request.

Use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a `GameSessionDetail` object is returned for each game session that matches the request.

 **Learn more**

 [Find a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-find)

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_DescribeGameSessionDetails_RequestSyntax"></a>

```
{
   "AliasId": "{{string}}",
   "FleetId": "{{string}}",
   "GameSessionId": "{{string}}",
   "Limit": {{number}},
   "Location": "{{string}}",
   "NextToken": "{{string}}",
   "StatusFilter": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGameSessionDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AliasId](#API_DescribeGameSessionDetails_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionDetails-request-AliasId"></a>
A unique identifier for the alias associated with the fleet to retrieve all game sessions for. You can use either the alias ID or ARN value.
Type: String
Pattern: `^alias-\S+|^arn:.*:alias\/alias-\S+`
Required: No

 ** [FleetId](#API_DescribeGameSessionDetails_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionDetails-request-FleetId"></a>
A unique identifier for the fleet to retrieve all game sessions active on the fleet. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** [GameSessionId](#API_DescribeGameSessionDetails_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionDetails-request-GameSessionId"></a>
An identifier for the game session that is unique across all regions to retrieve. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** [Limit](#API_DescribeGameSessionDetails_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionDetails-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Location](#API_DescribeGameSessionDetails_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionDetails-request-Location"></a>
A fleet location to get game session details for. You can specify a fleet's home Region or a remote location. Use the AWS Region code format, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** [NextToken](#API_DescribeGameSessionDetails_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionDetails-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [StatusFilter](#API_DescribeGameSessionDetails_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionDetails-request-StatusFilter"></a>
Game session status to filter results on. Possible game session statuses include `ACTIVE`, `TERMINATED`, `ACTIVATING` and `TERMINATING` (the last two are transitory).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribeGameSessionDetails_ResponseSyntax"></a>

```
{
   "GameSessionDetails": [
      {
         "GameSession": {
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
         },
         "ProtectionPolicy": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeGameSessionDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSessionDetails](#API_DescribeGameSessionDetails_ResponseSyntax) **   <a name="gameliftservers-DescribeGameSessionDetails-response-GameSessionDetails"></a>
A collection of properties for each game session that matches the request.
Type: Array of [GameSessionDetail](API_GameSessionDetail.md) objects

 ** [NextToken](#API_DescribeGameSessionDetails_ResponseSyntax) **   <a name="gameliftservers-DescribeGameSessionDetails-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeGameSessionDetails_Errors"></a>

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

## See Also
<a name="API_DescribeGameSessionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeGameSessionDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeGameSessionDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeGameSessionDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeGameSessionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeGameSessionDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeGameSessionDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeGameSessionDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeGameSessionDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeGameSessionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeGameSessionDetails)
