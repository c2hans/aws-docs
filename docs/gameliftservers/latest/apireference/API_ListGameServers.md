---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListGameServers.html
---

# ListGameServers
<a name="API_ListGameServers"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Retrieves information on all game servers that are currently active in a specified game server group. You can opt to sort the list by game server age. Use the pagination parameters to retrieve results in a set of sequential segments.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_ListGameServers_RequestSyntax"></a>

```
{
   "GameServerGroupName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListGameServers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_ListGameServers_RequestSyntax) **   <a name="gameliftservers-ListGameServers-request-GameServerGroupName"></a>
An identifier for the game server group to retrieve a list of game servers from. Use either the name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [Limit](#API_ListGameServers_RequestSyntax) **   <a name="gameliftservers-ListGameServers-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListGameServers_RequestSyntax) **   <a name="gameliftservers-ListGameServers-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [SortOrder](#API_ListGameServers_RequestSyntax) **   <a name="gameliftservers-ListGameServers-request-SortOrder"></a>
Indicates how to sort the returned data based on game server registration timestamp. Use `ASCENDING` to retrieve oldest game servers first, or use `DESCENDING` to retrieve newest game servers first. If this parameter is left empty, game servers are returned in no particular order.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListGameServers_ResponseSyntax"></a>

```
{
   "GameServers": [
      {
         "ClaimStatus": "string",
         "ConnectionInfo": "string",
         "GameServerData": "string",
         "GameServerGroupArn": "string",
         "GameServerGroupName": "string",
         "GameServerId": "string",
         "InstanceId": "string",
         "LastClaimTime": number,
         "LastHealthCheckTime": number,
         "RegistrationTime": number,
         "UtilizationStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListGameServers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServers](#API_ListGameServers_ResponseSyntax) **   <a name="gameliftservers-ListGameServers-response-GameServers"></a>
A collection of game server objects that match the request.
Type: Array of [GameServer](API_GameServer.md) objects

 ** [NextToken](#API_ListGameServers_ResponseSyntax) **   <a name="gameliftservers-ListGameServers-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListGameServers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_ListGameServers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListGameServers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListGameServers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListGameServers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListGameServers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListGameServers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListGameServers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListGameServers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListGameServers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListGameServers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListGameServers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
