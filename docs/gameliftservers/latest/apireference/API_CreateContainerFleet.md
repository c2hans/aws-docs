---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateContainerFleet.html
---

# CreateContainerFleet
<a name="API_CreateContainerFleet"></a>

 **This API works with the following fleet types:** Container

Creates a managed fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances to host your containerized game servers. Use this operation to define how to deploy a container architecture onto each fleet instance and configure fleet settings. You can create a container fleet in any AWS Regions that Amazon GameLift Servers supports for multi-location fleets. A container fleet can be deployed to a single location or multiple locations. Container fleets are deployed with Amazon Linux 2023 as the instance operating system.

Define the fleet's container architecture using container group definitions. Each fleet can have one of the following container group types:
+ The game server container group runs your game server build and dependent software. Amazon GameLift Servers deploys one or more replicas of this container group to each fleet instance. The number of replicas depends on the computing capabilities of the fleet instance in use.
+ An optional per-instance container group might be used to run other software that only needs to run once per instance, such as background services, logging, or test processes. One per-instance container group is deployed to each fleet instance.

Each container group can include the definition for one or more containers. A container definition specifies a container image that is stored in an Amazon Elastic Container Registry (Amazon ECR) public or private repository.

 **Request options**

Use this operation to make the following types of requests. Most fleet settings have default values, so you can create a working fleet with a minimal configuration and default values, which you can customize later.
+ Create a fleet with no container groups. You can configure a container fleet and then add container group definitions later. In this scenario, no fleet instances are deployed, and the fleet can't host game sessions until you add a game server container group definition. Provide the following required parameter values:
  +  `FleetRoleArn`
+ Create a fleet with a game server container group. Provide the following required parameter values:
  +  `FleetRoleArn`
  +  `GameServerContainerGroupDefinitionName`
+ Create a fleet with a game server container group and a per-instance container group. Provide the following required parameter values:
  +  `FleetRoleArn`
  +  `GameServerContainerGroupDefinitionName`
  +  `PerInstanceContainerGroupDefinitionName`

 **Results**

