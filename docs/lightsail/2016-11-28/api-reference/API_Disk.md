---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Disk.html
---

# Disk
<a name="API_Disk"></a>

Describes a block storage disk.

## Contents
<a name="API_Disk_Contents"></a>

 ** addOns **   <a name="Lightsail-Type-Disk-addOns"></a>
An array of objects representing the add-ons enabled on the disk.
Type: Array of [AddOn](API_AddOn.md) objects
Required: No

 ** arn **   <a name="Lightsail-Type-Disk-arn"></a>
The Amazon Resource Name (ARN) of the disk.
Type: String
Pattern: `.*\S.*`
Required: No

 ** attachedTo **   <a name="Lightsail-Type-Disk-attachedTo"></a>
The resources to which the disk is attached.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** attachmentState **   <a name="Lightsail-Type-Disk-attachmentState"></a>
 *This member has been deprecated.*
(Discontinued) The attachment state of the disk.
In releases prior to November 14, 2017, this parameter returned `attached` for system disks in the API response. It is now discontinued, but still included in the response. Use `isAttached` instead.
Type: String
Required: No

 ** autoMountStatus **   <a name="Lightsail-Type-Disk-autoMountStatus"></a>
The status of automatically mounting a storage disk to a virtual computer.
This parameter only applies to Lightsail for Research resources.
Type: String
Valid Values: `Failed | Pending | Mounted | NotMounted`
Required: No

 ** createdAt **   <a name="Lightsail-Type-Disk-createdAt"></a>
The date when the disk was created.
Type: Timestamp
Required: No

 ** gbInUse **   <a name="Lightsail-Type-Disk-gbInUse"></a>
 *This member has been deprecated.*
(Discontinued) The number of GB in use by the disk.
In releases prior to November 14, 2017, this parameter was not included in the API response. It is now discontinued.
Type: Integer
Required: No

 ** iops **   <a name="Lightsail-Type-Disk-iops"></a>
The input/output operations per second (IOPS) of the disk.
Type: Integer
Required: No

 ** isAttached **   <a name="Lightsail-Type-Disk-isAttached"></a>
A Boolean value indicating whether the disk is attached.
Type: Boolean
Required: No

 ** isSystemDisk **   <a name="Lightsail-Type-Disk-isSystemDisk"></a>
A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
Type: Boolean
Required: No

 ** location **   <a name="Lightsail-Type-Disk-location"></a>
The AWS Region and Availability Zone where the disk is located.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-Disk-name"></a>
The unique name of the disk.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** path **   <a name="Lightsail-Type-Disk-path"></a>
The disk path.
Type: String
Required: No

 ** resourceType **   <a name="Lightsail-Type-Disk-resourceType"></a>
The Lightsail resource type (`Disk`).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** sizeInGb **   <a name="Lightsail-Type-Disk-sizeInGb"></a>
The size of the disk in GB.
Type: Integer
Required: No

 ** state **   <a name="Lightsail-Type-Disk-state"></a>
Describes the status of the disk.
Type: String
Valid Values: `pending | error | available | in-use | unknown`
Required: No

 ** supportCode **   <a name="Lightsail-Type-Disk-supportCode"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-Disk-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Disk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Disk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Disk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Disk)
