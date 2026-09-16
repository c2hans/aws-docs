---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_SuspendGameServerGroup.html
---

# SuspendGameServerGroup
<a name="API_SuspendGameServerGroup"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Temporarily stops activity on a game server group without terminating instances or the game server group. You can restart activity by calling [ResumeGameServerGroup](gamelift/latest/apireference/API_ResumeGameServerGroup.html). You can suspend the following activity:
+  **Instance type replacement** - This activity evaluates the current game hosting viability of all Spot instance types that are defined for the game server group. It updates the Auto Scaling group to remove nonviable Spot Instance types, which have a higher chance of game server interruptions. It then balances capacity across the remaining viable Spot Instance types. When this activity is suspended, the Auto Scaling group continues with its current balance, regardless of viability. Instance protection, utilization metrics, and capacity scaling activities continue to be active.

To suspend activity, specify a game server group ARN and the type of activity to be suspended. If successful, a `GameServerGroup` object is returned showing that the activity is listed in `SuspendedActions`.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_SuspendGameServerGroup_RequestSyntax"></a>

```
{
   "GameServerGroupName": "{{string}}",
   "SuspendActions": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_SuspendGameServerGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_SuspendGameServerGroup_RequestSyntax) **   <a name="gameliftservers-SuspendGameServerGroup-request-GameServerGroupName"></a>
A unique identifier for the game server group. Use either the name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [SuspendActions](#API_SuspendGameServerGroup_RequestSyntax) **   <a name="gameliftservers-SuspendGameServerGroup-request-SuspendActions"></a>
The activity to suspend for this game server group.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `REPLACE_INSTANCE_TYPES`
Required: Yes

## Response Syntax
<a name="API_SuspendGameServerGroup_ResponseSyntax"></a>

```
{
   "GameServerGroup": {
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
}
```

## Response Elements
<a name="API_SuspendGameServerGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServerGroup](#API_SuspendGameServerGroup_ResponseSyntax) **   <a name="gameliftservers-SuspendGameServerGroup-response-GameServerGroup"></a>
An object that describes the game server group resource, with the `SuspendedActions` property updated to reflect the suspended activity.
Type: [GameServerGroup](API_GameServerGroup.md) object

## Errors
<a name="API_SuspendGameServerGroup_Errors"></a>

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
<a name="API_SuspendGameServerGroup_Examples"></a>

### Suspend a game server group activity
<a name="API_SuspendGameServerGroup_Example_1"></a>

This example suspends instance balancing activities for the game server group.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_SuspendGameServerGroup_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
   "SuspendActions": [ "REPLACE_INSTANCE_TYPES" ]
}

CLI command:

aws gamelift suspend-game-server-group \
    --game-server-group MegaFrogServers_NA \
    --suspend-actions REPLACE_INSTANCE_TYPES
```

#### Sample Response
<a name="API_SuspendGameServerGroup_Example_1_Response"></a>

```
{
   "GameServerGroup": {
      "AutoScalingGroupArn": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:1111aaaa-22bb-33cc-44dd-5555eeee66ff:autoScalingGroupName/MegaFrogServers_NA",
      "BalancingStrategy": "SPOT_PREFERRED",
      "CreationTime": 1496365885.44,
      "GameServerGroupArn": "arn:aws:gamelift:us-west-2::GameServerGroup/MegaFrogServers_NA",
      "GameServerGroupName": " MegaFrogServers_NA",
      "GameServerProtectionPolicy": "NO_PROTECTION",
      "InstanceDefinitions": [
         {
            "InstanceType": "c5.2xlarge",
            "WeightedCapacity": "1"
         },
         {
            "InstanceType": "c5.4xlarge",
            "WeightedCapacity": "2"
         }
      ],
      "LastUpdatedTime": 1496365885.44,
      "RoleArn": "arn:aws:iam:123456789012::role/GameLiftGsgRole",
      "Status": "ACTIVE",
      "StatusReason": "",
      "SuspendedActions": [REPLACE_INSTANCE_TYPES]
}
```

## See Also
<a name="API_SuspendGameServerGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/SuspendGameServerGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/SuspendGameServerGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/SuspendGameServerGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/SuspendGameServerGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/SuspendGameServerGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/SuspendGameServerGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/SuspendGameServerGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/SuspendGameServerGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/SuspendGameServerGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/SuspendGameServerGroup)
