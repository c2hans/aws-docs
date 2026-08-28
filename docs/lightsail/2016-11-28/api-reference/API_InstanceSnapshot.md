---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceSnapshot.html
---

# InstanceSnapshot
<a name="API_InstanceSnapshot"></a>

Describes an instance snapshot.

## Contents
<a name="API_InstanceSnapshot_Contents"></a>

 ** arn **   <a name="Lightsail-Type-InstanceSnapshot-arn"></a>
The Amazon Resource Name (ARN) of the snapshot (`arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-InstanceSnapshot-createdAt"></a>
The timestamp when the snapshot was created (`1479907467.024`).
Type: Timestamp
Required: No

 ** fromAttachedDisks **   <a name="Lightsail-Type-InstanceSnapshot-fromAttachedDisks"></a>
An array of disk objects containing information about all block storage disks.
Type: Array of [Disk](API_Disk.md) objects
Required: No

 ** fromBlueprintId **   <a name="Lightsail-Type-InstanceSnapshot-fromBlueprintId"></a>
The blueprint ID from which you created the snapshot (`amazon_linux_2023`). A blueprint is a virtual private server (or *instance*) image used to create instances quickly.
Type: String
Required: No

 ** fromBundleId **   <a name="Lightsail-Type-InstanceSnapshot-fromBundleId"></a>
The bundle ID from which you created the snapshot (`micro_x_x`).
Type: String
Required: No

 ** fromInstanceArn **   <a name="Lightsail-Type-InstanceSnapshot-fromInstanceArn"></a>
The Amazon Resource Name (ARN) of the instance from which the snapshot was created (`arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** fromInstanceName **   <a name="Lightsail-Type-InstanceSnapshot-fromInstanceName"></a>
The instance from which the snapshot was created.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** isFromAutoSnapshot **   <a name="Lightsail-Type-InstanceSnapshot-isFromAutoSnapshot"></a>
A Boolean value indicating whether the snapshot was created from an automatic snapshot.
Type: Boolean
Required: No

 ** location **   <a name="Lightsail-Type-InstanceSnapshot-location"></a>
The region name and Availability Zone where you created the snapshot.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-InstanceSnapshot-name"></a>
The name of the snapshot.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** progress **   <a name="Lightsail-Type-InstanceSnapshot-progress"></a>
The progress of the snapshot.
This is populated only for disk snapshots, and is `null` for instance snapshots.
Type: String
Required: No

 ** resourceType **   <a name="Lightsail-Type-InstanceSnapshot-resourceType"></a>
The type of resource (usually `InstanceSnapshot`).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** sizeInGb **   <a name="Lightsail-Type-InstanceSnapshot-sizeInGb"></a>
The size in GB of the SSD.
Type: Integer
Required: No

 ** state **   <a name="Lightsail-Type-InstanceSnapshot-state"></a>
The state the snapshot is in.
Type: String
Valid Values: `pending | error | available`
Required: No

 ** supportCode **   <a name="Lightsail-Type-InstanceSnapshot-supportCode"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-InstanceSnapshot-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_InstanceSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
