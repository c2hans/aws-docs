---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ResumeGameServerGroup.html
---

# ResumeGameServerGroup
<a name="API_ResumeGameServerGroup"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Reinstates activity on a game server group after it has been suspended. A game server group might be suspended by the [SuspendGameServerGroup](gamelift/latest/apireference/API_SuspendGameServerGroup.html) operation, or it might be suspended involuntarily due to a configuration problem. In the second case, you can manually resume activity on the group once the configuration problem has been resolved. Refer to the game server group status and status reason for more information on why group activity is suspended.

To resume activity, specify a game server group ARN and the type of activity to be resumed. If successful, a `GameServerGroup` object is returned showing that the resumed activity is no longer listed in `SuspendedActions`.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_ResumeGameServerGroup_RequestSyntax"></a>

```
{
   "GameServerGroupName": "{{string}}",
   "ResumeActions": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ResumeGameServerGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_ResumeGameServerGroup_RequestSyntax) **   <a name="gameliftservers-ResumeGameServerGroup-request-GameServerGroupName"></a>
A unique identifier for the game server group. Use either the name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [ResumeActions](#API_ResumeGameServerGroup_RequestSyntax) **   <a name="gameliftservers-ResumeGameServerGroup-request-ResumeActions"></a>
The activity to resume for this game server group.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `REPLACE_INSTANCE_TYPES`
Required: Yes

## Response Syntax
<a name="API_ResumeGameServerGroup_ResponseSyntax"></a>

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
<a name="API_ResumeGameServerGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServerGroup](#API_ResumeGameServerGroup_ResponseSyntax) **   <a name="gameliftservers-ResumeGameServerGroup-response-GameServerGroup"></a>
An object that describes the game server group resource, with the `SuspendedActions` property updated to reflect the resumed activity.
Type: [GameServerGroup](API_GameServerGroup.md) object

## Errors
<a name="API_ResumeGameServerGroup_Errors"></a>

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
<a name="API_ResumeGameServerGroup_Examples"></a>

### Restart a game server group activity
<a name="API_ResumeGameServerGroup_Example_1"></a>

This example restores instance balancing activities for the game server group.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_ResumeGameServerGroup_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
   "ResumeActions": [ "REPLACE_INSTANCE_TYPES" ]
}

CLI command:

aws gamelift resume-game-server-group \
    --game-server-group MegaFrogServers_NA \
    --resume-actions REPLACE_INSTANCE_TYPES
```

#### Sample Response
<a name="API_ResumeGameServerGroup_Example_1_Response"></a>

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
      "SuspendedActions": []
}
```

## See Also
<a name="API_ResumeGameServerGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ResumeGameServerGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ResumeGameServerGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ResumeGameServerGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ResumeGameServerGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ResumeGameServerGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ResumeGameServerGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ResumeGameServerGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ResumeGameServerGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ResumeGameServerGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ResumeGameServerGroup)
