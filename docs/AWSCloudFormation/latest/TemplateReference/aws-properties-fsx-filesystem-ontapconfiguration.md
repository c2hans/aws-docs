---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-ontapconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem OntapConfiguration
<a name="aws-properties-fsx-filesystem-ontapconfiguration"></a>

The configuration for this Amazon FSx for NetApp ONTAP file system.

## Syntax
<a name="aws-properties-fsx-filesystem-ontapconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-ontapconfiguration-syntax.json"></a>

```
{
  "[AutomaticBackupRetentionDays](#cfn-fsx-filesystem-ontapconfiguration-automaticbackupretentiondays)" : {{Integer}},
  "[DailyAutomaticBackupStartTime](#cfn-fsx-filesystem-ontapconfiguration-dailyautomaticbackupstarttime)" : {{String}},
  "[DeploymentType](#cfn-fsx-filesystem-ontapconfiguration-deploymenttype)" : {{String}},
  "[DiskIopsConfiguration](#cfn-fsx-filesystem-ontapconfiguration-diskiopsconfiguration)" : {{DiskIopsConfiguration}},
  "[EndpointIpAddressRange](#cfn-fsx-filesystem-ontapconfiguration-endpointipaddressrange)" : {{String}},
  "[EndpointIpv6AddressRange](#cfn-fsx-filesystem-ontapconfiguration-endpointipv6addressrange)" : {{String}},
  "[FsxAdminPassword](#cfn-fsx-filesystem-ontapconfiguration-fsxadminpassword)" : {{String}},
  "[HAPairs](#cfn-fsx-filesystem-ontapconfiguration-hapairs)" : {{Integer}},
  "[PreferredSubnetId](#cfn-fsx-filesystem-ontapconfiguration-preferredsubnetid)" : {{String}},
  "[RouteTableIds](#cfn-fsx-filesystem-ontapconfiguration-routetableids)" : {{[ String, ... ]}},
  "[ThroughputCapacity](#cfn-fsx-filesystem-ontapconfiguration-throughputcapacity)" : {{Integer}},
  "[ThroughputCapacityPerHAPair](#cfn-fsx-filesystem-ontapconfiguration-throughputcapacityperhapair)" : {{Integer}},
  "[WeeklyMaintenanceStartTime](#cfn-fsx-filesystem-ontapconfiguration-weeklymaintenancestarttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-ontapconfiguration-syntax.yaml"></a>

```
  [AutomaticBackupRetentionDays](#cfn-fsx-filesystem-ontapconfiguration-automaticbackupretentiondays): {{Integer}}
  [DailyAutomaticBackupStartTime](#cfn-fsx-filesystem-ontapconfiguration-dailyautomaticbackupstarttime): {{String}}
  [DeploymentType](#cfn-fsx-filesystem-ontapconfiguration-deploymenttype): {{String}}
  [DiskIopsConfiguration](#cfn-fsx-filesystem-ontapconfiguration-diskiopsconfiguration): {{
    DiskIopsConfiguration}}
  [EndpointIpAddressRange](#cfn-fsx-filesystem-ontapconfiguration-endpointipaddressrange): {{String}}
  [EndpointIpv6AddressRange](#cfn-fsx-filesystem-ontapconfiguration-endpointipv6addressrange): {{String}}
  [FsxAdminPassword](#cfn-fsx-filesystem-ontapconfiguration-fsxadminpassword): {{String}}
  [HAPairs](#cfn-fsx-filesystem-ontapconfiguration-hapairs): {{Integer}}
  [PreferredSubnetId](#cfn-fsx-filesystem-ontapconfiguration-preferredsubnetid): {{String}}
  [RouteTableIds](#cfn-fsx-filesystem-ontapconfiguration-routetableids): {{
    - String}}
  [ThroughputCapacity](#cfn-fsx-filesystem-ontapconfiguration-throughputcapacity): {{Integer}}
  [ThroughputCapacityPerHAPair](#cfn-fsx-filesystem-ontapconfiguration-throughputcapacityperhapair): {{Integer}}
  [WeeklyMaintenanceStartTime](#cfn-fsx-filesystem-ontapconfiguration-weeklymaintenancestarttime): {{String}}
```

## Properties
<a name="aws-properties-fsx-filesystem-ontapconfiguration-properties"></a>

`AutomaticBackupRetentionDays`  <a name="cfn-fsx-filesystem-ontapconfiguration-automaticbackupretentiondays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DailyAutomaticBackupStartTime`  <a name="cfn-fsx-filesystem-ontapconfiguration-dailyautomaticbackupstarttime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentType`  <a name="cfn-fsx-filesystem-ontapconfiguration-deploymenttype"></a>
Specifies the FSx for ONTAP file system deployment type to use in creating the file system.
+ `MULTI_AZ_1` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. This is a first-generation FSx for ONTAP file system.
+ `MULTI_AZ_2` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary AZ unavailability. This is a second-generation FSx for ONTAP file system.
+ `SINGLE_AZ_1` - A file system configured for Single-AZ redundancy. This is a first-generation FSx for ONTAP file system.
+ `SINGLE_AZ_2` - A file system configured with multiple high-availability (HA) pairs for Single-AZ redundancy. This is a second-generation FSx for ONTAP file system.
For information about the use cases for Multi-AZ and Single-AZ deployments, refer to [Choosing a file system deployment type](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html).
*Required*: Yes
*Type*: String
*Allowed values*: `MULTI_AZ_1 | SINGLE_AZ_1 | SINGLE_AZ_2 | MULTI_AZ_2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DiskIopsConfiguration`  <a name="cfn-fsx-filesystem-ontapconfiguration-diskiopsconfiguration"></a>
The SSD IOPS configuration for the FSx for ONTAP file system.
*Required*: No
*Type*: [DiskIopsConfiguration](aws-properties-fsx-filesystem-diskiopsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointIpAddressRange`  <a name="cfn-fsx-filesystem-ontapconfiguration-endpointipaddressrange"></a>
(Multi-AZ only) Specifies the IPv4 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API, Amazon FSx selects an unused IP address range for you from the 198.19.\* range. By default in the Amazon FSx console, Amazon FSx chooses the last 64 IP addresses from the VPC’s primary CIDR range to use as the endpoint IP address range for the file system. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{9,17}$`
*Minimum*: `9`
*Maximum*: `17`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointIpv6AddressRange`  <a name="cfn-fsx-filesystem-ontapconfiguration-endpointipv6addressrange"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FsxAdminPassword`  <a name="cfn-fsx-filesystem-ontapconfiguration-fsxadminpassword"></a>
The ONTAP administrative password for the `fsxadmin` user with which you administer your file system using the NetApp ONTAP CLI and REST API.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{8,50}$`
*Minimum*: `8`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HAPairs`  <a name="cfn-fsx-filesystem-ontapconfiguration-hapairs"></a>
Specifies how many high-availability (HA) pairs of file servers will power your file system. First-generation file systems are powered by 1 HA pair. Second-generation multi-AZ file systems are powered by 1 HA pair. Second generation single-AZ file systems are powered by up to 12 HA pairs. The default value is 1. The value of this property affects the values of `StorageCapacity`, `Iops`, and `ThroughputCapacity`. For more information, see [High-availability (HA) pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/administering-file-systems.html#HA-pairs) in the FSx for ONTAP user guide. Block storage protocol support (iSCSI and NVMe over TCP) is disabled on file systems with more than 6 HA pairs. For more information, see [Using block storage protocols](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/supported-fsx-clients.html#using-block-storage).
Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:
+ The value of `HAPairs` is less than 1 or greater than 12.
+ The value of `HAPairs` is greater than 1 and the value of `DeploymentType` is `SINGLE_AZ_1`, `MULTI_AZ_1`, or `MULTI_AZ_2`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredSubnetId`  <a name="cfn-fsx-filesystem-ontapconfiguration-preferredsubnetid"></a>
Required when `DeploymentType` is set to `MULTI_AZ_1` or `MULTI_AZ_2`. This specifies the subnet in which you want the preferred file server to be located.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RouteTableIds`  <a name="cfn-fsx-filesystem-ontapconfiguration-routetableids"></a>
(Multi-AZ only) Specifies the route tables in which Amazon FSx creates the rules for routing traffic to the correct file server. You should specify all virtual private cloud (VPC) route tables associated with the subnets in which your clients are located. By default, Amazon FSx selects your VPC's default route table.
Amazon FSx manages these route tables for Multi-AZ file systems using tag-based authentication. These route tables are tagged with `Key: AmazonFSx; Value: ManagedByAmazonFSx`. When creating FSx for ONTAP Multi-AZ file systems using CloudFormation we recommend that you add the `Key: AmazonFSx; Value: ManagedByAmazonFSx` tag manually.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThroughputCapacity`  <a name="cfn-fsx-filesystem-ontapconfiguration-throughputcapacity"></a>
Sets the throughput capacity for the file system that you're creating in megabytes per second (MBps). For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-throughput-capacity.html) in the FSx for ONTAP User Guide.
Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:
+ The value of `ThroughputCapacity` and `ThroughputCapacityPerHAPair` are not the same value.
+ The value of `ThroughputCapacity` when divided by the value of `HAPairs` is outside of the valid range for `ThroughputCapacity`.
*Required*: No
*Type*: Integer
*Minimum*: `8`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThroughputCapacityPerHAPair`  <a name="cfn-fsx-filesystem-ontapconfiguration-throughputcapacityperhapair"></a>
Use to choose the throughput capacity per HA pair, rather than the total throughput for the file system.
You can define either the `ThroughputCapacityPerHAPair` or the `ThroughputCapacity` when creating a file system, but not both.
This field and `ThroughputCapacity` are the same for file systems powered by one HA pair.
+ For `SINGLE_AZ_1` and `MULTI_AZ_1` file systems, valid values are 128, 256, 512, 1024, 2048, or 4096 MBps.
+ For `SINGLE_AZ_2`, valid values are 1536, 3072, or 6144 MBps.
+ For `MULTI_AZ_2`, valid values are 384, 768, 1536, 3072, or 6144 MBps.
Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:
+ The value of `ThroughputCapacity` and `ThroughputCapacityPerHAPair` are not the same value for file systems with one HA pair.
+ The value of deployment type is `SINGLE_AZ_2` and `ThroughputCapacity` / `ThroughputCapacityPerHAPair` is not a valid HA pair (a value between 1 and 12).
+ The value of `ThroughputCapacityPerHAPair` is not a valid value.
*Required*: No
*Type*: Integer
*Minimum*: `128`
*Maximum*: `6144`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeeklyMaintenanceStartTime`  <a name="cfn-fsx-filesystem-ontapconfiguration-weeklymaintenancestarttime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.
For example, `1:05:00` specifies maintenance at 5 AM Monday.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
