---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameServerGroup.html
---

# UpdateGameServerGroup
<a name="API_UpdateGameServerGroup"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Updates Amazon GameLift Servers FleetIQ-specific properties for a game server group. Many Auto Scaling group properties are updated on the Auto Scaling group directly, including the launch template, Auto Scaling policies, and maximum/minimum/desired instance counts.

To update the game server group, specify the game server group ID and provide the updated values. Before applying the updates, the new values are validated to ensure that Amazon GameLift Servers FleetIQ can continue to perform instance balancing activity. If successful, a `GameServerGroup` object is returned.

**Note**
Target tracking Auto Scaling policies on the Auto Scaling group cannot be updated through the AWS Management Console. Instead, use the Amazon Elastic Compute Cloud Auto Scaling [`PutScalingPolicy`](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScalingPolicy.html) API action to update these policies.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_UpdateGameServerGroup_RequestSyntax"></a>

```
{
   "BalancingStrategy": "{{string}}",
   "GameServerGroupName": "{{string}}",
   "GameServerProtectionPolicy": "{{string}}",
   "InstanceDefinitions": [
      {
         "InstanceType": "{{string}}",
         "WeightedCapacity": "{{string}}"
      }
   ],
   "RoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGameServerGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_UpdateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-UpdateGameServerGroup-request-GameServerGroupName"></a>
A unique identifier for the game server group. Use either the name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [BalancingStrategy](#API_UpdateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-UpdateGameServerGroup-request-BalancingStrategy"></a>
Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:
+  `SPOT_ONLY` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.
+  `SPOT_PREFERRED` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.
+  `ON_DEMAND_ONLY` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.
Type: String
Valid Values: `SPOT_ONLY | SPOT_PREFERRED | ON_DEMAND_ONLY`
Required: No

 ** [GameServerProtectionPolicy](#API_UpdateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-UpdateGameServerGroup-request-GameServerProtectionPolicy"></a>
A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by AWS regardless of protection status. This property is set to `NO_PROTECTION` by default.
Type: String
Valid Values: `NO_PROTECTION | FULL_PROTECTION`
Required: No

 ** [InstanceDefinitions](#API_UpdateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-UpdateGameServerGroup-request-InstanceDefinitions"></a>
An updated list of Amazon EC2 instance types to use in the Auto Scaling group. The instance definitions must specify at least two different instance types that are supported by Amazon GameLift Servers FleetIQ. This updated list replaces the entire current list of instance definitions for the game server group. For more information on instance types, see [EC2 Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*. You can optionally specify capacity weighting for each instance type. If no weight value is specified for an instance type, it is set to the default value "1". For more information about capacity weighting, see [ Instance Weighting for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html) in the Amazon EC2 Auto Scaling User Guide.
Type: Array of [InstanceDefinition](API_InstanceDefinition.md) objects
Array Members: Minimum number of 2 items. Maximum number of 20 items.
Required: No

 ** [RoleArn](#API_UpdateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-UpdateGameServerGroup-request-RoleArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:.*:role\/[\w+=,.@-]+`
Required: No

## Response Syntax
<a name="API_UpdateGameServerGroup_ResponseSyntax"></a>

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
<a name="API_UpdateGameServerGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServerGroup](#API_UpdateGameServerGroup_ResponseSyntax) **   <a name="gameliftservers-UpdateGameServerGroup-response-GameServerGroup"></a>
An object that describes the game server group resource with updated properties.
Type: [GameServerGroup](API_GameServerGroup.md) object

## Errors
<a name="API_UpdateGameServerGroup_Errors"></a>

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
<a name="API_UpdateGameServerGroup_Examples"></a>

### Update instance definitions for the game server group
<a name="API_UpdateGameServerGroup_Example_1"></a>

This example specifies a new set of instance definitions for the game server group. Previously, the game server group used a Spot-only balancing strategy with c3.xlarge and c4.xlarge instance types. This request removes the old instance definitions and replaces them. As shown in the response, because the new definitions do not specify `WeightedCapacity`, these are set to the default value of 1.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_UpdateGameServerGroup_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
     "InstanceDefinitions": [
        {"InstanceType": "c4.xlarge"},
        {"InstanceType": "c5.xlarge"}
     ]
}

CLI command:

aws gamelift update-game-server-group \
    --game-server-group MegaFrogServers_NA \
    --instance-definitions '[{"InstanceType": "c4.xlarge"}, {"InstanceType": "c5.xlarge"}]'
```

#### Sample Response
<a name="API_UpdateGameServerGroup_Example_1_Response"></a>

```
{
   "GameServerGroup": {
      "AutoScalingGroupArn": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:1111aaaa-22bb-33cc-44dd-5555eeee66ff:autoScalingGroupName/MegaFrogServers_NA",
      "BalancingStrategy": "SPOT_ONLY",
      "CreationTime": 1496365885.44,
      "GameServerGroupArn": "arn:aws:gamelift:us-west-2::GameServerGroup/MegaFrogServers_NA",
      "GameServerGroupName": " MegaFrogServers_NA",
      "GameServerProtectionPolicy": "NO_PROTECTION",
      "InstanceDefinitions": [
         {
            "InstanceType": "c4.xlarge",
            "WeightedCapacity": "1"
         },
         {
            "InstanceType": "c5.xlarge",
            "WeightedCapacity": "1"
         }
      ],
      "LastUpdatedTime": 1496365885.44,
      "RoleArn": "arn:aws:iam:123456789012::role/GameLiftGsgRole",
      "Status": "ACTIVE",
      "StatusReason": "",
      "SuspendedActions": []
}
```

### Change the balancing strategy for a game server group
<a name="API_UpdateGameServerGroup_Example_2"></a>

This example changes the game server group's balancing strategy from preferring Spot instances to using On-Demand instances only. In this example scenario, the game developer wants to eliminate the possibility of game session interruptions during an upcoming highly-anticipated content launch. Later, once player demand settles, the balancing strategy can be updated again to use Spot instances for cost savings.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_UpdateGameServerGroup_Example_2_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
      "BalancingStrategy": "ON_DEMAND_ONLY"
}

CLI command:

aws gamelift update-game-server-group \
    --game-server-group MegaFrogServers_NA \
    --balancing-strategy ON_DEMAND_ONLY
```

#### Sample Response
<a name="API_UpdateGameServerGroup_Example_2_Response"></a>

```
{
   "GameServerGroup": {
      "AutoScalingGroupArn": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:1111aaaa-22bb-33cc-44dd-5555eeee66ff:autoScalingGroupName/MegaFrogServers_NA",
      "BalancingStrategy": "ON_DEMAND_ONLY",
      "CreationTime": 1496365885.44,
      "GameServerGroupArn": "arn:aws:gamelift:us-west-2::GameServerGroup/MegaFrogServers_NA",
      "GameServerGroupName": " MegaFrogServers_NA",
      "GameServerProtectionPolicy": "FULL_PROTECTION",
      "InstanceDefinitions": [
         {
            "InstanceType": "c4.xlarge",
            "WeightedCapacity": "1"
         },
         {
            "InstanceType": "c5.xlarge",
            "WeightedCapacity": "1"
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
<a name="API_UpdateGameServerGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateGameServerGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateGameServerGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateGameServerGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateGameServerGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateGameServerGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateGameServerGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateGameServerGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateGameServerGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateGameServerGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateGameServerGroup)
