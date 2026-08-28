---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_ec2_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Amazon EC2 examples using Tools for PowerShell V4
<a name="powershell_ec2_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Amazon EC2.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-EC2CapacityReservation`
<a name="ec2_CreateCapacityReservation_powershell_topic"></a>

The following code example shows how to use `Add-EC2CapacityReservation`.

**Tools for PowerShell V4**
**Example 1: This example creates a new Capacity Reservation with the specified attributes**

```
Add-EC2CapacityReservation -InstanceType m4.xlarge -InstanceCount 2 -AvailabilityZone eu-west-1b -EbsOptimized True -InstancePlatform Windows
```
**Output:**

```
AvailabilityZone       : eu-west-1b
AvailableInstanceCount : 2
CapacityReservationId  : cr-0c1f2345db6f7cdba
CreateDate             : 3/28/2019 9:29:41 AM
EbsOptimized           : True
EndDate                : 1/1/0001 12:00:00 AM
EndDateType            : unlimited
EphemeralStorage       : False
InstanceMatchCriteria  : open
InstancePlatform       : Windows
InstanceType           : m4.xlarge
State                  : active
Tags                   : {}
Tenancy                : default
TotalInstanceCount     : 2
```
+  For API details, see [CreateCapacityReservation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Add-EC2InternetGateway`
<a name="ec2_AttachInternetGateway_powershell_topic"></a>

The following code example shows how to use `Add-EC2InternetGateway`.

**Tools for PowerShell V4**
**Example 1: This example attaches the specified Internet gateway to the specified VPC.**

```
Add-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678
```
**Example 2: This example creates a VPC and an Internet gateway, and then attaches the Internet gateway to the VPC.**

```
$vpc = New-EC2Vpc -CidrBlock 10.0.0.0/16
New-EC2InternetGateway | Add-EC2InternetGateway -VpcId $vpc.VpcId
```
+  For API details, see [AttachInternetGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Add-EC2NetworkInterface`
<a name="ec2_AttachNetworkInterface_powershell_topic"></a>

The following code example shows how to use `Add-EC2NetworkInterface`.

**Tools for PowerShell V4**
**Example 1: This example attaches the specified network interface to the specified instance.**

```
Add-EC2NetworkInterface -NetworkInterfaceId eni-12345678 -InstanceId i-1a2b3c4d -DeviceIndex 1
```
**Output:**

```
eni-attach-1a2b3c4d
```
+  For API details, see [AttachNetworkInterface](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Add-EC2Volume`
<a name="ec2_AttachVolume_powershell_topic"></a>

The following code example shows how to use `Add-EC2Volume`.

**Tools for PowerShell V4**
**Example 1: This example attaches the specified volume to the specified instance and exposes it with the specified device name.**

```
Add-EC2Volume -VolumeId vol-12345678 -InstanceId i-1a2b3c4d -Device /dev/sdh
```
**Output:**

```
AttachTime          : 12/22/2015 1:53:58 AM
DeleteOnTermination : False
Device              : /dev/sdh
InstanceId          : i-1a2b3c4d
State               : attaching
VolumeId            : vol-12345678
```
+  For API details, see [AttachVolume](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Add-EC2VpnGateway`
<a name="ec2_AttachVpnGateway_powershell_topic"></a>

The following code example shows how to use `Add-EC2VpnGateway`.

**Tools for PowerShell V4**
**Example 1: This example attaches the specified virtual private gateway to the specified VPC.**

```
Add-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678
```
**Output:**

```
State        VpcId
-----        -----
attaching    vpc-12345678
```
+  For API details, see [AttachVpnGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Approve-EC2VpcPeeringConnection`
<a name="ec2_AcceptVpcPeeringConnection_powershell_topic"></a>

The following code example shows how to use `Approve-EC2VpcPeeringConnection`.

**Tools for PowerShell V4**
**Example 1: This example approves the requested VpcPeeringConnectionId pcx-1dfad234b56ff78be**

```
Approve-EC2VpcPeeringConnection -VpcPeeringConnectionId pcx-1dfad234b56ff78be
```
**Output:**

```
AccepterVpcInfo        : Amazon.EC2.Model.VpcPeeringConnectionVpcInfo
ExpirationTime         : 1/1/0001 12:00:00 AM
RequesterVpcInfo       : Amazon.EC2.Model.VpcPeeringConnectionVpcInfo
Status                 : Amazon.EC2.Model.VpcPeeringConnectionStateReason
Tags                   : {}
VpcPeeringConnectionId : pcx-1dfad234b56ff78be
```
+  For API details, see [AcceptVpcPeeringConnection](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Confirm-EC2ProductInstance`
<a name="ec2_ConfirmProductInstance_powershell_topic"></a>

The following code example shows how to use `Confirm-EC2ProductInstance`.

**Tools for PowerShell V4**
**Example 1: This example determines whether the specified product code is associated with the specified instance.**

```
Confirm-EC2ProductInstance -ProductCode 774F4FF8 -InstanceId i-12345678
```
+  For API details, see [ConfirmProductInstance](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Copy-EC2Image`
<a name="ec2_CopyImage_powershell_topic"></a>

The following code example shows how to use `Copy-EC2Image`.

**Tools for PowerShell V4**
**Example 1: This example copies the specified AMI in the 'EU (Ireland)' region to the 'US West (Oregon)' region. If -Region is not specified, the current default region is used as the destination region.**

```
Copy-EC2Image -SourceRegion eu-west-1 -SourceImageId ami-12345678 -Region us-west-2 -Name "Copy of ami-12345678"
```
**Output:**

```
ami-87654321
```
+  For API details, see [CopyImage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Copy-EC2Snapshot`
<a name="ec2_CopySnapshot_powershell_topic"></a>

The following code example shows how to use `Copy-EC2Snapshot`.

**Tools for PowerShell V4**
**Example 1: This example copies the specified snapshot from the EU (Ireland) region to the US West (Oregon) region.**

```
Copy-EC2Snapshot -SourceRegion eu-west-1 -SourceSnapshotId snap-12345678 -Region us-west-2
```
**Example 2: If you set a default region and omit the Region parameter, the default destination region is the default region.**

```
Set-DefaultAWSRegion us-west-2
Copy-EC2Snapshot -SourceRegion eu-west-1 -SourceSnapshotId snap-12345678
```
+  For API details, see [CopySnapshot](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Deny-EC2VpcPeeringConnection`
<a name="ec2_RejectVpcPeeringConnection_powershell_topic"></a>

The following code example shows how to use `Deny-EC2VpcPeeringConnection`.

**Tools for PowerShell V4**
**Example 1: The above example denies the request for VpcPeering request id pcx-01a2b3ce45fe67eb8**

```
Deny-EC2VpcPeeringConnection -VpcPeeringConnectionId pcx-01a2b3ce45fe67eb8
```
+  For API details, see [RejectVpcPeeringConnection](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Disable-EC2VgwRoutePropagation`
<a name="ec2_DisableVgwRoutePropagation_powershell_topic"></a>

The following code example shows how to use `Disable-EC2VgwRoutePropagation`.

**Tools for PowerShell V4**
**Example 1: This example disables the VGW from automatically propagating routes to the specified routing table.**

```
Disable-EC2VgwRoutePropagation -RouteTableId rtb-12345678 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [DisableVgwRoutePropagation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Disable-EC2VpcClassicLink`
<a name="ec2_DisableVpcClassicLink_powershell_topic"></a>

The following code example shows how to use `Disable-EC2VpcClassicLink`.

**Tools for PowerShell V4**
**Example 1: This example disables EC2VpcClassicLink for the vpc-01e23c4a5d6db78e9. It returns either True or False**

```
Disable-EC2VpcClassicLink -VpcId vpc-01e23c4a5d6db78e9
```
+  For API details, see [DisableVpcClassicLink](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Disable-EC2VpcClassicLinkDnsSupport`
<a name="ec2_DisableVpcClassicLinkDnsSupport_powershell_topic"></a>

The following code example shows how to use `Disable-EC2VpcClassicLinkDnsSupport`.

**Tools for PowerShell V4**
**Example 1: This example disables ClassicLink DNS support for the vpc-0b12d3456a7e8910d**

```
Disable-EC2VpcClassicLinkDnsSupport -VpcId vpc-0b12d3456a7e8910d
```
+  For API details, see [DisableVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Dismount-EC2InternetGateway`
<a name="ec2_DetachInternetGateway_powershell_topic"></a>

The following code example shows how to use `Dismount-EC2InternetGateway`.

**Tools for PowerShell V4**
**Example 1: This example detaches the specified Internet gateway from the specified VPC.**

```
Dismount-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678
```
+  For API details, see [DetachInternetGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Dismount-EC2NetworkInterface`
<a name="ec2_DetachNetworkInterface_powershell_topic"></a>

The following code example shows how to use `Dismount-EC2NetworkInterface`.

**Tools for PowerShell V4**
**Example 1: This example removes the specified attachment between a network interface and an instance.**

```
Dismount-EC2NetworkInterface -AttachmentId eni-attach-1a2b3c4d -Force
```
+  For API details, see [DetachNetworkInterface](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Dismount-EC2Volume`
<a name="ec2_DetachVolume_powershell_topic"></a>

The following code example shows how to use `Dismount-EC2Volume`.

**Tools for PowerShell V4**
**Example 1: This example detaches the specified volume.**

```
Dismount-EC2Volume -VolumeId vol-12345678
```
**Output:**

```
AttachTime          : 12/22/2015 1:53:58 AM
DeleteOnTermination : False
Device              : /dev/sdh
InstanceId          : i-1a2b3c4d
State               : detaching
VolumeId            : vol-12345678
```
**Example 2: You can also specify the instance ID and device name to ensure that you are detaching the correct volume.**

```
Dismount-EC2Volume -VolumeId vol-12345678 -InstanceId i-1a2b3c4d -Device /dev/sdh
```
+  For API details, see [DetachVolume](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Dismount-EC2VpnGateway`
<a name="ec2_DetachVpnGateway_powershell_topic"></a>

The following code example shows how to use `Dismount-EC2VpnGateway`.

**Tools for PowerShell V4**
**Example 1: This example detaches the specified virtual private gateway from the specified VPC.**

```
Dismount-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678
```
+  For API details, see [DetachVpnGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2CapacityReservation`
<a name="ec2_ModifyCapacityReservation_powershell_topic"></a>

The following code example shows how to use `Edit-EC2CapacityReservation`.

**Tools for PowerShell V4**
**Example 1: This example modifies the CapacityReservationId cr-0c1f2345db6f7cdba by changing the instane count to 1**

```
Edit-EC2CapacityReservation -CapacityReservationId cr-0c1f2345db6f7cdba -InstanceCount 1
```
**Output:**

```
True
```
+  For API details, see [ModifyCapacityReservation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2Host`
<a name="ec2_ModifyHosts_powershell_topic"></a>

The following code example shows how to use `Edit-EC2Host`.

**Tools for PowerShell V4**
**Example 1: This example modifies the AutoPlacement settings to off for the dedicated host h-01e23f4cd567890f3**

```
Edit-EC2Host -HostId h-03e09f8cd681609f3 -AutoPlacement off
```
**Output:**

```
Successful            Unsuccessful
----------            ------------
{h-01e23f4cd567890f3} {}
```
+  For API details, see [ModifyHosts](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2IdFormat`
<a name="ec2_ModifyIdFormat_powershell_topic"></a>

The following code example shows how to use `Edit-EC2IdFormat`.

**Tools for PowerShell V4**
**Example 1: This example enables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $true
```
**Example 2: This example disables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $false
```
+  For API details, see [ModifyIdFormat](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2ImageAttribute`
<a name="ec2_ModifyImageAttribute_powershell_topic"></a>

The following code example shows how to use `Edit-EC2ImageAttribute`.

**Tools for PowerShell V4**
**Example 1: This example updates the description for the specified AMI.**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Description "New description"
```
**Example 2: This example makes the AMI public (for example, so any AWS account can use it).**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType add -UserGroup all
```
**Example 3: This example makes the AMI private (for example, so that only you as the owner can use it).**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType remove -UserGroup all
```
**Example 4: This example grants launch permission to the specified AWS account.**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType add -UserId 111122223333
```
**Example 5: This example removes launch permission from the specified AWS account.**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType remove -UserId 111122223333
```
+  For API details, see [ModifyImageAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2InstanceAttribute`
<a name="ec2_ModifyInstanceAttribute_powershell_topic"></a>

The following code example shows how to use `Edit-EC2InstanceAttribute`.

**Tools for PowerShell V4**
**Example 1: This example modifies the instance type of the specified instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -InstanceType m3.medium
```
**Example 2: This example enables enhanced networking for the specified instance, by specifying "simple" as the value of the single root I/O virtualization (SR-IOV) network support parameter, -SriovNetSupport..**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -SriovNetSupport "simple"
```
**Example 3: This example modifies the security groups for the specified instance. The instance must be in a VPC. You must specify the ID of each security group, not the name.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -Group @( "sg-12345678", "sg-45678901" )
```
**Example 4: This example enables EBS I/O optimization for the specified instance. This feature isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -EbsOptimized $true
```
**Example 5: This example enables source/destination checking for the specified instance. For a NAT instance to perform NAT, the value must be 'false'.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -SourceDestCheck $true
```
**Example 6: This example disables termination for the specified instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -DisableApiTermination $true
```
**Example 7: This example changes the specified instance so that it terminates when shutdown is initiated from the instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -InstanceInitiatedShutdownBehavior terminate
```
+  For API details, see [ModifyInstanceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2InstanceCreditSpecification`
<a name="ec2_ModifyInstanceCreditSpecification_powershell_topic"></a>

The following code example shows how to use `Edit-EC2InstanceCreditSpecification`.

**Tools for PowerShell V4**
**Example 1: This enables T2 unlimited credits for instance i-01234567890abcdef.**

```
$Credit = New-Object -TypeName Amazon.EC2.Model.InstanceCreditSpecificationRequest
$Credit.InstanceId = "i-01234567890abcdef"
$Credit.CpuCredits = "unlimited"
Edit-EC2InstanceCreditSpecification -InstanceCreditSpecification $Credit
```
+  For API details, see [ModifyInstanceCreditSpecification](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2NetworkInterfaceAttribute`
<a name="ec2_ModifyNetworkInterfaceAttribute_powershell_topic"></a>

The following code example shows how to use `Edit-EC2NetworkInterfaceAttribute`.

**Tools for PowerShell V4**
**Example 1: This example modifies the specified network interface so that the specified attachment is deleted on termination.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Attachment_AttachmentId eni-attach-1a2b3c4d -Attachment_DeleteOnTermination $true
```
**Example 2: This example modifies the description of the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Description "my description"
```
**Example 3: This example modifies the security group for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Groups sg-1a2b3c4d
```
**Example 4: This example disables source/destination checking for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -SourceDestCheck $false
```
+  For API details, see [ModifyNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2ReservedInstance`
<a name="ec2_ModifyReservedInstances_powershell_topic"></a>

The following code example shows how to use `Edit-EC2ReservedInstance`.

**Tools for PowerShell V4**
**Example 1: This example modifies the Availability Zone, instance count, and platform for the specified Reserved instances.**

```
$config = New-Object Amazon.EC2.Model.ReservedInstancesConfiguration
$config.AvailabilityZone = "us-west-2a"
$config.InstanceCount = 1
$config.Platform = "EC2-VPC"

Edit-EC2ReservedInstance `
-ReservedInstancesId @("FE32132D-70D5-4795-B400-AE435EXAMPLE", "0CC556F3-7AB8-4C00-B0E5-98666EXAMPLE") `
-TargetConfiguration $config
```
+  For API details, see [ModifyReservedInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2SnapshotAttribute`
<a name="ec2_ModifySnapshotAttribute_powershell_topic"></a>

The following code example shows how to use `Edit-EC2SnapshotAttribute`.

**Tools for PowerShell V4**
**Example 1: This example makes the specified snapshot public by setting its CreateVolumePermission attribute.**

```
Edit-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission -OperationType Add -GroupName all
```
+  For API details, see [ModifySnapshotAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2SpotFleetRequest`
<a name="ec2_ModifySpotFleetRequest_powershell_topic"></a>

The following code example shows how to use `Edit-EC2SpotFleetRequest`.

**Tools for PowerShell V4**
**Example 1: This example updates the target capacity of the specified Spot fleet request.**

```
Edit-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -TargetCapacity 10
```
**Output:**

```
True
```
+  For API details, see [ModifySpotFleetRequest](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2SubnetAttribute`
<a name="ec2_ModifySubnetAttribute_powershell_topic"></a>

The following code example shows how to use `Edit-EC2SubnetAttribute`.

**Tools for PowerShell V4**
**Example 1: This example enables public IP addressing for the specified subnet.**

```
Edit-EC2SubnetAttribute -SubnetId subnet-1a2b3c4d -MapPublicIpOnLaunch $true
```
**Example 2: This example disables public IP addressing for the specified subnet.**

```
Edit-EC2SubnetAttribute -SubnetId subnet-1a2b3c4d -MapPublicIpOnLaunch $false
```
+  For API details, see [ModifySubnetAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2VolumeAttribute`
<a name="ec2_ModifyVolumeAttribute_powershell_topic"></a>

The following code example shows how to use `Edit-EC2VolumeAttribute`.

**Tools for PowerShell V4**
**Example 1: This example modifies the specified attribute of the specified volume. I/O operations for the volume are automatically resumed after being suspended due to potentially inconsistent data.**

```
Edit-EC2VolumeAttribute -VolumeId vol-12345678 -AutoEnableIO $true
```
+  For API details, see [ModifyVolumeAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Edit-EC2VpcAttribute`
<a name="ec2_ModifyVpcAttribute_powershell_topic"></a>

The following code example shows how to use `Edit-EC2VpcAttribute`.

**Tools for PowerShell V4**
**Example 1: This example enables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $true
```
**Example 2: This example disables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $false
```
**Example 3: This example enables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $true
```
**Example 4: This example disables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $false
```
+  For API details, see [ModifyVpcAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Enable-EC2VgwRoutePropagation`
<a name="ec2_EnableVgwRoutePropagation_powershell_topic"></a>

The following code example shows how to use `Enable-EC2VgwRoutePropagation`.

**Tools for PowerShell V4**
**Example 1: This example enables the specified VGW to propagate routes automatically to the specified routing table.**

```
Enable-EC2VgwRoutePropagation -RouteTableId rtb-12345678 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [EnableVgwRoutePropagation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Enable-EC2VolumeIO`
<a name="ec2_EnableVolumeIo_powershell_topic"></a>

The following code example shows how to use `Enable-EC2VolumeIO`.

**Tools for PowerShell V4**
**Example 1: This example enables I/O operations for the specified volume, if I/O operations were disabled.**

```
Enable-EC2VolumeIO -VolumeId vol-12345678
```
+  For API details, see [EnableVolumeIo](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Enable-EC2VpcClassicLink`
<a name="ec2_EnableVpcClassicLink_powershell_topic"></a>

The following code example shows how to use `Enable-EC2VpcClassicLink`.

**Tools for PowerShell V4**
**Example 1: This example enables VPC vpc-0123456b789b0d12f for ClassicLink**

```
Enable-EC2VpcClassicLink -VpcId vpc-0123456b789b0d12f
```
**Output:**

```
True
```
+  For API details, see [EnableVpcClassicLink](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Enable-EC2VpcClassicLinkDnsSupport`
<a name="ec2_EnableVpcClassicLinkDnsSupport_powershell_topic"></a>

The following code example shows how to use `Enable-EC2VpcClassicLinkDnsSupport`.

**Tools for PowerShell V4**
**Example 1: This example enables vpc-0b12d3456a7e8910d to support DNS hostname resolution for ClassicLink**

```
Enable-EC2VpcClassicLinkDnsSupport -VpcId vpc-0b12d3456a7e8910d -Region eu-west-1
```
+  For API details, see [EnableVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2AccountAttribute`
<a name="ec2_DescribeAccountAttributes_powershell_topic"></a>

The following code example shows how to use `Get-EC2AccountAttribute`.

**Tools for PowerShell V4**
**Example 1: This example describes whether you can launch instances into EC2-Classic and EC2-VPC in the region, or only into EC2-VPC.**

```
(Get-EC2AccountAttribute -AttributeName supported-platforms).AttributeValues
```
**Output:**

```
AttributeValue
--------------
EC2
VPC
```
**Example 2: This example describes your default VPC, or is 'none' if you do not have a default VPC in the region.**

```
(Get-EC2AccountAttribute -AttributeName default-vpc).AttributeValues
```
**Output:**

```
AttributeValue
--------------
vpc-12345678
```
**Example 3: This example describes the maximum number of On-Demand instances that you can run.**

```
(Get-EC2AccountAttribute -AttributeName max-instances).AttributeValues
```
**Output:**

```
AttributeValue
--------------
20
```
+  For API details, see [DescribeAccountAttributes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Address`
<a name="ec2_DescribeAddresses_powershell_topic"></a>

The following code example shows how to use `Get-EC2Address`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified Elastic IP address for instances in EC2-Classic.**

```
Get-EC2Address -AllocationId eipalloc-12345678
```
**Output:**

```
AllocationId            : eipalloc-12345678
AssociationId           : eipassoc-12345678
Domain                  : vpc
InstanceId              : i-87654321
NetworkInterfaceId      : eni-12345678
NetworkInterfaceOwnerId : 12345678
PrivateIpAddress        : 10.0.2.172
PublicIp                : 198.51.100.2
```
**Example 2: This example describes your Elastic IP addresses for instances in a VPC. This syntax requires PowerShell version 3 or later.**

```
Get-EC2Address -Filter @{ Name="domain";Values="vpc" }
```
**Example 3: This example describes the specified Elastic IP address for instances in EC2-Classic.**

```
Get-EC2Address -PublicIp 203.0.113.17
```
**Output:**

```
AllocationId            :
AssociationId           :
Domain                  : standard
InstanceId              : i-12345678
NetworkInterfaceId      :
NetworkInterfaceOwnerId :
PrivateIpAddress        :
PublicIp                : 203.0.113.17
```
**Example 4: This example describes your Elastic IP addresses for instances in EC2-Classic. This syntax requires PowerShell version 3 or later.**

```
Get-EC2Address -Filter @{ Name="domain";Values="standard" }
```
**Example 5: This example describes all your Elastic IP addresses.**

```
Get-EC2Address
```
**Example 6: This example returns the public and private IP for the instance id provided in filter**

```
Get-EC2Address -Region eu-west-1 -Filter @{Name="instance-id";Values="i-0c12d3f4f567ffb89"} | Select-Object PrivateIpAddress, PublicIp
```
**Output:**

```
PrivateIpAddress PublicIp
---------------- --------
10.0.0.99        63.36.5.227
```
**Example 7: This example retrieves all the Elastic IPs with its allocation id, association id and instance ids**

```
Get-EC2Address -Region eu-west-1 | Select-Object InstanceId, AssociationId, AllocationId, PublicIp
```
**Output:**

```
InstanceId          AssociationId              AllocationId               PublicIp
----------          -------------              ------------               --------
                                               eipalloc-012e3b456789e1fad 17.212.120.178
i-0c123dfd3415bac67 eipassoc-0e123456bb7890bdb eipalloc-01cd23ebf45f7890c 17.212.124.77
                                               eipalloc-012345678eeabcfad 17.212.225.7
i-0123d405c67e89a0c eipassoc-0c123b456783966ba eipalloc-0123cdd456a8f7892 37.216.52.173
i-0f1bf2f34c5678d09 eipassoc-0e12934568a952d96 eipalloc-0e1c23e4d5e6789e4 37.218.222.278
i-012e3cb4df567e8aa eipassoc-0d1b2fa4d67d03810 eipalloc-0123f456f78a01b58 37.210.82.27
i-0123bcf4b567890e1 eipassoc-01d2345f678903fb1 eipalloc-0e1db23cfef5c45c7 37.215.222.270
```
**Example 8: This example fetches list of EC2 IP addresses matching tag key 'Category' with value 'Prod'**

```
Get-EC2Address -Filter @{Name="tag:Category";Values="Prod"}
```
**Output:**

```
AllocationId            : eipalloc-0123f456f81a01b58
AssociationId           : eipassoc-0d1b23a456d103810
CustomerOwnedIp         :
CustomerOwnedIpv4Pool   :
Domain                  : vpc
InstanceId              : i-012e3cb4df567e1aa
NetworkBorderGroup      : eu-west-1
NetworkInterfaceId      : eni-0123f41d5a60d5f40
NetworkInterfaceOwnerId : 123456789012
PrivateIpAddress        : 192.168.1.84
PublicIp                : 34.250.81.29
PublicIpv4Pool          : amazon
Tags                    : {Category, Name}
```
+  For API details, see [DescribeAddresses](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2AvailabilityZone`
<a name="ec2_DescribeAvailabilityZones_powershell_topic"></a>

The following code example shows how to use `Get-EC2AvailabilityZone`.

**Tools for PowerShell V4**
**Example 1: This example describes the Availability Zones for the current region that are available to you.**

```
Get-EC2AvailabilityZone
```
**Output:**

```
Messages    RegionName    State        ZoneName
--------    ----------    -----        --------
{}          us-west-2     available    us-west-2a
{}          us-west-2     available    us-west-2b
{}          us-west-2     available    us-west-2c
```
**Example 2: This example describes any Availability Zones that are in an impaired state. The syntax used by this example requires PowerShell version 3 or higher.**

```
Get-EC2AvailabilityZone -Filter @{ Name="state";Values="impaired" }
```
**Example 3: With PowerShell version 2, you must use New-Object to create the filter.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = "impaired"

Get-EC2AvailabilityZone -Filter $filter
```
+  For API details, see [DescribeAvailabilityZones](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2BundleTask`
<a name="ec2_DescribeBundleTasks_powershell_topic"></a>

The following code example shows how to use `Get-EC2BundleTask`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified bundle task.**

```
Get-EC2BundleTask -BundleId bun-12345678
```
**Example 2: This example describes the bundle tasks whose state is either 'complete' or 'failed'.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "complete", "failed" )

Get-EC2BundleTask -Filter $filter
```
+  For API details, see [DescribeBundleTasks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2CapacityReservation`
<a name="ec2_DescribeCapacityReservations_powershell_topic"></a>

The following code example shows how to use `Get-EC2CapacityReservation`.

**Tools for PowerShell V4**
**Example 1: This example describes one or more of your Capacity Reservations for the region**

```
Get-EC2CapacityReservation -Region eu-west-1
```
**Output:**

```
AvailabilityZone       : eu-west-1b
AvailableInstanceCount : 2
CapacityReservationId  : cr-0c1f2345db6f7cdba
CreateDate             : 3/28/2019 9:29:41 AM
EbsOptimized           : True
EndDate                : 1/1/0001 12:00:00 AM
EndDateType            : unlimited
EphemeralStorage       : False
InstanceMatchCriteria  : open
InstancePlatform       : Windows
InstanceType           : m4.xlarge
State                  : active
Tags                   : {}
Tenancy                : default
TotalInstanceCount     : 2
```
+  For API details, see [DescribeCapacityReservations](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2ConsoleOutput`
<a name="ec2_GetConsoleOutput_powershell_topic"></a>

The following code example shows how to use `Get-EC2ConsoleOutput`.

**Tools for PowerShell V4**
**Example 1: This example gets the console output for the specified Linux instance. The console output is encoded.**

```
Get-EC2ConsoleOutput -InstanceId i-0e19abcd47c123456
```
**Output:**

```
InstanceId          Output
----------          ------
i-0e194d3c47c123637 WyAgICAwLjAwMDAwMF0gQ29tbW...bGU9dHR5UzAgc2Vs
```
**Example 2: This example stores the encoded console output in a variable and then decodes it.**

```
$Output_encoded = (Get-EC2ConsoleOutput -InstanceId i-0e19abcd47c123456).Output
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($Output_encoded))
```
+  For API details, see [GetConsoleOutput](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2CustomerGateway`
<a name="ec2_DescribeCustomerGateways_powershell_topic"></a>

The following code example shows how to use `Get-EC2CustomerGateway`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified customer gateway.**

```
Get-EC2CustomerGateway -CustomerGatewayId cgw-1a2b3c4d
```
**Output:**

```
BgpAsn            : 65534
CustomerGatewayId : cgw-1a2b3c4d
IpAddress         : 203.0.113.12
State             : available
Tags              : {}
Type              : ipsec.1
```
**Example 2: This example describes any customer gateway whose state is either pending or available.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "pending", "available" )

Get-EC2CustomerGateway -Filter $filter
```
**Example 3: This example describes all your customer gateways.**

```
Get-EC2CustomerGateway
```
+  For API details, see [DescribeCustomerGateways](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2DhcpOption`
<a name="ec2_DescribeDhcpOptions_powershell_topic"></a>

The following code example shows how to use `Get-EC2DhcpOption`.

**Tools for PowerShell V4**
**Example 1: This example lists your DHCP options sets.**

```
Get-EC2DhcpOption
```
**Output:**

```
DhcpConfigurations                    DhcpOptionsId    Tag
------------------                    -------------    ---
{domain-name, domain-name-servers}    dopt-1a2b3c4d    {}
{domain-name, domain-name-servers}    dopt-2a3b4c5d    {}
{domain-name-servers}                 dopt-3a4b5c6d    {}
```
**Example 2: This example gets configuration details for the specified DHCP options set.**

```
(Get-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d).DhcpConfigurations
```
**Output:**

```
Key                    Values
---                    ------
domain-name            {abc.local}
domain-name-servers    {10.0.0.101, 10.0.0.102}
```
+  For API details, see [DescribeDhcpOptions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2FlowLog`
<a name="ec2_DescribeFlowLogs_powershell_topic"></a>

The following code example shows how to use `Get-EC2FlowLog`.

**Tools for PowerShell V4**
**Example 1: This example describes one or more flow logs with log destination type 's3'**

```
Get-EC2FlowLog -Filter @{Name="log-destination-type";Values="s3"}
```
**Output:**

```
CreationTime             : 2/25/2019 9:07:36 PM
DeliverLogsErrorMessage  :
DeliverLogsPermissionArn :
DeliverLogsStatus        : SUCCESS
FlowLogId                : fl-01b2e3d45f67f8901
FlowLogStatus            : ACTIVE
LogDestination           : arn:aws:s3:::amzn-s3-demo-bucket-dd-tata
LogDestinationType       : s3
LogGroupName             :
ResourceId               : eni-01d2dda3456b7e890
TrafficType              : ALL
```
+  For API details, see [DescribeFlowLogs](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Host`
<a name="ec2_DescribeHosts_powershell_topic"></a>

The following code example shows how to use `Get-EC2Host`.

**Tools for PowerShell V4**
**Example 1: This example returns the EC2 host details**

```
Get-EC2Host
```
**Output:**

```
AllocationTime    : 3/23/2019 4:55:22 PM
AutoPlacement     : off
AvailabilityZone  : eu-west-1b
AvailableCapacity : Amazon.EC2.Model.AvailableCapacity
ClientToken       :
HostId            : h-01e23f4cd567890f1
HostProperties    : Amazon.EC2.Model.HostProperties
HostReservationId :
Instances         : {}
ReleaseTime       : 1/1/0001 12:00:00 AM
State             : available
Tags              : {}
```
**Example 2: This example queries the AvailableInstanceCapacity for the host h-01e23f4cd567899f1**

```
Get-EC2Host -HostId h-01e23f4cd567899f1 | Select-Object -ExpandProperty AvailableCapacity | Select-Object -expand AvailableInstanceCapacity
```
**Output:**

```
AvailableCapacity InstanceType TotalCapacity
----------------- ------------ -------------
11                m4.xlarge    11
```
+  For API details, see [DescribeHosts](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2HostReservationOffering`
<a name="ec2_DescribeHostReservationOfferings_powershell_topic"></a>

The following code example shows how to use `Get-EC2HostReservationOffering`.

**Tools for PowerShell V4**
**Example 1: This example describes the Dedicated Host reservations that are available to purchase for the given filter 'instance-family' where PaymentOption is 'NoUpfront'**

```
Get-EC2HostReservationOffering -Filter @{Name="instance-family";Values="m4"} | Where-Object PaymentOption -eq NoUpfront
```
**Output:**

```
CurrencyCode   :
Duration       : 94608000
HourlyPrice    : 1.307
InstanceFamily : m4
OfferingId     : hro-0c1f234567890d9ab
PaymentOption  : NoUpfront
UpfrontPrice   : 0.000

CurrencyCode   :
Duration       : 31536000
HourlyPrice    : 1.830
InstanceFamily : m4
OfferingId     : hro-04ad12aaaf34b5a67
PaymentOption  : NoUpfront
UpfrontPrice   : 0.000
```
+  For API details, see [DescribeHostReservationOfferings](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2HostReservationPurchasePreview`
<a name="ec2_GetHostReservationPurchasePreview_powershell_topic"></a>

The following code example shows how to use `Get-EC2HostReservationPurchasePreview`.

**Tools for PowerShell V4**
**Example 1: This example previews a reservation purchase with configurations that match those of your Dedicated Host h-01e23f4cd567890f1**

```
Get-EC2HostReservationPurchasePreview -OfferingId hro-0c1f23456789d0ab -HostIdSet h-01e23f4cd567890f1
```
**Output:**

```
CurrencyCode Purchase TotalHourlyPrice TotalUpfrontPrice
------------ -------- ---------------- -----------------
             {}       1.307            0.000
```
+  For API details, see [GetHostReservationPurchasePreview](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2IdFormat`
<a name="ec2_DescribeIdFormat_powershell_topic"></a>

The following code example shows how to use `Get-EC2IdFormat`.

**Tools for PowerShell V4**
**Example 1: This example describes the ID format for the specified resource type.**

```
Get-EC2IdFormat -Resource instance
```
**Output:**

```
Resource       UseLongIds
--------       ----------
instance       False
```
**Example 2: This example describes the ID formats for all resource types that support longer IDs.**

```
Get-EC2IdFormat
```
**Output:**

```
Resource       UseLongIds
--------       ----------
reservation    False
instance       False
```
+  For API details, see [DescribeIdFormat](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2IdentityIdFormat`
<a name="ec2_DescribeIdentityIdFormat_powershell_topic"></a>

The following code example shows how to use `Get-EC2IdentityIdFormat`.

**Tools for PowerShell V4**
**Example 1: This example returns the ID format for the resouce 'image' for the role given**

```
Get-EC2IdentityIdFormat -PrincipalArn arn:aws:iam::123456789511:role/JDBC -Resource image
```
**Output:**

```
Deadline             Resource UseLongIds
--------             -------- ----------
8/2/2018 11:30:00 PM image    True
```
+  For API details, see [DescribeIdentityIdFormat](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Image`
<a name="ec2_DescribeImages_powershell_topic"></a>

The following code example shows how to use `Get-EC2Image`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified AMI.**

```
Get-EC2Image -ImageId ami-12345678
```
**Output:**

```
Architecture        : x86_64
BlockDeviceMappings : {/dev/xvda}
CreationDate        : 2014-10-20T00:56:28.000Z
Description         : My image
Hypervisor          : xen
ImageId             : ami-12345678
ImageLocation       : 123456789012/my-image
ImageOwnerAlias     :
ImageType           : machine
KernelId            :
Name                : my-image
OwnerId             : 123456789012
Platform            :
ProductCodes        : {}
Public              : False
RamdiskId           :
RootDeviceName      : /dev/xvda
RootDeviceType      : ebs
SriovNetSupport     : simple
State               : available
StateReason         :
Tags                : {Name}
VirtualizationType  : hvm
```
**Example 2: This example describes the AMIs that you own.**

```
Get-EC2Image -owner self
```
**Example 3: This example describes the public AMIs that run Microsoft Windows Server.**

```
Get-EC2Image -Filter @{ Name="platform"; Values="windows" }
```
**Example 4: This example describes all public AMIs in the 'us-west-2' region.**

```
Get-EC2Image -Region us-west-2
```
+  For API details, see [DescribeImages](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2ImageAttribute`
<a name="ec2_DescribeImageAttribute_powershell_topic"></a>

The following code example shows how to use `Get-EC2ImageAttribute`.

**Tools for PowerShell V4**
**Example 1: This example gets the description for the specified AMI.**

```
Get-EC2ImageAttribute -ImageId ami-12345678 -Attribute description
```
**Output:**

```
BlockDeviceMappings : {}
Description         : My image description
ImageId             : ami-12345678
KernelId            :
LaunchPermissions   : {}
ProductCodes        : {}
RamdiskId           :
SriovNetSupport     :
```
**Example 2: This example gets the launch permissions for the specified AMI.**

```
Get-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission
```
**Output:**

```
BlockDeviceMappings : {}
Description         :
ImageId             : ami-12345678
KernelId            :
LaunchPermissions   : {all}
ProductCodes        : {}
RamdiskId           :
SriovNetSupport     :
```
**Example 3: This example test whether enhanced networking is enabled.**

```
Get-EC2ImageAttribute -ImageId ami-12345678 -Attribute sriovNetSupport
```
**Output:**

```
BlockDeviceMappings : {}
Description         :
ImageId             : ami-12345678
KernelId            :
LaunchPermissions   : {}
ProductCodes        : {}
RamdiskId           :
SriovNetSupport     : simple
```
+  For API details, see [DescribeImageAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2ImageByName`
<a name="ec2_Get-EC2ImageByName_powershell_topic"></a>

The following code example shows how to use `Get-EC2ImageByName`.

**Tools for PowerShell V4**
**Example 1: This example describes the complete set of filter names that are currently supported.**

```
Get-EC2ImageByName
```
**Output:**

```
WINDOWS_2016_BASE
WINDOWS_2016_NANO
WINDOWS_2016_CORE
WINDOWS_2016_CONTAINER
WINDOWS_2016_SQL_SERVER_ENTERPRISE_2016
WINDOWS_2016_SQL_SERVER_STANDARD_2016
WINDOWS_2016_SQL_SERVER_WEB_2016
WINDOWS_2016_SQL_SERVER_EXPRESS_2016
WINDOWS_2012R2_BASE
WINDOWS_2012R2_CORE
WINDOWS_2012R2_SQL_SERVER_EXPRESS_2016
WINDOWS_2012R2_SQL_SERVER_STANDARD_2016
WINDOWS_2012R2_SQL_SERVER_WEB_2016
WINDOWS_2012R2_SQL_SERVER_EXPRESS_2014
WINDOWS_2012R2_SQL_SERVER_STANDARD_2014
WINDOWS_2012R2_SQL_SERVER_WEB_2014
WINDOWS_2012_BASE
WINDOWS_2012_SQL_SERVER_EXPRESS_2014
WINDOWS_2012_SQL_SERVER_STANDARD_2014
WINDOWS_2012_SQL_SERVER_WEB_2014
WINDOWS_2012_SQL_SERVER_EXPRESS_2012
WINDOWS_2012_SQL_SERVER_STANDARD_2012
WINDOWS_2012_SQL_SERVER_WEB_2012
WINDOWS_2012_SQL_SERVER_EXPRESS_2008
WINDOWS_2012_SQL_SERVER_STANDARD_2008
WINDOWS_2012_SQL_SERVER_WEB_2008
WINDOWS_2008R2_BASE
WINDOWS_2008R2_SQL_SERVER_EXPRESS_2012
WINDOWS_2008R2_SQL_SERVER_STANDARD_2012
WINDOWS_2008R2_SQL_SERVER_WEB_2012
WINDOWS_2008R2_SQL_SERVER_EXPRESS_2008
WINDOWS_2008R2_SQL_SERVER_STANDARD_2008
WINDOWS_2008R2_SQL_SERVER_WEB_2008
WINDOWS_2008RTM_BASE
WINDOWS_2008RTM_SQL_SERVER_EXPRESS_2008
WINDOWS_2008RTM_SQL_SERVER_STANDARD_2008
WINDOWS_2008_BEANSTALK_IIS75
WINDOWS_2012_BEANSTALK_IIS8
VPC_NAT
```
**Example 2: This example describes the specified AMI. Using this command to locate an AMI is helpful because AWS releases new Windows AMIs with the latest updates each month. You can specify the 'ImageId' to New-EC2Instance to launch an instance using the current AMI for the specified filter.**

```
Get-EC2ImageByName -Names WINDOWS_2016_BASE
```
**Output:**

```
Architecture        : x86_64
BlockDeviceMappings : {/dev/sda1, xvdca, xvdcb, xvdcc...}
CreationDate        : yyyy.mm.ddThh:mm:ss.000Z
Description         : Microsoft Windows Server 2016 with Desktop Experience Locale English AMI provided by Amazon
Hypervisor          : xen
ImageId             : ami-xxxxxxxx
ImageLocation       : amazon/Windows_Server-2016-English-Full-Base-yyyy.mm.dd
ImageOwnerAlias     : amazon
ImageType           : machine
KernelId            :
Name                : Windows_Server-2016-English-Full-Base-yyyy.mm.dd
OwnerId             : 801119661308
Platform            : Windows
ProductCodes        : {}
Public              : True
RamdiskId           :
RootDeviceName      : /dev/sda1
RootDeviceType      : ebs
SriovNetSupport     : simple
State               : available
StateReason         :
Tags                : {}
VirtualizationType  : hvm
```
+  For API details, see [Get-EC2ImageByName](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2ImportImageTask`
<a name="ec2_DescribeImportImageTasks_powershell_topic"></a>

The following code example shows how to use `Get-EC2ImportImageTask`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified image import task.**

```
Get-EC2ImportImageTask -ImportTaskId import-ami-hgfedcba
```
**Output:**

```
Architecture    : x86_64
Description     : Windows Image 2
Hypervisor      :
ImageId         : ami-1a2b3c4d
ImportTaskId    : import-ami-hgfedcba
LicenseType     : AWS
Platform        : Windows
Progress        :
SnapshotDetails : {/dev/sda1}
Status          : completed
StatusMessage   :
```
**Example 2: This example describes all your image import tasks.**

```
Get-EC2ImportImageTask
```
**Output:**

```
Architecture    :
Description     : Windows Image 1
Hypervisor      :
ImageId         :
ImportTaskId    : import-ami-abcdefgh
LicenseType     : AWS
Platform        : Windows
Progress        :
SnapshotDetails : {}
Status          : deleted
StatusMessage   : User initiated task cancelation

Architecture    : x86_64
Description     : Windows Image 2
Hypervisor      :
ImageId         : ami-1a2b3c4d
ImportTaskId    : import-ami-hgfedcba
LicenseType     : AWS
Platform        : Windows
Progress        :
SnapshotDetails : {/dev/sda1}
Status          : completed
StatusMessage   :
```
+  For API details, see [DescribeImportImageTasks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2ImportSnapshotTask`
<a name="ec2_DescribeImportSnapshotTasks_powershell_topic"></a>

The following code example shows how to use `Get-EC2ImportSnapshotTask`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified snapshot import task.**

```
Get-EC2ImportSnapshotTask -ImportTaskId import-snap-abcdefgh
```
**Output:**

```
Description             ImportTaskId               SnapshotTaskDetail
-----------------       --------------------       ------------------
Disk Image Import 1     import-snap-abcdefgh       Amazon.EC2.Model.SnapshotTaskDetail
```
**Example 2: This example describes all your snapshot import tasks.**

```
Get-EC2ImportSnapshotTask
```
**Output:**

```
Description             ImportTaskId               SnapshotTaskDetail
-----------------       --------------------       ------------------
Disk Image Import 1     import-snap-abcdefgh       Amazon.EC2.Model.SnapshotTaskDetail
Disk Image Import 2     import-snap-hgfedcba       Amazon.EC2.Model.SnapshotTaskDetail
```
+  For API details, see [DescribeImportSnapshotTasks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Instance`
<a name="ec2_DescribeInstances_powershell_topic"></a>

The following code example shows how to use `Get-EC2Instance`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified instance.**

```
(Get-EC2Instance -InstanceId i-12345678).Instances
```
**Output:**

```
AmiLaunchIndex        : 0
Architecture          : x86_64
BlockDeviceMappings   : {/dev/sda1}
ClientToken           : TleEy1448154045270
EbsOptimized          : False
Hypervisor            : xen
IamInstanceProfile    : Amazon.EC2.Model.IamInstanceProfile
ImageId               : ami-12345678
InstanceId            : i-12345678
InstanceLifecycle     :
InstanceType          : t2.micro
KernelId              :
KeyName               : my-key-pair
LaunchTime            : 12/4/2015 4:44:40 PM
Monitoring            : Amazon.EC2.Model.Monitoring
NetworkInterfaces     : {ip-10-0-2-172.us-west-2.compute.internal}
Placement             : Amazon.EC2.Model.Placement
Platform              : Windows
PrivateDnsName        : ip-10-0-2-172.us-west-2.compute.internal
PrivateIpAddress      : 10.0.2.172
ProductCodes          : {}
PublicDnsName         :
PublicIpAddress       :
RamdiskId             :
RootDeviceName        : /dev/sda1
RootDeviceType        : ebs
SecurityGroups        : {default}
SourceDestCheck       : True
SpotInstanceRequestId :
SriovNetSupport       :
State                 : Amazon.EC2.Model.InstanceState
StateReason           :
StateTransitionReason :
SubnetId              : subnet-12345678
Tags                  : {Name}
VirtualizationType    : hvm
VpcId                 : vpc-12345678
```
**Example 2: This example describes all your instances in the current region, grouped by reservation. To see the instance details expand the Instances collection within each reservation object.**

```
Get-EC2Instance
```
**Output:**

```
GroupNames    : {}
Groups        : {}
Instances     : {}
OwnerId       : 123456789012
RequesterId   : 226008221399
ReservationId : r-c5df370c

GroupNames    : {}
Groups        : {}
Instances     : {}
OwnerId       : 123456789012
RequesterId   : 854251627541
ReservationId : r-63e65bab
...
```
**Example 3: This example illustrates using a filter to query for EC2 instances in a specific subnet of a VPC.**

```
(Get-EC2Instance -Filter @{Name="vpc-id";Values="vpc-1a2bc34d"},@{Name="subnet-id";Values="subnet-1a2b3c4d"}).Instances
```
**Output:**

```
InstanceId          InstanceType Platform PrivateIpAddress PublicIpAddress SecurityGroups SubnetId        VpcId
----------          ------------ -------- ---------------- --------------- -------------- --------        -----
i-01af...82cf180e19 t2.medium    Windows  10.0.0.98                        ...            subnet-1a2b3c4d vpc-1a2b3c4d
i-0374...7e9d5b0c45 t2.xlarge    Windows  10.0.0.53                        ...            subnet-1a2b3c4d vpc-1a2b3c4d
```
**Example 4: This example illustrates using a filter with multiple values to query for EC2 instances that are both running and stopped**

```
$InstanceParams = @{
    Filter = @(
        @{'Name' = 'instance-state-name';'Values' = @("running","stopped")}
    )
}

(Get-EC2Instance @InstanceParams).Instances
```
**Output:**

```
InstanceId          InstanceType Platform PrivateIpAddress PublicIpAddress SecurityGroups SubnetId        VpcId
----------          ------------ -------- ---------------- --------------- -------------- --------        -----
i-05a9...f6c5f46e18 t3.medium             10.0.1.7                         ...            subnet-1a2b3c4d vpc-1a2b3c4d
i-02cf...945c4fdd07 t3.medium    Windows  10.0.1.8                         ...            subnet-1a2b3c4d vpc-1a2b3c4d
i-0ac0...c037f9f3a1 t3.xlarge    Windows  10.0.1.10                        ...            subnet-1a2b3c4d vpc-1a2b3c4d
i-066b...57b7b08888 t3.medium    Windows  10.0.1.11                        ...            subnet-1a2b3c4d vpc-1a2b3c4d
i-0fee...82e83ccd72 t3.medium    Windows  10.0.1.5                         ...            subnet-1a2b3c4d vpc-1a2b3c4d
i-0a68...274cc5043b t3.medium    Windows  10.0.1.6                         ...            subnet-1a2b3c4d vpc-1a2b3c4d
```
**Example 5: This example illustrates using a filter with multiple values to query for EC2 instances that are both running and stopped and using the Select-Object cmdlet for choosing specific values to output.**

```
$InstanceParams = @{
    Filter = @(
        @{'Name' = 'instance-state-name';'Values' = @("running","stopped")}
    )
}

$SelectParams = @{
    Property = @(
        "InstanceID", "InstanceType", "Platform", "PrivateIpAddress",
        @{Name="Name";Expression={$_.Tags[$_.Tags.Key.IndexOf("Name")].Value}},
        @{Name="State";Expression={$_.State.Name}}
    )
}

$result = Get-EC2Instance @InstanceParams
$result.Instances | Select-Object @SelectParams | Format-Table -AutoSize
```
**Output:**

```
InstanceId          InstanceType Platform PrivateIpAddress Name         State
----------          ------------ -------- ---------------- ----         -----
i-05a9...f6c5f46e18 t3.medium             10.0.1.7         ec2-name-01  running
i-02cf...945c4fdd07 t3.medium    Windows  10.0.1.8         ec2-name-02  stopped
i-0ac0...c037f9f3a1 t3.xlarge    Windows  10.0.1.10        ec2-name-03  running
i-066b...57b7b08888 t3.medium    Windows  10.0.1.11        ec2-name-04  stopped
i-0fee...82e83ccd72 t3.medium    Windows  10.0.1.5         ec2-name-05  running
i-0a68...274cc5043b t3.medium    Windows  10.0.1.6         ec2-name-06  stopped
```
+  For API details, see [DescribeInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2InstanceAttribute`
<a name="ec2_DescribeInstanceAttribute_powershell_topic"></a>

The following code example shows how to use `Get-EC2InstanceAttribute`.

**Tools for PowerShell V4**
**Example 1: This example describes the instance type of the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceType
```
**Output:**

```
InstanceType                      : t2.micro
```
**Example 2: This example describes whether enhanced networking is enabled for the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sriovNetSupport
```
**Output:**

```
SriovNetSupport                   : simple
```
**Example 3: This example describes the security groups for the specified instance.**

```
(Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute groupSet).Groups
```
**Output:**

```
GroupId
-------
sg-12345678
sg-45678901
```
**Example 4: This example describes whether EBS optimization is enabled for the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute ebsOptimized
```
**Output:**

```
EbsOptimized                      : False
```
**Example 5: This example describes the 'disableApiTermination' attribute of the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute disableApiTermination
```
**Output:**

```
DisableApiTermination             : False
```
**Example 6: This example describes the 'instanceInitiatedShutdownBehavior' attribute of the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceInitiatedShutdownBehavior
```
**Output:**

```
InstanceInitiatedShutdownBehavior : stop
```
+  For API details, see [DescribeInstanceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2InstanceMetadata`
<a name="ec2_Get-EC2InstanceMetadata_powershell_topic"></a>

The following code example shows how to use `Get-EC2InstanceMetadata`.

**Tools for PowerShell V4**
**Example 1: Lists the available categories of instance metadata that can be queried.**

```
Get-EC2InstanceMetadata -ListCategory
```
**Output:**

```
AmiId
LaunchIndex
ManifestPath
AncestorAmiId
BlockDeviceMapping
InstanceId
InstanceType
LocalHostname
LocalIpv4
KernelId
AvailabilityZone
ProductCode
PublicHostname
PublicIpv4
PublicKey
RamdiskId
Region
ReservationId
SecurityGroup
UserData
InstanceMonitoring
IdentityDocument
IdentitySignature
IdentityPkcs7
```
**Example 2: Returns the id of the Amazon Machine Image (AMI) that was used to launch the instance.**

```
Get-EC2InstanceMetadata -Category AmiId
```
**Output:**

```
ami-b2e756ca
```
**Example 3: This example queries the JSON-formatted identity document for the instance.**

```
Get-EC2InstanceMetadata -Category IdentityDocument
{
  "availabilityZone" : "us-west-2a",
  "devpayProductCodes" : null,
  "marketplaceProductCodes" : null,
  "version" : "2017-09-30",
  "instanceId" : "i-01ed50f7e2607f09e",
  "billingProducts" : [ "bp-6ba54002" ],
  "instanceType" : "t2.small",
  "pendingTime" : "2018-03-07T16:26:04Z",
  "imageId" : "ami-b2e756ca",
  "privateIp" : "10.0.0.171",
  "accountId" : "111122223333",
  "architecture" : "x86_64",
  "kernelId" : null,
  "ramdiskId" : null,
  "region" : "us-west-2"
}
```
**Example 4: This example uses a path query to obtain the network interface macs for the instance.**

```
Get-EC2InstanceMetadata -Path "/network/interfaces/macs"
```
**Output:**

```
02:80:7f:ef:4c:e0/
```
**Example 5: If there is an IAM role associated with the instance, returns information about the last time the instance profile was updated, including the instance's LastUpdated date, InstanceProfileArn, and InstanceProfileId.**

```
Get-EC2InstanceMetadata -Path "/iam/info"
```
**Output:**

```
{
  "Code" : "Success",
  "LastUpdated" : "2018-03-08T03:38:40Z",
  "InstanceProfileArn" : "arn:aws:iam::111122223333:instance-profile/MyLaunchRole_Profile",
  "InstanceProfileId" : "AIPAI4...WVK2RW"
}
```
+  For API details, see [Get-EC2InstanceMetadata](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2InstanceStatus`
<a name="ec2_DescribeInstanceStatus_powershell_topic"></a>

The following code example shows how to use `Get-EC2InstanceStatus`.

**Tools for PowerShell V4**
**Example 1: This example describes the status of the specified instance.**

```
Get-EC2InstanceStatus -InstanceId i-12345678
```
**Output:**

```
AvailabilityZone : us-west-2a
Events           : {}
InstanceId       : i-12345678
InstanceState    : Amazon.EC2.Model.InstanceState
Status           : Amazon.EC2.Model.InstanceStatusSummary
SystemStatus     : Amazon.EC2.Model.InstanceStatusSummary
```

```
$status = Get-EC2InstanceStatus -InstanceId i-12345678
$status.InstanceState
```
**Output:**

```
Code    Name
----    ----
16      running
```

```
$status.Status
```
**Output:**

```
Details           Status
-------           ------
{reachability}    ok
```

```
$status.SystemStatus
```
**Output:**

```
Details           Status
-------           ------
{reachability}    ok
```
+  For API details, see [DescribeInstanceStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2InternetGateway`
<a name="ec2_DescribeInternetGateways_powershell_topic"></a>

The following code example shows how to use `Get-EC2InternetGateway`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified Internet gateway.**

```
Get-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d
```
**Output:**

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
```
**Example 2: This example describes all your Internet gateways.**

```
Get-EC2InternetGateway
```
**Output:**

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
{}                igw-2a3b4c5d          {}
```
+  For API details, see [DescribeInternetGateways](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2KeyPair`
<a name="ec2_DescribeKeyPairs_powershell_topic"></a>

The following code example shows how to use `Get-EC2KeyPair`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified key pair.**

```
Get-EC2KeyPair -KeyName my-key-pair
```
**Output:**

```
KeyFingerprint                                              KeyName
--------------                                              -------
1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f my-key-pair
```
**Example 2: This example describes all your key pairs.**

```
Get-EC2KeyPair
```
+  For API details, see [DescribeKeyPairs](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2NetworkAcl`
<a name="ec2_DescribeNetworkAcls_powershell_topic"></a>

The following code example shows how to use `Get-EC2NetworkAcl`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified network ACL.**

```
Get-EC2NetworkAcl -NetworkAclId acl-12345678
```
**Output:**

```
Associations : {aclassoc-1a2b3c4d}
Entries      : {Amazon.EC2.Model.NetworkAclEntry, Amazon.EC2.Model.NetworkAclEntry}
IsDefault    : False
NetworkAclId : acl-12345678
Tags         : {Name}
VpcId        : vpc-12345678
```
**Example 2: This example describes the rules for the specified network ACL.**

```
(Get-EC2NetworkAcl -NetworkAclId acl-12345678).Entries
```
**Output:**

```
CidrBlock    : 0.0.0.0/0
Egress       : True
IcmpTypeCode :
PortRange    :
Protocol     : -1
RuleAction   : deny
RuleNumber   : 32767

CidrBlock    : 0.0.0.0/0
Egress       : False
IcmpTypeCode :
PortRange    :
Protocol     : -1
RuleAction   : deny
RuleNumber   : 32767
```
**Example 3: This example describes all your network ACLs.**

```
Get-EC2NetworkAcl
```
+  For API details, see [DescribeNetworkAcls](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2NetworkInterface`
<a name="ec2_DescribeNetworkInterfaces_powershell_topic"></a>

The following code example shows how to use `Get-EC2NetworkInterface`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified network interface.**

```
Get-EC2NetworkInterface -NetworkInterfaceId eni-12345678
```
**Output:**

```
Association        :
Attachment         : Amazon.EC2.Model.NetworkInterfaceAttachment
AvailabilityZone   : us-west-2c
Description        :
Groups             : {my-security-group}
MacAddress         : 0a:e9:a6:19:4c:7f
NetworkInterfaceId : eni-12345678
OwnerId            : 123456789012
PrivateDnsName     : ip-10-0-0-107.us-west-2.compute.internal
PrivateIpAddress   : 10.0.0.107
PrivateIpAddresses : {ip-10-0-0-107.us-west-2.compute.internal}
RequesterId        :
RequesterManaged   : False
SourceDestCheck    : True
Status             : in-use
SubnetId           : subnet-1a2b3c4d
TagSet             : {}
VpcId              : vpc-12345678
```
**Example 2: This example describes all your network interfaces.**

```
Get-EC2NetworkInterface
```
+  For API details, see [DescribeNetworkInterfaces](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2NetworkInterfaceAttribute`
<a name="ec2_DescribeNetworkInterfaceAttribute_powershell_topic"></a>

The following code example shows how to use `Get-EC2NetworkInterfaceAttribute`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute Attachment
```
**Output:**

```
Attachment         : Amazon.EC2.Model.NetworkInterfaceAttachment
```
**Example 2: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute Description
```
**Output:**

```
Description        : My description
```
**Example 3: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute GroupSet
```
**Output:**

```
Groups             : {my-security-group}
```
**Example 4: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute SourceDestCheck
```
**Output:**

```
SourceDestCheck    : True
```
+  For API details, see [DescribeNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2PasswordData`
<a name="ec2_GetPasswordData_powershell_topic"></a>

The following code example shows how to use `Get-EC2PasswordData`.

**Tools for PowerShell V4**
**Example 1: This example decrypts the password that Amazon EC2 assigned to the Administrator account for the specified Windows instance. As a pem file was specified, the setting of the -Decrypt switch is automatically assumed.**

```
Get-EC2PasswordData -InstanceId i-12345678 -PemFile C:\path\my-key-pair.pem
```
**Output:**

```
mYZ(PA9?C)Q
```
**Example 2: (Windows PowerShell only) Inspects the instance to determine the name of the keypair used to launch the instance and then attempts to find the corresponding keypair data in the configuration store of the AWS Toolkit for Visual Studio. If the keypair data is found the password is decrypted.**

```
Get-EC2PasswordData -InstanceId i-12345678 -Decrypt
```
**Output:**

```
mYZ(PA9?C)Q
```
**Example 3: Returns the encrypted password data for the instance.**

```
Get-EC2PasswordData -InstanceId i-12345678
```
**Output:**

```
iVz3BAK/WAXV.....dqt8WeMA==
```
+  For API details, see [GetPasswordData](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2PlacementGroup`
<a name="ec2_DescribePlacementGroups_powershell_topic"></a>

The following code example shows how to use `Get-EC2PlacementGroup`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified placement group.**

```
Get-EC2PlacementGroup -GroupName my-placement-group
```
**Output:**

```
GroupName             State        Strategy
---------             -----        --------
my-placement-group    available    cluster
```
+  For API details, see [DescribePlacementGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2PrefixList`
<a name="ec2_DescribePrefixLists_powershell_topic"></a>

The following code example shows how to use `Get-EC2PrefixList`.

**Tools for PowerShell V4**
**Example 1: This example fetches the available AWS services in a prefix list format for the region**

```
Get-EC2PrefixList
```
**Output:**

```
Cidrs                                          PrefixListId PrefixListName
-----                                          ------------ --------------
{52.94.5.0/24, 52.119.240.0/21, 52.94.24.0/23} pl-6fa54006  com.amazonaws.eu-west-1.dynamodb
{52.218.0.0/17, 54.231.128.0/19}               pl-6da54004  com.amazonaws.eu-west-1.s3
```
+  For API details, see [DescribePrefixLists](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Region`
<a name="ec2_DescribeRegions_powershell_topic"></a>

The following code example shows how to use `Get-EC2Region`.

**Tools for PowerShell V4**
**Example 1: This example describes the regions that are available to you.**

```
Get-EC2Region
```
**Output:**

```
Endpoint                            RegionName
--------                            ----------
ec2.eu-west-1.amazonaws.com         eu-west-1
ec2.ap-southeast-1.amazonaws.com    ap-southeast-1
ec2.ap-southeast-2.amazonaws.com    ap-southeast-2
ec2.eu-central-1.amazonaws.com      eu-central-1
ec2.ap-northeast-1.amazonaws.com    ap-northeast-1
ec2.us-east-1.amazonaws.com         us-east-1
ec2.sa-east-1.amazonaws.com         sa-east-1
ec2.us-west-1.amazonaws.com         us-west-1
ec2.us-west-2.amazonaws.com         us-west-2
```
+  For API details, see [DescribeRegions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2RouteTable`
<a name="ec2_DescribeRouteTables_powershell_topic"></a>

The following code example shows how to use `Get-EC2RouteTable`.

**Tools for PowerShell V4**
**Example 1: This example describes all your route tables.**

```
Get-EC2RouteTable
```
**Output:**

```
DestinationCidrBlock    : 10.0.0.0/16
DestinationPrefixListId :
GatewayId               : local
InstanceId              :
InstanceOwnerId         :
NetworkInterfaceId      :
Origin                  : CreateRouteTable
State                   : active
VpcPeeringConnectionId  :

DestinationCidrBlock    : 0.0.0.0/0
DestinationPrefixListId :
GatewayId               : igw-1a2b3c4d
InstanceId              :
InstanceOwnerId         :
NetworkInterfaceId      :
Origin                  : CreateRoute
State                   : active
VpcPeeringConnectionId  :
```
**Example 2: This example returns details for the specified route table.**

```
Get-EC2RouteTable -RouteTableId rtb-1a2b3c4d
```
**Example 3: This example describes the route tables for the specified VPC.**

```
Get-EC2RouteTable -Filter @{ Name="vpc-id"; Values="vpc-1a2b3c4d" }
```
**Output:**

```
Associations    : {rtbassoc-12345678}
PropagatingVgws : {}
Routes          : {, }
RouteTableId    : rtb-1a2b3c4d
Tags            : {}
VpcId           : vpc-1a2b3c4d
```
+  For API details, see [DescribeRouteTables](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2ScheduledInstance`
<a name="ec2_DescribeScheduledInstances_powershell_topic"></a>

The following code example shows how to use `Get-EC2ScheduledInstance`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified Scheduled Instance.**

```
Get-EC2ScheduledInstance -ScheduledInstanceId sci-1234-1234-1234-1234-123456789012
```
**Output:**

```
AvailabilityZone            : us-west-2b
CreateDate                  : 1/25/2016 1:43:38 PM
HourlyPrice                 : 0.095
InstanceCount               : 1
InstanceType                : c4.large
NetworkPlatform             : EC2-VPC
NextSlotStartTime           : 1/31/2016 1:00:00 AM
Platform                    : Linux/UNIX
PreviousSlotEndTime         :
Recurrence                  : Amazon.EC2.Model.ScheduledInstanceRecurrence
ScheduledInstanceId         : sci-1234-1234-1234-1234-123456789012
SlotDurationInHours         : 32
TermEndDate                 : 1/31/2017 1:00:00 AM
TermStartDate               : 1/31/2016 1:00:00 AM
TotalScheduledInstanceHours : 1696
```
**Example 2: This example describes all your Scheduled Instances.**

```
Get-EC2ScheduledInstance
```
+  For API details, see [DescribeScheduledInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2ScheduledInstanceAvailability`
<a name="ec2_DescribeScheduledInstanceAvailability_powershell_topic"></a>

The following code example shows how to use `Get-EC2ScheduledInstanceAvailability`.

**Tools for PowerShell V4**
**Example 1: This example describes a schedule that occurs every week on Sunday, starting on the specified date.**

```
Get-EC2ScheduledInstanceAvailability -Recurrence_Frequency Weekly -Recurrence_Interval 1 -Recurrence_OccurrenceDay 1 -FirstSlotStartTimeRange_EarliestTime 2016-01-31T00:00:00Z -FirstSlotStartTimeRange_LatestTime 2016-01-31T04:00:00Z
```
**Output:**

```
AvailabilityZone            : us-west-2b
AvailableInstanceCount      : 20
FirstSlotStartTime          : 1/31/2016 8:00:00 AM
HourlyPrice                 : 0.095
InstanceType                : c4.large
MaxTermDurationInDays       : 366
MinTermDurationInDays       : 366
NetworkPlatform             : EC2-VPC
Platform                    : Linux/UNIX
PurchaseToken               : eyJ2IjoiMSIsInMiOjEsImMiOi...
Recurrence                  : Amazon.EC2.Model.ScheduledInstanceRecurrence
SlotDurationInHours         : 23
TotalScheduledInstanceHours : 1219

...
```
**Example 2: To narrow the results, you can add filters for criteria such as operating system, network, and instance type.**

```
-Filter @{ Name="platform";Values="Linux/UNIX" },@{ Name="network-platform";Values="EC2-VPC" },@{ Name="instance-type";Values="c4.large" }
```
+  For API details, see [DescribeScheduledInstanceAvailability](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2SecurityGroup`
<a name="ec2_DescribeSecurityGroups_powershell_topic"></a>

The following code example shows how to use `Get-EC2SecurityGroup`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified security group for a VPC. When working with security groups belonging to a VPC you must use the security group ID (-GroupId parameter), not name (-GroupName parameter), to reference the group.**

```
Get-EC2SecurityGroup -GroupId sg-12345678
```
**Output:**

```
Description         : default VPC security group
GroupId             : sg-12345678
GroupName           : default
IpPermissions       : {Amazon.EC2.Model.IpPermission}
IpPermissionsEgress : {Amazon.EC2.Model.IpPermission}
OwnerId             : 123456789012
Tags                : {}
VpcId               : vpc-12345678
```
**Example 2: This example describes the specified security group for EC2-Classic. When working with security groups for EC2-Classic you may use either the group name (-GroupName parameter) or group ID (-GroupId parameter) to reference the security group.**

```
Get-EC2SecurityGroup -GroupName my-security-group
```
**Output:**

```
Description         : my security group
GroupId             : sg-45678901
GroupName           : my-security-group
IpPermissions       : {Amazon.EC2.Model.IpPermission, Amazon.EC2.Model.IpPermission}
IpPermissionsEgress : {}
OwnerId             : 123456789012
Tags                : {}
VpcId               :
```
**Example 3: This example retrieves all the security groups for the vpc-0fc1ff23456b789eb**

```
Get-EC2SecurityGroup -Filter @{Name="vpc-id";Values="vpc-0fc1ff23456b789eb"}
```
+  For API details, see [DescribeSecurityGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Snapshot`
<a name="ec2_DescribeSnapshots_powershell_topic"></a>

The following code example shows how to use `Get-EC2Snapshot`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified snapshot.**

```
Get-EC2Snapshot -SnapshotId snap-12345678
```
**Output:**

```
DataEncryptionKeyId :
Description         : Created by CreateImage(i-1a2b3c4d) for ami-12345678 from vol-12345678
Encrypted           : False
KmsKeyId            :
OwnerAlias          :
OwnerId             : 123456789012
Progress            : 100%
SnapshotId          : snap-12345678
StartTime           : 10/23/2014 6:01:28 AM
State               : completed
StateMessage        :
Tags                : {}
VolumeId            : vol-12345678
VolumeSize          : 8
```
**Example 2: This example describes the snapshots that have a 'Name' tag.**

```
Get-EC2Snapshot | ? { $_.Tags.Count -gt 0 -and $_.Tags.Key -eq "Name" }
```
**Example 3: This example describes the snapshots that have a 'Name' tag with the value 'TestValue'.**

```
Get-EC2Snapshot | ? { $_.Tags.Count -gt 0 -and $_.Tags.Key -eq "Name" -and $_.Tags.Value -eq "TestValue" }
```
**Example 4: This example describes all your snapshots.**

```
Get-EC2Snapshot -Owner self
```
+  For API details, see [DescribeSnapshots](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2SnapshotAttribute`
<a name="ec2_DescribeSnapshotAttribute_powershell_topic"></a>

The following code example shows how to use `Get-EC2SnapshotAttribute`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified attribute of the specified snapshot.**

```
Get-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute ProductCodes
```
**Output:**

```
CreateVolumePermissions    ProductCodes    SnapshotId
-----------------------    ------------    ----------
{}                         {}              snap-12345678
```
**Example 2: This example describes the specified attribute of the specified snapshot.**

```
(Get-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission).CreateVolumePermissions
```
**Output:**

```
Group    UserId
-----    ------
all
```
+  For API details, see [DescribeSnapshotAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2SpotDatafeedSubscription`
<a name="ec2_DescribeSpotDatafeedSubscription_powershell_topic"></a>

The following code example shows how to use `Get-EC2SpotDatafeedSubscription`.

**Tools for PowerShell V4**
**Example 1: This example describes your Spot instance data feed.**

```
Get-EC2SpotDatafeedSubscription
```
**Output:**

```
Bucket  : amzn-s3-demo-bucket
Fault   :
OwnerId : 123456789012
Prefix  : spotdata
State   : Active
```
+  For API details, see [DescribeSpotDatafeedSubscription](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2SpotFleetInstance`
<a name="ec2_DescribeSpotFleetInstances_powershell_topic"></a>

The following code example shows how to use `Get-EC2SpotFleetInstance`.

**Tools for PowerShell V4**
**Example 1: This example describes the instances associated with the specified Spot fleet request.**

```
Get-EC2SpotFleetInstance -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE
```
**Output:**

```
InstanceId    InstanceType    SpotInstanceRequestId
----------    ------------    ---------------------
i-f089262a    c3.large        sir-12345678
i-7e8b24a4    c3.large        sir-87654321
```
+  For API details, see [DescribeSpotFleetInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2SpotFleetRequest`
<a name="ec2_DescribeSpotFleetRequests_powershell_topic"></a>

The following code example shows how to use `Get-EC2SpotFleetRequest`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified Spot fleet request.**

```
Get-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE | format-list
```
**Output:**

```
ConfigData            : Amazon.EC2.Model.SpotFleetRequestConfigData
CreateTime            : 12/26/2015 8:23:33 AM
SpotFleetRequestId    : sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE
SpotFleetRequestState : active
```
**Example 2: This example describes all your Spot fleet requests.**

```
Get-EC2SpotFleetRequest
```
+  For API details, see [DescribeSpotFleetRequests](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2SpotFleetRequestHistory`
<a name="ec2_DescribeSpotFleetRequestHistory_powershell_topic"></a>

The following code example shows how to use `Get-EC2SpotFleetRequestHistory`.

**Tools for PowerShell V4**
**Example 1: This example describes the history of the specified Spot fleet request.**

```
Get-EC2SpotFleetRequestHistory -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -StartTime 2015-12-26T00:00:00Z
```
**Output:**

```
HistoryRecords     : {Amazon.EC2.Model.HistoryRecord, Amazon.EC2.Model.HistoryRecord...}
LastEvaluatedTime  : 12/26/2015 8:29:11 AM
NextToken          :
SpotFleetRequestId : sfr-088bc5f1-7e7b-451a-bd13-757f10672b93
StartTime          : 12/25/2015 8:00:00 AM
```

```
(Get-EC2SpotFleetRequestHistory -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -StartTime 2015-12-26T00:00:00Z).HistoryRecords
```
**Output:**

```
EventInformation                     EventType             Timestamp
----------------                     ---------             ---------
Amazon.EC2.Model.EventInformation    fleetRequestChange    12/26/2015 8:23:33 AM
Amazon.EC2.Model.EventInformation    fleetRequestChange    12/26/2015 8:23:33 AM
Amazon.EC2.Model.EventInformation    fleetRequestChange    12/26/2015 8:23:33 AM
Amazon.EC2.Model.EventInformation    launched              12/26/2015 8:25:34 AM
Amazon.EC2.Model.EventInformation    launched              12/26/2015 8:25:05 AM
```
+  For API details, see [DescribeSpotFleetRequestHistory](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2SpotInstanceRequest`
<a name="ec2_DescribeSpotInstanceRequests_powershell_topic"></a>

The following code example shows how to use `Get-EC2SpotInstanceRequest`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified Spot instance request.**

```
Get-EC2SpotInstanceRequest -SpotInstanceRequestId sir-12345678
```
**Output:**

```
ActualBlockHourlyPrice   :
AvailabilityZoneGroup    :
BlockDurationMinutes     : 0
CreateTime               : 4/8/2015 2:51:33 PM
Fault                    :
InstanceId               : i-12345678
LaunchedAvailabilityZone : us-west-2b
LaunchGroup              :
LaunchSpecification      : Amazon.EC2.Model.LaunchSpecification
ProductDescription       : Linux/UNIX
SpotInstanceRequestId    : sir-12345678
SpotPrice                : 0.020000
State                    : active
Status                   : Amazon.EC2.Model.SpotInstanceStatus
Tags                     : {Name}
Type                     : one-time
```
**Example 2: This example describes all your Spot instance requests.**

```
Get-EC2SpotInstanceRequest
```
+  For API details, see [DescribeSpotInstanceRequests](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2SpotPriceHistory`
<a name="ec2_DescribeSpotPriceHistory_powershell_topic"></a>

The following code example shows how to use `Get-EC2SpotPriceHistory`.

**Tools for PowerShell V4**
**Example 1: This example gets the last 10 entries in the Spot price history for the specified instance type and Availability Zone. Note that the value specified for the -AvailabilityZone parameter must be valid for the region value supplied to either the cmdlet's -Region parameter (not shown in the example) or set as default in the shell. This example command assumes a default region of 'us-west-2' has been set in the environment.**

```
Get-EC2SpotPriceHistory -InstanceType c3.large -AvailabilityZone us-west-2a -MaxResult 10
```
**Output:**

```
AvailabilityZone   : us-west-2a
InstanceType       : c3.large
Price              : 0.017300
ProductDescription : Linux/UNIX (Amazon VPC)
Timestamp          : 12/25/2015 7:39:49 AM

AvailabilityZone   : us-west-2a
InstanceType       : c3.large
Price              : 0.017200
ProductDescription : Linux/UNIX (Amazon VPC)
Timestamp          : 12/25/2015 7:38:29 AM

AvailabilityZone   : us-west-2a
InstanceType       : c3.large
Price              : 0.017300
ProductDescription : Linux/UNIX (Amazon VPC)
Timestamp          : 12/25/2015 6:57:13 AM
...
```
+  For API details, see [DescribeSpotPriceHistory](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Subnet`
<a name="ec2_DescribeSubnets_powershell_topic"></a>

The following code example shows how to use `Get-EC2Subnet`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified subnet.**

```
Get-EC2Subnet -SubnetId subnet-1a2b3c4d
```
**Output:**

```
AvailabilityZone        : us-west-2c
AvailableIpAddressCount : 251
CidrBlock               : 10.0.0.0/24
DefaultForAz            : False
MapPublicIpOnLaunch     : False
State                   : available
SubnetId                : subnet-1a2b3c4d
Tags                    : {}
VpcId                   : vpc-12345678
```
**Example 2: This example describes all your subnets.**

```
Get-EC2Subnet
```
+  For API details, see [DescribeSubnets](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Tag`
<a name="ec2_DescribeTags_powershell_topic"></a>

The following code example shows how to use `Get-EC2Tag`.

**Tools for PowerShell V4**
**Example 1: This example fetches the tags for resource-type 'image'**

```
Get-EC2Tag -Filter @{Name="resource-type";Values="image"}
```
**Output:**

```
Key         ResourceId            ResourceType Value
---         ----------            ------------ -----
Name        ami-0a123b4ccb567a8ea image        Win7-Imported
auto-delete ami-0a123b4ccb567a8ea image        never
```
**Example 2: This example fetches all the tags for all the resources and groups them by resource type**

```
Get-EC2Tag | Group-Object resourcetype
```
**Output:**

```
Count Name                      Group
----- ----                      -----
    9 subnet                    {Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription...}
   53 instance                  {Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription...}
    3 route-table               {Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription}
    5 security-group            {Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription...}
   30 volume                    {Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription...}
    1 internet-gateway          {Amazon.EC2.Model.TagDescription}
    3 network-interface         {Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription}
    4 elastic-ip                {Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription}
    1 dhcp-options              {Amazon.EC2.Model.TagDescription}
    2 image                     {Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription}
    3 vpc                       {Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription, Amazon.EC2.Model.TagDescription}
```
**Example 3: This example displays all the resources with tag 'auto-delete' with value 'no' for the given region**

```
Get-EC2Tag -Region eu-west-1 -Filter @{Name="tag:auto-delete";Values="no"}
```
**Output:**

```
Key         ResourceId            ResourceType Value
---         ----------            ------------ -----
auto-delete i-0f1bce234d5dd678b   instance     no
auto-delete vol-01d234aa5678901a2 volume       no
auto-delete vol-01234bfb5def6f7b8 volume       no
auto-delete vol-01ccb23f4c5e67890 volume       no
```
**Example 4: This example obtains all the resources with tag 'auto-delete' with 'no' value and further filters in the next pipe to parse only 'instance' resource types and eventually creates 'ThisInstance' tag for each instance resources with value being the instance id itself **

```
Get-EC2Tag -Region eu-west-1 -Filter @{Name="tag:auto-delete";Values="no"} | Where-Object ResourceType -eq "instance" | ForEach-Object {New-EC2Tag -ResourceId $_.ResourceId -Tag @{Key="ThisInstance";Value=$_.ResourceId}}
```
**Example 5: This example fetches tags for all the instance resources as well as 'Name' keys and displays them in a table format**

```
Get-EC2Tag -Filter @{Name="resource-type";Values="instance"},@{Name="key";Values="Name"} | Select-Object ResourceId, @{Name="Name-Tag";Expression={$PSItem.Value}} | Format-Table -AutoSize
```
**Output:**

```
ResourceId          Name-Tag
----------          --------
i-012e3cb4df567e1aa jump1
i-01c23a45d6fc7a89f repro-3
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Volume`
<a name="ec2_DescribeVolumes_powershell_topic"></a>

The following code example shows how to use `Get-EC2Volume`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified EBS volume.**

```
Get-EC2Volume -VolumeId vol-12345678
```
**Output:**

```
Attachments      : {}
AvailabilityZone : us-west-2c
CreateTime       : 7/17/2015 4:35:19 PM
Encrypted        : False
Iops             : 90
KmsKeyId         :
Size             : 30
SnapshotId       : snap-12345678
State            : in-use
Tags             : {}
VolumeId         : vol-12345678
VolumeType       : standard
```
**Example 2: This example describes your EBS volumes that have the status 'available'.**

```
Get-EC2Volume -Filter @{ Name="status"; Values="available" }
```
**Output:**

```
Attachments      : {}
AvailabilityZone : us-west-2c
CreateTime       : 12/21/2015 2:31:29 PM
Encrypted        : False
Iops             : 60
KmsKeyId         :
Size             : 20
SnapshotId       : snap-12345678
State            : available
Tags             : {}
VolumeId         : vol-12345678
VolumeType       : gp2
...
```
**Example 3: This example describes all your EBS volumes.**

```
Get-EC2Volume
```
+  For API details, see [DescribeVolumes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2VolumeAttribute`
<a name="ec2_DescribeVolumeAttribute_powershell_topic"></a>

The following code example shows how to use `Get-EC2VolumeAttribute`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified attribute of the specified volume.**

```
Get-EC2VolumeAttribute -VolumeId vol-12345678 -Attribute AutoEnableIO
```
**Output:**

```
AutoEnableIO    ProductCodes    VolumeId
------------    ------------    --------
False           {}              vol-12345678
```
+  For API details, see [DescribeVolumeAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2VolumeStatus`
<a name="ec2_DescribeVolumeStatus_powershell_topic"></a>

The following code example shows how to use `Get-EC2VolumeStatus`.

**Tools for PowerShell V4**
**Example 1: This example describes the status of the specified volume.**

```
Get-EC2VolumeStatus -VolumeId vol-12345678
```
**Output:**

```
Actions          : {}
AvailabilityZone : us-west-2a
Events           : {}
VolumeId         : vol-12345678
VolumeStatus     : Amazon.EC2.Model.VolumeStatusInfo
```

```
(Get-EC2VolumeStatus -VolumeId vol-12345678).VolumeStatus
```
**Output:**

```
Details                         Status
-------                         ------
{io-enabled, io-performance}    ok
```

```
(Get-EC2VolumeStatus -VolumeId vol-12345678).VolumeStatus.Details
```
**Output:**

```
Name                            Status
----                            ------
io-enabled                      passed
io-performance                  not-applicable
```
+  For API details, see [DescribeVolumeStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2Vpc`
<a name="ec2_DescribeVpcs_powershell_topic"></a>

The following code example shows how to use `Get-EC2Vpc`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified VPC.**

```
Get-EC2Vpc -VpcId vpc-12345678
```
**Output:**

```
CidrBlock       : 10.0.0.0/16
DhcpOptionsId   : dopt-1a2b3c4d
InstanceTenancy : default
IsDefault       : False
State           : available
Tags            : {Name}
VpcId           : vpc-12345678
```
**Example 2: This example describes the default VPC (there can be only one per region). If your account supports EC2-Classic in this region, there is no default VPC.**

```
Get-EC2Vpc -Filter @{Name="isDefault"; Values="true"}
```
**Output:**

```
CidrBlock       : 172.31.0.0/16
DhcpOptionsId   : dopt-12345678
InstanceTenancy : default
IsDefault       : True
State           : available
Tags            : {}
VpcId           : vpc-45678901
```
**Example 3: This example describes the VPCs that match the specified filter (that is, have a CIDR that matches the value '10.0.0.0/16' and are in the state 'available').**

```
Get-EC2Vpc -Filter @{Name="cidr"; Values="10.0.0.0/16"},@{Name="state";Values="available"}
```
**Example 4: This example describes all your VPCs.**

```
Get-EC2Vpc
```
+  For API details, see [DescribeVpcs](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2VpcAttribute`
<a name="ec2_DescribeVpcAttribute_powershell_topic"></a>

The following code example shows how to use `Get-EC2VpcAttribute`.

**Tools for PowerShell V4**
**Example 1: This example describes the 'enableDnsSupport' attribute.**

```
Get-EC2VpcAttribute -VpcId vpc-12345678 -Attribute enableDnsSupport
```
**Output:**

```
EnableDnsSupport
----------------
True
```
**Example 2: This example describes the 'enableDnsHostnames' attribute.**

```
Get-EC2VpcAttribute -VpcId vpc-12345678 -Attribute enableDnsHostnames
```
**Output:**

```
EnableDnsHostnames
------------------
True
```
+  For API details, see [DescribeVpcAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2VpcClassicLink`
<a name="ec2_DescribeVpcClassicLink_powershell_topic"></a>

The following code example shows how to use `Get-EC2VpcClassicLink`.

**Tools for PowerShell V4**
**Example 1: Above example returns all the VPCs with their ClassicLinkEnabled state for the region**

```
Get-EC2VpcClassicLink -Region eu-west-1
```
**Output:**

```
ClassicLinkEnabled Tags   VpcId
------------------ ----   -----
False              {Name} vpc-0fc1ff23f45b678eb
False              {}     vpc-01e23c4a5d6db78e9
False              {Name} vpc-0123456b078b9d01f
False              {}     vpc-12cf3b4f
False              {Name} vpc-0b12d3456a7e8901d
```
+  For API details, see [DescribeVpcClassicLink](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2VpcClassicLinkDnsSupport`
<a name="ec2_DescribeVpcClassicLinkDnsSupport_powershell_topic"></a>

The following code example shows how to use `Get-EC2VpcClassicLinkDnsSupport`.

**Tools for PowerShell V4**
**Example 1: This example describes the ClassicLink DNS support status of VPCs for the region eu-west-1**

```
Get-EC2VpcClassicLinkDnsSupport -VpcId vpc-0b12d3456a7e8910d -Region eu-west-1
```
**Output:**

```
ClassicLinkDnsSupported VpcId
----------------------- -----
False                   vpc-0b12d3456a7e8910d
False                   vpc-12cf3b4f
```
+  For API details, see [DescribeVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2VpcEndpoint`
<a name="ec2_DescribeVpcEndpoints_powershell_topic"></a>

The following code example shows how to use `Get-EC2VpcEndpoint`.

**Tools for PowerShell V4**
**Example 1: This example describes one or more of your VPC endpoints for the region eu-west-1. It then pipes the output to the next command, which select the VpcEndpointId property and returns array VPC ID as string array**

```
Get-EC2VpcEndpoint -Region eu-west-1 | Select-Object -ExpandProperty VpcEndpointId
```
**Output:**

```
vpce-01a2ab3f4f5cc6f7d
vpce-01d2b345a6787890b
vpce-0012e34d567890e12
vpce-0c123db4567890123
```
**Example 2: This example describes all the vpc endpoints for the region eu-west-1 and selects VpcEndpointId, VpcId, ServiceName and PrivateDnsEnabled properties to present it in a tabular format**

```
Get-EC2VpcEndpoint -Region eu-west-1 | Select-Object VpcEndpointId, VpcId, ServiceName, PrivateDnsEnabled | Format-Table -AutoSize
```
**Output:**

```
VpcEndpointId          VpcId                 ServiceName                         PrivateDnsEnabled
-------------          -----                 -----------                         -----------------
vpce-02a2ab2f2f2cc2f2d vpc-0fc6ff46f65b039eb com.amazonaws.eu-west-1.ssm                      True
vpce-01d1b111a1114561b vpc-0fc6ff46f65b039eb com.amazonaws.eu-west-1.ec2                      True
vpce-0011e23d45167e838 vpc-0fc6ff46f65b039eb com.amazonaws.eu-west-1.ec2messages              True
vpce-0c123db4567890123 vpc-0fc6ff46f65b039eb com.amazonaws.eu-west-1.ssmmessages              True
```
**Example 3: This example exports the policy document for the VPC Endpoint vpce-01a2ab3f4f5cc6f7d into a json file**

```
Get-EC2VpcEndpoint -Region eu-west-1 -VpcEndpointId vpce-01a2ab3f4f5cc6f7d | Select-Object -expand PolicyDocument | Out-File vpce_policyDocument.json
```
+  For API details, see [DescribeVpcEndpoints](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2VpcEndpointService`
<a name="ec2_DescribeVpcEndpointServices_powershell_topic"></a>

The following code example shows how to use `Get-EC2VpcEndpointService`.

**Tools for PowerShell V4**
**Example 1: This example describes EC2 VPC endpoint service with the given filter, in this case com.amazonaws.eu-west-1.ecs. Further, it also expands the ServiceDetails property and displays the details**

```
Get-EC2VpcEndpointService -Region eu-west-1 -MaxResult 5 -Filter @{Name="service-name";Values="com.amazonaws.eu-west-1.ecs"} | Select-Object -ExpandProperty ServiceDetails
```
**Output:**

```
AcceptanceRequired         : False
AvailabilityZones          : {eu-west-1a, eu-west-1b, eu-west-1c}
BaseEndpointDnsNames       : {ecs.eu-west-1.vpce.amazonaws.com}
Owner                      : amazon
PrivateDnsName             : ecs.eu-west-1.amazonaws.com
ServiceName                : com.amazonaws.eu-west-1.ecs
ServiceType                : {Amazon.EC2.Model.ServiceTypeDetail}
VpcEndpointPolicySupported : False
```
**Example 2: This example retrieves all the EC2 VPC Endpoint services and returns the ServiceNames matching "ssm"**

```
Get-EC2VpcEndpointService -Region eu-west-1 | Select-Object -ExpandProperty Servicenames | Where-Object { -match "ssm"}
```
**Output:**

```
com.amazonaws.eu-west-1.ssm
com.amazonaws.eu-west-1.ssmmessages
```
+  For API details, see [DescribeVpcEndpointServices](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2VpnConnection`
<a name="ec2_DescribeVpnConnections_powershell_topic"></a>

The following code example shows how to use `Get-EC2VpnConnection`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified VPN connection.**

```
Get-EC2VpnConnection -VpnConnectionId vpn-12345678
```
**Output:**

```
CustomerGatewayConfiguration : [XML document]
CustomerGatewayId            : cgw-1a2b3c4d
Options                      : Amazon.EC2.Model.VpnConnectionOptions
Routes                       : {Amazon.EC2.Model.VpnStaticRoute}
State                        : available
Tags                         : {}
Type                         : ipsec.1
VgwTelemetry                 : {Amazon.EC2.Model.VgwTelemetry, Amazon.EC2.Model.VgwTelemetry}
VpnConnectionId              : vpn-12345678
VpnGatewayId                 : vgw-1a2b3c4d
```
**Example 2: This example describes any VPN connection whose state is either pending or available.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "pending", "available" )

Get-EC2VpnConnection -Filter $filter
```
**Example 3: This example describes all your VPN connections.**

```
Get-EC2VpnConnection
```
+  For API details, see [DescribeVpnConnections](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EC2VpnGateway`
<a name="ec2_DescribeVpnGateways_powershell_topic"></a>

The following code example shows how to use `Get-EC2VpnGateway`.

**Tools for PowerShell V4**
**Example 1: This example describes the specified virtual private gateway.**

```
Get-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d
```
**Output:**

```
AvailabilityZone :
State            : available
Tags             : {}
Type             : ipsec.1
VpcAttachments   : {vpc-12345678}
VpnGatewayId     : vgw-1a2b3c4d
```
**Example 2: This example describes any virtual private gateway whose state is either pending or available.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "pending", "available" )

Get-EC2VpnGateway -Filter $filter
```
**Example 3: This example describes all your virtual private gateways.**

```
Get-EC2VpnGateway
```
+  For API details, see [DescribeVpnGateways](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Grant-EC2SecurityGroupEgress`
<a name="ec2_AuthorizeSecurityGroupEgress_powershell_topic"></a>

The following code example shows how to use `Grant-EC2SecurityGroupEgress`.

**Tools for PowerShell V4**
**Example 1: This example defines an egress rule for the specified security group for EC2-VPC. The rule grants access to the specified IP address range on TCP port 80. The syntax used by this example requires PowerShell version 3 or higher.**

```
$ip = @{ IpProtocol="tcp"; FromPort="80"; ToPort="80"; IpRanges="203.0.113.0/24" }
Grant-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission $ip
```
**Example 2: With PowerShell version 2, you must use New-Object to create the IpPermission object.**

```
$ip = New-Object Amazon.EC2.Model.IpPermission
$ip.IpProtocol = "tcp"
$ip.FromPort = 80
$ip.ToPort = 80
$ip.IpRanges.Add("203.0.113.0/24")

Grant-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission $ip
```
**Example 3: This example grants access to the specified source security group on TCP port 80.**

```
$ug = New-Object Amazon.EC2.Model.UserIdGroupPair
$ug.GroupId = "sg-1a2b3c4d"
$ug.UserId = "123456789012"

Grant-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission @( @{ IpProtocol="tcp"; FromPort="80"; ToPort="80"; UserIdGroupPairs=$ug } )
```
+  For API details, see [AuthorizeSecurityGroupEgress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Grant-EC2SecurityGroupIngress`
<a name="ec2_AuthorizeSecurityGroupIngress_powershell_topic"></a>

The following code example shows how to use `Grant-EC2SecurityGroupIngress`.

**Tools for PowerShell V4**
**Example 1: This example defines ingress rules for a security group for EC2-VPC. These rules grant access to a specific IP address for SSH (port 22) and RDC (port 3389). Note that you must identify security groups for EC2-VPC using the security group ID not the security group name. The syntax used by this example requires PowerShell version 3 or higher.**

```
$ip1 = @{ IpProtocol="tcp"; FromPort="22"; ToPort="22"; IpRanges="203.0.113.25/32" }
$ip2 = @{ IpProtocol="tcp"; FromPort="3389"; ToPort="3389"; IpRanges="203.0.113.25/32" }

Grant-EC2SecurityGroupIngress -GroupId sg-12345678 -IpPermission @( $ip1, $ip2 )
```
**Example 2: With PowerShell version 2, you must use New-Object to create the IpPermission objects.**

```
$ip1 = New-Object Amazon.EC2.Model.IpPermission
$ip1.IpProtocol = "tcp"
$ip1.FromPort = 22
$ip1.ToPort = 22
$ip1.IpRanges.Add("203.0.113.25/32")

$ip2 = new-object Amazon.EC2.Model.IpPermission
$ip2.IpProtocol = "tcp"
$ip2.FromPort = 3389
$ip2.ToPort = 3389
$ip2.IpRanges.Add("203.0.113.25/32")

Grant-EC2SecurityGroupIngress -GroupId sg-12345678 -IpPermission @( $ip1, $ip2 )
```
**Example 3: This example defines ingress rules for a security group for EC2-Classic. These rules grant access to a specific IP address for SSH (port 22) and RDC (port 3389). The syntax used by this example requires PowerShell version 3 or higher.**

```
$ip1 = @{ IpProtocol="tcp"; FromPort="22"; ToPort="22"; IpRanges="203.0.113.25/32" }
$ip2 = @{ IpProtocol="tcp"; FromPort="3389"; ToPort="3389"; IpRanges="203.0.113.25/32" }

Grant-EC2SecurityGroupIngress -GroupName "my-security-group" -IpPermission @( $ip1, $ip2 )
```
**Example 4: With PowerShell version 2, you must use New-Object to create the IpPermission objects.**

```
$ip1 = New-Object Amazon.EC2.Model.IpPermission
$ip1.IpProtocol = "tcp"
$ip1.FromPort = 22
$ip1.ToPort = 22
$ip1.IpRanges.Add("203.0.113.25/32")

$ip2 = new-object Amazon.EC2.Model.IpPermission
$ip2.IpProtocol = "tcp"
$ip2.FromPort = 3389
$ip2.ToPort = 3389
$ip2.IpRanges.Add("203.0.113.25/32")

Grant-EC2SecurityGroupIngress -GroupName "my-security-group" -IpPermission @( $ip1, $ip2 )
```
**Example 5: This example grants TCP port 8081 access from the specified source security group (sg-1a2b3c4d) to the specified security group (sg-12345678).**

```
$ug = New-Object Amazon.EC2.Model.UserIdGroupPair
$ug.GroupId = "sg-1a2b3c4d"
$ug.UserId = "123456789012"

Grant-EC2SecurityGroupIngress -GroupId sg-12345678 -IpPermission @( @{ IpProtocol="tcp"; FromPort="8081"; ToPort="8081"; UserIdGroupPairs=$ug } )
```
**Example 6: This example adds the CIDR 5.5.5.5/32 to the Ingress rules of security Group sg-1234abcd for TCP port 22 traffic with a description.**

```
$IpRange = New-Object -TypeName Amazon.EC2.Model.IpRange
$IpRange.CidrIp = "5.5.5.5/32"
$IpRange.Description = "SSH from Office"
$IpPermission = New-Object Amazon.EC2.Model.IpPermission
$IpPermission.IpProtocol = "tcp"
$IpPermission.ToPort = 22
$IpPermission.FromPort = 22
$IpPermission.Ipv4Ranges = $IpRange
Grant-EC2SecurityGroupIngress -GroupId sg-1234abcd -IpPermission $IpPermission
```
+  For API details, see [AuthorizeSecurityGroupIngress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Import-EC2Image`
<a name="ec2_ImportImage_powershell_topic"></a>

The following code example shows how to use `Import-EC2Image`.

**Tools for PowerShell V4**
**Example 1: This example imports a single-disk virtual machine image from the specified Amazon S3 bucket to Amazon EC2 with an idempotency token. The example requires that a VM Import Service Role with the default name 'vmimport' exists, with a policy allowing Amazon EC2 access to the specified bucket, as explained in the VM Import Prequisites topic. To use a custom role, specify the role name using the `-RoleName` parameter.**

```
$container = New-Object Amazon.EC2.Model.ImageDiskContainer
$container.Format="VMDK"
$container.UserBucket = New-Object Amazon.EC2.Model.UserBucket
$container.UserBucket.S3Bucket = "amzn-s3-demo-bucket"
$container.UserBucket.S3Key = "Win_2008_Server_Standard_SP2_64-bit-disk1.vmdk"

$parms = @{
    "ClientToken"="idempotencyToken"
    "Description"="Windows 2008 Standard Image Import"
    "Platform"="Windows"
    "LicenseType"="AWS"
}

Import-EC2Image -DiskContainer $container @parms
```
**Output:**

```
Architecture    :
Description     : Windows 2008 Standard Image
Hypervisor      :
ImageId         :
ImportTaskId    : import-ami-abcdefgh
LicenseType     : AWS
Platform        : Windows
Progress        : 2
SnapshotDetails : {}
Status          : active
StatusMessage   : pending
```
+  For API details, see [ImportImage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Import-EC2KeyPair`
<a name="ec2_ImportKeyPair_powershell_topic"></a>

The following code example shows how to use `Import-EC2KeyPair`.

**Tools for PowerShell V4**
**Example 1: This example imports a public key to EC2. The first line stores the contents of the public key file (\*.pub) in the variable `$publickey`. Next, the example converts the UTF8 format of the public key file to a Base64-encoded string, and stores the converted string in the variable `$pkbase64`. In the last line, the converted public key is imported to EC2. The cmdlet returns the key fingerprint and name as results.**

```
$publickey=[Io.File]::ReadAllText("C:\Users\TestUser\.ssh\id_rsa.pub")
$pkbase64 = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($publickey))
Import-EC2KeyPair -KeyName Example-user-key -PublicKey $pkbase64
```
**Output:**

```
KeyFingerprint                                  KeyName
--------------                                  -------
do:d0:15:8f:79:97:12:be:00:fd:df:31:z3:b1:42:z1 Example-user-key
```
+  For API details, see [ImportKeyPair](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Import-EC2Snapshot`
<a name="ec2_ImportSnapshot_powershell_topic"></a>

The following code example shows how to use `Import-EC2Snapshot`.

**Tools for PowerShell V4**
**Example 1: This example imports a VM disk image of format 'VMDK' to an Amazon EBS snapshot. The example requires a VM Import Service Role with the default name 'vmimport', with a policy allowing Amazon EC2 access to the specified bucket, as explained in the `VM Import Prequisites` topic in http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/VMImportPrerequisites.html. To use a custom role, specify the role name using the `-RoleName` parameter.**

```
$parms = @{
    "ClientToken"="idempotencyToken"
    "Description"="Disk Image Import"
    "DiskContainer_Description" = "Data disk"
    "DiskContainer_Format" = "VMDK"
    "DiskContainer_S3Bucket" = "amzn-s3-demo-bucket"
    "DiskContainer_S3Key" = "datadiskimage.vmdk"
}

Import-EC2Snapshot @parms
```
**Output:**

```
Description            ImportTaskId               SnapshotTaskDetail
-----------------      --------------------       ------------------
Disk Image Import      import-snap-abcdefgh       Amazon.EC2.Model.SnapshotTaskDetail
```
+  For API details, see [ImportSnapshot](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Move-EC2AddressToVpc`
<a name="ec2_MoveAddressToVpc_powershell_topic"></a>

The following code example shows how to use `Move-EC2AddressToVpc`.

**Tools for PowerShell V4**
**Example 1: This example moves an EC2 instance with a public IP address of 12.345.67.89 to the EC2-VPC platform in the US East (Northern Virginia) region.**

```
Move-EC2AddressToVpc -PublicIp 12.345.67.89 -Region us-east-1
```
**Example 2: This example pipes the results of a Get-EC2Instance command to the Move-EC2AddressToVpc cmdlet. The Get-EC2Instance command gets an instance that is specified by instance ID, then returns the public IP address property of the instance.**

```
(Get-EC2Instance -Instance i-12345678).Instances.PublicIpAddress | Move-EC2AddressToVpc
```
+  For API details, see [MoveAddressToVpc](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Address`
<a name="ec2_AllocateAddress_powershell_topic"></a>

The following code example shows how to use `New-EC2Address`.

**Tools for PowerShell V4**
**Example 1: This example allocates an Elastic IP address to use with an instance in a VPC.**

```
New-EC2Address -Domain Vpc
```
**Output:**

```
AllocationId         Domain      PublicIp
------------         ------      --------
eipalloc-12345678    vpc         198.51.100.2
```
**Example 2: This example allocates an Elastic IP address to use with an instance in EC2-Classic.**

```
New-EC2Address
```
**Output:**

```
AllocationId         Domain      PublicIp
------------         ------      --------
                     standard    203.0.113.17
```
+  For API details, see [AllocateAddress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2CustomerGateway`
<a name="ec2_CreateCustomerGateway_powershell_topic"></a>

The following code example shows how to use `New-EC2CustomerGateway`.

**Tools for PowerShell V4**
**Example 1: This example creates the specified customer gateway.**

```
New-EC2CustomerGateway -Type ipsec.1 -PublicIp 203.0.113.12 -BgpAsn 65534
```
**Output:**

```
BgpAsn            : 65534
CustomerGatewayId : cgw-1a2b3c4d
IpAddress         : 203.0.113.12
State             : available
Tags              : {}
Type              : ipsec.1
```
+  For API details, see [CreateCustomerGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2DhcpOption`
<a name="ec2_CreateDhcpOptions_powershell_topic"></a>

The following code example shows how to use `New-EC2DhcpOption`.

**Tools for PowerShell V4**
**Example 1: This example creates the specified set of DHCP options. The syntax used by this example requires PowerShell version 3 or later.**

```
$options = @( @{Key="domain-name";Values=@("abc.local")}, @{Key="domain-name-servers";Values=@("10.0.0.101","10.0.0.102")})
New-EC2DhcpOption -DhcpConfiguration $options
```
**Output:**

```
DhcpConfigurations                    DhcpOptionsId    Tags
------------------                    -------------    ----
{domain-name, domain-name-servers}    dopt-1a2b3c4d    {}
```
**Example 2: With PowerShell version 2, you must use New-Object to create each DHCP option.**

```
$option1 = New-Object Amazon.EC2.Model.DhcpConfiguration
$option1.Key = "domain-name"
$option1.Values = "abc.local"

$option2 = New-Object Amazon.EC2.Model.DhcpConfiguration
$option2.Key = "domain-name-servers"
$option2.Values = @("10.0.0.101","10.0.0.102")

New-EC2DhcpOption -DhcpConfiguration @($option1, $option2)
```
**Output:**

```
DhcpConfigurations                    DhcpOptionsId    Tags
------------------                    -------------    ----
{domain-name, domain-name-servers}    dopt-2a3b4c5d    {}
```
+  For API details, see [CreateDhcpOptions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2FlowLog`
<a name="ec2_CreateFlowLogs_powershell_topic"></a>

The following code example shows how to use `New-EC2FlowLog`.

**Tools for PowerShell V4**
**Example 1: This example creates EC2 flowlog for the subnet subnet-1d234567 to the cloud-watch-log named 'subnet1-log' for all 'REJECT' traffic using the perimssions of the 'Admin' role**

```
New-EC2FlowLog -ResourceId "subnet-1d234567" -LogDestinationType cloud-watch-logs -LogGroupName subnet1-log -TrafficType "REJECT" -ResourceType Subnet -DeliverLogsPermissionArn "arn:aws:iam::98765432109:role/Admin"
```
**Output:**

```
ClientToken                                  FlowLogIds             Unsuccessful
-----------                                  ----------             ------------
m1VN2cxP3iB4qo//VUKl5EU6cF7gQLOxcqNefvjeTGw= {fl-012fc34eed5678c9d} {}
```
+  For API details, see [CreateFlowLogs](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Host`
<a name="ec2_AllocateHosts_powershell_topic"></a>

The following code example shows how to use `New-EC2Host`.

**Tools for PowerShell V4**
**Example 1: This example allocates a Dedicated Host to your account for the given instance type and availability zone**

```
New-EC2Host -AutoPlacement on -AvailabilityZone eu-west-1b -InstanceType m4.xlarge -Quantity 1
```
**Output:**

```
h-01e23f4cd567890f3
```
+  For API details, see [AllocateHosts](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2HostReservation`
<a name="ec2_PurchaseHostReservation_powershell_topic"></a>

The following code example shows how to use `New-EC2HostReservation`.

**Tools for PowerShell V4**
**Example 1: This example purchases the reservation offering hro-0c1f23456789d0ab with configurations that match those of your Dedicated Host h-01e23f4cd567890f1**

```
New-EC2HostReservation -OfferingId hro-0c1f23456789d0ab HostIdSet h-01e23f4cd567890f1
```
**Output:**

```
ClientToken       :
CurrencyCode      :
Purchase          : {hr-0123f4b5d67bedc89}
TotalHourlyPrice  : 1.307
TotalUpfrontPrice : 0.000
```
+  For API details, see [PurchaseHostReservation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Image`
<a name="ec2_CreateImage_powershell_topic"></a>

The following code example shows how to use `New-EC2Image`.

**Tools for PowerShell V4**
**Example 1: This example creates an AMI with the specified name and description, from the specified instance. Amazon EC2 attempts to cleanly shut down the instance before creating the image, and restarts the instance on completion.**

```
New-EC2Image -InstanceId i-12345678 -Name "my-web-server" -Description "My web server AMI"
```
**Example 2: This example creates an AMI with the specified name and description, from the specified instance. Amazon EC2 creates the image without shutting down and restarting the instance; therefore, file system integrity on the created image can't be guaranteed.**

```
New-EC2Image -InstanceId i-12345678 -Name "my-web-server" -Description "My web server AMI" -NoReboot $true
```
**Example 3: This example creates an AMI with three volumes. The first volume is based on an Amazon EBS snapshot. The second volume is an empty 100 GiB Amazon EBS volume. The third volume is an instance store volume. The syntax used by this example requires PowerShell version 3 or higher.**

```
$ebsBlock1 = @{SnapshotId="snap-1a2b3c4d"}
$ebsBlock2 = @{VolumeSize=100}

New-EC2Image -InstanceId i-12345678 -Name "my-web-server" -Description "My web server AMI" -BlockDeviceMapping @( @{DeviceName="/dev/sdf";Ebs=$ebsBlock1}, @{DeviceName="/dev/sdg";Ebs=$ebsBlock2}, @{DeviceName="/dev/sdc";VirtualName="ephemeral0"})
```
+  For API details, see [CreateImage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Instance`
<a name="ec2_RunInstances_powershell_topic"></a>

The following code example shows how to use `New-EC2Instance`.

**Tools for PowerShell V4**
**Example 1: This example launches a single instance of the specified AMI in EC2-Classic or a default VPC.**

```
New-EC2Instance -ImageId ami-12345678 -MinCount 1 -MaxCount 1 -InstanceType m3.medium -KeyName my-key-pair -SecurityGroup my-security-group
```
**Example 2: This example launches a single instance of the specified AMI in a VPC.**

```
New-EC2Instance -ImageId ami-12345678 -MinCount 1 -MaxCount 1 -SubnetId subnet-12345678 -InstanceType t2.micro -KeyName my-key-pair -SecurityGroupId sg-12345678
```
**Example 3: To add an EBS volume or an instance store volume, define a block device mapping and add it to the command. This example adds an instance store volume.**

```
$bdm = New-Object Amazon.EC2.Model.BlockDeviceMapping
$bdm.VirtualName = "ephemeral0"
$bdm.DeviceName = "/dev/sdf"

New-EC2Instance -ImageId ami-12345678 -BlockDeviceMapping $bdm ...
```
**Example 4: To specify one of the current Windows AMIs, get its AMI ID using Get-EC2ImageByName. This example launches an instance from the current base AMI for Windows Server 2016.**

```
$ami = Get-EC2ImageByName WINDOWS_2016_BASE

New-EC2Instance -ImageId $ami.ImageId ...
```
**Example 5: Launches an instance into the specified dedicated host environment.**

```
New-EC2Instance -ImageId ami-1a2b3c4d -InstanceType m4.large -KeyName my-key-pair -SecurityGroupId sg-1a2b3c4d  -AvailabilityZone us-west-1a -Tenancy host -HostID h-1a2b3c4d5e6f1a2b3
```
**Example 6: This request launches two instances and applies a tag with a key of webserver and a value of production to the instances. The request also applies a tag with a key of cost-center and a value of cc123 to the volumes that are created (in this case, the root volume for each instance).**

```
$tag1 = @{ Key="webserver"; Value="production" }
$tag2 = @{ Key="cost-center"; Value="cc123" }

$tagspec1 = new-object Amazon.EC2.Model.TagSpecification
$tagspec1.ResourceType = "instance"
$tagspec1.Tags.Add($tag1)

$tagspec2 = new-object Amazon.EC2.Model.TagSpecification
$tagspec2.ResourceType = "volume"
$tagspec2.Tags.Add($tag2)

New-EC2Instance -ImageId "ami-1a2b3c4d" -KeyName "my-key-pair" -MaxCount 2 -InstanceType "t2.large" -SubnetId "subnet-1a2b3c4d" -TagSpecification $tagspec1,$tagspec2
```
+  For API details, see [RunInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2InstanceExportTask`
<a name="ec2_CreateInstanceExportTask_powershell_topic"></a>

The following code example shows how to use `New-EC2InstanceExportTask`.

**Tools for PowerShell V4**
**Example 1: This example exports a stopped instance, `i-0800b00a00EXAMPLE`, as a virtual hard disk (VHD) to the S3 bucket `testbucket-export-instances-2019`. The target environment is `Microsoft`, and the region parameter is added because the instance is in the `us-east-1` region, while the user's default AWS Region is not us-east-1. To get the status of the export task, copy the `ExportTaskId` value from the results of this command, then run `Get-EC2ExportTask -ExportTaskId export_task_ID_from_results.`**

```
New-EC2InstanceExportTask -InstanceId i-0800b00a00EXAMPLE -ExportToS3Task_DiskImageFormat VHD -ExportToS3Task_S3Bucket "amzn-s3-demo-bucket" -TargetEnvironment Microsoft -Region us-east-1
```
**Output:**

```
Description           :
ExportTaskId          : export-i-077c73108aEXAMPLE
ExportToS3Task        : Amazon.EC2.Model.ExportToS3Task
InstanceExportDetails : Amazon.EC2.Model.InstanceExportDetails
State                 : active
StatusMessage         :
```
+  For API details, see [CreateInstanceExportTask](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2InternetGateway`
<a name="ec2_CreateInternetGateway_powershell_topic"></a>

The following code example shows how to use `New-EC2InternetGateway`.

**Tools for PowerShell V4**
**Example 1: This example creates an Internet gateway.**

```
New-EC2InternetGateway
```
**Output:**

```
Attachments    InternetGatewayId    Tags
-----------    -----------------    ----
{}             igw-1a2b3c4d         {}
```
+  For API details, see [CreateInternetGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2KeyPair`
<a name="ec2_CreateKeyPair_powershell_topic"></a>

The following code example shows how to use `New-EC2KeyPair`.

**Tools for PowerShell V4**
**Example 1: This example creates a key pair and captures the PEM-encoded RSA private key in a file with the specified name. When you are using PowerShell, the encoding must be set to ascii to generate a valid key. For more information, see Create, Display, and Delete Amazon EC2 Key Pairs (https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-keypairs.html) in the AWS Command Line Interface User Guide.**

```
(New-EC2KeyPair -KeyName "my-key-pair").KeyMaterial | Out-File -Encoding ascii -FilePath C:\path\my-key-pair.pem
```
+  For API details, see [CreateKeyPair](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2NetworkAcl`
<a name="ec2_CreateNetworkAcl_powershell_topic"></a>

The following code example shows how to use `New-EC2NetworkAcl`.

**Tools for PowerShell V4**
**Example 1: This example creates a network ACL for the specified VPC.**

```
New-EC2NetworkAcl -VpcId vpc-12345678
```
**Output:**

```
Associations : {}
Entries      : {Amazon.EC2.Model.NetworkAclEntry, Amazon.EC2.Model.NetworkAclEntry}
IsDefault    : False
NetworkAclId : acl-12345678
Tags         : {}
VpcId        : vpc-12345678
```
+  For API details, see [CreateNetworkAcl](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2NetworkAclEntry`
<a name="ec2_CreateNetworkAclEntry_powershell_topic"></a>

The following code example shows how to use `New-EC2NetworkAclEntry`.

**Tools for PowerShell V4**
**Example 1: This example creates an entry for the specified network ACL. The rule allows inbound traffic from anywhere (0.0.0.0/0) on UDP port 53 (DNS) into any associated subnet.**

```
New-EC2NetworkAclEntry -NetworkAclId acl-12345678 -Egress $false -RuleNumber 100 -Protocol 17 -PortRange_From 53 -PortRange_To 53 -CidrBlock 0.0.0.0/0 -RuleAction allow
```
+  For API details, see [CreateNetworkAclEntry](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2NetworkInterface`
<a name="ec2_CreateNetworkInterface_powershell_topic"></a>

The following code example shows how to use `New-EC2NetworkInterface`.

**Tools for PowerShell V4**
**Example 1: This example creates the specified network interface.**

```
New-EC2NetworkInterface -SubnetId subnet-1a2b3c4d -Description "my network interface" -Group sg-12345678 -PrivateIpAddress 10.0.0.17
```
**Output:**

```
Association        :
Attachment         :
AvailabilityZone   : us-west-2c
Description        : my network interface
Groups             : {my-security-group}
MacAddress         : 0a:72:bc:1a:cd:7f
NetworkInterfaceId : eni-12345678
OwnerId            : 123456789012
PrivateDnsName     : ip-10-0-0-17.us-west-2.compute.internal
PrivateIpAddress   : 10.0.0.17
PrivateIpAddresses : {}
RequesterId        :
RequesterManaged   : False
SourceDestCheck    : True
Status             : pending
SubnetId           : subnet-1a2b3c4d
TagSet             : {}
VpcId              : vpc-12345678
```
+  For API details, see [CreateNetworkInterface](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2PlacementGroup`
<a name="ec2_CreatePlacementGroup_powershell_topic"></a>

The following code example shows how to use `New-EC2PlacementGroup`.

**Tools for PowerShell V4**
**Example 1: This example creates a placement group with the specified name.**

```
New-EC2PlacementGroup -GroupName my-placement-group -Strategy cluster
```
+  For API details, see [CreatePlacementGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Route`
<a name="ec2_CreateRoute_powershell_topic"></a>

The following code example shows how to use `New-EC2Route`.

**Tools for PowerShell V4**
**Example 1: This example creates the specified route for the specified route table. The route matches all traffic and sends it to the specified Internet gateway.**

```
New-EC2Route -RouteTableId rtb-1a2b3c4d -DestinationCidrBlock 0.0.0.0/0 -GatewayId igw-1a2b3c4d
```
**Output:**

```
True
```
+  For API details, see [CreateRoute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2RouteTable`
<a name="ec2_CreateRouteTable_powershell_topic"></a>

The following code example shows how to use `New-EC2RouteTable`.

**Tools for PowerShell V4**
**Example 1: This example creates a route table for the specified VPC.**

```
New-EC2RouteTable -VpcId vpc-12345678
```
**Output:**

```
Associations    : {}
PropagatingVgws : {}
Routes          : {}
RouteTableId    : rtb-1a2b3c4d
Tags            : {}
VpcId           : vpc-12345678
```
+  For API details, see [CreateRouteTable](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2ScheduledInstance`
<a name="ec2_RunScheduledInstances_powershell_topic"></a>

The following code example shows how to use `New-EC2ScheduledInstance`.

**Tools for PowerShell V4**
**Example 1: This example launches the specified Scheduled Instance.**

```
New-EC2ScheduledInstance -ScheduledInstanceId sci-1234-1234-1234-1234-123456789012 -InstanceCount 1 `
-IamInstanceProfile_Name my-iam-role `
-LaunchSpecification_ImageId ami-12345678 `
-LaunchSpecification_InstanceType c4.large `
-LaunchSpecification_SubnetId subnet-12345678`
-LaunchSpecification_SecurityGroupId sg-12345678
```
+  For API details, see [RunScheduledInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2ScheduledInstancePurchase`
<a name="ec2_PurchaseScheduledInstances_powershell_topic"></a>

The following code example shows how to use `New-EC2ScheduledInstancePurchase`.

**Tools for PowerShell V4**
**Example 1: This example purchases a Scheduled Instance.**

```
$request = New-Object Amazon.EC2.Model.PurchaseRequest
$request.InstanceCount = 1
$request.PurchaseToken = "eyJ2IjoiMSIsInMiOjEsImMiOi..."
New-EC2ScheduledInstancePurchase -PurchaseRequest $request
```
**Output:**

```
AvailabilityZone            : us-west-2b
CreateDate                  : 1/25/2016 1:43:38 PM
HourlyPrice                 : 0.095
InstanceCount               : 1
InstanceType                : c4.large
NetworkPlatform             : EC2-VPC
NextSlotStartTime           : 1/31/2016 1:00:00 AM
Platform                    : Linux/UNIX
PreviousSlotEndTime         :
Recurrence                  : Amazon.EC2.Model.ScheduledInstanceRecurrence
ScheduledInstanceId         : sci-1234-1234-1234-1234-123456789012
SlotDurationInHours         : 32
TermEndDate                 : 1/31/2017 1:00:00 AM
TermStartDate               : 1/31/2016 1:00:00 AM
TotalScheduledInstanceHours : 1696
```
+  For API details, see [PurchaseScheduledInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2SecurityGroup`
<a name="ec2_CreateSecurityGroup_powershell_topic"></a>

The following code example shows how to use `New-EC2SecurityGroup`.

**Tools for PowerShell V4**
**Example 1: This example creates a security group for the specified VPC.**

```
New-EC2SecurityGroup -GroupName my-security-group -Description "my security group" -VpcId vpc-12345678
```
**Output:**

```
sg-12345678
```
**Example 2: This example creates a security group for EC2-Classic.**

```
New-EC2SecurityGroup -GroupName my-security-group -Description "my security group"
```
**Output:**

```
sg-45678901
```
+  For API details, see [CreateSecurityGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Snapshot`
<a name="ec2_CreateSnapshot_powershell_topic"></a>

The following code example shows how to use `New-EC2Snapshot`.

**Tools for PowerShell V4**
**Example 1: This example creates a snapshot of the specified volume.**

```
New-EC2Snapshot -VolumeId vol-12345678 -Description "This is a test"
```
**Output:**

```
DataEncryptionKeyId :
Description         : This is a test
Encrypted           : False
KmsKeyId            :
OwnerAlias          :
OwnerId             : 123456789012
Progress            :
SnapshotId          : snap-12345678
StartTime           : 12/22/2015 1:28:42 AM
State               : pending
StateMessage        :
Tags                : {}
VolumeId            : vol-12345678
VolumeSize          : 20
```
+  For API details, see [CreateSnapshot](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2SpotDatafeedSubscription`
<a name="ec2_CreateSpotDatafeedSubscription_powershell_topic"></a>

The following code example shows how to use `New-EC2SpotDatafeedSubscription`.

**Tools for PowerShell V4**
**Example 1: This example creates a Spot instance data feed.**

```
New-EC2SpotDatafeedSubscription -Bucket amzn-s3-demo-bucket -Prefix spotdata
```
**Output:**

```
Bucket  : amzn-s3-demo-bucket
Fault   :
OwnerId : 123456789012
Prefix  : spotdata
State   : Active
```
+  For API details, see [CreateSpotDatafeedSubscription](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Subnet`
<a name="ec2_CreateSubnet_powershell_topic"></a>

The following code example shows how to use `New-EC2Subnet`.

**Tools for PowerShell V4**
**Example 1: This example creates a subnet with the specified CIDR.**

```
New-EC2Subnet -VpcId vpc-12345678 -CidrBlock 10.0.0.0/24
```
**Output:**

```
AvailabilityZone        : us-west-2c
AvailableIpAddressCount : 251
CidrBlock               : 10.0.0.0/24
DefaultForAz            : False
MapPublicIpOnLaunch     : False
State                   : pending
SubnetId                : subnet-1a2b3c4d
Tag                     : {}
VpcId                   : vpc-12345678
```
+  For API details, see [CreateSubnet](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Tag`
<a name="ec2_CreateTags_powershell_topic"></a>

The following code example shows how to use `New-EC2Tag`.

**Tools for PowerShell V4**
**Example 1: This example adds a single tag to the specified resource. The tag key is 'myTag' and the tag value is 'myTagValue'. The syntax used by this example requires PowerShell version 3 or higher.**

```
New-EC2Tag -Resource i-12345678 -Tag @{ Key="myTag"; Value="myTagValue" }
```
**Example 2: This example updates or adds the specified tags to the specified resource. The syntax used by this example requires PowerShell version 3 or higher.**

```
New-EC2Tag -Resource i-12345678 -Tag @( @{ Key="myTag"; Value="newTagValue" }, @{ Key="test"; Value="anotherTagValue" } )
```
**Example 3: With PowerShell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.EC2.Model.Tag
$tag.Key = "myTag"
$tag.Value = "myTagValue"

New-EC2Tag -Resource i-12345678 -Tag $tag
```
+  For API details, see [CreateTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Volume`
<a name="ec2_CreateVolume_powershell_topic"></a>

The following code example shows how to use `New-EC2Volume`.

**Tools for PowerShell V4**
**Example 1: This example creates the specified volume.**

```
New-EC2Volume -Size 50 -AvailabilityZone us-west-2a -VolumeType gp2
```
**Output:**

```
Attachments      : {}
AvailabilityZone : us-west-2a
CreateTime       : 12/22/2015 1:42:07 AM
Encrypted        : False
Iops             : 150
KmsKeyId         :
Size             : 50
SnapshotId       :
State            : creating
Tags             : {}
VolumeId         : vol-12345678
VolumeType       : gp2
```
**Example 2: This example request creates a volume and applies a tag with a key of stack and a value of production.**

```
$tag = @{ Key="stack"; Value="production" }

$tagspec = new-object Amazon.EC2.Model.TagSpecification
$tagspec.ResourceType = "volume"
$tagspec.Tags.Add($tag)

New-EC2Volume -Size 80 -AvailabilityZone "us-west-2a" -TagSpecification $tagspec
```
+  For API details, see [CreateVolume](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2Vpc`
<a name="ec2_CreateVpc_powershell_topic"></a>

The following code example shows how to use `New-EC2Vpc`.

**Tools for PowerShell V4**
**Example 1: This example creates a VPC with the specified CIDR. Amazon VPC also creates the following for the VPC: a default DHCP options set, a main route table, and a default network ACL.**

```
New-EC2VPC -CidrBlock 10.0.0.0/16
```
**Output:**

```
CidrBlock       : 10.0.0.0/16
DhcpOptionsId   : dopt-1a2b3c4d
InstanceTenancy : default
IsDefault       : False
State           : pending
Tags            : {}
VpcId           : vpc-12345678
```
+  For API details, see [CreateVpc](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2VpcEndpoint`
<a name="ec2_CreateVpcEndpoint_powershell_topic"></a>

The following code example shows how to use `New-EC2VpcEndpoint`.

**Tools for PowerShell V4**
**Example 1: This example create a new VPC Endpoint for the service com.amazonaws.eu-west-1.s3 in the VPC vpc-0fc1ff23f45b678eb**

```
New-EC2VpcEndpoint -ServiceName com.amazonaws.eu-west-1.s3 -VpcId vpc-0fc1ff23f45b678eb
```
**Output:**

```
ClientToken VpcEndpoint
----------- -----------
            Amazon.EC2.Model.VpcEndpoint
```
+  For API details, see [CreateVpcEndpoint](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2VpnConnection`
<a name="ec2_CreateVpnConnection_powershell_topic"></a>

The following code example shows how to use `New-EC2VpnConnection`.

**Tools for PowerShell V4**
**Example 1: This example creates a VPN connection between the specified virtual private gateway and the specified customer gateway. The output includes the configuration information that your network administrator needs, in XML format.**

```
New-EC2VpnConnection -Type ipsec.1 -CustomerGatewayId cgw-1a2b3c4d -VpnGatewayId vgw-1a2b3c4d
```
**Output:**

```
CustomerGatewayConfiguration : [XML document]
CustomerGatewayId            : cgw-1a2b3c4d
Options                      :
Routes                       : {}
State                        : pending
Tags                         : {}
Type                         :
VgwTelemetry                 : {}
VpnConnectionId              : vpn-12345678
VpnGatewayId                 : vgw-1a2b3c4d
```
**Example 2: This example creates the VPN connection and captures the configuration in a file with the specified name.**

```
(New-EC2VpnConnection -CustomerGatewayId cgw-1a2b3c4d -VpnGatewayId vgw-1a2b3c4d).CustomerGatewayConfiguration | Out-File C:\path\vpn-configuration.xml
```
**Example 3: This example creates a VPN connection, with static routing, between the specified virtual private gateway and the specified customer gateway.**

```
New-EC2VpnConnection -Type ipsec.1 -CustomerGatewayId cgw-1a2b3c4d -VpnGatewayId vgw-1a2b3c4d -Options_StaticRoutesOnly $true
```
+  For API details, see [CreateVpnConnection](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2VpnConnectionRoute`
<a name="ec2_CreateVpnConnectionRoute_powershell_topic"></a>

The following code example shows how to use `New-EC2VpnConnectionRoute`.

**Tools for PowerShell V4**
**Example 1: This example creates the specified static route for the specified VPN connection.**

```
New-EC2VpnConnectionRoute -VpnConnectionId vpn-12345678 -DestinationCidrBlock 11.12.0.0/16
```
+  For API details, see [CreateVpnConnectionRoute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EC2VpnGateway`
<a name="ec2_CreateVpnGateway_powershell_topic"></a>

The following code example shows how to use `New-EC2VpnGateway`.

**Tools for PowerShell V4**
**Example 1: This example creates the specified virtual private gateway.**

```
New-EC2VpnGateway -Type ipsec.1
```
**Output:**

```
AvailabilityZone :
State            : available
Tags             : {}
Type             : ipsec.1
VpcAttachments   : {}
VpnGatewayId     : vgw-1a2b3c4d
```
+  For API details, see [CreateVpnGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-EC2Address`
<a name="ec2_AssociateAddress_powershell_topic"></a>

The following code example shows how to use `Register-EC2Address`.

**Tools for PowerShell V4**
**Example 1: This example associates the specified Elastic IP address with the specified instance in a VPC.**

```
C:\> Register-EC2Address -InstanceId i-12345678 -AllocationId eipalloc-12345678
```
**Output:**

```
eipassoc-12345678
```
**Example 2: This example associates the specified Elastic IP address with the specified instance in EC2-Classic.**

```
C:\> Register-EC2Address -InstanceId i-12345678 -PublicIp 203.0.113.17
```
+  For API details, see [AssociateAddress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-EC2DhcpOption`
<a name="ec2_AssociateDhcpOptions_powershell_topic"></a>

The following code example shows how to use `Register-EC2DhcpOption`.

**Tools for PowerShell V4**
**Example 1: This example associates the specified DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d -VpcId vpc-12345678
```
**Example 2: This example associates the default DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId default -VpcId vpc-12345678
```
+  For API details, see [AssociateDhcpOptions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-EC2Image`
<a name="ec2_RegisterImage_powershell_topic"></a>

The following code example shows how to use `Register-EC2Image`.

**Tools for PowerShell V4**
**Example 1: This example registers an AMI using the specified manifest file in Amazon S3.**

```
Register-EC2Image -ImageLocation amzn-s3-demo-bucket/my-web-server-ami/image.manifest.xml -Name my-web-server-ami
```
+  For API details, see [RegisterImage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-EC2PrivateIpAddress`
<a name="ec2_AssignPrivateIpAddresses_powershell_topic"></a>

The following code example shows how to use `Register-EC2PrivateIpAddress`.

**Tools for PowerShell V4**
**Example 1: This example assigns the specified secondary private IP address to the specified network interface.**

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82
```
**Example 2: This example creates two secondary private IP addresses and assigns them to the specified network interface.**

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -SecondaryPrivateIpAddressCount 2
```
+  For API details, see [AssignPrivateIpAddresses](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Register-EC2RouteTable`
<a name="ec2_AssociateRouteTable_powershell_topic"></a>

The following code example shows how to use `Register-EC2RouteTable`.

**Tools for PowerShell V4**
**Example 1: This example associates the specified route table with the specified subnet.**

```
Register-EC2RouteTable -RouteTableId rtb-1a2b3c4d -SubnetId subnet-1a2b3c4d
```
**Output:**

```
rtbassoc-12345678
```
+  For API details, see [AssociateRouteTable](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2Address`
<a name="ec2_ReleaseAddress_powershell_topic"></a>

The following code example shows how to use `Remove-EC2Address`.

**Tools for PowerShell V4**
**Example 1: This example releases the specified Elastic IP address for instances in a VPC.**

```
Remove-EC2Address -AllocationId eipalloc-12345678 -Force
```
**Example 2: This example releases the specified Elastic IP address for instances in EC2-Classic.**

```
Remove-EC2Address -PublicIp 198.51.100.2 -Force
```
+  For API details, see [ReleaseAddress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2CapacityReservation`
<a name="ec2_CancelCapacityReservation_powershell_topic"></a>

The following code example shows how to use `Remove-EC2CapacityReservation`.

**Tools for PowerShell V4**
**Example 1: This example cancels the capacity reservation cr-0c1f2345db6f7cdba**

```
Remove-EC2CapacityReservation -CapacityReservationId cr-0c1f2345db6f7cdba
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2CapacityReservation (CancelCapacityReservation)" on target "cr-0c1f2345db6f7cdba".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
True
```
+  For API details, see [CancelCapacityReservation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2CustomerGateway`
<a name="ec2_DeleteCustomerGateway_powershell_topic"></a>

The following code example shows how to use `Remove-EC2CustomerGateway`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified customer gateway. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2CustomerGateway -CustomerGatewayId cgw-1a2b3c4d
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2CustomerGateway (DeleteCustomerGateway)" on Target "cgw-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteCustomerGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2DhcpOption`
<a name="ec2_DeleteDhcpOptions_powershell_topic"></a>

The following code example shows how to use `Remove-EC2DhcpOption`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified DHCP options set. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2DhcpOption (DeleteDhcpOptions)" on Target "dopt-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteDhcpOptions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2FlowLog`
<a name="ec2_DeleteFlowLogs_powershell_topic"></a>

The following code example shows how to use `Remove-EC2FlowLog`.

**Tools for PowerShell V4**
**Example 1: This example removes the given FlowLogId fl-01a2b3456a789c01**

```
Remove-EC2FlowLog -FlowLogId fl-01a2b3456a789c01
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2FlowLog (DeleteFlowLogs)" on target "fl-01a2b3456a789c01".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteFlowLogs](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2Host`
<a name="ec2_ReleaseHosts_powershell_topic"></a>

The following code example shows how to use `Remove-EC2Host`.

**Tools for PowerShell V4**
**Example 1: This example releases the given host ID h-0badafd1dcb2f3456**

```
Remove-EC2Host -HostId h-0badafd1dcb2f3456
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2Host (ReleaseHosts)" on target "h-0badafd1dcb2f3456".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

Successful            Unsuccessful
----------            ------------
{h-0badafd1dcb2f3456} {}
```
+  For API details, see [ReleaseHosts](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2Instance`
<a name="ec2_TerminateInstances_powershell_topic"></a>

The following code example shows how to use `Remove-EC2Instance`.

**Tools for PowerShell V4**
**Example 1: This example terminates the specified instance (the instance may be running or in 'stopped' state). The cmdlet will prompt for confirmation before proceeding; use the -Force switch to suppress the prompt.**

```
Remove-EC2Instance -InstanceId i-12345678
```
**Output:**

```
CurrentState                      InstanceId    PreviousState
------------                      ----------    -------------
Amazon.EC2.Model.InstanceState    i-12345678    Amazon.EC2.Model.InstanceState
```
+  For API details, see [TerminateInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2InternetGateway`
<a name="ec2_DeleteInternetGateway_powershell_topic"></a>

The following code example shows how to use `Remove-EC2InternetGateway`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified Internet gateway. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2InternetGateway (DeleteInternetGateway)" on Target "igw-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteInternetGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2KeyPair`
<a name="ec2_DeleteKeyPair_powershell_topic"></a>

The following code example shows how to use `Remove-EC2KeyPair`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified key pair. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2KeyPair -KeyName my-key-pair
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2KeyPair (DeleteKeyPair)" on Target "my-key-pair".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteKeyPair](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2NetworkAcl`
<a name="ec2_DeleteNetworkAcl_powershell_topic"></a>

The following code example shows how to use `Remove-EC2NetworkAcl`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified network ACL. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2NetworkAcl -NetworkAclId acl-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2NetworkAcl (DeleteNetworkAcl)" on Target "acl-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteNetworkAcl](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2NetworkAclEntry`
<a name="ec2_DeleteNetworkAclEntry_powershell_topic"></a>

The following code example shows how to use `Remove-EC2NetworkAclEntry`.

**Tools for PowerShell V4**
**Example 1: This example removes the specified rule from the specified network ACL. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2NetworkAclEntry -NetworkAclId acl-12345678 -Egress $false -RuleNumber 100
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2NetworkAclEntry (DeleteNetworkAclEntry)" on Target "acl-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteNetworkAclEntry](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2NetworkInterface`
<a name="ec2_DeleteNetworkInterface_powershell_topic"></a>

The following code example shows how to use `Remove-EC2NetworkInterface`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified network interface. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2NetworkInterface -NetworkInterfaceId eni-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2NetworkInterface (DeleteNetworkInterface)" on Target "eni-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteNetworkInterface](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2PlacementGroup`
<a name="ec2_DeletePlacementGroup_powershell_topic"></a>

The following code example shows how to use `Remove-EC2PlacementGroup`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified placement group. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2PlacementGroup -GroupName my-placement-group
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2PlacementGroup (DeletePlacementGroup)" on Target "my-placement-group".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeletePlacementGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2Route`
<a name="ec2_DeleteRoute_powershell_topic"></a>

The following code example shows how to use `Remove-EC2Route`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified route from the specified route table. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2Route -RouteTableId rtb-1a2b3c4d -DestinationCidrBlock 0.0.0.0/0
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2Route (DeleteRoute)" on Target "rtb-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteRoute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2RouteTable`
<a name="ec2_DeleteRouteTable_powershell_topic"></a>

The following code example shows how to use `Remove-EC2RouteTable`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified route table. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2RouteTable -RouteTableId rtb-1a2b3c4d
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2RouteTable (DeleteRouteTable)" on Target "rtb-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteRouteTable](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2SecurityGroup`
<a name="ec2_DeleteSecurityGroup_powershell_topic"></a>

The following code example shows how to use `Remove-EC2SecurityGroup`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified security group for EC2-VPC. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2SecurityGroup -GroupId sg-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2SecurityGroup (DeleteSecurityGroup)" on Target "sg-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: This example deletes the specified security group for EC2-Classic.**

```
Remove-EC2SecurityGroup -GroupName my-security-group -Force
```
+  For API details, see [DeleteSecurityGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2Snapshot`
<a name="ec2_DeleteSnapshot_powershell_topic"></a>

The following code example shows how to use `Remove-EC2Snapshot`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified snapshot. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2Snapshot -SnapshotId snap-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2Snapshot (DeleteSnapshot)" on target "snap-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteSnapshot](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2SpotDatafeedSubscription`
<a name="ec2_DeleteSpotDatafeedSubscription_powershell_topic"></a>

The following code example shows how to use `Remove-EC2SpotDatafeedSubscription`.

**Tools for PowerShell V4**
**Example 1: This example deletes your Spot instance data feed. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2SpotDatafeedSubscription
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2SpotDatafeedSubscription (DeleteSpotDatafeedSubscription)" on Target "".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteSpotDatafeedSubscription](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2Subnet`
<a name="ec2_DeleteSubnet_powershell_topic"></a>

The following code example shows how to use `Remove-EC2Subnet`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified subnet. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2Subnet -SubnetId subnet-1a2b3c4d
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2Subnet (DeleteSubnet)" on Target "subnet-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteSubnet](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2Tag`
<a name="ec2_DeleteTags_powershell_topic"></a>

The following code example shows how to use `Remove-EC2Tag`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified tag from the specified resource, regardless of the tag value. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-EC2Tag -Resource i-12345678 -Tag @{ Key="myTag" } -Force
```
**Example 2: This example deletes the specified tag from the specified resource, but only if the tag value matches. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-EC2Tag -Resource i-12345678 -Tag @{ Key="myTag";Value="myTagValue" } -Force
```
**Example 3: This example deletes the specified tag from the specified resource, regardless of the tag value.**

```
$tag = New-Object Amazon.EC2.Model.Tag
$tag.Key = "myTag"

Remove-EC2Tag -Resource i-12345678 -Tag $tag -Force
```
**Example 4: This example deletes the specified tag from the specified resource, but only if the tag value matches.**

```
$tag = New-Object Amazon.EC2.Model.Tag
$tag.Key = "myTag"
$tag.Value = "myTagValue"

Remove-EC2Tag -Resource i-12345678 -Tag $tag -Force
```
+  For API details, see [DeleteTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2Volume`
<a name="ec2_DeleteVolume_powershell_topic"></a>

The following code example shows how to use `Remove-EC2Volume`.

**Tools for PowerShell V4**
**Example 1: This example detaches the specified volume. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2Volume -VolumeId vol-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2Volume (DeleteVolume)" on target "vol-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVolume](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2Vpc`
<a name="ec2_DeleteVpc_powershell_topic"></a>

The following code example shows how to use `Remove-EC2Vpc`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified VPC. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2Vpc -VpcId vpc-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2Vpc (DeleteVpc)" on Target "vpc-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVpc](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2VpnConnection`
<a name="ec2_DeleteVpnConnection_powershell_topic"></a>

The following code example shows how to use `Remove-EC2VpnConnection`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified VPN connection. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2VpnConnection -VpnConnectionId vpn-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2VpnConnection (DeleteVpnConnection)" on Target "vpn-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVpnConnection](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2VpnConnectionRoute`
<a name="ec2_DeleteVpnConnectionRoute_powershell_topic"></a>

The following code example shows how to use `Remove-EC2VpnConnectionRoute`.

**Tools for PowerShell V4**
**Example 1: This example removes the specified static route from the specified VPN connection. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2VpnConnectionRoute -VpnConnectionId vpn-12345678 -DestinationCidrBlock 11.12.0.0/16
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2VpnConnectionRoute (DeleteVpnConnectionRoute)" on Target "vpn-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVpnConnectionRoute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EC2VpnGateway`
<a name="ec2_DeleteVpnGateway_powershell_topic"></a>

The following code example shows how to use `Remove-EC2VpnGateway`.

**Tools for PowerShell V4**
**Example 1: This example deletes the specified virtual private gateway. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2VpnGateway (DeleteVpnGateway)" on Target "vgw-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVpnGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Request-EC2SpotFleet`
<a name="ec2_RequestSpotFleet_powershell_topic"></a>

The following code example shows how to use `Request-EC2SpotFleet`.

**Tools for PowerShell V4**
**Example 1: This example creates a Spot fleet request in the Availability Zone with the lowest price for the specified instance type. If your account supports EC2-VPC only, the Spot fleet launches the instances in the lowest-priced Availability Zone that has a default subnet. If your account supports EC2-Classic, the Spot fleet launches the instances in EC2-Classic in the lowest-priced Availability Zone. Note that the price you pay will not exceed the specified Spot price for the request.**

```
$sg = New-Object Amazon.EC2.Model.GroupIdentifier
$sg.GroupId = "sg-12345678"
$lc = New-Object Amazon.EC2.Model.SpotFleetLaunchSpecification
$lc.ImageId = "ami-12345678"
$lc.InstanceType = "m3.medium"
$lc.SecurityGroups.Add($sg)
Request-EC2SpotFleet -SpotFleetRequestConfig_SpotPrice 0.04 `
-SpotFleetRequestConfig_TargetCapacity 2 `
-SpotFleetRequestConfig_IamFleetRole arn:aws:iam::123456789012:role/my-spot-fleet-role `
-SpotFleetRequestConfig_LaunchSpecification $lc
```
+  For API details, see [RequestSpotFleet](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Request-EC2SpotInstance`
<a name="ec2_RequestSpotInstances_powershell_topic"></a>

The following code example shows how to use `Request-EC2SpotInstance`.

**Tools for PowerShell V4**
**Example 1: This example requests a one-time Spot instance in the specified subnet. Note that the security group must be created for the VPC that contains the specified subnet, and it must be specified by ID using the network interface. When you specify a network interface, you must include the subnet ID using the network interface.**

```
$n = New-Object Amazon.EC2.Model.InstanceNetworkInterfaceSpecification
$n.DeviceIndex = 0
$n.SubnetId = "subnet-12345678"
$n.Groups.Add("sg-12345678")
Request-EC2SpotInstance -InstanceCount 1 -SpotPrice 0.050 -Type one-time `
-IamInstanceProfile_Arn arn:aws:iam::123456789012:instance-profile/my-iam-role `
-LaunchSpecification_ImageId ami-12345678 `
-LaunchSpecification_InstanceType m3.medium `
-LaunchSpecification_NetworkInterface $n
```
**Output:**

```
ActualBlockHourlyPrice   :
AvailabilityZoneGroup    :
BlockDurationMinutes     : 0
CreateTime               : 12/26/2015 7:44:10 AM
Fault                    :
InstanceId               :
LaunchedAvailabilityZone :
LaunchGroup              :
LaunchSpecification      : Amazon.EC2.Model.LaunchSpecification
ProductDescription       : Linux/UNIX
SpotInstanceRequestId    : sir-12345678
SpotPrice                : 0.050000
State                    : open
Status                   : Amazon.EC2.Model.SpotInstanceStatus
Tags                     : {}
Type                     : one-time
```
+  For API details, see [RequestSpotInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Reset-EC2ImageAttribute`
<a name="ec2_ResetImageAttribute_powershell_topic"></a>

The following code example shows how to use `Reset-EC2ImageAttribute`.

**Tools for PowerShell V4**
**Example 1: This example resets the 'launchPermission' attribute to its default value. By default, AMIs are private.**

```
Reset-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission
```
+  For API details, see [ResetImageAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Reset-EC2InstanceAttribute`
<a name="ec2_ResetInstanceAttribute_powershell_topic"></a>

The following code example shows how to use `Reset-EC2InstanceAttribute`.

**Tools for PowerShell V4**
**Example 1: This example resets the 'sriovNetSupport' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sriovNetSupport
```
**Example 2: This example resets the 'ebsOptimized' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute ebsOptimized
```
**Example 3: This example resets the 'sourceDestCheck' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sourceDestCheck
```
**Example 4: This example resets the 'disableApiTermination' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute disableApiTermination
```
**Example 5: This example resets the 'instanceInitiatedShutdownBehavior' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceInitiatedShutdownBehavior
```
+  For API details, see [ResetInstanceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Reset-EC2NetworkInterfaceAttribute`
<a name="ec2_ResetNetworkInterfaceAttribute_powershell_topic"></a>

The following code example shows how to use `Reset-EC2NetworkInterfaceAttribute`.

**Tools for PowerShell V4**
**Example 1: This example resets source/destination checking for the specified network interface.**

```
Reset-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -SourceDestCheck
```
+  For API details, see [ResetNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Reset-EC2SnapshotAttribute`
<a name="ec2_ResetSnapshotAttribute_powershell_topic"></a>

The following code example shows how to use `Reset-EC2SnapshotAttribute`.

**Tools for PowerShell V4**
**Example 1: This example resets the specified attribute of the specified snapshot.**

```
Reset-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission
```
+  For API details, see [ResetSnapshotAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Restart-EC2Instance`
<a name="ec2_RebootInstances_powershell_topic"></a>

The following code example shows how to use `Restart-EC2Instance`.

**Tools for PowerShell V4**
**Example 1: This example reboots the specified instance.**

```
Restart-EC2Instance -InstanceId i-12345678
```
+  For API details, see [RebootInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Revoke-EC2SecurityGroupEgress`
<a name="ec2_RevokeSecurityGroupEgress_powershell_topic"></a>

The following code example shows how to use `Revoke-EC2SecurityGroupEgress`.

**Tools for PowerShell V4**
**Example 1: This example removes the rule for the specified security group for EC2-VPC. This revokes access to the specified IP address range on TCP port 80. The syntax used by this example requires PowerShell version 3 or higher.**

```
$ip = @{ IpProtocol="tcp"; FromPort="80"; ToPort="80"; IpRanges="203.0.113.0/24" }
Revoke-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission $ip
```
**Example 2: With PowerShell version 2, you must use New-Object to create the IpPermission object.**

```
$ip = New-Object Amazon.EC2.Model.IpPermission
$ip.IpProtocol = "tcp"
$ip.FromPort = 80
$ip.ToPort = 80
$ip.IpRanges.Add("203.0.113.0/24")
Revoke-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission $ip
```
**Example 3: This example revokes access to the specified source security group on TCP port 80.**

```
$ug = New-Object Amazon.EC2.Model.UserIdGroupPair
$ug.GroupId = "sg-1a2b3c4d"
$ug.UserId = "123456789012"
Revoke-EC2SecurityGroupEgress -GroupId sg-12345678 -IpPermission @( @{ IpProtocol="tcp"; FromPort="80"; ToPort="80"; UserIdGroupPairs=$ug } )
```
+  For API details, see [RevokeSecurityGroupEgress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Revoke-EC2SecurityGroupIngress`
<a name="ec2_RevokeSecurityGroupIngress_powershell_topic"></a>

The following code example shows how to use `Revoke-EC2SecurityGroupIngress`.

**Tools for PowerShell V4**
**Example 1: This example revokes access to TCP port 22 from the specified address range for the specified security group for EC2-VPC. Note that you must identify security groups for EC2-VPC using the security group ID not the security group name. The syntax used by this example requires PowerShell version 3 or higher.**

```
$ip = @{ IpProtocol="tcp"; FromPort="22"; ToPort="22"; IpRanges="203.0.113.0/24" }
Revoke-EC2SecurityGroupIngress -GroupId sg-12345678 -IpPermission $ip
```
**Example 2: With PowerShell version 2, you must use New-Object to create the IpPermission object.**

```
$ip = New-Object Amazon.EC2.Model.IpPermission
$ip.IpProtocol = "tcp"
$ip.FromPort = 22
$ip.ToPort = 22
$ip.IpRanges.Add("203.0.113.0/24")

Revoke-EC2SecurityGroupIngress -GroupId sg-12345678 -IpPermission $ip
```
**Example 3: This example revokes access to TCP port 22 from the specified address range for the specified security group for EC2-Classic. The syntax used by this example requires PowerShell version 3 or higher.**

```
$ip = @{ IpProtocol="tcp"; FromPort="22"; ToPort="22"; IpRanges="203.0.113.0/24" }

Revoke-EC2SecurityGroupIngress -GroupName "my-security-group" -IpPermission $ip
```
**Example 4: With PowerShell version 2, you must use New-Object to create the IpPermission object.**

```
$ip = New-Object Amazon.EC2.Model.IpPermission
$ip.IpProtocol = "tcp"
$ip.FromPort = 22
$ip.ToPort = 22
$ip.IpRanges.Add("203.0.113.0/24")

Revoke-EC2SecurityGroupIngress -GroupName "my-security-group" -IpPermission $ip
```
+  For API details, see [RevokeSecurityGroupIngress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Send-EC2InstanceStatus`
<a name="ec2_ReportInstanceStatus_powershell_topic"></a>

The following code example shows how to use `Send-EC2InstanceStatus`.

**Tools for PowerShell V4**
**Example 1: This example reports status feedback for the specified instance.**

```
Send-EC2InstanceStatus -Instance i-12345678 -Status impaired -ReasonCode unresponsive
```
+  For API details, see [ReportInstanceStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Set-EC2NetworkAclAssociation`
<a name="ec2_ReplaceNetworkAclAssociation_powershell_topic"></a>

The following code example shows how to use `Set-EC2NetworkAclAssociation`.

**Tools for PowerShell V4**
**Example 1: This example associates the specified network ACL with the subnet for the specified network ACL association.**

```
Set-EC2NetworkAclAssociation -NetworkAclId acl-12345678 -AssociationId aclassoc-1a2b3c4d
```
**Output:**

```
aclassoc-87654321
```
+  For API details, see [ReplaceNetworkAclAssociation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Set-EC2NetworkAclEntry`
<a name="ec2_ReplaceNetworkAclEntry_powershell_topic"></a>

The following code example shows how to use `Set-EC2NetworkAclEntry`.

**Tools for PowerShell V4**
**Example 1: This example replaces the specified entry for the specified network ACL. The new rule allows inbound traffic from the specified address to any associated subnet.**

```
Set-EC2NetworkAclEntry -NetworkAclId acl-12345678 -Egress $false -RuleNumber 100 -Protocol 17 -PortRange_From 53 -PortRange_To 53 -CidrBlock 203.0.113.12/24 -RuleAction allow
```
+  For API details, see [ReplaceNetworkAclEntry](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Set-EC2Route`
<a name="ec2_ReplaceRoute_powershell_topic"></a>

The following code example shows how to use `Set-EC2Route`.

**Tools for PowerShell V4**
**Example 1: This example replaces the specified route for the specified route table. The new route sends the specified traffic to the specified virtual private gateway.**

```
Set-EC2Route -RouteTableId rtb-1a2b3c4d -DestinationCidrBlock 10.0.0.0/24 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [ReplaceRoute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Set-EC2RouteTableAssociation`
<a name="ec2_ReplaceRouteTableAssociation_powershell_topic"></a>

The following code example shows how to use `Set-EC2RouteTableAssociation`.

**Tools for PowerShell V4**
**Example 1: This example associates the specified route table with the subnet for the specified route table association.**

```
Set-EC2RouteTableAssociation -RouteTableId rtb-1a2b3c4d -AssociationId rtbassoc-12345678
```
**Output:**

```
rtbassoc-87654321
```
+  For API details, see [ReplaceRouteTableAssociation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Start-EC2Instance`
<a name="ec2_StartInstances_powershell_topic"></a>

The following code example shows how to use `Start-EC2Instance`.

**Tools for PowerShell V4**
**Example 1: This example starts the specified instance.**

```
Start-EC2Instance -InstanceId i-12345678
```
**Output:**

```
CurrentState                      InstanceId    PreviousState
------------                      ----------    -------------
Amazon.EC2.Model.InstanceState    i-12345678    Amazon.EC2.Model.InstanceState
```
**Example 2: This example starts the specified instances.**

```
@("i-12345678", "i-76543210") | Start-EC2Instance
```
**Example 3: This example starts the set of instances that are currently stopped. The Instance objects returned by Get-EC2Instance are piped to Start-EC2Instance. The syntax used by this example requires PowerShell version 3 or higher.**

```
(Get-EC2Instance -Filter @{ Name="instance-state-name"; Values="stopped"}).Instances | Start-EC2Instance
```
**Example 4: With PowerShell version 2, you must use New-Object to create the filter for the Filter parameter.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "instance-state-name"
$filter.Values = "stopped"

(Get-EC2Instance -Filter $filter).Instances | Start-EC2Instance
```
+  For API details, see [StartInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Start-EC2InstanceMonitoring`
<a name="ec2_MonitorInstances_powershell_topic"></a>

The following code example shows how to use `Start-EC2InstanceMonitoring`.

**Tools for PowerShell V4**
**Example 1: This example enables detailed monitoring for the specified instance.**

```
Start-EC2InstanceMonitoring -InstanceId i-12345678
```
**Output:**

```
InstanceId    Monitoring
----------    ----------
i-12345678    Amazon.EC2.Model.Monitoring
```
+  For API details, see [MonitorInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Stop-EC2ImportTask`
<a name="ec2_CancelImportTask_powershell_topic"></a>

The following code example shows how to use `Stop-EC2ImportTask`.

**Tools for PowerShell V4**
**Example 1: This example cancels the specified import task (either snapshot or image import). If required, a reason can be providing using the `-CancelReason` parameter.**

```
Stop-EC2ImportTask -ImportTaskId import-ami-abcdefgh
```
+  For API details, see [CancelImportTask](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Stop-EC2Instance`
<a name="ec2_StopInstances_powershell_topic"></a>

The following code example shows how to use `Stop-EC2Instance`.

**Tools for PowerShell V4**
**Example 1: This example stops the specified instance.**

```
Stop-EC2Instance -InstanceId i-12345678
```
**Output:**

```
CurrentState                      InstanceId    PreviousState
------------                      ----------    -------------
Amazon.EC2.Model.InstanceState    i-12345678    Amazon.EC2.Model.InstanceState
```
+  For API details, see [StopInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Stop-EC2InstanceMonitoring`
<a name="ec2_UnmonitorInstances_powershell_topic"></a>

The following code example shows how to use `Stop-EC2InstanceMonitoring`.

**Tools for PowerShell V4**
**Example 1: This example disables detailed monitoring for the specified instance.**

```
Stop-EC2InstanceMonitoring -InstanceId i-12345678
```
**Output:**

```
InstanceId    Monitoring
----------    ----------
i-12345678    Amazon.EC2.Model.Monitoring
```
+  For API details, see [UnmonitorInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Stop-EC2SpotFleetRequest`
<a name="ec2_CancelSpotFleetRequests_powershell_topic"></a>

The following code example shows how to use `Stop-EC2SpotFleetRequest`.

**Tools for PowerShell V4**
**Example 1: This example cancels the specified Spot fleet request and terminates the associated Spot instances.**

```
Stop-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -TerminateInstance $true
```
**Example 2: This example cancels the specified Spot fleet request without terminating the associated Spot instances.**

```
Stop-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -TerminateInstance $false
```
+  For API details, see [CancelSpotFleetRequests](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Stop-EC2SpotInstanceRequest`
<a name="ec2_CancelSpotInstanceRequests_powershell_topic"></a>

The following code example shows how to use `Stop-EC2SpotInstanceRequest`.

**Tools for PowerShell V4**
**Example 1: This example cancels the specified Spot instance request.**

```
Stop-EC2SpotInstanceRequest -SpotInstanceRequestId sir-12345678
```
**Output:**

```
SpotInstanceRequestId    State
---------------------    -----
sir-12345678             cancelled
```
+  For API details, see [CancelSpotInstanceRequests](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-EC2Address`
<a name="ec2_DisassociateAddress_powershell_topic"></a>

The following code example shows how to use `Unregister-EC2Address`.

**Tools for PowerShell V4**
**Example 1: This example disassociates the specified Elastic IP address from the specified instance in a VPC.**

```
Unregister-EC2Address -AssociationId eipassoc-12345678
```
**Example 2: This example disassociates the specified Elastic IP address from the specified instance in EC2-Classic.**

```
Unregister-EC2Address -PublicIp 203.0.113.17
```
+  For API details, see [DisassociateAddress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-EC2Image`
<a name="ec2_DeregisterImage_powershell_topic"></a>

The following code example shows how to use `Unregister-EC2Image`.

**Tools for PowerShell V4**
**Example 1: This example deregisters the specified AMI.**

```
Unregister-EC2Image -ImageId ami-12345678
```
+  For API details, see [DeregisterImage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-EC2PrivateIpAddress`
<a name="ec2_UnassignPrivateIpAddresses_powershell_topic"></a>

The following code example shows how to use `Unregister-EC2PrivateIpAddress`.

**Tools for PowerShell V4**
**Example 1: This example unassigns the specified private IP address from the specified network interface.**

```
Unregister-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82
```
+  For API details, see [UnassignPrivateIpAddresses](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Unregister-EC2RouteTable`
<a name="ec2_DisassociateRouteTable_powershell_topic"></a>

The following code example shows how to use `Unregister-EC2RouteTable`.

**Tools for PowerShell V4**
**Example 1: This example removes the specified association between a route table and a subnet.**

```
Unregister-EC2RouteTable -AssociationId rtbassoc-1a2b3c4d
```
+  For API details, see [DisassociateRouteTable](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-EC2SecurityGroupRuleIngressDescription`
<a name="ec2_UpdateSecurityGroupRuleDescriptionsIngress_powershell_topic"></a>

The following code example shows how to use `Update-EC2SecurityGroupRuleIngressDescription`.

**Tools for PowerShell V4**
**Example 1: Updates the description of an existing ingress (inbound) security group rule.**

```
$existingInboundRule = Get-EC2SecurityGroupRule -SecurityGroupRuleId "sgr-1234567890"
$ruleWithUpdatedDescription = [Amazon.EC2.Model.SecurityGroupRuleDescription]@{
  "SecurityGroupRuleId" = $existingInboundRule.SecurityGroupRuleId
  "Description" = "Updated rule description"
}

Update-EC2SecurityGroupRuleIngressDescription -GroupId $existingInboundRule.GroupId -SecurityGroupRuleDescription $ruleWithUpdatedDescription
```
**Example 2: Removes the description of an existing ingress (inbound) security group rule (by omitting the parameter in the request).**

```
$existingInboundRule = Get-EC2SecurityGroupRule -SecurityGroupRuleId "sgr-1234567890"
$ruleWithoutDescription = [Amazon.EC2.Model.SecurityGroupRuleDescription]@{
  "SecurityGroupRuleId" = $existingInboundRule.SecurityGroupRuleId
}

Update-EC2SecurityGroupRuleIngressDescription -GroupId $existingInboundRule.GroupId -SecurityGroupRuleDescription $ruleWithoutDescription
```
+  For API details, see [UpdateSecurityGroupRuleDescriptionsIngress](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
