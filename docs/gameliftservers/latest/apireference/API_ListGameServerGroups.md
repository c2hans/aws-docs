---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListGameServerGroups.html
---

# ListGameServerGroups
<a name="API_ListGameServerGroups"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Lists a game server groups.

## Request Syntax
<a name="API_ListGameServerGroups_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListGameServerGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Limit](#API_ListGameServerGroups_RequestSyntax) **   <a name="gameliftservers-ListGameServerGroups-request-Limit"></a>
The game server groups' limit.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListGameServerGroups_RequestSyntax) **   <a name="gameliftservers-ListGameServerGroups-request-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListGameServerGroups_ResponseSyntax"></a>

```
{
   "GameServerGroups": [
      {
         "AutoScalingGroupArn": "string",
         "BalancingStrategy": "string",
         "CreationTime": number,
         "GameServerGroupArn": "string",
         "GameServerGroupName": "string",
         "GameServerProtectionPolicy": "string",
         "InstanceDefinitions": [
            {
               "InstanceType": "string",
               "WeightedCapacity": "string"
            }
         ],
         "LastUpdatedTime": number,
         "RoleArn": "string",
         "Status": "string",
         "StatusReason": "string",
         "SuspendedActions": [ "string" ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListGameServerGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServerGroups](#API_ListGameServerGroups_ResponseSyntax) **   <a name="gameliftservers-ListGameServerGroups-response-GameServerGroups"></a>
The game server groups' game server groups.
Type: Array of [GameServerGroup](API_GameServerGroup.md) objects

 ** [NextToken](#API_ListGameServerGroups_ResponseSyntax) **   <a name="gameliftservers-ListGameServerGroups-response-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListGameServerGroups_Errors"></a>

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
<a name="API_ListGameServerGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListGameServerGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListGameServerGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListGameServerGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListGameServerGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListGameServerGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListGameServerGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListGameServerGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListGameServerGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListGameServerGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListGameServerGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
