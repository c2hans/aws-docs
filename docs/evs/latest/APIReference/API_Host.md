---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_Host.html
---

# Host
<a name="API_Host"></a>

An ESX host that runs on an Amazon EC2 bare metal instance.

## Contents
<a name="API_Host_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** createdAt **   <a name="evs-Type-Host-createdAt"></a>
 The date and time that the host was created.
Type: Timestamp
Required: No

 ** dedicatedHostId **   <a name="evs-Type-Host-dedicatedHostId"></a>
The unique ID of the Amazon EC2 Dedicated Host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `h-[a-f0-9]{8}([a-f0-9]{9})?`
Required: No

 ** ec2InstanceId **   <a name="evs-Type-Host-ec2InstanceId"></a>
The unique ID of the EC2 instance that represents the host.
Type: String
Required: No

 ** hostName **   <a name="evs-Type-Host-hostName"></a>
The DNS hostname of the host. DNS hostnames for hosts must be unique across Amazon EVS environments and within VCF.
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: No

 ** hostState **   <a name="evs-Type-Host-hostState"></a>
 The state of the host.
Type: String
Valid Values: `CREATING | CREATED | UPDATING | DELETING | DELETED | CREATE_FAILED | UPDATE_FAILED`
Required: No

 ** instanceType **   <a name="evs-Type-Host-instanceType"></a>
The EC2 instance type of the host.
EC2 instances created through Amazon EVS do not support associating an IAM instance profile.
Type: String
Valid Values: `i4i.metal | i7i.metal-24xl`
Required: No

 ** ipAddress **   <a name="evs-Type-Host-ipAddress"></a>
The IP address of the host.
Type: String
Pattern: `(\d{1,3}\.){3}\d{1,3}`
Required: No

 ** keyName **   <a name="evs-Type-Host-keyName"></a>
The name of the SSH key that is used to access the host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** modifiedAt **   <a name="evs-Type-Host-modifiedAt"></a>
 The date and time that the host was modified.
Type: Timestamp
Required: No

 ** networkInterfaces **   <a name="evs-Type-Host-networkInterfaces"></a>
The elastic network interfaces that are attached to the host.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

 ** placementGroupId **   <a name="evs-Type-Host-placementGroupId"></a>
The unique ID of the placement group where the host is placed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `pg-[a-f0-9]{8}([a-f0-9]{9})?`
Required: No

 ** stateDetails **   <a name="evs-Type-Host-stateDetails"></a>
 A detailed description of the `hostState` of a host.
Type: String
Required: No

## See Also
<a name="API_Host_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/Host)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/Host)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/Host)
