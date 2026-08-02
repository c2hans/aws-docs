---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-containerfleet.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet
<a name="aws-resource-gamelift-containerfleet"></a>

Describes an Amazon GameLift Servers managed container fleet.

## Syntax
<a name="aws-resource-gamelift-containerfleet-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-gamelift-containerfleet-syntax.json"></a>

```
{
  "Type" : "AWS::GameLift::ContainerFleet",
  "Properties" : {
      "[BillingType](#cfn-gamelift-containerfleet-billingtype)" : {{String}},
      "[DeploymentConfiguration](#cfn-gamelift-containerfleet-deploymentconfiguration)" : {{DeploymentConfiguration}},
      "[Description](#cfn-gamelift-containerfleet-description)" : {{String}},
      "[FleetRoleArn](#cfn-gamelift-containerfleet-fleetrolearn)" : {{String}},
      "[GameServerContainerGroupDefinitionName](#cfn-gamelift-containerfleet-gameservercontainergroupdefinitionname)" : {{String}},
      "[GameServerContainerGroupsPerInstance](#cfn-gamelift-containerfleet-gameservercontainergroupsperinstance)" : {{Integer}},
      "[GameSessionCreationLimitPolicy](#cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy)" : {{GameSessionCreationLimitPolicy}},
      "[InstanceConnectionPortRange](#cfn-gamelift-containerfleet-instanceconnectionportrange)" : {{ConnectionPortRange}},
      "[InstanceInboundPermissions](#cfn-gamelift-containerfleet-instanceinboundpermissions)" : {{[ IpPermission, ... ]}},
      "[InstanceType](#cfn-gamelift-containerfleet-instancetype)" : {{String}},
      "[Locations](#cfn-gamelift-containerfleet-locations)" : {{[ LocationConfiguration, ... ]}},
      "[LogConfiguration](#cfn-gamelift-containerfleet-logconfiguration)" : {{LogConfiguration}},
      "[MetricGroups](#cfn-gamelift-containerfleet-metricgroups)" : {{[ String, ... ]}},
      "[NewGameSessionProtectionPolicy](#cfn-gamelift-containerfleet-newgamesessionprotectionpolicy)" : {{String}},
      "[PerInstanceContainerGroupDefinitionName](#cfn-gamelift-containerfleet-perinstancecontainergroupdefinitionname)" : {{String}},
      "[PlayerGatewayMode](#cfn-gamelift-containerfleet-playergatewaymode)" : {{String}},
      "[ScalingPolicies](#cfn-gamelift-containerfleet-scalingpolicies)" : {{[ ScalingPolicy, ... ]}},
      "[Tags](#cfn-gamelift-containerfleet-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-gamelift-containerfleet-syntax.yaml"></a>

```
Type: AWS::GameLift::ContainerFleet
Properties:
  [BillingType](#cfn-gamelift-containerfleet-billingtype): {{String}}
  [DeploymentConfiguration](#cfn-gamelift-containerfleet-deploymentconfiguration): {{
    DeploymentConfiguration}}
  [Description](#cfn-gamelift-containerfleet-description): {{String}}
  [FleetRoleArn](#cfn-gamelift-containerfleet-fleetrolearn): {{String}}
  [GameServerContainerGroupDefinitionName](#cfn-gamelift-containerfleet-gameservercontainergroupdefinitionname): {{String}}
  [GameServerContainerGroupsPerInstance](#cfn-gamelift-containerfleet-gameservercontainergroupsperinstance): {{Integer}}
  [GameSessionCreationLimitPolicy](#cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy): {{
    GameSessionCreationLimitPolicy}}
  [InstanceConnectionPortRange](#cfn-gamelift-containerfleet-instanceconnectionportrange): {{
    ConnectionPortRange}}
  [InstanceInboundPermissions](#cfn-gamelift-containerfleet-instanceinboundpermissions): {{
    - IpPermission}}
  [InstanceType](#cfn-gamelift-containerfleet-instancetype): {{String}}
  [Locations](#cfn-gamelift-containerfleet-locations): {{
    - LocationConfiguration}}
  [LogConfiguration](#cfn-gamelift-containerfleet-logconfiguration): {{
    LogConfiguration}}
  [MetricGroups](#cfn-gamelift-containerfleet-metricgroups): {{
    - String}}
  [NewGameSessionProtectionPolicy](#cfn-gamelift-containerfleet-newgamesessionprotectionpolicy): {{String}}
  [PerInstanceContainerGroupDefinitionName](#cfn-gamelift-containerfleet-perinstancecontainergroupdefinitionname): {{String}}
  [PlayerGatewayMode](#cfn-gamelift-containerfleet-playergatewaymode): {{String}}
  [ScalingPolicies](#cfn-gamelift-containerfleet-scalingpolicies): {{
    - ScalingPolicy}}
  [Tags](#cfn-gamelift-containerfleet-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-gamelift-containerfleet-properties"></a>

`BillingType`  <a name="cfn-gamelift-containerfleet-billingtype"></a>
Indicates whether the fleet uses On-Demand or Spot instances for this fleet. Learn more about when to use [ On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot). You can't update this fleet property.
By default, this property is set to `ON_DEMAND`.
*Required*: No
*Type*: String
*Allowed values*: `ON_DEMAND | SPOT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeploymentConfiguration`  <a name="cfn-gamelift-containerfleet-deploymentconfiguration"></a>
Set of rules for processing a deployment for a container fleet update.
*Required*: No
*Type*: [DeploymentConfiguration](aws-properties-gamelift-containerfleet-deploymentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-gamelift-containerfleet-description"></a>
A meaningful description of the container fleet.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FleetRoleArn`  <a name="cfn-gamelift-containerfleet-fleetrolearn"></a>
The unique identifier for an AWS Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers. See [Set up an IAM service role](https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html). This fleet property can't be changed.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-.*)?:[a-z-]+:(([a-z]+-)+[0-9])?:([0-9]{12})?:[^.]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GameServerContainerGroupDefinitionName`  <a name="cfn-gamelift-containerfleet-gameservercontainergroupdefinitionname"></a>
The name of the fleet's game server container group definition, which describes how to deploy containers with your game server build and support software onto each fleet instance.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GameServerContainerGroupsPerInstance`  <a name="cfn-gamelift-containerfleet-gameservercontainergroupsperinstance"></a>
The number of times to replicate the game server container group on each fleet instance.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GameSessionCreationLimitPolicy`  <a name="cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy"></a>
A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.
*Required*: No
*Type*: [GameSessionCreationLimitPolicy](aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceConnectionPortRange`  <a name="cfn-gamelift-containerfleet-instanceconnectionportrange"></a>
The set of port numbers to open on each instance in a container fleet. Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.
The port range must not overlap with the Amazon GameLift Servers reserved port range `4092-4191`. This range is reserved for internal Amazon GameLift Servers services.
*Required*: No
*Type*: [ConnectionPortRange](aws-properties-gamelift-containerfleet-connectionportrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceInboundPermissions`  <a name="cfn-gamelift-containerfleet-instanceinboundpermissions"></a>
The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.
*Required*: No
*Type*: Array of [IpPermission](aws-properties-gamelift-containerfleet-ippermission.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-gamelift-containerfleet-instancetype"></a>
The Amazon EC2 instance type to use for all instances in the fleet. Instance type determines the computing resources and processing power that's available to host your game servers. This includes including CPU, memory, storage, and networking capacity. You can't update this fleet property.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Locations`  <a name="cfn-gamelift-containerfleet-locations"></a>
A set of locations to deploy container fleet instances to. You can add any AWS Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more AWS Region codes, such as `us-west-2`, or Local Zone names. Also include the fleet's home Region, which is the AWS Region where the fleet is created. For a list of supported Regions and Local Zones, see [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.
*Required*: No
*Type*: Array of [LocationConfiguration](aws-properties-gamelift-containerfleet-locationconfiguration.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-gamelift-containerfleet-logconfiguration"></a>
The method that is used to collect container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs.
+ `CLOUDWATCH` -- Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
+ `S3` -- Store logs in an Amazon S3 bucket that you define.
+ `NONE` -- Don't collect container logs.
*Required*: No
*Type*: [LogConfiguration](aws-properties-gamelift-containerfleet-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricGroups`  <a name="cfn-gamelift-containerfleet-metricgroups"></a>
The name of an AWS CloudWatch metric group to add this fleet to. Metric groups aggregate metrics for multiple fleets.
*Required*: No
*Type*: Array of String
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewGameSessionProtectionPolicy`  <a name="cfn-gamelift-containerfleet-newgamesessionprotectionpolicy"></a>
Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift Servers might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using [UpdateGameSession](gamelift/latest/apireference/API_UpdateGameSession.html).
+ **NoProtection** -- Game sessions can be shut down during active gameplay.
+ **FullProtection** -- Game sessions in `ACTIVE` status can't be shut down.
*Required*: No
*Type*: String
*Allowed values*: `FullProtection | NoProtection`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerInstanceContainerGroupDefinitionName`  <a name="cfn-gamelift-containerfleet-perinstancecontainergroupdefinitionname"></a>
The name of the fleet's per-instance container group definition.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlayerGatewayMode`  <a name="cfn-gamelift-containerfleet-playergatewaymode"></a>
Configures player gateway for your fleet. Player gateway provides benefits such as DDoS protection by rate limiting and validating traﬃc before it reaches game servers, hiding game server IP addresses from players, and providing updated endpoints when relay endpoints become unhealthy.
**How it works:** When enabled, game clients connect to relay endpoints instead of to your game servers. Player gateway validates player gateway tokens and routes traffic to the appropriate game server. Your game backend calls [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html) to retrieve relay endpoints and player gateway tokens for your game clients. To learn more about this topic, see [DDoS protection with Amazon GameLift Servers player gateway](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html).
Possible values include:
+ `DISABLED` (default) -- Game clients connect to the game server endpoint. Use this when you do not intend to integrate your game with player gateway.
+ `ENABLED` -- Player gateway is available in fleet locations where it is supported. Your game backend can call [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html) to obtain a player gateway token and endpoints for game clients.
+ `REQUIRED` -- Player gateway is available in fleet locations where it is supported, and the fleet can only use locations that support this feature. Attempting to add a remote location to your fleet which does not support player gateway will result in an `InvalidRequestException`.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED | REQUIRED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScalingPolicies`  <a name="cfn-gamelift-containerfleet-scalingpolicies"></a>
Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.
*Required*: No
*Type*: Array of [ScalingPolicy](aws-properties-gamelift-containerfleet-scalingpolicy.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-gamelift-containerfleet-tags"></a>
A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.
*Required*: No
*Type*: Array of [Tag](aws-properties-gamelift-containerfleet-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-gamelift-containerfleet-return-values"></a>

### Ref
<a name="aws-resource-gamelift-containerfleet-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-gamelift-containerfleet-return-values-fn--getatt"></a>

####
<a name="aws-resource-gamelift-containerfleet-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).

`FleetArn`  <a name="FleetArn-fn::getatt"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`. In a GameLift fleet ARN, the resource ID matches the `FleetId` value.

`FleetId`  <a name="FleetId-fn::getatt"></a>
A unique identifier for the container fleet to retrieve.

`GameServerContainerGroupDefinitionArn`  <a name="GameServerContainerGroupDefinitionArn-fn::getatt"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to the fleet's game server container group. The ARN value also identifies the specific container group definition version in use.

`MaximumGameServerContainerGroupsPerInstance`  <a name="MaximumGameServerContainerGroupsPerInstance-fn::getatt"></a>
The calculated maximum number of game server container group that can be deployed on each fleet instance. The calculation depends on the resource needs of the container group and the CPU and memory resources of the fleet's instance type.

`PerInstanceContainerGroupDefinitionArn`  <a name="PerInstanceContainerGroupDefinitionArn-fn::getatt"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to the fleet's per-instance container group. The ARN value also identifies the specific container group definition version in use.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the container fleet.
+ `PENDING` -- A new container fleet has been requested.
+ `CREATING` -- A new container fleet resource is being created.
+ `CREATED` -- A new container fleet resource has been created. No fleet instances have been deployed.
+ `ACTIVATING` -- New container fleet instances are being deployed.
+ `ACTIVE` -- The container fleet has been deployed and is ready to host game sessions.
+ `UPDATING` -- Updates to the container fleet is being updated. A deployment is in progress.
+ `EXPIRED` -- The container fleet has been expired. The fleet is scaled down to zero instances and cannot host new game sessions.