If successful, this operation creates a new container fleet resource, places it in `PENDING` status, and initiates the [fleet creation workflow](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-all.html#fleets-creation-workflow). For fleets with container groups, this workflow starts a fleet deployment and transitions the status to `ACTIVE`. Fleets without a container group are placed in `CREATED` status.

You can update most of the properties of a fleet, including container group definitions, and deploy the update across all fleet instances. Use [UpdateContainerFleet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerFleet.html) to deploy a new game server version update across the container fleet.

**Note**
A managed fleet's runtime environment depends on the Amazon Machine Image (AMI) version it uses. When a new fleet is created, Amazon GameLift Servers assigns the latest available AMI version to the fleet, and all compute instances in that fleet are deployed with that version. To update the AMI version, you must create a new fleet. As a best practice, we recommend replacing your managed fleets every 30 days to maintain a secure and up-to-date runtime environment for your hosted game servers. For guidance, see [ Security best practices for Amazon GameLift Servers](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-best-practices.html).

## Request Syntax
<a name="API_CreateContainerFleet_RequestSyntax"></a>

```
{
   "BillingType": "{{string}}",
   "Description": "{{string}}",
   "FleetRoleArn": "{{string}}",
   "GameServerContainerGroupDefinitionName": "{{string}}",
   "GameServerContainerGroupsPerInstance": {{number}},
   "GameSessionCreationLimitPolicy": {
      "NewGameSessionsPerCreator": {{number}},
      "PolicyPeriodInMinutes": {{number}}
   },
   "InstanceConnectionPortRange": {
      "FromPort": {{number}},
      "ToPort": {{number}}
   },
   "InstanceInboundPermissions": [
      {
         "FromPort": {{number}},
         "IpRange": "{{string}}",
         "Protocol": "{{string}}",
         "ToPort": {{number}}
      }
   ],
   "InstanceType": "{{string}}",
   "Locations": [
      {
         "Location": "{{string}}"
      }
   ],
   "LogConfiguration": {
      "LogDestination": "{{string}}",
      "LogGroupArn": "{{string}}",
      "S3BucketName": "{{string}}"
   },
   "MetricGroups": [ "{{string}}" ],
   "NewGameSessionProtectionPolicy": "{{string}}",
   "PerInstanceContainerGroupDefinitionName": "{{string}}",
   "PlayerGatewayMode": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateContainerFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetRoleArn](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-FleetRoleArn"></a>
The unique identifier for an AWS Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers. Use an IAM service role with the `GameLiftContainerFleetPolicy` managed policy attached. For more information, see [Set up an IAM service role](https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html). You can't change this fleet property after the fleet is created.
IAM role ARN values use the following pattern: `arn:aws:iam::[AWS account]:role/[role name]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:.*:role\/[\w+=,.@-]+`
Required: Yes

 ** [BillingType](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-BillingType"></a>
Indicates whether to use On-Demand or Spot instances for this fleet. Learn more about when to use [ On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot). This fleet property can't be changed after the fleet is created.
By default, this property is set to `ON_DEMAND`.
You can't update this fleet property later.
Type: String
Valid Values: `ON_DEMAND | SPOT`
Required: No

 ** [Description](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-Description"></a>
A meaningful description of the container fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [GameServerContainerGroupDefinitionName](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-GameServerContainerGroupDefinitionName"></a>
A container group definition resource that describes how to deploy containers with your game server build and support software onto each fleet instance. You can specify the container group definition's name to use the latest version. Alternatively, provide an ARN value with a specific version number.
Create a container group definition by calling [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html). This operation creates a [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** [GameServerContainerGroupsPerInstance](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-GameServerContainerGroupsPerInstance"></a>
The number of times to replicate the game server container group on each fleet instance.
By default, Amazon GameLift Servers calculates the maximum number of game server container groups that can fit on each instance. This calculation is based on the CPU and memory resources of the fleet's instance type). To use the calculated maximum, don't set this parameter. If you set this number manually, Amazon GameLift Servers uses your value as long as it's less than the calculated maximum.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** [GameSessionCreationLimitPolicy](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-GameSessionCreationLimitPolicy"></a>
A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.
Type: [GameSessionCreationLimitPolicy](API_GameSessionCreationLimitPolicy.md) object
Required: No

 ** [InstanceConnectionPortRange](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-InstanceConnectionPortRange"></a>
The set of port numbers to open on each fleet instance. A fleet's connection ports map to container ports that are configured in the fleet's container group definitions.
By default, Amazon GameLift Servers calculates an optimal port range based on your fleet configuration. To use the calculated range, don't set this parameter. The values are:
+ Port range: 4192 to a number calculated based on your fleet configuration. Amazon GameLift Servers uses the following formula: `4192 + [# of game server container groups per fleet instance] * [# of container ports in the game server container group definition] + [# of container ports in the per instance container group definition]`
You can also choose to manually set this parameter. When manually setting this parameter, you must use port numbers that match the fleet's inbound permissions port range.
If you set values manually, Amazon GameLift Servers no longer calculates a port range for you, even if you later remove the manual settings.
The port range must not overlap with the Amazon GameLift Servers reserved port range `4092-4191`. This range is reserved for internal Amazon GameLift Servers services.
Type: [ConnectionPortRange](API_ConnectionPortRange.md) object
Required: No

 ** [InstanceInboundPermissions](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-InstanceInboundPermissions"></a>
The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. As a best practice, when remotely accessing a fleet instance, we recommend opening ports only when you need them and closing them when you're finished.
By default, Amazon GameLift Servers calculates an optimal port range based on your fleet configuration. To use the calculated range, don't set this parameter. The values are:
+ Protocol: UDP
+ Port range: 4192 to a number calculated based on your fleet configuration. Amazon GameLift Servers uses the following formula: `4192 + [# of game server container groups per fleet instance] * [# of container ports in the game server container group definition] + [# of container ports in the per instance container group definition]`
You can also choose to manually set this parameter. When manually setting this parameter, you must use port numbers that match the fleet's connection port range.
If you set values manually, Amazon GameLift Servers no longer calculates a port range for you, even if you later remove the manual settings.
The port range must not overlap with the Amazon GameLift Servers reserved port range `4092-4191`. This range is reserved for internal Amazon GameLift Servers services.
Type: Array of [IpPermission](API_IpPermission.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** [InstanceType](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-InstanceType"></a>
The Amazon EC2 instance type to use for all instances in the fleet. For multi-location fleets, the instance type must be available in the home region and all remote locations. Instance type determines the computing resources and processing power that's available to host your game servers. This includes including CPU, memory, storage, and networking capacity.
By default, Amazon GameLift Servers uses the `c5.large` instance type. If this instance type does not have sufficient resources for your container groups, you can choose a different instance type that better fits your needs. See [Amazon Elastic Compute Cloud Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed descriptions of Amazon EC2 instance types.
You can't update this fleet property later.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [Locations](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-Locations"></a>
A set of locations to deploy container fleet instances to. You can add any AWS Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more AWS Region codes, such as `us-west-2`, or Local Zone names. Also include the fleet's home Region, which is the AWS Region where the fleet is created. For a list of supported Regions and Local Zones, see [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.
Type: Array of [LocationConfiguration](API_LocationConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [LogConfiguration](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-LogConfiguration"></a>
A method for collecting container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs. You can select from the following methods:
+  `CLOUDWATCH` -- Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
+  `S3` -- Store logs in an Amazon S3 bucket that you define.
+  `NONE` -- Don't collect container logs.
By default, this property is set to `CLOUDWATCH`.
Amazon GameLift Servers requires permissions to send logs other AWS services in your account. These permissions are included in the IAM fleet role for this container fleet (see `FleetRoleArn)`.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

 ** [MetricGroups](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-MetricGroups"></a>
The name of an AWS CloudWatch metric group to add this fleet to. You can use a metric group to aggregate metrics for multiple fleets. You can specify an existing metric group name or use a new name to create a new metric group. Each fleet can have only one metric group, but you can change this value at any time.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [NewGameSessionProtectionPolicy](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-NewGameSessionProtectionPolicy"></a>
Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift Servers might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using [UpdateGameSession](gamelift/latest/apireference/API_UpdateGameSession.html).
+  **NoProtection** -- Game sessions can be shut down during active gameplay.
+  **FullProtection** -- Game sessions in `ACTIVE` status can't be shut down.
By default, this property is set to `NoProtection`.
Type: String
Valid Values: `NoProtection | FullProtection`
Required: No

 ** [PerInstanceContainerGroupDefinitionName](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-PerInstanceContainerGroupDefinitionName"></a>
The name of a container group definition resource that describes a set of axillary software. A fleet instance has one process for executables in this container group. A per-instance container group is optional. You can update the fleet to add or remove a per-instance container group at any time. You can specify the container group definition's name to use the latest version. Alternatively, provide an ARN value with a specific version number.
Create a container group definition by calling [https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html). This operation creates a [https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** [PlayerGatewayMode](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-PlayerGatewayMode"></a>
Configures player gateway for your fleet. Player gateway provides benefits such as DDoS protection by rate limiting and validating traﬃc before it reaches game servers, hiding game server IP addresses from players, and providing updated endpoints when relay endpoints become unhealthy.
 **How it works:** When enabled, game clients connect to relay endpoints instead of to your game servers. Player gateway validates player gateway tokens and routes traffic to the appropriate game server. Your game backend calls [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html) to retrieve relay endpoints and player gateway tokens for your game clients. To learn more about this topic, see [DDoS protection with Amazon GameLift Servers player gateway](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html).
Possible values include:
+  `DISABLED` (default) -- Game clients connect to the game server endpoint. Use this when you do not intend to integrate your game with player gateway.
+  `ENABLED` -- Player gateway is available in fleet locations where it is supported. Your game backend can call [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html) to obtain a player gateway token and endpoints for game clients.
+  `REQUIRED` -- Player gateway is available in fleet locations where it is supported, and the fleet can only use locations that support this feature. Attempting to add a remote location to your fleet which does not support player gateway will result in an `InvalidRequestException`.
Type: String
Valid Values: `DISABLED | ENABLED | REQUIRED`
Required: No

 ** [Tags](#API_CreateContainerFleet_RequestSyntax) **   <a name="gameliftservers-CreateContainerFleet-request-Tags"></a>
A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateContainerFleet_ResponseSyntax"></a>

```
{
   "ContainerFleet": {
      "BillingType": "string",
      "CreationTime": number,
      "DeploymentDetails": {
         "LatestDeploymentId": "string"
      },
      "Description": "string",
      "FleetArn": "string",
      "FleetId": "string",
      "FleetRoleArn": "string",
      "GameServerContainerGroupDefinitionArn": "string",
      "GameServerContainerGroupDefinitionName": "string",
      "GameServerContainerGroupsPerInstance": number,
      "GameSessionCreationLimitPolicy": {
         "NewGameSessionsPerCreator": number,
         "PolicyPeriodInMinutes": number
      },
      "InstanceConnectionPortRange": {
         "FromPort": number,
         "ToPort": number
      },
      "InstanceInboundPermissions": [
         {
            "FromPort": number,
            "IpRange": "string",
            "Protocol": "string",
            "ToPort": number
         }
      ],
      "InstanceType": "string",
      "LocationAttributes": [
         {
            "Location": "string",
            "PlayerGatewayStatus": "string",
            "Status": "string"
         }
      ],
      "LogConfiguration": {
         "LogDestination": "string",
         "LogGroupArn": "string",
         "S3BucketName": "string"
      },
      "MaximumGameServerContainerGroupsPerInstance": number,
      "MetricGroups": [ "string" ],
      "NewGameSessionProtectionPolicy": "string",
      "PerInstanceContainerGroupDefinitionArn": "string",
      "PerInstanceContainerGroupDefinitionName": "string",
      "PlayerGatewayMode": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_CreateContainerFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerFleet](#API_CreateContainerFleet_ResponseSyntax) **   <a name="gameliftservers-CreateContainerFleet-response-ContainerFleet"></a>
The properties for the new container fleet, including current status. All fleets are initially placed in `PENDING` status.
Type: [ContainerFleet](API_ContainerFleet.md) object

## Errors
<a name="API_CreateContainerFleet_Errors"></a>

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

 ** TaggingFailedException **
The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_CreateContainerFleet_Examples"></a>

### Create a simple single-region container fleet
<a name="API_CreateContainerFleet_Example_1"></a>

This example creates a container fleet with a game server container group definition only. It uses all the Amazon GameLift Servers defaults.

#### Sample Request
<a name="API_CreateContainerFleet_Example_1_Request"></a>

```
{
    "FleetRoleArn": "arn:aws:iam::MyAccount:role/MyRole",
    "GameServerContainerGroupDefinitionName": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:2"
    }
}
```

#### Sample Response
<a name="API_CreateContainerFleet_Example_1_Response"></a>

```
{
   "ContainerFleet": {
      "BillingType": ON_DEMAND,
      "CreationTime": 1736365885.22,
      "DeploymentDetails": {
         "LatestDeploymentId": "deployment-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
      },
      "FleetArn": "arn:aws:gamelift:us-west-2:111122223333:containerfleet/containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
      "FleetId": "containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
      "FleetRoleArn": "arn:aws:iam::MyAccount:role/MyRole",
      "GameServerContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:2",
      "GameServerContainerGroupDefinitionName": "MyAdventureGameContainerGroup",
      "GameServerContainerGroupsPerInstance": number,
      "InstanceConnectionPortRange": {
         "FromPort": 4192,
         "ToPort": 4242
      },
      "InstanceInboundPermissions": [
         {
            "FromPort": 4192,
            "IpRange": "string",
            "Protocol": "UDP",
            "ToPort": 4242,
         }
      ],
      "InstanceType": "c5.large",
      "LogConfiguration": {
         "LogGroupArn": "arn:aws:logs:us-west-2:111222333444:log-group:customerLogs",
         "LogDestination": "CLOUDWATCH"
      },
      "MaximumGameServerContainerGroupsPerInstance": 10,
      "NewGameSessionProtectionPolicy": "NoProtection",
      "Status": "PENDING"
   }
}
```

## See Also
<a name="API_CreateContainerFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateContainerFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateContainerFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateContainerFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateContainerFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateContainerFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateContainerFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateContainerFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateContainerFleet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateContainerFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateContainerFleet)
