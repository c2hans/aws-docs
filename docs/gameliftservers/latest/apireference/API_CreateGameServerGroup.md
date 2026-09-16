---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameServerGroup.html
---

# CreateGameServerGroup
<a name="API_CreateGameServerGroup"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Creates a Amazon GameLift Servers FleetIQ game server group for managing game hosting on a collection of Amazon Elastic Compute Cloud instances for game hosting. This operation creates the game server group, creates an Auto Scaling group in your AWS account, and establishes a link between the two groups. You can view the status of your game server groups in the Amazon GameLift Servers console. Game server group metrics and events are emitted to Amazon CloudWatch.

Before creating a new game server group, you must have the following:
+ An Amazon Elastic Compute Cloud launch template that specifies how to launch Amazon Elastic Compute Cloud instances with your game server build. For more information, see [ Launching an Instance from a Launch Template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon Elastic Compute Cloud User Guide*.
+ An IAM role that extends limited access to your AWS account to allow Amazon GameLift Servers FleetIQ to create and interact with the Auto Scaling group. For more information, see [Create IAM roles for cross-service interaction](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-iam-permissions-roles.html) in the *Amazon GameLift Servers FleetIQ Developer Guide*.

To create a new game server group, specify a unique group name, IAM role and Amazon Elastic Compute Cloud launch template, and provide a list of instance types that can be used in the group. You must also set initial maximum and minimum limits on the group's instance count. You can optionally set an Auto Scaling policy with target tracking based on a Amazon GameLift Servers FleetIQ metric.

Once the game server group and corresponding Auto Scaling group are created, you have full access to change the Auto Scaling group's configuration as needed. Several properties that are set when creating a game server group, including maximum/minimum size and auto-scaling policy settings, must be updated directly in the Auto Scaling group. Keep in mind that some Auto Scaling group properties are periodically updated by Amazon GameLift Servers FleetIQ as part of its balancing activities to optimize for availability and cost.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_CreateGameServerGroup_RequestSyntax"></a>

```
{
   "AutoScalingPolicy": {
      "EstimatedInstanceWarmup": {{number}},
      "TargetTrackingConfiguration": {
         "TargetValue": {{number}}
      }
   },
   "BalancingStrategy": "{{string}}",
   "GameServerGroupName": "{{string}}",
   "GameServerProtectionPolicy": "{{string}}",
   "InstanceDefinitions": [
      {
         "InstanceType": "{{string}}",
         "WeightedCapacity": "{{string}}"
      }
   ],
   "LaunchTemplate": {
      "LaunchTemplateId": "{{string}}",
      "LaunchTemplateName": "{{string}}",
      "Version": "{{string}}"
   },
   "MaxSize": {{number}},
   "MinSize": {{number}},
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcSubnets": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateGameServerGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-GameServerGroupName"></a>
An identifier for the new game server group. This value is used to generate unique ARN identifiers for the Amazon EC2 Auto Scaling group and the Amazon GameLift Servers FleetIQ game server group. The name must be unique per Region per AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]+`
Required: Yes

 ** [InstanceDefinitions](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-InstanceDefinitions"></a>
The Amazon EC2 instance types and sizes to use in the Auto Scaling group. The instance definitions must specify at least two different instance types that are supported by Amazon GameLift Servers FleetIQ. For more information on instance types, see [EC2 Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon Elastic Compute Cloud User Guide*. You can optionally specify capacity weighting for each instance type. If no weight value is specified for an instance type, it is set to the default value "1". For more information about capacity weighting, see [ Instance Weighting for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html) in the Amazon EC2 Auto Scaling User Guide.
Type: Array of [InstanceDefinition](API_InstanceDefinition.md) objects
Array Members: Minimum number of 2 items. Maximum number of 20 items.
Required: Yes

 ** [LaunchTemplate](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-LaunchTemplate"></a>
The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. You can specify the template using either the template name or ID. For help with creating a launch template, see [Creating a Launch Template for an Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html) in the *Amazon Elastic Compute Cloud Auto Scaling User Guide*. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
If you specify network interfaces in your launch template, you must explicitly set the property `AssociatePublicIpAddress` to "true". If no network interface is specified in the launch template, Amazon GameLift Servers FleetIQ uses your account's default VPC.
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object
Required: Yes

 ** [MaxSize](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-MaxSize"></a>
The maximum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** [MinSize](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-MinSize"></a>
The minimum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** [RoleArn](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-RoleArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:.*:role\/[\w+=,.@-]+`
Required: Yes

 ** [AutoScalingPolicy](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-AutoScalingPolicy"></a>
Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. The scaling policy uses the metric `"PercentUtilizedGameServers"` to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
Type: [GameServerGroupAutoScalingPolicy](API_GameServerGroupAutoScalingPolicy.md) object
Required: No

 ** [BalancingStrategy](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-BalancingStrategy"></a>
Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:
+  `SPOT_ONLY` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.
+  `SPOT_PREFERRED` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.
+  `ON_DEMAND_ONLY` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.
Type: String
Valid Values: `SPOT_ONLY | SPOT_PREFERRED | ON_DEMAND_ONLY`
Required: No

 ** [GameServerProtectionPolicy](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-GameServerProtectionPolicy"></a>
A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by AWS regardless of protection status. This property is set to `NO_PROTECTION` by default.
Type: String
Valid Values: `NO_PROTECTION | FULL_PROTECTION`
Required: No

 ** [Tags](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-Tags"></a>
A list of labels to assign to the new game server group resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management, and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [VpcSubnets](#API_CreateGameServerGroup_RequestSyntax) **   <a name="gameliftservers-CreateGameServerGroup-request-VpcSubnets"></a>
A list of virtual private cloud (VPC) subnets to use with instances in the game server group. By default, all Amazon GameLift Servers FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that you've set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `^subnet-[0-9a-z]+$`
Required: No

## Response Syntax
<a name="API_CreateGameServerGroup_ResponseSyntax"></a>

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
<a name="API_CreateGameServerGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServerGroup](#API_CreateGameServerGroup_ResponseSyntax) **   <a name="gameliftservers-CreateGameServerGroup-response-GameServerGroup"></a>
The newly created game server group object, including the new ARN value for the Amazon GameLift Servers FleetIQ game server group and the object's status. The Amazon EC2 Auto Scaling group ARN is initially null, since the group has not yet been created. This value is added once the game server group status reaches `ACTIVE`.
Type: [GameServerGroup](API_GameServerGroup.md) object

## Errors
<a name="API_CreateGameServerGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_CreateGameServerGroup_Examples"></a>

### Create a new game server group
<a name="API_CreateGameServerGroup_Example_1"></a>

This example creates a game server group and Auto Scaling group that deploys your game server software to Spot instances of two instance types. The game server group is set up to use Spot Instances only, so if no Spot Instances of these types are available, the game server group will effectively stop starting new game servers until Spot resources are available again. This request also triggers creation of a target-tracking Auto Scaling policy. With this policy, the Auto Scaling group will maintain approximately 75% game server utilization. The 25% of idle capacity enables the game server group to immediately accommodate sudden increases in player demand.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_CreateGameServerGroup_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
   "RoleArn": "arn:aws:iam:123456789012::role/GameLiftGsgRole",
   "MinSize": 1,
   "MaxSize": 1000,
   "GameServerProtectionPolicy": "NO_PROTECTION",
   "BalancingStrategy": "SPOT_ONLY",
   "LaunchTemplate": {
      "LaunchTemplateId": "lt-1234567890abcdef",
   },
   "InstanceDefinitions": [
      {"InstanceType": "c5.xlarge"},
      {"InstanceType": "m5.xlarge"}
   ],
   "AutoScalingPolicy": {
      "TargetTrackingConfiguration": {
         "TargetValue": 75
      }
   }
}

CLI command:

aws gamelift create-game-server-group \
    --game-server-group-name MegaFrogServers_NA \
    --role-arn arn:aws:iam::123456789012:role/GameLiftGSGRole \
    --min-size 1 \
    --max-size 1000 \
    --game-server-protection-policy NO_PROTECTION \
    --balancing-strategy SPOT_ONLY
    --launch-template LaunchTemplateId=lt-012ab345cde6789ff \
    --instance-definitions '[{"InstanceType": "c5.xlarge"}, {"InstanceType": "m5.xlarge"}]' \
         --auto-scaling-policy '{"TargetTrackingConfiguration": {"TargetValue": 75}}'
```

#### Sample Response
<a name="API_CreateGameServerGroup_Example_1_Response"></a>

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
            "InstanceType": "c5.xlarge",
            "WeightedCapacity": "1"
         }
         {
            "InstanceType": "m5.xlarge",
            "WeightedCapacity": "1"
         }
      ],
      "LastUpdatedTime": 1496365885.44,
      "RoleArn": "arn:aws:iam:123456789012::role/GameLiftGsgRole",
      "Status": "NEW",
      "StatusReason": "",
      "SuspendedActions": []
}
```

### Create a new game server group with weighted instances
<a name="API_CreateGameServerGroup_Example_2"></a>

This example creates a game server group with three weighted instance types. Because a balancing strategy is not defined in this example, the default `"SPOT_PREFERRED"` is used.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_CreateGameServerGroup_Example_2_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
   "RoleArn": "arn:aws:iam:123456789012::role/GameLiftGsgRole",
   "MinSize": 1,
   "MaxSize": 200,
   "InstanceDefinitions": [
      {
         "InstanceType": "c5.2xlarge",
         "WeightedCapacity": "1"
      },
      {
         "InstanceType": "c5.4xlarge",
         "WeightedCapacity": "2"
      },
      {
         "InstanceType": "c5.24xlarge",
         "WeightedCapacity": "12"
      }
   ],
   "LaunchTemplate": {
      "LaunchTemplateName": "MegaFrogServers"
   }
}

CLI command:

aws gamelift create-game-server-group \
    --game-server-group-name MegaFrogServers_NA \
    --role-arn arn:aws:iam:123456789012::role/GameLiftGsgRole \
    --min-size 1 \
    --max-size 200 \
    --launch-template {"LaunchTemplateName": MegaFrogServers} \
    --instance-definitions '[{"IntanceType":"m5.2xlarge","WeightedCapacity":"1"},{"InstanceType":"m5.4xlarge","WeightedCapacity":"2"},{"InstanceType":"m5.24xlarge","WeightedCapacity":"12"}]'
```

#### Sample Response
<a name="API_CreateGameServerGroup_Example_2_Response"></a>

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
         },
         {
            "InstanceType": "c5.24xlarge",
            "WeightedCapacity": "12"
         }
      ],
      "LastUpdatedTime": 1496365885.44,
      "RoleArn": "arn:aws:iam:123456789012::role/GameLiftGsgRole",
      "Status": "NEW",
      "StatusReason": "",
      "SuspendedActions": []
}
```

## See Also
<a name="API_CreateGameServerGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateGameServerGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateGameServerGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateGameServerGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateGameServerGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateGameServerGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateGameServerGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateGameServerGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateGameServerGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateGameServerGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateGameServerGroup)
