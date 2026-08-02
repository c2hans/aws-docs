---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ExportSnapshotRecordSourceInfo.html
---

# ExportSnapshotRecordSourceInfo
<a name="API_ExportSnapshotRecordSourceInfo"></a>

Describes the source of an export snapshot record.

## Contents
<a name="API_ExportSnapshotRecordSourceInfo_Contents"></a>

 ** arn **   <a name="Lightsail-Type-ExportSnapshotRecordSourceInfo-arn"></a>
The Amazon Resource Name (ARN) of the source instance or disk snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-ExportSnapshotRecordSourceInfo-createdAt"></a>
The date when the source instance or disk snapshot was created.
Type: Timestamp
Required: No

 ** diskSnapshotInfo **   <a name="Lightsail-Type-ExportSnapshotRecordSourceInfo-diskSnapshotInfo"></a>
A list of objects describing a disk snapshot.
Type: [DiskSnapshotInfo](API_DiskSnapshotInfo.md) object
Required: No

 ** fromResourceArn **   <a name="Lightsail-Type-ExportSnapshotRecordSourceInfo-fromResourceArn"></a>
The Amazon Resource Name (ARN) of the snapshot's source instance or disk.
Type: String
Pattern: `.*\S.*`
Required: No

 ** fromResourceName **   <a name="Lightsail-Type-ExportSnapshotRecordSourceInfo-fromResourceName"></a>
The name of the snapshot's source instance or disk.
Type: String
Pattern: `.*\S.*`
Required: No

 ** instanceSnapshotInfo **   <a name="Lightsail-Type-ExportSnapshotRecordSourceInfo-instanceSnapshotInfo"></a>
A list of objects describing an instance snapshot.
Type: [InstanceSnapshotInfo](API_InstanceSnapshotInfo.md) object
Required: No

 ** name **   <a name="Lightsail-Type-ExportSnapshotRecordSourceInfo-name"></a>
The name of the source instance or disk snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** resourceType **   <a name="Lightsail-Type-ExportSnapshotRecordSourceInfo-resourceType"></a>
The Lightsail resource type (`InstanceSnapshot` or `DiskSnapshot`).
Type: String
Valid Values: `InstanceSnapshot | DiskSnapshot`
Required: No

## See Also
<a name="API_ExportSnapshotRecordSourceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ExportSnapshotRecordSourceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ExportSnapshotRecordSourceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ExportSnapshotRecordSourceInfo)
