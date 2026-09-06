---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_Compute.html
---

# Compute
<a name="API_Compute"></a>

An Amazon GameLift Servers compute resource for hosting your game servers. Computes in an Amazon GameLift Servers fleet differs depending on the fleet's compute type property as follows:
+ For managed EC2 fleets, a compute is an EC2 instance.
+ For Anywhere fleets, a compute is a computing resource that you provide and is registered to the fleet.
+ For managed container fleets, a compute is a container group in the fleet.

## Contents
<a name="API_Compute_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputeArn **   <a name="gameliftservers-Type-Compute-ComputeArn"></a>
The ARN that is assigned to a compute resource and uniquely identifies it. ARNs are unique across locations. Instances in managed EC2 fleets are not assigned a Compute ARN.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
Required: No

 ** ComputeName **   <a name="gameliftservers-Type-Compute-ComputeName"></a>
A descriptive label for the compute resource. For instances in a managed EC2 fleet, the compute name is the same value as the `InstanceId` ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
Required: No

 ** ComputeStatus **   <a name="gameliftservers-Type-Compute-ComputeStatus"></a>
Current status of the compute. A compute must have an `ACTIVE` status to host game sessions. Valid values include `PENDING`, `ACTIVE`, `TERMINATING`, and `IMPAIRED`.
While the ComputeStatus enum type is valid for Container based servers, the result may also include other non-enumerated string values such as "Active" for fleets which are not Container-based.
Type: String
Valid Values: `PENDING | ACTIVE | TERMINATING | IMPAIRED`
Required: No

 ** ContainerAttributes **   <a name="gameliftservers-Type-Compute-ContainerAttributes"></a>
