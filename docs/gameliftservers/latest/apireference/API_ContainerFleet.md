---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerFleet.html
---

# ContainerFleet
<a name="API_ContainerFleet"></a>

Describes an Amazon GameLift Servers managed container fleet.

## Contents
<a name="API_ContainerFleet_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BillingType **   <a name="gameliftservers-Type-ContainerFleet-BillingType"></a>
Indicates whether the fleet uses On-Demand or Spot instances for this fleet. Learn more about when to use [ On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot). You can't update this fleet property.
By default, this property is set to `ON_DEMAND`.
Type: String
Valid Values: `ON_DEMAND | SPOT`
Required: No

 ** CreationTime **   <a name="gameliftservers-Type-ContainerFleet-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** DeploymentDetails **   <a name="gameliftservers-Type-ContainerFleet-DeploymentDetails"></a>
Information about the most recent deployment for the container fleet.
Type: [DeploymentDetails](API_DeploymentDetails.md) object
Required: No

 ** Description **   <a name="gameliftservers-Type-ContainerFleet-Description"></a>
A meaningful description of the container fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** FleetArn **   <a name="gameliftservers-Type-ContainerFleet-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`. In a GameLift fleet ARN, the resource ID matches the `FleetId` value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** FleetId **   <a name="gameliftservers-Type-ContainerFleet-FleetId"></a>
A unique identifier for the container fleet to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** FleetRoleArn **   <a name="gameliftservers-Type-ContainerFleet-FleetRoleArn"></a>
The unique identifier for an AWS Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers. See [Set up an IAM service role](https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html). This fleet property can't be changed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:.*:role\/[\w+=,.@-]+`
Required: No

 ** GameServerContainerGroupDefinitionArn **   <a name="gameliftservers-Type-ContainerFleet-GameServerContainerGroupDefinitionArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to the fleet's game server container group. The ARN value also identifies the specific container group definition version in use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** GameServerContainerGroupDefinitionName **   <a name="gameliftservers-Type-ContainerFleet-GameServerContainerGroupDefinitionName"></a>
The name of the fleet's game server container group definition, which describes how to deploy containers with your game server build and support software onto each fleet instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: No

 ** GameServerContainerGroupsPerInstance **   <a name="gameliftservers-Type-ContainerFleet-GameServerContainerGroupsPerInstance"></a>
The number of times to replicate the game server container group on each fleet instance.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** GameSessionCreationLimitPolicy **   <a name="gameliftservers-Type-ContainerFleet-GameSessionCreationLimitPolicy"></a>
A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.
Type: [GameSessionCreationLimitPolicy](API_GameSessionCreationLimitPolicy.md) object
Required: No

 ** InstanceConnectionPortRange **   <a name="gameliftservers-Type-ContainerFleet-InstanceConnectionPortRange"></a>
The set of port numbers to open on each instance in a container fleet. Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.
The port range must not overlap with the Amazon GameLift Servers reserved port range `4092-4191`. This range is reserved for internal Amazon GameLift Servers services.
Type: [ConnectionPortRange](API_ConnectionPortRange.md) object
Required: No

 ** InstanceInboundPermissions **   <a name="gameliftservers-Type-ContainerFleet-InstanceInboundPermissions"></a>
The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.
Type: Array of [IpPermission](API_IpPermission.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** InstanceType **   <a name="gameliftservers-Type-ContainerFleet-InstanceType"></a>
The Amazon EC2 instance type to use for all instances in the fleet. Instance type determines the computing resources and processing power that's available to host your game servers. This includes including CPU, memory, storage, and networking capacity. You can't update this fleet property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** LocationAttributes **   <a name="gameliftservers-Type-ContainerFleet-LocationAttributes"></a>
Information about the container fleet's remote locations where fleet instances are deployed.
Type: Array of [ContainerFleetLocationAttributes](API_ContainerFleetLocationAttributes.md) objects
Required: No

 ** LogConfiguration **   <a name="gameliftservers-Type-ContainerFleet-LogConfiguration"></a>
The method that is used to collect container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs.
+  `CLOUDWATCH` -- Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
+  `S3` -- Store logs in an Amazon S3 bucket that you define.
+  `NONE` -- Don't collect container logs.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

 ** MaximumGameServerContainerGroupsPerInstance **   <a name="gameliftservers-Type-ContainerFleet-MaximumGameServerContainerGroupsPerInstance"></a>
The calculated maximum number of game server container group that can be deployed on each fleet instance. The calculation depends on the resource needs of the container group and the CPU and memory resources of the fleet's instance type.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** MetricGroups **   <a name="gameliftservers-Type-ContainerFleet-MetricGroups"></a>
The name of an AWS CloudWatch metric group to add this fleet to. Metric groups aggregate metrics for multiple fleets.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** NewGameSessionProtectionPolicy **   <a name="gameliftservers-Type-ContainerFleet-NewGameSessionProtectionPolicy"></a>
Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift Servers might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using [UpdateGameSession](gamelift/latest/apireference/API_UpdateGameSession.html).
+  **NoProtection** -- Game sessions can be shut down during active gameplay.
+  **FullProtection** -- Game sessions in `ACTIVE` status can't be shut down.
Type: String
Valid Values: `NoProtection | FullProtection`
Required: No

 ** PerInstanceContainerGroupDefinitionArn **   <a name="gameliftservers-Type-ContainerFleet-PerInstanceContainerGroupDefinitionArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to the fleet's per-instance container group. The ARN value also identifies the specific container group definition version in use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** PerInstanceContainerGroupDefinitionName **   <a name="gameliftservers-Type-ContainerFleet-PerInstanceContainerGroupDefinitionName"></a>
The name of the fleet's per-instance container group definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: No

 ** PlayerGatewayMode **   <a name="gameliftservers-Type-ContainerFleet-PlayerGatewayMode"></a>
Indicates whether player gateway is enabled for this container fleet. Player gateway provides benefits such as DDoS protection with negligible impact to latency.
If `ENABLED` or `REQUIRED`, game clients can use player gateway to connect with the game server. If `DISABLED`, game clients cannot use player gateway. Instead, they have to directly connect to the game server.
Type: String
Valid Values: `DISABLED | ENABLED | REQUIRED`
Required: No

 ** Status **   <a name="gameliftservers-Type-ContainerFleet-Status"></a>
The current status of the container fleet.
+  `PENDING` -- A new container fleet has been requested.
+  `CREATING` -- A new container fleet resource is being created.
+  `CREATED` -- A new container fleet resource has been created. No fleet instances have been deployed.
+  `ACTIVATING` -- New container fleet instances are being deployed.
+  `ACTIVE` -- The container fleet has been deployed and is ready to host game sessions.
+  `UPDATING` -- Updates to the container fleet is being updated. A deployment is in progress.
+  `EXPIRED` -- The container fleet has been expired. The fleet is scaled down to zero instances and cannot host new game sessions.
Type: String
Valid Values: `PENDING | CREATING | CREATED | ACTIVATING | ACTIVE | UPDATING | DELETING`
Required: No

## See Also
<a name="API_ContainerFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerFleet)
