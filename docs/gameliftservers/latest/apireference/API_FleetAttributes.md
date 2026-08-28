---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_FleetAttributes.html
---

# FleetAttributes
<a name="API_FleetAttributes"></a>

Describes an Amazon GameLift Servers fleet of game hosting resources. Attributes differ based on the fleet's compute type, as follows:
+ EC2 fleet attributes identify a `Build` resource (for fleets with customer game server builds) or a `Script` resource (for Amazon GameLift Servers Realtime fleets).
+ Amazon GameLift Servers Anywhere fleets have an abbreviated set of attributes, because most fleet configurations are set directly on the fleet's computes. Attributes include fleet identifiers and descriptive properties, creation/termination time, and fleet status.

 **Returned by:** [https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetAttributes](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetAttributes)

## Contents
<a name="API_FleetAttributes_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnywhereConfiguration **   <a name="gameliftservers-Type-FleetAttributes-AnywhereConfiguration"></a>
A set of attributes that are specific to an Anywhere fleet.
Type: [AnywhereConfiguration](API_AnywhereConfiguration.md) object
Required: No

 ** BuildArn **   <a name="gameliftservers-Type-FleetAttributes-BuildArn"></a>
 The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) associated with the Amazon GameLift Servers build resource that is deployed on instances in this fleet. In a GameLift build ARN, the resource ID matches the `BuildId` value. This attribute is used with fleets where `ComputeType` is "EC2".
Type: String
Pattern: `^arn:.*:build\/build-\S+`
Required: No

 ** BuildId **   <a name="gameliftservers-Type-FleetAttributes-BuildId"></a>
A unique identifier for the build resource that is deployed on instances in this fleet. This attribute is used with fleets where `ComputeType` is "EC2".
Type: String
Pattern: `^build-\S+`
Required: No

 ** CertificateConfiguration **   <a name="gameliftservers-Type-FleetAttributes-CertificateConfiguration"></a>
Determines whether a TLS/SSL certificate is generated for a fleet. This feature must be enabled when creating the fleet. All instances in a fleet share the same certificate.
Type: [CertificateConfiguration](API_CertificateConfiguration.md) object
Required: No

 ** ComputeType **   <a name="gameliftservers-Type-FleetAttributes-ComputeType"></a>
The type of compute resource used to host your game servers. You can use your own compute resources with Amazon GameLift Servers Anywhere or use Amazon EC2 instances with managed Amazon GameLift Servers.
Type: String
Valid Values: `EC2 | ANYWHERE`
Required: No

 ** CreationTime **   <a name="gameliftservers-Type-FleetAttributes-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** Description **   <a name="gameliftservers-Type-FleetAttributes-Description"></a>
A human-readable description of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** FleetArn **   <a name="gameliftservers-Type-FleetAttributes-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`. In a GameLift fleet ARN, the resource ID matches the `FleetId` value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** FleetId **   <a name="gameliftservers-Type-FleetAttributes-FleetId"></a>
A unique identifier for the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** FleetType **   <a name="gameliftservers-Type-FleetAttributes-FleetType"></a>
Indicates whether the fleet uses On-Demand or Spot instances. For more information, see [ On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot). This fleet property can't be changed after the fleet is created.
Type: String
Valid Values: `ON_DEMAND | SPOT`
Required: No

 ** InstanceRoleArn **   <a name="gameliftservers-Type-FleetAttributes-InstanceRoleArn"></a>
