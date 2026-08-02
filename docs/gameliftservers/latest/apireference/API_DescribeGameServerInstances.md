---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameServerInstances.html
---

# DescribeGameServerInstances
<a name="API_DescribeGameServerInstances"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Retrieves status information about the Amazon EC2 instances associated with a Amazon GameLift Servers FleetIQ game server group. Use this operation to detect when instances are active or not available to host new game servers.

To request status for all instances in the game server group, provide a game server group ID only. To request status for specific instances, provide the game server group ID and one or more instance IDs. Use the pagination parameters to retrieve results in sequential segments. If successful, a collection of `GameServerInstance` objects is returned.

This operation is not designed to be called with every game server claim request; this practice can cause you to exceed your API limit, which results in errors. Instead, as a best practice, cache the results and refresh your cache no more than once every 10 seconds.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_DescribeGameServerInstances_RequestSyntax"></a>

```
{
   "GameServerGroupName": "{{string}}",
   "InstanceIds": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGameServerInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_DescribeGameServerInstances_RequestSyntax) **   <a name="gameliftservers-DescribeGameServerInstances-request-GameServerGroupName"></a>
A unique identifier for the game server group. Use either the name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [InstanceIds](#API_DescribeGameServerInstances_RequestSyntax) **   <a name="gameliftservers-DescribeGameServerInstances-request-InstanceIds"></a>
The Amazon EC2 instance IDs that you want to retrieve status on. Amazon EC2 instance IDs use a 17-character format, for example: `i-1234567890abcdef0`. To retrieve all instances in the game server group, leave this parameter empty.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Fixed length of 19.
Pattern: `^i-[0-9a-zA-Z]{17}$`
Required: No

 ** [Limit](#API_DescribeGameServerInstances_RequestSyntax) **   <a name="gameliftservers-DescribeGameServerInstances-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_DescribeGameServerInstances_RequestSyntax) **   <a name="gameliftservers-DescribeGameServerInstances-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribeGameServerInstances_ResponseSyntax"></a>

```
{
   "GameServerInstances": [
      {
         "GameServerGroupArn": "string",
         "GameServerGroupName": "string",
         "InstanceId": "string",
         "InstanceStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeGameServerInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServerInstances](#API_DescribeGameServerInstances_ResponseSyntax) **   <a name="gameliftservers-DescribeGameServerInstances-response-GameServerInstances"></a>
The collection of requested game server instances.
Type: Array of [GameServerInstance](API_GameServerInstance.md) objects

 ** [NextToken](#API_DescribeGameServerInstances_ResponseSyntax) **   <a name="gameliftservers-DescribeGameServerInstances-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeGameServerInstances_Errors"></a>

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

## Examples
<a name="API_DescribeGameServerInstances_Examples"></a>

### Retrieve game server instance status
<a name="API_DescribeGameServerInstances_Example_1"></a>

This example retrieves the current status of the first twenty instances in a game server group. Since no instance IDs are specified in this request, there is no error information to be returned.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeGameServerInstances_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
   "Limit": "20"
}

CLI command:

aws gamelift describe-game-server-instances \
    --game-server-group-name MegaFrogServers_NA \
    --limit 20
```

#### Sample Response
<a name="API_DescribeGameServerInstances_Example_1_Response"></a>

```
{
   "GameServerInstances": [
      {
         "GameServerGroupArn": "arn:aws:gamelift:us-west-2::GameServerGroup/MegaFrogServers_NA",
         "GameServerGroupName": " MegaFrogServers_NA",
         "InstanceId": "i-1234567890abcdef0",
         "InstanceStatus: "ACTIVE"
      },
      {
         "GameServerGroupArn": "arn:aws:gamelift:us-west-2::GameServerGroup/MegaFrogServers_NA",
         "GameServerGroupName": " MegaFrogServers_NA",
         "InstanceId": "i-9876543210abcdef1",
         "InstanceStatus: "DRAINING"
      }
   ],
   "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2"
}
```

## See Also
<a name="API_DescribeGameServerInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeGameServerInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeGameServerInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeGameServerInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeGameServerInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeGameServerInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeGameServerInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeGameServerInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeGameServerInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeGameServerInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeGameServerInstances)
