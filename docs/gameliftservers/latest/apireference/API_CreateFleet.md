---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateFleet.html
---

# CreateFleet
<a name="API_CreateFleet"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Creates a fleet of compute resources to host your game servers. Use this operation to set up a fleet for the following compute types:

 **Managed EC2 fleet**

An EC2 fleet is a set of Amazon Elastic Compute Cloud (Amazon EC2) instances. Your game server build is deployed to each fleet instance. Amazon GameLift Servers manages the fleet's instances and controls the lifecycle of game server processes, which host game sessions for players. EC2 fleets can have instances in multiple locations. Each instance in the fleet is designated a `Compute`.

To create an EC2 fleet, provide these required parameters:
+ Either `BuildId` or `ScriptId`
+  `ComputeType` set to `EC2` (the default value)
+  `EC2InboundPermissions`
+  `EC2InstanceType`
+  `FleetType`
+  `Name`
+  `RuntimeConfiguration` with at least one `ServerProcesses` configuration

If successful, this operation creates a new fleet resource and places it in `NEW` status while Amazon GameLift Servers initiates the [fleet creation workflow](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-all.html#fleets-creation-workflow). To debug your fleet, fetch logs, view performance metrics or other actions on the fleet, create a development fleet with port 22/3389 open. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished.

When the fleet status is ACTIVE, you can adjust capacity settings and turn autoscaling on/off for each location.

**Note**
A managed fleet's runtime environment depends on the Amazon Machine Image (AMI) version it uses. When a new fleet is created, Amazon GameLift Servers assigns the latest available AMI version to the fleet, and all compute instances in that fleet are deployed with that version. To update the AMI version, you must create a new fleet. As a best practice, we recommend replacing your managed fleets every 30 days to maintain a secure and up-to-date runtime environment for your hosted game servers. For guidance, see [ Security best practices for Amazon GameLift Servers](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-best-practices.html).

 **Anywhere fleet**

An Anywhere fleet represents compute resources that are not owned or managed by Amazon GameLift Servers. You might create an Anywhere fleet with your local machine for testing, or use one to host game servers with on-premises hardware or other game hosting solutions.

To create an Anywhere fleet, provide these required parameters:
+  `ComputeType` set to `ANYWHERE`
+  `Locations` specifying a custom location
+  `Name`

If successful, this operation creates a new fleet resource and places it in `ACTIVE` status. You can register computes with a fleet in `ACTIVE` status.

 **Learn more**

 [Setting up fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

 [Debug fleet creation issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html#fleets-creating-debug-creation)

 [Multi-location fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_CreateFleet_RequestSyntax"></a>

```
{
   "AnywhereConfiguration": {
      "Cost": "{{string}}"
   },
   "BuildId": "{{string}}",
   "CertificateConfiguration": {
      "CertificateType": "{{string}}"
   },
   "ComputeType": "{{string}}",
   "Description": "{{string}}",
   "EC2InboundPermissions": [
      {
         "FromPort": {{number}},
         "IpRange": "{{string}}",
         "Protocol": "{{string}}",
         "ToPort": {{number}}
      }
   ],
   "EC2InstanceType": "{{string}}",
   "FleetType": "{{string}}",
   "InstanceRoleArn": "{{string}}",
   "InstanceRoleCredentialsProvider": "{{string}}",
   "Locations": [
      {
         "Location": "{{string}}"
      }
   ],
   "LogPaths": [ "{{string}}" ],
   "MetricGroups": [ "{{string}}" ],
   "Name": "{{string}}",
   "NewGameSessionProtectionPolicy": "{{string}}",
   "PeerVpcAwsAccountId": "{{string}}",
   "PeerVpcId": "{{string}}",
   "PlayerGatewayConfiguration": {
      "GameServerIpProtocolSupported": "{{string}}"
   },
   "PlayerGatewayMode": "{{string}}",
   "ResourceCreationLimitPolicy": {
      "NewGameSessionsPerCreator": {{number}},
      "PolicyPeriodInMinutes": {{number}}
   },
   "RuntimeConfiguration": {
      "GameSessionActivationTimeoutSeconds": {{number}},
      "MaxConcurrentGameSessionActivations": {{number}},
      "ServerProcesses": [
         {
            "ConcurrentExecutions": {{number}},
            "LaunchPath": "{{string}}",
            "Parameters": "{{string}}"
         }
      ]
   },
   "ScriptId": "{{string}}",
   "ServerLaunchParameters": "{{string}}",
   "ServerLaunchPath": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-Name"></a>
A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [AnywhereConfiguration](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-AnywhereConfiguration"></a>
Amazon GameLift Servers Anywhere configuration options.
Type: [AnywhereConfiguration](API_AnywhereConfiguration.md) object
Required: No

 ** [BuildId](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-BuildId"></a>
The unique identifier for a custom game server build to be deployed to a fleet with compute type `EC2`. You can use either the build ID or ARN. The build must be uploaded to Amazon GameLift Servers and in `READY` status. This fleet property can't be changed after the fleet is created.
Type: String
Pattern: `^build-\S+|^arn:.*:build\/build-\S+`
Required: No

 ** [CertificateConfiguration](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-CertificateConfiguration"></a>
Prompts Amazon GameLift Servers to generate a TLS/SSL certificate for the fleet. Amazon GameLift Servers uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift Servers. By default, the `CertificateConfiguration` is `DISABLED`. You can't change this property after you create the fleet.
 AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition.
ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see [Supported Regions](https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html) in the * AWS Certificate Manager User Guide*.
Type: [CertificateConfiguration](API_CertificateConfiguration.md) object
Required: No

 ** [ComputeType](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-ComputeType"></a>
The type of compute resource used to host your game servers.
+  `EC2` – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting.
+  `ANYWHERE` – Game servers and supporting software are deployed to compute resources that you provide and manage. With this compute type, you can also set the `AnywhereConfiguration` parameter.
Type: String
Valid Values: `EC2 | ANYWHERE`
Required: No

 ** [Description](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-Description"></a>
A description for the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [EC2InboundPermissions](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-EC2InboundPermissions"></a>
The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. Set this parameter for managed EC2 fleets. You can leave this parameter empty when creating the fleet, but you must call [https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings) to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Amazon GameLift Servers Realtime fleets, Amazon GameLift Servers automatically sets TCP and UDP ranges.
Type: Array of [IpPermission](API_IpPermission.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** [EC2InstanceType](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-EC2InstanceType"></a>
The Amazon GameLift Servers-supported Amazon EC2 instance type to use with managed EC2 fleets. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See [Amazon Elastic Compute Cloud Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed descriptions of Amazon EC2 instance types.
Type: String
Valid Values: `t2.micro | t2.small | t2.medium | t2.large | c3.large | c3.xlarge | c3.2xlarge | c3.4xlarge | c3.8xlarge | c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge | c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.12xlarge | c5.18xlarge | c5.24xlarge | c5a.large | c5a.xlarge | c5a.2xlarge | c5a.4xlarge | c5a.8xlarge | c5a.12xlarge | c5a.16xlarge | c5a.24xlarge | r3.large | r3.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge | r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge | r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.8xlarge | r5.12xlarge | r5.16xlarge | r5.24xlarge | r5a.large | r5a.xlarge | r5a.2xlarge | r5a.4xlarge | r5a.8xlarge | r5a.12xlarge | r5a.16xlarge | r5a.24xlarge | m3.medium | m3.large | m3.xlarge | m3.2xlarge | m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.8xlarge | m5.12xlarge | m5.16xlarge | m5.24xlarge | m5a.large | m5a.xlarge | m5a.2xlarge | m5a.4xlarge | m5a.8xlarge | m5a.12xlarge | m5a.16xlarge | m5a.24xlarge | c5d.large | c5d.xlarge | c5d.2xlarge | c5d.4xlarge | c5d.9xlarge | c5d.12xlarge | c5d.18xlarge | c5d.24xlarge | c6a.large | c6a.xlarge | c6a.2xlarge | c6a.4xlarge | c6a.8xlarge | c6a.12xlarge | c6a.16xlarge | c6a.24xlarge | c6i.large | c6i.xlarge | c6i.2xlarge | c6i.4xlarge | c6i.8xlarge | c6i.12xlarge | c6i.16xlarge | c6i.24xlarge | r5d.large | r5d.xlarge | r5d.2xlarge | r5d.4xlarge | r5d.8xlarge | r5d.12xlarge | r5d.16xlarge | r5d.24xlarge | m6g.medium | m6g.large | m6g.xlarge | m6g.2xlarge | m6g.4xlarge | m6g.8xlarge | m6g.12xlarge | m6g.16xlarge | c6g.medium | c6g.large | c6g.xlarge | c6g.2xlarge | c6g.4xlarge | c6g.8xlarge | c6g.12xlarge | c6g.16xlarge | r6g.medium | r6g.large | r6g.xlarge | r6g.2xlarge | r6g.4xlarge | r6g.8xlarge | r6g.12xlarge | r6g.16xlarge | c6gn.medium | c6gn.large | c6gn.xlarge | c6gn.2xlarge | c6gn.4xlarge | c6gn.8xlarge | c6gn.12xlarge | c6gn.16xlarge | c7g.medium | c7g.large | c7g.xlarge | c7g.2xlarge | c7g.4xlarge | c7g.8xlarge | c7g.12xlarge | c7g.16xlarge | r7g.medium | r7g.large | r7g.xlarge | r7g.2xlarge | r7g.4xlarge | r7g.8xlarge | r7g.12xlarge | r7g.16xlarge | m7g.medium | m7g.large | m7g.xlarge | m7g.2xlarge | m7g.4xlarge | m7g.8xlarge | m7g.12xlarge | m7g.16xlarge | g5g.xlarge | g5g.2xlarge | g5g.4xlarge | g5g.8xlarge | g5g.16xlarge | r6i.large | r6i.xlarge | r6i.2xlarge | r6i.4xlarge | r6i.8xlarge | r6i.12xlarge | r6i.16xlarge | c6gd.medium | c6gd.large | c6gd.xlarge | c6gd.2xlarge | c6gd.4xlarge | c6gd.8xlarge | c6gd.12xlarge | c6gd.16xlarge | c6in.large | c6in.xlarge | c6in.2xlarge | c6in.4xlarge | c6in.8xlarge | c6in.12xlarge | c6in.16xlarge | c7a.medium | c7a.large | c7a.xlarge | c7a.2xlarge | c7a.4xlarge | c7a.8xlarge | c7a.12xlarge | c7a.16xlarge | c7gd.medium | c7gd.large | c7gd.xlarge | c7gd.2xlarge | c7gd.4xlarge | c7gd.8xlarge | c7gd.12xlarge | c7gd.16xlarge | c7gn.medium | c7gn.large | c7gn.xlarge | c7gn.2xlarge | c7gn.4xlarge | c7gn.8xlarge | c7gn.12xlarge | c7gn.16xlarge | c7i.large | c7i.xlarge | c7i.2xlarge | c7i.4xlarge | c7i.8xlarge | c7i.12xlarge | c7i.16xlarge | m6a.large | m6a.xlarge | m6a.2xlarge | m6a.4xlarge | m6a.8xlarge | m6a.12xlarge | m6a.16xlarge | m6gd.medium | m6gd.large | m6gd.xlarge | m6gd.2xlarge | m6gd.4xlarge | m6gd.8xlarge | m6gd.12xlarge | m6gd.16xlarge | m6i.large | m6i.xlarge | m6i.2xlarge | m6i.4xlarge | m6i.8xlarge | m6i.12xlarge | m6i.16xlarge | m7a.medium | m7a.large | m7a.xlarge | m7a.2xlarge | m7a.4xlarge | m7a.8xlarge | m7a.12xlarge | m7a.16xlarge | m7gd.medium | m7gd.large | m7gd.xlarge | m7gd.2xlarge | m7gd.4xlarge | m7gd.8xlarge | m7gd.12xlarge | m7gd.16xlarge | m7i.large | m7i.xlarge | m7i.2xlarge | m7i.4xlarge | m7i.8xlarge | m7i.12xlarge | m7i.16xlarge | r6gd.medium | r6gd.large | r6gd.xlarge | r6gd.2xlarge | r6gd.4xlarge | r6gd.8xlarge | r6gd.12xlarge | r6gd.16xlarge | r7a.medium | r7a.large | r7a.xlarge | r7a.2xlarge | r7a.4xlarge | r7a.8xlarge | r7a.12xlarge | r7a.16xlarge | r7gd.medium | r7gd.large | r7gd.xlarge | r7gd.2xlarge | r7gd.4xlarge | r7gd.8xlarge | r7gd.12xlarge | r7gd.16xlarge | r7i.large | r7i.xlarge | r7i.2xlarge | r7i.4xlarge | r7i.8xlarge | r7i.12xlarge | r7i.16xlarge | r7i.24xlarge | r7i.48xlarge | c5ad.large | c5ad.xlarge | c5ad.2xlarge | c5ad.4xlarge | c5ad.8xlarge | c5ad.12xlarge | c5ad.16xlarge | c5ad.24xlarge | c5n.large | c5n.xlarge | c5n.2xlarge | c5n.4xlarge | c5n.9xlarge | c5n.18xlarge | r5ad.large | r5ad.xlarge | r5ad.2xlarge | r5ad.4xlarge | r5ad.8xlarge | r5ad.12xlarge | r5ad.16xlarge | r5ad.24xlarge | c6id.large | c6id.xlarge | c6id.2xlarge | c6id.4xlarge | c6id.8xlarge | c6id.12xlarge | c6id.16xlarge | c6id.24xlarge | c6id.32xlarge | c8g.medium | c8g.large | c8g.xlarge | c8g.2xlarge | c8g.4xlarge | c8g.8xlarge | c8g.12xlarge | c8g.16xlarge | c8g.24xlarge | c8g.48xlarge | m5ad.large | m5ad.xlarge | m5ad.2xlarge | m5ad.4xlarge | m5ad.8xlarge | m5ad.12xlarge | m5ad.16xlarge | m5ad.24xlarge | m5d.large | m5d.xlarge | m5d.2xlarge | m5d.4xlarge | m5d.8xlarge | m5d.12xlarge | m5d.16xlarge | m5d.24xlarge | m5dn.large | m5dn.xlarge | m5dn.2xlarge | m5dn.4xlarge | m5dn.8xlarge | m5dn.12xlarge | m5dn.16xlarge | m5dn.24xlarge | m5n.large | m5n.xlarge | m5n.2xlarge | m5n.4xlarge | m5n.8xlarge | m5n.12xlarge | m5n.16xlarge | m5n.24xlarge | m6id.large | m6id.xlarge | m6id.2xlarge | m6id.4xlarge | m6id.8xlarge | m6id.12xlarge | m6id.16xlarge | m6id.24xlarge | m6id.32xlarge | m6idn.large | m6idn.xlarge | m6idn.2xlarge | m6idn.4xlarge | m6idn.8xlarge | m6idn.12xlarge | m6idn.16xlarge | m6idn.24xlarge | m6idn.32xlarge | m6in.large | m6in.xlarge | m6in.2xlarge | m6in.4xlarge | m6in.8xlarge | m6in.12xlarge | m6in.16xlarge | m6in.24xlarge | m6in.32xlarge | m8g.medium | m8g.large | m8g.xlarge | m8g.2xlarge | m8g.4xlarge | m8g.8xlarge | m8g.12xlarge | m8g.16xlarge | m8g.24xlarge | m8g.48xlarge | r5dn.large | r5dn.xlarge | r5dn.2xlarge | r5dn.4xlarge | r5dn.8xlarge | r5dn.12xlarge | r5dn.16xlarge | r5dn.24xlarge | r5n.large | r5n.xlarge | r5n.2xlarge | r5n.4xlarge | r5n.8xlarge | r5n.12xlarge | r5n.16xlarge | r5n.24xlarge | r6a.large | r6a.xlarge | r6a.2xlarge | r6a.4xlarge | r6a.8xlarge | r6a.12xlarge | r6a.16xlarge | r6a.24xlarge | r6a.32xlarge | r6a.48xlarge | r6id.large | r6id.xlarge | r6id.2xlarge | r6id.4xlarge | r6id.8xlarge | r6id.12xlarge | r6id.16xlarge | r6id.24xlarge | r6id.32xlarge | r6idn.large | r6idn.xlarge | r6idn.2xlarge | r6idn.4xlarge | r6idn.8xlarge | r6idn.12xlarge | r6idn.16xlarge | r6idn.24xlarge | r6idn.32xlarge | r6in.large | r6in.xlarge | r6in.2xlarge | r6in.4xlarge | r6in.8xlarge | r6in.12xlarge | r6in.16xlarge | r6in.24xlarge | r6in.32xlarge | r8g.medium | r8g.large | r8g.xlarge | r8g.2xlarge | r8g.4xlarge | r8g.8xlarge | r8g.12xlarge | r8g.16xlarge | r8g.24xlarge | r8g.48xlarge | m4.16xlarge | c6a.32xlarge | c6a.48xlarge | c6i.32xlarge | r6i.24xlarge | r6i.32xlarge | c6in.24xlarge | c6in.32xlarge | c7a.24xlarge | c7a.32xlarge | c7a.48xlarge | c7i.24xlarge | c7i.48xlarge | m6a.24xlarge | m6a.32xlarge | m6a.48xlarge | m6i.24xlarge | m6i.32xlarge | m7a.24xlarge | m7a.32xlarge | m7a.48xlarge | m7i.24xlarge | m7i.48xlarge | r7a.24xlarge | r7a.32xlarge | r7a.48xlarge`
Required: No

 ** [FleetType](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-FleetType"></a>
Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to `ON_DEMAND`. Learn more about when to use [ On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot). This fleet property can't be changed after the fleet is created.
Type: String
Valid Values: `ON_DEMAND | SPOT`
Required: No

 ** [InstanceRoleArn](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-InstanceRoleArn"></a>
A unique identifier for an IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the [IAM dashboard](https://console.aws.amazon.com/iam/) in the AWS Management Console. Learn more about using on-box credentials for your game servers at [ Access external resources from a game server](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html). This fleet property can't be changed after the fleet is created.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [InstanceRoleCredentialsProvider](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-InstanceRoleCredentialsProvider"></a>
Prompts Amazon GameLift Servers to generate a shared credentials file for the IAM role that's defined in `InstanceRoleArn`. The shared credentials file is stored on each fleet instance and refreshed as needed. Use shared credentials for applications that are deployed along with the game server executable, if the game server is integrated with server SDK version 5.x. For more information about using shared credentials, see [ Communicate with other AWS resources from your fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html).
Type: String
Valid Values: `SHARED_CREDENTIAL_FILE`
Required: No

 ** [Locations](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-Locations"></a>
A set of remote locations to deploy additional instances to and manage as a multi-location fleet. Use this parameter when creating a fleet in AWS Regions that support multiple locations. You can add any AWS Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more AWS Region codes, such as `us-west-2`, or Local Zone names. When using this parameter, Amazon GameLift Servers requires you to include your home location in the request. For a list of supported Regions and Local Zones, see [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.
Type: Array of [LocationConfiguration](API_LocationConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [LogPaths](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-LogPaths"></a>
 **This parameter is no longer used.** To specify where Amazon GameLift Servers should store log files once a server process shuts down, use the Amazon GameLift Servers server API `ProcessReady()` and specify one or more directory paths in `logParameters`. For more information, see [Initialize the server process](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-initialize) in the *Amazon GameLift Servers Developer Guide*.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [MetricGroups](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-MetricGroups"></a>
The name of an AWS CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [NewGameSessionProtectionPolicy](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-NewGameSessionProtectionPolicy"></a>
The status of termination protection for active game sessions on the fleet. By default, this property is set to `NoProtection`. You can also set game session protection for an individual game session by calling [UpdateGameSession](gamelift/latest/apireference/API_UpdateGameSession.html).
+  **NoProtection** - Game sessions can be terminated during active gameplay as a result of a scale-down event.
+  **FullProtection** - Game sessions in `ACTIVE` status cannot be terminated during a scale-down event.
Type: String
Valid Values: `NoProtection | FullProtection`
Required: No

 ** [PeerVpcAwsAccountId](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-PeerVpcAwsAccountId"></a>
Used when peering your Amazon GameLift Servers fleet with a VPC, the unique identifier for the AWS account that owns the VPC. You can find your account ID in the AWS Management Console under account settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [PeerVpcId](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-PeerVpcId"></a>
A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the [VPC Dashboard](https://console.aws.amazon.com/vpc/) in the AWS Management Console. Learn more about VPC peering in [VPC Peering with Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [PlayerGatewayConfiguration](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-PlayerGatewayConfiguration"></a>
Configuration settings for player gateway. Use this to specify advanced options for how player gateway handles connections.
Type: [PlayerGatewayConfiguration](API_PlayerGatewayConfiguration.md) object
Required: No

 ** [PlayerGatewayMode](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-PlayerGatewayMode"></a>
Configures player gateway for your fleet. Player gateway provides benefits such as DDoS protection by rate limiting and validating traﬃc before it reaches game servers, hiding game server IP addresses from players, and providing updated endpoints when relay endpoints become unhealthy. Note, player gateway is only available for fleets using server SDK 5.x or later game server builds.
 **How it works:** When enabled, game clients connect to relay endpoints instead of to your game servers. Player gateway validates player gateway tokens and routes traffic to the appropriate game server. Your game backend calls [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html) to retrieve relay endpoints and player gateway tokens for your game clients. To learn more about this topic, see [DDoS protection with Amazon GameLift Servers player gateway](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html).
Possible values include:
+  `DISABLED` (default) -- Game clients connect to the game server endpoint. Use this when you do not intend to integrate your game with player gateway.
+  `ENABLED` -- Player gateway is available in fleet locations where it is supported. Your game backend can call [GetPlayerConnectionDetails](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html) to obtain a player gateway token and endpoints for game clients.
+  `REQUIRED` -- Player gateway is available in fleet locations where it is supported, and the fleet can only use locations that support this feature. Attempting to add a remote location to your fleet which does not support player gateway will result in an `InvalidRequestException`.
Type: String
Valid Values: `DISABLED | ENABLED | REQUIRED`
Required: No

 ** [ResourceCreationLimitPolicy](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-ResourceCreationLimitPolicy"></a>
A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.
Type: [ResourceCreationLimitPolicy](API_ResourceCreationLimitPolicy.md) object
Required: No

 ** [RuntimeConfiguration](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-RuntimeConfiguration"></a>
Instructions for how to launch and run server processes on the fleet. Set runtime configuration for managed EC2 fleets. For an Anywhere fleets, set this parameter only if the fleet is running the Amazon GameLift Servers Agent. The runtime configuration defines one or more server process configurations. Each server process identifies a game executable or Realtime script file and the number of processes to run concurrently.
This parameter replaces the parameters `ServerLaunchPath` and `ServerLaunchParameters`, which are still supported for backward compatibility.
Type: [RuntimeConfiguration](API_RuntimeConfiguration.md) object
Required: No

 ** [ScriptId](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-ScriptId"></a>
The unique identifier for a Realtime configuration script to be deployed to a fleet with compute type `EC2`. You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift Servers prior to creating the fleet. This fleet property can't be changed after the fleet is created.
Type: String
Pattern: `^script-\S+|^arn:.*:script\/script-\S+`
Required: No

 ** [ServerLaunchParameters](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-ServerLaunchParameters"></a>
 **This parameter is no longer used.** Specify server launch parameters using the `RuntimeConfiguration` parameter. Requests that use this parameter instead continue to be valid.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_:.+\/\\\- =@;{},?'\[\]"]+`
Required: No

 ** [ServerLaunchPath](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-ServerLaunchPath"></a>
 **This parameter is no longer used.** Specify a server launch path using the `RuntimeConfiguration` parameter. Requests that use this parameter instead continue to be valid.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_:.+\/\\\- ]+`
Required: No

 ** [Tags](#API_CreateFleet_RequestSyntax) **   <a name="gameliftservers-CreateFleet-request-Tags"></a>
A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateFleet_ResponseSyntax"></a>

```
{
   "FleetAttributes": {
      "AnywhereConfiguration": {
         "Cost": "string"
      },
      "BuildArn": "string",
      "BuildId": "string",
      "CertificateConfiguration": {
         "CertificateType": "string"
      },
      "ComputeType": "string",
      "CreationTime": number,
      "Description": "string",
      "FleetArn": "string",
      "FleetId": "string",
      "FleetType": "string",
      "InstanceRoleArn": "string",
      "InstanceRoleCredentialsProvider": "string",
      "InstanceType": "string",
      "LogPaths": [ "string" ],
      "MetricGroups": [ "string" ],
      "Name": "string",
      "NewGameSessionProtectionPolicy": "string",
      "OperatingSystem": "string",
      "PlayerGatewayConfiguration": {
         "GameServerIpProtocolSupported": "string"
      },
      "PlayerGatewayMode": "string",
      "ResourceCreationLimitPolicy": {
         "NewGameSessionsPerCreator": number,
         "PolicyPeriodInMinutes": number
      },
      "ScriptArn": "string",
      "ScriptId": "string",
      "ServerLaunchParameters": "string",
      "ServerLaunchPath": "string",
      "Status": "string",
      "StoppedActions": [ "string" ],
      "TerminationTime": number
   },
   "LocationStates": [
      {
         "Location": "string",
         "PlayerGatewayStatus": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetAttributes](#API_CreateFleet_ResponseSyntax) **   <a name="gameliftservers-CreateFleet-response-FleetAttributes"></a>
The properties for the new fleet, including the current status. All fleets are placed in `NEW` status on creation.
Type: [FleetAttributes](API_FleetAttributes.md) object

 ** [LocationStates](#API_CreateFleet_ResponseSyntax) **   <a name="gameliftservers-CreateFleet-response-LocationStates"></a>
The fleet's locations and life-cycle status of each location. For new fleets, the status of all locations is set to `NEW`. During fleet creation, Amazon GameLift Servers updates each location status as instances are deployed there and prepared for game hosting. This list includes an entry for the fleet's home Region. For fleets with no remote locations, only one entry, representing the home Region, is returned.
Type: Array of [LocationState](API_LocationState.md) objects

## Errors
<a name="API_CreateFleet_Errors"></a>

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

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** NotReadyException **
 The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with [exponential backoffs and jitter](http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).
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
<a name="API_CreateFleet_Examples"></a>

### Create fleet with minimal configuration
<a name="API_CreateFleet_Example_1"></a>

This example creates an EC2 fleet for a game server build with a minimal configuration and a placeholder launch path. You can use this fleet to create queues and matchmakers, test Amazon GameLift Servers Server API calls, etc. When you're ready to start hosting game sessions, complete the configuration settings using the `UpdateFleet` operations. If the fleet is in a Region that supports multiple locations, you can add remote locations with `CreateFleetLocations` later. Note: this example generates a TLS certificate for the fleet, which can only be enabled during fleet creation.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_CreateFleet_Example_1_Request"></a>

```
{
    "Name": "My_Fleet_1",
    "Description": "A minimal sample fleet",
    "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "CertificateConfiguration": {
        "CertificateType": "GENERATED"
    },
    "ComputeType": "EC2",
    "EC2InstanceType": "c4.large",
    "FleetType": "ON_DEMAND",
    "RuntimeConfiguration": {
        "ServerProcesses": [
            {"LaunchPath": "/local/game/mygame.exe",
             "ConcurrentExecutions": 1}
        ]
    }
}
```

#### Sample Response
<a name="API_CreateFleet_Example_1_Response"></a>

```
{
    "FleetAttributes": {
        "BuildArn": "arn:aws:gamelift:us-west-2::build/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "CertificateConfiguration": {
            "CertificateType": "GENERATED"
        },
        "ComputeType": "EC2",
        "CreationTime": 1496365885.44,
        "Description": "A minimal sample fleet",
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetType": "ON_DEMAND",
        "InstanceType": "c4.large",
        "MetricGroups": [
            "default"
        ],
        "Name": "My_Fleet_1",
        "NewGameSessionProtectionPolicy": "NoProtection",
        "OperatingSystem": "AMAZON_LINUX_2023",
        "Status": "NEW"
    }
}
```

### Create fleet with minimal configuration (Windows)
<a name="API_CreateFleet_Example_2"></a>

This example creates a fleet for a game server build with a minimal configuration and a placeholder launch path. You can use this fleet to create queues and matchmakers, test Amazon GameLift Servers Server API calls, etc. Once you're ready to start hosting game sessions, complete the configuration settings with the `UpdateFleet` operations. If the fleet is created in a Region that supports multiple locations, you can add remote locations with `CreateFleetLocations` later.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_CreateFleet_Example_2_Request"></a>

```
{
    "Name": "My_Fleet_1",
    "Description": "A minimal sample fleet",
    "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "ComputeType": "EC2",
    "EC2InstanceType": "c4.large",
    "FleetType": "ON_DEMAND",
    "RuntimeConfiguration": {
        "ServerProcesses": [
            {"LaunchPath": "c:\\game\\mygame.exe",
             "ConcurrentExecutions": 1}
        ]
    }
}
```

#### Sample Response
<a name="API_CreateFleet_Example_2_Response"></a>

```
{
    "FleetAttributes": {
        "BuildArn": "arn:aws:gamelift:us-west-2::build/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "CertificateConfiguration": {
            "CertificateType": "DISABLED"
        },
        "ComputeType": "EC2",
        "CreationTime": 1496365885.44,
        "Description": "A minimal sample fleet",
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetType": "ON_DEMAND",
        "InstanceType": "c4.large",
        "MetricGroups": [
            "default"
        ],
        "Name": "My_Fleet_1",
        "NewGameSessionProtectionPolicy": "NoProtection",
        "OperatingSystem": "WINDOWS_2022",
        "Status": "ACTIVE"
    }
}
```

### Create fleet with full configuration
<a name="API_CreateFleet_Example_3"></a>

This example creates an EC2 fleet with complete configuration details. The new fleet, which is created in the AWS Region `us-west-2`, also deploys instances to two remote locations. In this example, the runtime configuration defines two server process configurations. The first configuration calls for three concurrent processes of the game server to run in standard mode. The second configuration calls for one process of the game server to run in a test mode. As a result, all fleet instances will maintain a total of four processes concurrently. This example also references an instance role ARN, which allows the processes running on each instance to access other AWS resources. The example opens port 22 for debugging the fleet. The game server build in this example runs on Windows.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_CreateFleet_Example_3_Request"></a>

```
{
    "Name": "My_Fleet_1",
    "Description": "A fully configured sample fleet with",
    "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "CertificateConfiguration": {
        "CertificateType": "GENERATED"
    },
    "ComputeType": "EC2",
    "EC2InstanceType": "c5.large",
    "EC2InboundPermissions": [
        {"FromPort": 33435,
         "ToPort": 33435,
         "IpRange": "10.24.34.0/23",
         "Protocol": "UDP"},
        {"FromPort": 22,
         "ToPort": 22,
         "IpRange": "10.24.34.0/23",
         "Protocol": "TCP"}
    ],
    "FleetType": "ON_DEMAND",
    "Locations": [
        {"Location": "us-east-2"},
        {"Location": "ca-central-1"}
    ],
    "NewGameSessionProtectionPolicy": "FullProtection",
    "RuntimeConfiguration": {
        "ServerProcesses": [
            {"LaunchPath": "c:\\game\\mygame.exe",
             "Parameters": "+map Winter444",
             "ConcurrentExecutions": 3},
            {"LaunchPath": "c:\\game\\mygame.exe",
             "Parameters": "-dev -console +map Winter444",
             "ConcurrentExecutions": 1}
        ],
        "MaxConcurrentGameSessionActivations": 2,
        "GameSessionActivationTimeoutSeconds": 300
    },
    "ResourceCreationLimitPolicy": {
        "NewGameSessionsPerCreator": 3,
        "PolicyPeriodInMinutes": 15
    },
    "MetricGroups": ["EMEAfleets"],
    "InstanceRoleArn": "arn:aws:iam::444455556666:role/S3AccessForGameLift",
}
```

#### Sample Response
<a name="API_CreateFleet_Example_3_Response"></a>

```
{
    "FleetAttributes": {
        "BuildArn": "arn:aws:gamelift:us-west-2::build/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "CertificateConfiguration": {
            "CertificateType": "GENERATED"
        },
        "ComputeType": "EC2",
        "CreationTime": 1496375088.502,
        "Description": "A fully configured sample fleet",
        "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetType": "ON_DEMAND",
        "InstanceRoleArn": "arn:aws:iam::444455556666:role/S3AccessForGameLift",
        "MetricGroups": [
            "EMEAfleets"
        ],
        "Name": "My_Fleet_One",
        "NewGameSessionProtectionPolicy": "FullProtection",
        "OperatingSystem": "WINDOWS_2022",
        "ResourceCreationLimitPolicy": {
            "NewGameSessionsPerCreator": 3,
            "PolicyPeriodInMinutes": 15
        }
    },
    "LocationStates": [
        {
            "Location": "us-east-2",
            "Status": "NEW"
        },
        {
            "Location": "ca-central-1",
            "Status": "NEW"
        }
    ]
        "Status": "NEW",
}
```

### Create a Realtime Servers fleet
<a name="API_CreateFleet_Example_4"></a>

This example creates a fleet using a Realtime script that has been uploaded to Amazon GameLift Servers. All Realtime servers are deployed onto Linux machines. This example represents a simple yet complete fleet configuration. You can change configuration settings with the [UpdateRuntimeConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateRuntimeConfiguration.html) operation. The new fleet, which is created in the AWS Region `us-west-2`, also deploys instances to two remote locations.

In this example, the uploaded Realtime script includes multiple script files, with the `Init()` function located in the script file called "myMainScript.js". This file is identified as the launch script in the runtime configuration.

**Note**
We recommend using a minimal version of the Realtime script when creating your fleets (see this [ working code example](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-script.html#realtime-script-examples)). This will make it much easier to troubleshoot fleet creation issues. After the fleet has reached ACTIVE status, you can update your Realtime script as needed.

#### Sample Request
<a name="API_CreateFleet_Example_4_Request"></a>

```
{
    "Name": "My_Realtime_Fleet_1",
    "Description": "A complete Realtime sample fleet",
    "CertificateConfiguration": {
        "CertificateType": "GENERATED"
    },
    "EC2InstanceType": "c4.large",
    "FleetType": "SPOT",
    "ComputeType": "EC2",
    "Locations": [
        {"Location": "us-east-2"},
        {"Location": "ca-central-1"}
    ],
    "RuntimeConfiguration": {
        "ServerProcesses": [
            {"LaunchPath": "/local/game/myMainScript.js",
             "Parameters": "+map Winter444",
             "ConcurrentExecutions": 5}
        ]
    },
    "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
}
```

#### Sample Response
<a name="API_CreateFleet_Example_4_Response"></a>

```
{
    "FleetAttributes": {
        "CertificateConfiguration": {
            "CertificateType": "GENERATED"
        },
        "ComputeType": "EC2",
        "CreationTime": 1496375088.502,
        "Description": "A complete Realtime sample fleet",
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetType": "SPOT",
        "MetricGroups": [
            "default"
        ],
        "Name": "My_Realtime_Fleet_1",
        "NewGameSessionProtectionPolicy": "NoProtection",
        "OperatingSystem": "AMAZON_LINUX_2023",
        "ScriptArn": "arn:aws:gamelift:us-west-2::script/script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "Status": "NEW"
    },
    "LocationStates": [
        {
           "Location": "us-east-2",
           "Status": "NEW"
        },
        {
           "Location": "ca-central-1",
           "Status": "NEW"
        }
    ]
}
```

## See Also
<a name="API_CreateFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateFleet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateFleet)