A unique identifier for an IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the [IAM dashboard](https://console.aws.amazon.com/iam/) in the AWS Management Console. Learn more about using on-box credentials for your game servers at [ Access external resources from a game server](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html). This attribute is used with fleets where `ComputeType` is `EC2`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** InstanceRoleCredentialsProvider **   <a name="gameliftservers-Type-FleetAttributes-InstanceRoleCredentialsProvider"></a>
Indicates that fleet instances maintain a shared credentials file for the IAM role defined in `InstanceRoleArn`. Shared credentials allow applications that are deployed with the game server executable to communicate with other AWS resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see [ Communicate with other AWS resources from your fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html). This attribute is used with fleets where `ComputeType` is `EC2`.
Type: String
Valid Values: `SHARED_CREDENTIAL_FILE`
Required: No

 ** InstanceType **   <a name="gameliftservers-Type-FleetAttributes-InstanceType"></a>
The Amazon EC2 instance type that the fleet uses. Instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. See [Amazon Elastic Compute Cloud Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed descriptions. This attribute is used with fleets where `ComputeType` is `EC2`.
Type: String
Valid Values: `t2.micro | t2.small | t2.medium | t2.large | c3.large | c3.xlarge | c3.2xlarge | c3.4xlarge | c3.8xlarge | c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge | c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.12xlarge | c5.18xlarge | c5.24xlarge | c5a.large | c5a.xlarge | c5a.2xlarge | c5a.4xlarge | c5a.8xlarge | c5a.12xlarge | c5a.16xlarge | c5a.24xlarge | r3.large | r3.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge | r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge | r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.8xlarge | r5.12xlarge | r5.16xlarge | r5.24xlarge | r5a.large | r5a.xlarge | r5a.2xlarge | r5a.4xlarge | r5a.8xlarge | r5a.12xlarge | r5a.16xlarge | r5a.24xlarge | m3.medium | m3.large | m3.xlarge | m3.2xlarge | m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.8xlarge | m5.12xlarge | m5.16xlarge | m5.24xlarge | m5a.large | m5a.xlarge | m5a.2xlarge | m5a.4xlarge | m5a.8xlarge | m5a.12xlarge | m5a.16xlarge | m5a.24xlarge | c5d.large | c5d.xlarge | c5d.2xlarge | c5d.4xlarge | c5d.9xlarge | c5d.12xlarge | c5d.18xlarge | c5d.24xlarge | c6a.large | c6a.xlarge | c6a.2xlarge | c6a.4xlarge | c6a.8xlarge | c6a.12xlarge | c6a.16xlarge | c6a.24xlarge | c6i.large | c6i.xlarge | c6i.2xlarge | c6i.4xlarge | c6i.8xlarge | c6i.12xlarge | c6i.16xlarge | c6i.24xlarge | r5d.large | r5d.xlarge | r5d.2xlarge | r5d.4xlarge | r5d.8xlarge | r5d.12xlarge | r5d.16xlarge | r5d.24xlarge | m6g.medium | m6g.large | m6g.xlarge | m6g.2xlarge | m6g.4xlarge | m6g.8xlarge | m6g.12xlarge | m6g.16xlarge | c6g.medium | c6g.large | c6g.xlarge | c6g.2xlarge | c6g.4xlarge | c6g.8xlarge | c6g.12xlarge | c6g.16xlarge | r6g.medium | r6g.large | r6g.xlarge | r6g.2xlarge | r6g.4xlarge | r6g.8xlarge | r6g.12xlarge | r6g.16xlarge | c6gn.medium | c6gn.large | c6gn.xlarge | c6gn.2xlarge | c6gn.4xlarge | c6gn.8xlarge | c6gn.12xlarge | c6gn.16xlarge | c7g.medium | c7g.large | c7g.xlarge | c7g.2xlarge | c7g.4xlarge | c7g.8xlarge | c7g.12xlarge | c7g.16xlarge | r7g.medium | r7g.large | r7g.xlarge | r7g.2xlarge | r7g.4xlarge | r7g.8xlarge | r7g.12xlarge | r7g.16xlarge | m7g.medium | m7g.large | m7g.xlarge | m7g.2xlarge | m7g.4xlarge | m7g.8xlarge | m7g.12xlarge | m7g.16xlarge | g5g.xlarge | g5g.2xlarge | g5g.4xlarge | g5g.8xlarge | g5g.16xlarge | r6i.large | r6i.xlarge | r6i.2xlarge | r6i.4xlarge | r6i.8xlarge | r6i.12xlarge | r6i.16xlarge | c6gd.medium | c6gd.large | c6gd.xlarge | c6gd.2xlarge | c6gd.4xlarge | c6gd.8xlarge | c6gd.12xlarge | c6gd.16xlarge | c6in.large | c6in.xlarge | c6in.2xlarge | c6in.4xlarge | c6in.8xlarge | c6in.12xlarge | c6in.16xlarge | c7a.medium | c7a.large | c7a.xlarge | c7a.2xlarge | c7a.4xlarge | c7a.8xlarge | c7a.12xlarge | c7a.16xlarge | c7gd.medium | c7gd.large | c7gd.xlarge | c7gd.2xlarge | c7gd.4xlarge | c7gd.8xlarge | c7gd.12xlarge | c7gd.16xlarge | c7gn.medium | c7gn.large | c7gn.xlarge | c7gn.2xlarge | c7gn.4xlarge | c7gn.8xlarge | c7gn.12xlarge | c7gn.16xlarge | c7i.large | c7i.xlarge | c7i.2xlarge | c7i.4xlarge | c7i.8xlarge | c7i.12xlarge | c7i.16xlarge | m6a.large | m6a.xlarge | m6a.2xlarge | m6a.4xlarge | m6a.8xlarge | m6a.12xlarge | m6a.16xlarge | m6gd.medium | m6gd.large | m6gd.xlarge | m6gd.2xlarge | m6gd.4xlarge | m6gd.8xlarge | m6gd.12xlarge | m6gd.16xlarge | m6i.large | m6i.xlarge | m6i.2xlarge | m6i.4xlarge | m6i.8xlarge | m6i.12xlarge | m6i.16xlarge | m7a.medium | m7a.large | m7a.xlarge | m7a.2xlarge | m7a.4xlarge | m7a.8xlarge | m7a.12xlarge | m7a.16xlarge | m7gd.medium | m7gd.large | m7gd.xlarge | m7gd.2xlarge | m7gd.4xlarge | m7gd.8xlarge | m7gd.12xlarge | m7gd.16xlarge | m7i.large | m7i.xlarge | m7i.2xlarge | m7i.4xlarge | m7i.8xlarge | m7i.12xlarge | m7i.16xlarge | r6gd.medium | r6gd.large | r6gd.xlarge | r6gd.2xlarge | r6gd.4xlarge | r6gd.8xlarge | r6gd.12xlarge | r6gd.16xlarge | r7a.medium | r7a.large | r7a.xlarge | r7a.2xlarge | r7a.4xlarge | r7a.8xlarge | r7a.12xlarge | r7a.16xlarge | r7gd.medium | r7gd.large | r7gd.xlarge | r7gd.2xlarge | r7gd.4xlarge | r7gd.8xlarge | r7gd.12xlarge | r7gd.16xlarge | r7i.large | r7i.xlarge | r7i.2xlarge | r7i.4xlarge | r7i.8xlarge | r7i.12xlarge | r7i.16xlarge | r7i.24xlarge | r7i.48xlarge | c5ad.large | c5ad.xlarge | c5ad.2xlarge | c5ad.4xlarge | c5ad.8xlarge | c5ad.12xlarge | c5ad.16xlarge | c5ad.24xlarge | c5n.large | c5n.xlarge | c5n.2xlarge | c5n.4xlarge | c5n.9xlarge | c5n.18xlarge | r5ad.large | r5ad.xlarge | r5ad.2xlarge | r5ad.4xlarge | r5ad.8xlarge | r5ad.12xlarge | r5ad.16xlarge | r5ad.24xlarge | c6id.large | c6id.xlarge | c6id.2xlarge | c6id.4xlarge | c6id.8xlarge | c6id.12xlarge | c6id.16xlarge | c6id.24xlarge | c6id.32xlarge | c8g.medium | c8g.large | c8g.xlarge | c8g.2xlarge | c8g.4xlarge | c8g.8xlarge | c8g.12xlarge | c8g.16xlarge | c8g.24xlarge | c8g.48xlarge | m5ad.large | m5ad.xlarge | m5ad.2xlarge | m5ad.4xlarge | m5ad.8xlarge | m5ad.12xlarge | m5ad.16xlarge | m5ad.24xlarge | m5d.large | m5d.xlarge | m5d.2xlarge | m5d.4xlarge | m5d.8xlarge | m5d.12xlarge | m5d.16xlarge | m5d.24xlarge | m5dn.large | m5dn.xlarge | m5dn.2xlarge | m5dn.4xlarge | m5dn.8xlarge | m5dn.12xlarge | m5dn.16xlarge | m5dn.24xlarge | m5n.large | m5n.xlarge | m5n.2xlarge | m5n.4xlarge | m5n.8xlarge | m5n.12xlarge | m5n.16xlarge | m5n.24xlarge | m6id.large | m6id.xlarge | m6id.2xlarge | m6id.4xlarge | m6id.8xlarge | m6id.12xlarge | m6id.16xlarge | m6id.24xlarge | m6id.32xlarge | m6idn.large | m6idn.xlarge | m6idn.2xlarge | m6idn.4xlarge | m6idn.8xlarge | m6idn.12xlarge | m6idn.16xlarge | m6idn.24xlarge | m6idn.32xlarge | m6in.large | m6in.xlarge | m6in.2xlarge | m6in.4xlarge | m6in.8xlarge | m6in.12xlarge | m6in.16xlarge | m6in.24xlarge | m6in.32xlarge | m8g.medium | m8g.large | m8g.xlarge | m8g.2xlarge | m8g.4xlarge | m8g.8xlarge | m8g.12xlarge | m8g.16xlarge | m8g.24xlarge | m8g.48xlarge | r5dn.large | r5dn.xlarge | r5dn.2xlarge | r5dn.4xlarge | r5dn.8xlarge | r5dn.12xlarge | r5dn.16xlarge | r5dn.24xlarge | r5n.large | r5n.xlarge | r5n.2xlarge | r5n.4xlarge | r5n.8xlarge | r5n.12xlarge | r5n.16xlarge | r5n.24xlarge | r6a.large | r6a.xlarge | r6a.2xlarge | r6a.4xlarge | r6a.8xlarge | r6a.12xlarge | r6a.16xlarge | r6a.24xlarge | r6a.32xlarge | r6a.48xlarge | r6id.large | r6id.xlarge | r6id.2xlarge | r6id.4xlarge | r6id.8xlarge | r6id.12xlarge | r6id.16xlarge | r6id.24xlarge | r6id.32xlarge | r6idn.large | r6idn.xlarge | r6idn.2xlarge | r6idn.4xlarge | r6idn.8xlarge | r6idn.12xlarge | r6idn.16xlarge | r6idn.24xlarge | r6idn.32xlarge | r6in.large | r6in.xlarge | r6in.2xlarge | r6in.4xlarge | r6in.8xlarge | r6in.12xlarge | r6in.16xlarge | r6in.24xlarge | r6in.32xlarge | r8g.medium | r8g.large | r8g.xlarge | r8g.2xlarge | r8g.4xlarge | r8g.8xlarge | r8g.12xlarge | r8g.16xlarge | r8g.24xlarge | r8g.48xlarge | m4.16xlarge | c6a.32xlarge | c6a.48xlarge | c6i.32xlarge | r6i.24xlarge | r6i.32xlarge | c6in.24xlarge | c6in.32xlarge | c7a.24xlarge | c7a.32xlarge | c7a.48xlarge | c7i.24xlarge | c7i.48xlarge | m6a.24xlarge | m6a.32xlarge | m6a.48xlarge | m6i.24xlarge | m6i.32xlarge | m7a.24xlarge | m7a.32xlarge | m7a.48xlarge | m7i.24xlarge | m7i.48xlarge | r7a.24xlarge | r7a.32xlarge | r7a.48xlarge`
Required: No

 ** LogPaths **   <a name="gameliftservers-Type-FleetAttributes-LogPaths"></a>
 **This parameter is no longer used.** Game session log paths are now defined using the Amazon GameLift Servers server API `ProcessReady()` `logParameters`. See more information in the [Server API Reference](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api-ref.html#gamelift-sdk-server-api-ref-dataypes-process).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** MetricGroups **   <a name="gameliftservers-Type-FleetAttributes-MetricGroups"></a>
Name of a metric group that metrics for this fleet are added to. In Amazon CloudWatch, you can view aggregated metrics for fleets that are in a metric group. A fleet can be included in only one metric group at a time. This attribute is used with fleets where `ComputeType` is `EC2`.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Name **   <a name="gameliftservers-Type-FleetAttributes-Name"></a>
A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** NewGameSessionProtectionPolicy **   <a name="gameliftservers-Type-FleetAttributes-NewGameSessionProtectionPolicy"></a>
The type of game session protection to set on all new instances that are started in the fleet. This attribute is used with fleets where `ComputeType` is `EC2`.
+  **NoProtection** -- The game session can be terminated during a scale-down event.
+  **FullProtection** -- If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.
Type: String
Valid Values: `NoProtection | FullProtection`
Required: No

 ** OperatingSystem **   <a name="gameliftservers-Type-FleetAttributes-OperatingSystem"></a>
The operating system of the fleet's computing resources. A fleet's operating system is determined by the OS of the build or script that is deployed on this fleet. This attribute is used with fleets where `ComputeType` is `EC2`.
Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the [Amazon Linux 2 FAQs](http://aws.amazon.com/aws.amazon.com/amazon-linux-2/faqs/). For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
Type: String
Valid Values: `WINDOWS_2012 | AMAZON_LINUX | AMAZON_LINUX_2 | WINDOWS_2016 | AMAZON_LINUX_2023 | WINDOWS_2022`
Required: No

 ** PlayerGatewayConfiguration **   <a name="gameliftservers-Type-FleetAttributes-PlayerGatewayConfiguration"></a>
Configuration settings for player gateway on this fleet.
Type: [PlayerGatewayConfiguration](API_PlayerGatewayConfiguration.md) object
Required: No

 ** PlayerGatewayMode **   <a name="gameliftservers-Type-FleetAttributes-PlayerGatewayMode"></a>
Indicates whether player gateway is enabled for this fleet. Player gateway provides benefits such as DDoS protection with negligible impact to latency.
If `ENABLED` or `REQUIRED`, game clients can use player gateway to connect with the game server. If `DISABLED`, game clients cannot use player gateway. Instead, they have to directly connect to the game server.
Type: String
Valid Values: `DISABLED | ENABLED | REQUIRED`
Required: No

 ** ResourceCreationLimitPolicy **   <a name="gameliftservers-Type-FleetAttributes-ResourceCreationLimitPolicy"></a>
A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources.
The policy is evaluated when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift Servers checks that the player (identified by `CreatorId`) has created fewer than game session limit in the specified time period.
The purpose of this policy is to prevent a single player from consuming a large share of available hosting resources. For example, setting `NewGameSessionsPerCreator` to `4` and `PolicyPeriodInMinutes` to `10` limits each player to creating 4 game sessions every 10 minutes. Setting these values too high (for example, 200 game sessions every 1000 minutes) still allows a single player to rapidly consume resources. We recommend keeping these values small.
Type: [ResourceCreationLimitPolicy](API_ResourceCreationLimitPolicy.md) object
Required: No

 ** ScriptArn **   <a name="gameliftservers-Type-FleetAttributes-ScriptArn"></a>
 The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) associated with the GameLift script resource that is deployed on instances in this fleet. In a GameLift script ARN, the resource ID matches the `ScriptId` value.
Type: String
Pattern: `^arn:.*:script\/script-\S+`
Required: No

 ** ScriptId **   <a name="gameliftservers-Type-FleetAttributes-ScriptId"></a>
A unique identifier for the Realtime script resource that is deployed on instances in this fleet. This attribute is used with fleets where `ComputeType` is "EC2".
Type: String
Pattern: `^script-\S+`
Required: No

 ** ServerLaunchParameters **   <a name="gameliftservers-Type-FleetAttributes-ServerLaunchParameters"></a>
 **This parameter is no longer used.** Server launch parameters are now defined using the fleet's runtime configuration. Requests that use this parameter continue to be valid.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_:.+\/\\\- =@;{},?'\[\]"]+`
Required: No

 ** ServerLaunchPath **   <a name="gameliftservers-Type-FleetAttributes-ServerLaunchPath"></a>
 **This parameter is no longer used.** Server launch paths are now defined using the fleet's [RuntimeConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/RuntimeConfiguration.html). Requests that use this parameter continue to be valid.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_:.+\/\\\- ]+`
Required: No

 ** Status **   <a name="gameliftservers-Type-FleetAttributes-Status"></a>
Current status of the fleet. Possible fleet statuses include the following:
+ NEW -- A new fleet resource has been defined and Amazon GameLift Servers has started creating the fleet. Desired instances is set to 1.
+ DOWNLOADING/VALIDATING/BUILDING -- Amazon GameLift Servers is download the game server build, running install scripts, and then validating the build files. When complete, Amazon GameLift Servers launches a fleet instance.
+ ACTIVATING -- Amazon GameLift Servers is launching a game server process and testing its connectivity with the Amazon GameLift Servers service.
+ ACTIVE -- The fleet is now ready to host game sessions.
+ ERROR -- An error occurred when downloading, validating, building, or activating the fleet.
+ EXPIRED -- The fleet has been expired. The fleet is scaled down to zero instances and cannot host new game sessions.
+ DELETING -- Hosts are responding to a delete fleet request.
+ TERMINATED -- The fleet no longer exists.
Type: String
Valid Values: `NEW | DOWNLOADING | VALIDATING | BUILDING | ACTIVATING | ACTIVE | DELETING | ERROR | TERMINATED | NOT_FOUND`
Required: No

 ** StoppedActions **   <a name="gameliftservers-Type-FleetAttributes-StoppedActions"></a>
A list of fleet activity that has been suspended using [StopFleetActions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html). This includes fleet auto-scaling. This attribute is used with fleets where `ComputeType` is `EC2`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `AUTO_SCALING`
Required: No

 ** TerminationTime **   <a name="gameliftservers-Type-FleetAttributes-TerminationTime"></a>
A time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

## See Also
<a name="API_FleetAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/FleetAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/FleetAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/FleetAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
