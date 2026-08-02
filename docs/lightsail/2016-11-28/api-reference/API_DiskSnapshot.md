---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DiskSnapshot.html
---

# DiskSnapshot
<a name="API_DiskSnapshot"></a>

Describes a block storage disk snapshot.

## Contents
<a name="API_DiskSnapshot_Contents"></a>

 ** arn **   <a name="Lightsail-Type-DiskSnapshot-arn"></a>
The Amazon Resource Name (ARN) of the disk snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-DiskSnapshot-createdAt"></a>
The date when the disk snapshot was created.
Type: Timestamp
Required: No

 ** fromDiskArn **   <a name="Lightsail-Type-DiskSnapshot-fromDiskArn"></a>
The Amazon Resource Name (ARN) of the source disk from which the disk snapshot was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** fromDiskName **   <a name="Lightsail-Type-DiskSnapshot-fromDiskName"></a>
The unique name of the source disk from which the disk snapshot was created.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** fromInstanceArn **   <a name="Lightsail-Type-DiskSnapshot-fromInstanceArn"></a>
The Amazon Resource Name (ARN) of the source instance from which the disk (system volume) snapshot was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** fromInstanceName **   <a name="Lightsail-Type-DiskSnapshot-fromInstanceName"></a>
The unique name of the source instance from which the disk (system volume) snapshot was created.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** isFromAutoSnapshot **   <a name="Lightsail-Type-DiskSnapshot-isFromAutoSnapshot"></a>
A Boolean value indicating whether the snapshot was created from an automatic snapshot.
Type: Boolean
Required: No

 ** location **   <a name="Lightsail-Type-DiskSnapshot-location"></a>
The AWS Region and Availability Zone where the disk snapshot was created.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-DiskSnapshot-name"></a>
The name of the disk snapshot (`my-disk-snapshot`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** progress **   <a name="Lightsail-Type-DiskSnapshot-progress"></a>
The progress of the snapshot.
Type: String
Required: No

 ** resourceType **   <a name="Lightsail-Type-DiskSnapshot-resourceType"></a>
The Lightsail resource type (`DiskSnapshot`).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** sizeInGb **   <a name="Lightsail-Type-DiskSnapshot-sizeInGb"></a>
The size of the disk in GB.
Type: Integer
Required: No

 ** state **   <a name="Lightsail-Type-DiskSnapshot-state"></a>
The status of the disk snapshot operation.
Type: String
Valid Values: `pending | completed | error | unknown`
Required: No

 ** supportCode **   <a name="Lightsail-Type-DiskSnapshot-supportCode"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-DiskSnapshot-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_DiskSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DiskSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DiskSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DiskSnapshot)
