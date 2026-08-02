---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ExportSnapshotRecord.html
---

# ExportSnapshotRecord
<a name="API_ExportSnapshotRecord"></a>

Describes an export snapshot record.

## Contents
<a name="API_ExportSnapshotRecord_Contents"></a>

 ** arn **   <a name="Lightsail-Type-ExportSnapshotRecord-arn"></a>
The Amazon Resource Name (ARN) of the export snapshot record.
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-ExportSnapshotRecord-createdAt"></a>
The date when the export snapshot record was created.
Type: Timestamp
Required: No

 ** destinationInfo **   <a name="Lightsail-Type-ExportSnapshotRecord-destinationInfo"></a>
A list of objects describing the destination of the export snapshot record.
Type: [DestinationInfo](API_DestinationInfo.md) object
Required: No

 ** location **   <a name="Lightsail-Type-ExportSnapshotRecord-location"></a>
The AWS Region and Availability Zone where the export snapshot record is located.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-ExportSnapshotRecord-name"></a>
The export snapshot record name.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** resourceType **   <a name="Lightsail-Type-ExportSnapshotRecord-resourceType"></a>
The Lightsail resource type (`ExportSnapshotRecord`).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** sourceInfo **   <a name="Lightsail-Type-ExportSnapshotRecord-sourceInfo"></a>
A list of objects describing the source of the export snapshot record.
Type: [ExportSnapshotRecordSourceInfo](API_ExportSnapshotRecordSourceInfo.md) object
Required: No

 ** state **   <a name="Lightsail-Type-ExportSnapshotRecord-state"></a>
The state of the export snapshot record.
Type: String
Valid Values: `Started | Succeeded | Failed`
Required: No

## See Also
<a name="API_ExportSnapshotRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ExportSnapshotRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ExportSnapshotRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ExportSnapshotRecord)