A set of attributes for each container in the compute.
Type: Array of [ContainerAttribute](API_ContainerAttribute.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** CreationTime **   <a name="gameliftservers-Type-Compute-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** DnsName **   <a name="gameliftservers-Type-Compute-DnsName"></a>
The DNS name of a compute resource. Amazon GameLift Servers requires a DNS name or IP address for a compute.
Type: String
Required: No

 ** FleetArn **   <a name="gameliftservers-Type-Compute-FleetArn"></a>
The Amazon Resource Name (ARN) of the fleet that the compute belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** FleetId **   <a name="gameliftservers-Type-Compute-FleetId"></a>
A unique identifier for the fleet that the compute belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** GameLiftAgentEndpoint **   <a name="gameliftservers-Type-Compute-GameLiftAgentEndpoint"></a>
 The endpoint of the Amazon GameLift Servers Agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** GameLiftServiceSdkEndpoint **   <a name="gameliftservers-Type-Compute-GameLiftServiceSdkEndpoint"></a>
The Amazon GameLift Servers SDK endpoint connection for a registered compute resource in an Anywhere fleet. The game servers on the compute use this endpoint to connect to the Amazon GameLift Servers service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** GameServerContainerGroupDefinitionArn **   <a name="gameliftservers-Type-Compute-GameServerContainerGroupDefinitionArn"></a>
The game server container group definition for the compute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** InstanceId **   <a name="gameliftservers-Type-Compute-InstanceId"></a>
 The `InstanceID` of the EC2 instance that is hosting the compute.
Type: String
Pattern: `[a-zA-Z0-9\.-]+`
Required: No

 ** IpAddress **   <a name="gameliftservers-Type-Compute-IpAddress"></a>
The IP address of a compute resource. Amazon GameLift Servers requires a DNS name or IP address for a compute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9A-Fa-f\:\.]+`
Required: No

 ** Location **   <a name="gameliftservers-Type-Compute-Location"></a>
The name of the custom location you added to the fleet that this compute resource resides in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** OperatingSystem **   <a name="gameliftservers-Type-Compute-OperatingSystem"></a>
The type of operating system on the compute resource.
Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the [Amazon Linux 2 FAQs](http://aws.amazon.com/aws.amazon.com/amazon-linux-2/faqs/). For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
Type: String
Valid Values: `WINDOWS_2012 | AMAZON_LINUX | AMAZON_LINUX_2 | WINDOWS_2016 | AMAZON_LINUX_2023 | WINDOWS_2022`
Required: No

 ** Type **   <a name="gameliftservers-Type-Compute-Type"></a>
The Amazon EC2 instance type that the fleet uses. For registered computes in an Amazon GameLift Servers Anywhere fleet, this property is empty.
Type: String
Valid Values: `t2.micro | t2.small | t2.medium | t2.large | c3.large | c3.xlarge | c3.2xlarge | c3.4xlarge | c3.8xlarge | c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge | c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.12xlarge | c5.18xlarge | c5.24xlarge | c5a.large | c5a.xlarge | c5a.2xlarge | c5a.4xlarge | c5a.8xlarge | c5a.12xlarge | c5a.16xlarge | c5a.24xlarge | r3.large | r3.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge | r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge | r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.8xlarge | r5.12xlarge | r5.16xlarge | r5.24xlarge | r5a.large | r5a.xlarge | r5a.2xlarge | r5a.4xlarge | r5a.8xlarge | r5a.12xlarge | r5a.16xlarge | r5a.24xlarge | m3.medium | m3.large | m3.xlarge | m3.2xlarge | m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.8xlarge | m5.12xlarge | m5.16xlarge | m5.24xlarge | m5a.large | m5a.xlarge | m5a.2xlarge | m5a.4xlarge | m5a.8xlarge | m5a.12xlarge | m5a.16xlarge | m5a.24xlarge | c5d.large | c5d.xlarge | c5d.2xlarge | c5d.4xlarge | c5d.9xlarge | c5d.12xlarge | c5d.18xlarge | c5d.24xlarge | c6a.large | c6a.xlarge | c6a.2xlarge | c6a.4xlarge | c6a.8xlarge | c6a.12xlarge | c6a.16xlarge | c6a.24xlarge | c6i.large | c6i.xlarge | c6i.2xlarge | c6i.4xlarge | c6i.8xlarge | c6i.12xlarge | c6i.16xlarge | c6i.24xlarge | r5d.large | r5d.xlarge | r5d.2xlarge | r5d.4xlarge | r5d.8xlarge | r5d.12xlarge | r5d.16xlarge | r5d.24xlarge | m6g.medium | m6g.large | m6g.xlarge | m6g.2xlarge | m6g.4xlarge | m6g.8xlarge | m6g.12xlarge | m6g.16xlarge | c6g.medium | c6g.large | c6g.xlarge | c6g.2xlarge | c6g.4xlarge | c6g.8xlarge | c6g.12xlarge | c6g.16xlarge | r6g.medium | r6g.large | r6g.xlarge | r6g.2xlarge | r6g.4xlarge | r6g.8xlarge | r6g.12xlarge | r6g.16xlarge | c6gn.medium | c6gn.large | c6gn.xlarge | c6gn.2xlarge | c6gn.4xlarge | c6gn.8xlarge | c6gn.12xlarge | c6gn.16xlarge | c7g.medium | c7g.large | c7g.xlarge | c7g.2xlarge | c7g.4xlarge | c7g.8xlarge | c7g.12xlarge | c7g.16xlarge | r7g.medium | r7g.large | r7g.xlarge | r7g.2xlarge | r7g.4xlarge | r7g.8xlarge | r7g.12xlarge | r7g.16xlarge | m7g.medium | m7g.large | m7g.xlarge | m7g.2xlarge | m7g.4xlarge | m7g.8xlarge | m7g.12xlarge | m7g.16xlarge | g5g.xlarge | g5g.2xlarge | g5g.4xlarge | g5g.8xlarge | g5g.16xlarge | r6i.large | r6i.xlarge | r6i.2xlarge | r6i.4xlarge | r6i.8xlarge | r6i.12xlarge | r6i.16xlarge | c6gd.medium | c6gd.large | c6gd.xlarge | c6gd.2xlarge | c6gd.4xlarge | c6gd.8xlarge | c6gd.12xlarge | c6gd.16xlarge | c6in.large | c6in.xlarge | c6in.2xlarge | c6in.4xlarge | c6in.8xlarge | c6in.12xlarge | c6in.16xlarge | c7a.medium | c7a.large | c7a.xlarge | c7a.2xlarge | c7a.4xlarge | c7a.8xlarge | c7a.12xlarge | c7a.16xlarge | c7gd.medium | c7gd.large | c7gd.xlarge | c7gd.2xlarge | c7gd.4xlarge | c7gd.8xlarge | c7gd.12xlarge | c7gd.16xlarge | c7gn.medium | c7gn.large | c7gn.xlarge | c7gn.2xlarge | c7gn.4xlarge | c7gn.8xlarge | c7gn.12xlarge | c7gn.16xlarge | c7i.large | c7i.xlarge | c7i.2xlarge | c7i.4xlarge | c7i.8xlarge | c7i.12xlarge | c7i.16xlarge | m6a.large | m6a.xlarge | m6a.2xlarge | m6a.4xlarge | m6a.8xlarge | m6a.12xlarge | m6a.16xlarge | m6gd.medium | m6gd.large | m6gd.xlarge | m6gd.2xlarge | m6gd.4xlarge | m6gd.8xlarge | m6gd.12xlarge | m6gd.16xlarge | m6i.large | m6i.xlarge | m6i.2xlarge | m6i.4xlarge | m6i.8xlarge | m6i.12xlarge | m6i.16xlarge | m7a.medium | m7a.large | m7a.xlarge | m7a.2xlarge | m7a.4xlarge | m7a.8xlarge | m7a.12xlarge | m7a.16xlarge | m7gd.medium | m7gd.large | m7gd.xlarge | m7gd.2xlarge | m7gd.4xlarge | m7gd.8xlarge | m7gd.12xlarge | m7gd.16xlarge | m7i.large | m7i.xlarge | m7i.2xlarge | m7i.4xlarge | m7i.8xlarge | m7i.12xlarge | m7i.16xlarge | r6gd.medium | r6gd.large | r6gd.xlarge | r6gd.2xlarge | r6gd.4xlarge | r6gd.8xlarge | r6gd.12xlarge | r6gd.16xlarge | r7a.medium | r7a.large | r7a.xlarge | r7a.2xlarge | r7a.4xlarge | r7a.8xlarge | r7a.12xlarge | r7a.16xlarge | r7gd.medium | r7gd.large | r7gd.xlarge | r7gd.2xlarge | r7gd.4xlarge | r7gd.8xlarge | r7gd.12xlarge | r7gd.16xlarge | r7i.large | r7i.xlarge | r7i.2xlarge | r7i.4xlarge | r7i.8xlarge | r7i.12xlarge | r7i.16xlarge | r7i.24xlarge | r7i.48xlarge | c5ad.large | c5ad.xlarge | c5ad.2xlarge | c5ad.4xlarge | c5ad.8xlarge | c5ad.12xlarge | c5ad.16xlarge | c5ad.24xlarge | c5n.large | c5n.xlarge | c5n.2xlarge | c5n.4xlarge | c5n.9xlarge | c5n.18xlarge | r5ad.large | r5ad.xlarge | r5ad.2xlarge | r5ad.4xlarge | r5ad.8xlarge | r5ad.12xlarge | r5ad.16xlarge | r5ad.24xlarge | c6id.large | c6id.xlarge | c6id.2xlarge | c6id.4xlarge | c6id.8xlarge | c6id.12xlarge | c6id.16xlarge | c6id.24xlarge | c6id.32xlarge | c8g.medium | c8g.large | c8g.xlarge | c8g.2xlarge | c8g.4xlarge | c8g.8xlarge | c8g.12xlarge | c8g.16xlarge | c8g.24xlarge | c8g.48xlarge | m5ad.large | m5ad.xlarge | m5ad.2xlarge | m5ad.4xlarge | m5ad.8xlarge | m5ad.12xlarge | m5ad.16xlarge | m5ad.24xlarge | m5d.large | m5d.xlarge | m5d.2xlarge | m5d.4xlarge | m5d.8xlarge | m5d.12xlarge | m5d.16xlarge | m5d.24xlarge | m5dn.large | m5dn.xlarge | m5dn.2xlarge | m5dn.4xlarge | m5dn.8xlarge | m5dn.12xlarge | m5dn.16xlarge | m5dn.24xlarge | m5n.large | m5n.xlarge | m5n.2xlarge | m5n.4xlarge | m5n.8xlarge | m5n.12xlarge | m5n.16xlarge | m5n.24xlarge | m6id.large | m6id.xlarge | m6id.2xlarge | m6id.4xlarge | m6id.8xlarge | m6id.12xlarge | m6id.16xlarge | m6id.24xlarge | m6id.32xlarge | m6idn.large | m6idn.xlarge | m6idn.2xlarge | m6idn.4xlarge | m6idn.8xlarge | m6idn.12xlarge | m6idn.16xlarge | m6idn.24xlarge | m6idn.32xlarge | m6in.large | m6in.xlarge | m6in.2xlarge | m6in.4xlarge | m6in.8xlarge | m6in.12xlarge | m6in.16xlarge | m6in.24xlarge | m6in.32xlarge | m8g.medium | m8g.large | m8g.xlarge | m8g.2xlarge | m8g.4xlarge | m8g.8xlarge | m8g.12xlarge | m8g.16xlarge | m8g.24xlarge | m8g.48xlarge | r5dn.large | r5dn.xlarge | r5dn.2xlarge | r5dn.4xlarge | r5dn.8xlarge | r5dn.12xlarge | r5dn.16xlarge | r5dn.24xlarge | r5n.large | r5n.xlarge | r5n.2xlarge | r5n.4xlarge | r5n.8xlarge | r5n.12xlarge | r5n.16xlarge | r5n.24xlarge | r6a.large | r6a.xlarge | r6a.2xlarge | r6a.4xlarge | r6a.8xlarge | r6a.12xlarge | r6a.16xlarge | r6a.24xlarge | r6a.32xlarge | r6a.48xlarge | r6id.large | r6id.xlarge | r6id.2xlarge | r6id.4xlarge | r6id.8xlarge | r6id.12xlarge | r6id.16xlarge | r6id.24xlarge | r6id.32xlarge | r6idn.large | r6idn.xlarge | r6idn.2xlarge | r6idn.4xlarge | r6idn.8xlarge | r6idn.12xlarge | r6idn.16xlarge | r6idn.24xlarge | r6idn.32xlarge | r6in.large | r6in.xlarge | r6in.2xlarge | r6in.4xlarge | r6in.8xlarge | r6in.12xlarge | r6in.16xlarge | r6in.24xlarge | r6in.32xlarge | r8g.medium | r8g.large | r8g.xlarge | r8g.2xlarge | r8g.4xlarge | r8g.8xlarge | r8g.12xlarge | r8g.16xlarge | r8g.24xlarge | r8g.48xlarge | m4.16xlarge | c6a.32xlarge | c6a.48xlarge | c6i.32xlarge | r6i.24xlarge | r6i.32xlarge | c6in.24xlarge | c6in.32xlarge | c7a.24xlarge | c7a.32xlarge | c7a.48xlarge | c7i.24xlarge | c7i.48xlarge | m6a.24xlarge | m6a.32xlarge | m6a.48xlarge | m6i.24xlarge | m6i.32xlarge | m7a.24xlarge | m7a.32xlarge | m7a.48xlarge | m7i.24xlarge | m7i.48xlarge | r7a.24xlarge | r7a.32xlarge | r7a.48xlarge`
Required: No

## See Also
<a name="API_Compute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/Compute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/Compute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/Compute)
