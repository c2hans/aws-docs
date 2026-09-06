---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-fleet.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Fleet
<a name="aws-resource-gamelift-fleet"></a>

The `AWS::GameLift::Fleet` resource creates an Amazon GameLift (GameLift) fleet to host custom game server or Realtime Servers. A fleet is a set of EC2 instances, configured with instructions to run game servers on each instance.

## Syntax
<a name="aws-resource-gamelift-fleet-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-gamelift-fleet-syntax.json"></a>

```
{
  "Type" : "AWS::GameLift::Fleet",
  "Properties" : {
      "[AnywhereConfiguration](#cfn-gamelift-fleet-anywhereconfiguration)" : {{AnywhereConfiguration}},
      "[ApplyCapacity](#cfn-gamelift-fleet-applycapacity)" : {{String}},
      "[BuildId](#cfn-gamelift-fleet-buildid)" : {{String}},
      "[CertificateConfiguration](#cfn-gamelift-fleet-certificateconfiguration)" : {{CertificateConfiguration}},
      "[ComputeType](#cfn-gamelift-fleet-computetype)" : {{String}},
      "[Description](#cfn-gamelift-fleet-description)" : {{String}},
      "[EC2InboundPermissions](#cfn-gamelift-fleet-ec2inboundpermissions)" : {{[ IpPermission, ... ]}},
      "[EC2InstanceType](#cfn-gamelift-fleet-ec2instancetype)" : {{String}},
      "[FleetType](#cfn-gamelift-fleet-fleettype)" : {{String}},
      "[InstanceRoleARN](#cfn-gamelift-fleet-instancerolearn)" : {{String}},
      "[InstanceRoleCredentialsProvider](#cfn-gamelift-fleet-instancerolecredentialsprovider)" : {{String}},
      "[Locations](#cfn-gamelift-fleet-locations)" : {{[ LocationConfiguration, ... ]}},
      "[MetricGroups](#cfn-gamelift-fleet-metricgroups)" : {{[ String, ... ]}},
      "[Name](#cfn-gamelift-fleet-name)" : {{String}},
      "[NewGameSessionProtectionPolicy](#cfn-gamelift-fleet-newgamesessionprotectionpolicy)" : {{String}},
      "[PeerVpcAwsAccountId](#cfn-gamelift-fleet-peervpcawsaccountid)" : {{String}},
      "[PeerVpcId](#cfn-gamelift-fleet-peervpcid)" : {{String}},
      "[PlayerGatewayConfiguration](#cfn-gamelift-fleet-playergatewayconfiguration)" : {{PlayerGatewayConfiguration}},
      "[PlayerGatewayMode](#cfn-gamelift-fleet-playergatewaymode)" : {{String}},
      "[ResourceCreationLimitPolicy](#cfn-gamelift-fleet-resourcecreationlimitpolicy)" : {{ResourceCreationLimitPolicy}},
      "[RuntimeConfiguration](#cfn-gamelift-fleet-runtimeconfiguration)" : {{RuntimeConfiguration}},
      "[ScalingPolicies](#cfn-gamelift-fleet-scalingpolicies)" : {{[ ScalingPolicy, ... ]}},
      "[ScriptId](#cfn-gamelift-fleet-scriptid)" : {{String}},
      "[Tags](#cfn-gamelift-fleet-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-gamelift-fleet-syntax.yaml"></a>

```
Type: AWS::GameLift::Fleet
Properties:
  [AnywhereConfiguration](#cfn-gamelift-fleet-anywhereconfiguration): {{
    AnywhereConfiguration}}
  [ApplyCapacity](#cfn-gamelift-fleet-applycapacity): {{String}}
  [BuildId](#cfn-gamelift-fleet-buildid): {{String}}
  [CertificateConfiguration](#cfn-gamelift-fleet-certificateconfiguration): {{
    CertificateConfiguration}}
  [ComputeType](#cfn-gamelift-fleet-computetype): {{String}}
  [Description](#cfn-gamelift-fleet-description): {{String}}
  [EC2InboundPermissions](#cfn-gamelift-fleet-ec2inboundpermissions): {{
    - IpPermission}}
  [EC2InstanceType](#cfn-gamelift-fleet-ec2instancetype): {{String}}
  [FleetType](#cfn-gamelift-fleet-fleettype): {{String}}
  [InstanceRoleARN](#cfn-gamelift-fleet-instancerolearn): {{String}}
  [InstanceRoleCredentialsProvider](#cfn-gamelift-fleet-instancerolecredentialsprovider): {{String}}
  [Locations](#cfn-gamelift-fleet-locations): {{
    - LocationConfiguration}}
  [MetricGroups](#cfn-gamelift-fleet-metricgroups): {{
    - String}}
  [Name](#cfn-gamelift-fleet-name): {{String}}
  [NewGameSessionProtectionPolicy](#cfn-gamelift-fleet-newgamesessionprotectionpolicy): {{String}}
  [PeerVpcAwsAccountId](#cfn-gamelift-fleet-peervpcawsaccountid): {{String}}
  [PeerVpcId](#cfn-gamelift-fleet-peervpcid): {{String}}
  [PlayerGatewayConfiguration](#cfn-gamelift-fleet-playergatewayconfiguration): {{
    PlayerGatewayConfiguration}}
  [PlayerGatewayMode](#cfn-gamelift-fleet-playergatewaymode): {{String}}
  [ResourceCreationLimitPolicy](#cfn-gamelift-fleet-resourcecreationlimitpolicy): {{
    ResourceCreationLimitPolicy}}
  [RuntimeConfiguration](#cfn-gamelift-fleet-runtimeconfiguration): {{
    RuntimeConfiguration}}
  [ScalingPolicies](#cfn-gamelift-fleet-scalingpolicies): {{
    - ScalingPolicy}}
  [ScriptId](#cfn-gamelift-fleet-scriptid): {{String}}
  [Tags](#cfn-gamelift-fleet-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-gamelift-fleet-properties"></a>

`AnywhereConfiguration`  <a name="cfn-gamelift-fleet-anywhereconfiguration"></a>
Amazon GameLift Servers Anywhere configuration options.
*Required*: No
*Type*: [AnywhereConfiguration](aws-properties-gamelift-fleet-anywhereconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplyCapacity`  <a name="cfn-gamelift-fleet-applycapacity"></a>
Current resource capacity settings for managed EC2 fleets and managed container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region.
**Returned by:**[DescribeFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html), [DescribeFleetLocationCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html), [UpdateFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html)
*Required*: No
*Type*: String
*Allowed values*: `ON_UPDATE | ON_CREATE_AND_UPDATE | ON_CREATE_AND_UPDATE_WITH_AUTOSCALING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuildId`  <a name="cfn-gamelift-fleet-buildid"></a>
A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a `READY` status. This fleet setting cannot be changed once the fleet is created.
*Required*: Conditional
*Type*: String
*Pattern*: `^build-\S+|^arn:.*:build/build-\S+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CertificateConfiguration`  <a name="cfn-gamelift-fleet-certificateconfiguration"></a>
Prompts Amazon GameLift Servers to generate a TLS/SSL certificate for the fleet. Amazon GameLift Servers uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift Servers. By default, the `CertificateConfiguration` is `DISABLED`. You can't change this property after you create the fleet.
AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition.
ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see [Supported Regions](https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html) in the *AWS Certificate Manager User Guide*.
*Required*: No
*Type*: [CertificateConfiguration](aws-properties-gamelift-fleet-certificateconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComputeType`  <a name="cfn-gamelift-fleet-computetype"></a>
The type of compute resource used to host your game servers.
+ `EC2` – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting.
+ `ANYWHERE` – Game servers and supporting software are deployed to compute resources that you provide and manage. With this compute type, you can also set the `AnywhereConfiguration` parameter.
*Required*: No
*Type*: String
*Allowed values*: `EC2 | ANYWHERE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-gamelift-fleet-description"></a>
A description for the fleet.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EC2InboundPermissions`  <a name="cfn-gamelift-fleet-ec2inboundpermissions"></a>
The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. Set this parameter for managed EC2 fleets. You can leave this parameter empty when creating the fleet, but you must call [https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings) to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Amazon GameLift Servers Realtime fleets, Amazon GameLift Servers automatically sets TCP and UDP ranges.
*Required*: No
*Type*: Array of [IpPermission](aws-properties-gamelift-fleet-ippermission.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EC2InstanceType`  <a name="cfn-gamelift-fleet-ec2instancetype"></a>
The Amazon GameLift Servers-supported Amazon EC2 instance type to use with managed EC2 fleets. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See [Amazon Elastic Compute Cloud Instance Types](https://aws.amazon.com/ec2/instance-types/) for detailed descriptions of Amazon EC2 instance types.
*Required*: No
*Type*: String
*Pattern*: `^.*..*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FleetType`  <a name="cfn-gamelift-fleet-fleettype"></a>
Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to `ON_DEMAND`. Learn more about when to use [ On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot). This fleet property can't be changed after the fleet is created.
*Required*: No
*Type*: String
*Allowed values*: `ON_DEMAND | SPOT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceRoleARN`  <a name="cfn-gamelift-fleet-instancerolearn"></a>
A unique identifier for an IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the [IAM dashboard](https://console.aws.amazon.com/iam/) in the AWS Management Console. Learn more about using on-box credentials for your game servers at [ Access external resources from a game server](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html). This attribute is used with fleets where `ComputeType` is `EC2`.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-.*)?:[a-z-]+:(([a-z]+-)+[0-9])?:([0-9]{12})?:[^.]+$`
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceRoleCredentialsProvider`  <a name="cfn-gamelift-fleet-instancerolecredentialsprovider"></a>
Indicates that fleet instances maintain a shared credentials file for the IAM role defined in `InstanceRoleArn`. Shared credentials allow applications that are deployed with the game server executable to communicate with other AWS resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see [ Communicate with other AWS resources from your fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html). This attribute is used with fleets where `ComputeType` is `EC2`.
*Required*: No
*Type*: String
*Allowed values*: `SHARED_CREDENTIAL_FILE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Locations`  <a name="cfn-gamelift-fleet-locations"></a>
A set of remote locations to deploy additional instances to and manage as a multi-location fleet. Use this parameter when creating a fleet in AWS Regions that support multiple locations. You can add any AWS Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more AWS Region codes, such as `us-west-2`, or Local Zone names. When using this parameter, Amazon GameLift Servers requires you to include your home location in the request. For a list of supported Regions and Local Zones, see [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.
*Required*: No
*Type*: Array of [LocationConfiguration](aws-properties-gamelift-fleet-locationconfiguration.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricGroups`  <a name="cfn-gamelift-fleet-metricgroups"></a>
The name of an AWS CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.
*Required*: No
*Type*: Array of String
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-gamelift-fleet-name"></a>
A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewGameSessionProtectionPolicy`  <a name="cfn-gamelift-fleet-newgamesessionprotectionpolicy"></a>
The status of termination protection for active game sessions on the fleet. By default, this property is set to `NoProtection`.
+ **NoProtection** - Game sessions can be terminated during active gameplay as a result of a scale-down event.
+ **FullProtection** - Game sessions in `ACTIVE` status cannot be terminated during a scale-down event.
*Required*: No
*Type*: String
*Allowed values*: `FullProtection | NoProtection`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeerVpcAwsAccountId`  <a name="cfn-gamelift-fleet-peervpcawsaccountid"></a>
Used when peering your Amazon GameLift Servers fleet with a VPC, the unique identifier for the AWS account that owns the VPC. You can find your account ID in the AWS Management Console under account settings.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerVpcId`  <a name="cfn-gamelift-fleet-peervpcid"></a>
A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the [VPC Dashboard](https://console.aws.amazon.com/vpc/) in the AWS Management Console. Learn more about VPC peering in [VPC Peering with Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html).
*Required*: No
*Type*: String
*Pattern*: `^vpc-\S+`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlayerGatewayConfiguration`  <a name="cfn-gamelift-fleet-playergatewayconfiguration"></a>
Configuration settings for player gateway. Use this to specify advanced options for how player gateway handles connections.
*Required*: No
*Type*: [PlayerGatewayConfiguration](aws-properties-gamelift-fleet-playergatewayconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlayerGatewayMode`  <a name="cfn-gamelift-fleet-playergatewaymode"></a>
Configures player gateway for your fleet. Player gateway provides benefits such as DDoS protection by rate limiting and validating traﬃc before it reaches game servers, hiding game server IP addresses from players, and providing updated endpoints when relay endpoints become unhealthy. Note, player gateway is only available for fleets using server SDK 5.x or later game server builds.
**How it works:** When enabled, game clients connect to relay endpoints instead of to your game servers. Player gateway validates player gateway tokens and routes traffic to the appropriate game server. Your game backend calls [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html) to retrieve relay endpoints and player gateway tokens for your game clients. To learn more about this topic, see [DDoS protection with Amazon GameLift Servers player gateway](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html).
Possible values include:
+ `DISABLED` (default) -- Game clients connect to the game server endpoint. Use this when you do not intend to integrate your game with player gateway.
+ `ENABLED` -- Player gateway is available in fleet locations where it is supported. Your game backend can call [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html) to obtain a player gateway token and endpoints for game clients.
+ `REQUIRED` -- Player gateway is available in fleet locations where it is supported, and the fleet can only use locations that support this feature. Attempting to add a remote location to your fleet which does not support player gateway will result in an `InvalidRequestException`.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED | REQUIRED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceCreationLimitPolicy`  <a name="cfn-gamelift-fleet-resourcecreationlimitpolicy"></a>
A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.
*Required*: No
*Type*: [ResourceCreationLimitPolicy](aws-properties-gamelift-fleet-resourcecreationlimitpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeConfiguration`  <a name="cfn-gamelift-fleet-runtimeconfiguration"></a>
Instructions for how to launch and maintain server processes on instances in the fleet. The runtime configuration defines one or more server process configurations, each identifying a build executable or Realtime script file and the number of processes of that type to run concurrently.
The `RuntimeConfiguration` parameter is required unless the fleet is being configured using the older parameters `ServerLaunchPath` and `ServerLaunchParameters`, which are still supported for backward compatibility.
*Required*: Conditional
*Type*: [RuntimeConfiguration](aws-properties-gamelift-fleet-runtimeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingPolicies`  <a name="cfn-gamelift-fleet-scalingpolicies"></a>
Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.
*Required*: No
*Type*: Array of [ScalingPolicy](aws-properties-gamelift-fleet-scalingpolicy.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScriptId`  <a name="cfn-gamelift-fleet-scriptid"></a>
The unique identifier for a Realtime configuration script to be deployed on fleet instances. You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift Servers prior to creating the fleet. This fleet property cannot be changed later.
You can't use the `!Ref` command to reference a script created with a CloudFormation template for the fleet property `ScriptId`. Instead, use `Fn::GetAtt Script.Arn` or `Fn::GetAtt Script.Id` to retrieve either of these properties as input for `ScriptId`. Alternatively, enter a `ScriptId` string manually.
*Required*: Conditional
*Type*: String
*Pattern*: `^script-\S+|^arn:.*:script/script-\S+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-gamelift-fleet-tags"></a>
A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.
*Required*: No
*Type*: Array of [Tag](aws-properties-gamelift-fleet-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-gamelift-fleet-return-values"></a>

### Ref
<a name="aws-resource-gamelift-fleet-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the fleet ID, such as `fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-gamelift-fleet-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-gamelift-fleet-return-values-fn--getatt-fn--getatt"></a>

`FleetArn`  <a name="FleetArn-fn::getatt"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`. In a GameLift fleet ARN, the resource ID matches the `FleetId` value.

`FleetId`  <a name="FleetId-fn::getatt"></a>
A unique identifier for the fleet.

## Examples
<a name="aws-resource-gamelift-fleet--examples"></a>

**Topics**
+ [Create GameLift fleet with a Build](#aws-resource-gamelift-fleet--examples--Create_GameLift_fleet_with_a_Build)
+ [Create GameLift fleet with a Script](#aws-resource-gamelift-fleet--examples--Create_GameLift_fleet_with_a_Script)

### Create GameLift fleet with a Build
<a name="aws-resource-gamelift-fleet--examples--Create_GameLift_fleet_with_a_Build"></a>

The following example creates and configures a GameLift fleet for a custom game build. The fleet uses a `Ref` intrinsic function to specify a build, which can be declared elsewhere in the same template. The example syntax for log path and server launch path uses values for a Windows build.

Note: the JSON example shows how to escape the slashes (`\\`).

#### JSON
<a name="aws-resource-gamelift-fleet--examples--Create_GameLift_fleet_with_a_Build--json"></a>

```
{
    "Resources": {
        "FleetResource": {
            "Type": "AWS::GameLift::Fleet",
            "Properties": {
                "BuildId": {
                    "Ref": "BuildResource"
                },
                "CertificateConfiguration": {
                    "CertificateType": "DISABLED"
                },
                "Description": "Description of my Fleet",
                "DesiredEC2Instances": 1,
                "EC2InboundPermissions": [
                    {
                        "FromPort": 1234,
                        "ToPort": 1324,
                        "IpRange": "0.0.0.0/24",
                        "Protocol": "TCP"
                    },
                    {
                        "FromPort": 1356,
                        "ToPort": 1578,
                        "IpRange": "192.168.0.0/24",
                        "Protocol": "UDP"
                    }
                ],
                "EC2InstanceType": "c4.large",
                "FleetType": "SPOT",
                "LogPaths": [
                    "c:\\game\\testlog.log",
                    "c:\\game\\testlog2.log"
                ],
                "MetricGroups": [
                    "MetricGroupName"
                ],
                "Name": "MyGameFleet",
                "NewGameSessionProtectionPolicy": "FullProtection",
                "ResourceCreationLimitPolicy": {
                    "NewGameSessionsPerCreator": 5,
                    "PolicyPeriodInMinutes": 2
                },
                "RuntimeConfiguration": {
                    "GameSessionActivationTimeoutSeconds": 300,
                    "MaxConcurrentGameSessionActivations": 1,
                    "ServerProcesses": [
                        {
                            "ConcurrentExecutions": 1,
                            "LaunchPath": "c:\\game\\TestApplicationServer.exe"
                        }
                    ]
                },
                "Locations": [
                  "us-west-2",
                  "us-east-1",
                  "eu-west-1"
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-gamelift-fleet--examples--Create_GameLift_fleet_with_a_Build--yaml"></a>

```
Resources:
  FleetResource:
    Type: AWS::GameLift::Fleet
    Properties:
      BuildId: !Ref BuildResource
      CertificateConfiguration:
        CertificateType: DISABLED
      Description: Description of my Game Fleet
      DesiredEC2Instances: 1
      EC2InboundPermissions:
        - FromPort: 1234
          ToPort: 1324
          IpRange: 0.0.0.0/24
          Protocol: TCP
        - FromPort: 1356
          ToPort: 1578
          IpRange: 192.168.0.0/24
          Protocol: UDP
      EC2InstanceType: c4.large
      FleetType: SPOT
      LogPaths:
        - c:\game\testlog.log
        - c:\game\testlog2.log
      MetricGroups:
        - MetricGroupName
      Name: MyGameFleet
      NewGameSessionProtectionPolicy: FullProtection
      ResourceCreationLimitPolicy:
        NewGameSessionsPerCreator: 5
        PolicyPeriodInMinutes: 2
      RuntimeConfiguration:
        GameSessionActivationTimeoutSeconds: 300
        MaxConcurrentGameSessionActivations: 1
        ServerProcesses:
          - ConcurrentExecutions: 1
            LaunchPath: c:\game\TestApplicationServer.exe
        Locations:
          - Location: 'us-west-2'
          - Location: 'us-east-1'
          - Location: 'eu-west-1'
```

### Create GameLift fleet with a Script
<a name="aws-resource-gamelift-fleet--examples--Create_GameLift_fleet_with_a_Script"></a>

The following example creates and configures a GameLift fleet to run Realtime Servers. The fleet uses a `GetAtt` intrinsic function to specify a script, which can be declared elsewhere in the same template. Note that the syntax example for the log path and server launch path are for Linux, as all Realtime Servers are deployed with Linux.

#### JSON
<a name="aws-resource-gamelift-fleet--examples--Create_GameLift_fleet_with_a_Script--json"></a>

```
{
    "Resources": {
        "FleetResource": {
            "Type": "AWS::GameLift::Fleet",
            "Properties": {
                "CertificateConfiguration": {
                    "CertificateType": "DISABLED"
                },
                "Description": "Description of my Game Fleet",
                "DesiredEC2Instances": 1,
                "EC2InboundPermissions": [
                    {
                        "FromPort": 1234,
                        "ToPort": 1324,
                        "IpRange": "0.0.0.0/24",
                        "Protocol": "TCP"
                    },
                    {
                        "FromPort": 1356,
                        "ToPort": 1578,
                        "IpRange": "192.168.0.0/24",
                        "Protocol": "UDP"
                    }
                ],
                "EC2InstanceType": "c4.large",
                "FleetType": "SPOT",
                "LogPaths": [
                    "/local/game/testlog.log",
                    "/local/game/testlog2.log"
                ],
                "MetricGroups": [
                    "MetricGroupName"
                ],
                "Name": "MyGameFleet",
                "NewGameSessionProtectionPolicy": "FullProtection",
                "ResourceCreationLimitPolicy": {
                    "NewGameSessionsPerCreator": 5,
                    "PolicyPeriodInMinutes": 2
                },
                "RuntimeConfiguration": {
                    "GameSessionActivationTimeoutSeconds": 300,
                    "MaxConcurrentGameSessionActivations": 1,
                    "ServerProcesses": [
                        {
                            "ConcurrentExecutions": 1,
                            "LaunchPath": "/local/game/myscript.js"
                        }
                    ]
                },
                "ScriptId": {
                    "Fn::GetAtt": [
                        "ScriptResource",
                        "Id"
                    ]
                },
                "Locations": [
                  "us-west-2",
                  "us-east-1",
                  "eu-west-1"
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-gamelift-fleet--examples--Create_GameLift_fleet_with_a_Script--yaml"></a>

```
Resources:
  FleetResource:
    Type: AWS::GameLift::Fleet
    Properties:
      CertificateConfiguration:
        CertificateType: DISABLED
      Description: Description of my game fleet
      DesiredEC2Instances: 1
      EC2InboundPermissions:
        - FromPort: 1234
          ToPort: 1324
          IpRange: 0.0.0.0/24
          Protocol: TCP
        - FromPort: 1356
          ToPort: 1578
          IpRange: 192.168.0.0/24
          Protocol: UDP
      EC2InstanceType: c4.large
      FleetType: SPOT
      LogPaths:
        - '/local/game/testlog.log'
        - '/local/game/testlog2.log'
      MetricGroups:
        - MetricGroupName
      Name: MyGameFleet
      NewGameSessionProtectionPolicy: FullProtection
      ResourceCreationLimitPolicy:
        NewGameSessionsPerCreator: 5
        PolicyPeriodInMinutes: 2
      RuntimeConfiguration:
        GameSessionActivationTimeoutSeconds: 300
        MaxConcurrentGameSessionActivations: 1
        ServerProcesses:
          - ConcurrentExecutions: 1
            LaunchPath: '/local/game/myscript.js'
      ScriptId: !GetAtt ScriptResource.Id
      Locations:
          - Location: 'us-west-2'
          - Location: 'us-east-1'
          - Location: 'eu-west-1'
```

## See also
<a name="aws-resource-gamelift-fleet--seealso"></a>
+ [ Create GameLift resources using Amazon CloudFront](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Developer Guide*
+ [Setting up GameLift fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html) in the *Amazon GameLift Developer Guide*
+ [CreateFleet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateFleet.html) in the *Amazon GameLift API Reference*
