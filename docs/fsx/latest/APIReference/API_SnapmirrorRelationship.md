---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapmirrorRelationship.html
---

# SnapmirrorRelationship

Describes an Amazon FSx for NetApp ONTAP SnapMirror relationship.

## Contents
<a name="API_SnapmirrorRelationship_Contents"></a>

 ** Destination **   <a name="FSx-Type-SnapmirrorRelationship-Destination"></a>
The destination endpoint of the SnapMirror relationship.
Type: [SnapmirrorDestination](API_SnapmirrorDestination.md) object
Required: No

 ** ExportedSnapshot **   <a name="FSx-Type-SnapmirrorRelationship-ExportedSnapshot"></a>
The latest snapshot that SnapMirror transferred to the destination volume.
Type: [SnapmirrorExportedSnapshot](API_SnapmirrorExportedSnapshot.md) object
Required: No

 ** FileSystemId **   <a name="FSx-Type-SnapmirrorRelationship-FileSystemId"></a>
The globally unique ID of the file system that the destination volume is on, assigned by Amazon FSx.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `^(fs-[0-9a-f]{8,})$`
Required: No

 ** Healthy **   <a name="FSx-Type-SnapmirrorRelationship-Healthy"></a>
Indicates whether ONTAP reports the SnapMirror relationship as healthy.
Type: Boolean
Required: No

 ** LagTimeInMinutes **   <a name="FSx-Type-SnapmirrorRelationship-LagTimeInMinutes"></a>
The time, in minutes, since ONTAP created the latest snapshot that SnapMirror transferred to the destination volume.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** Lifecycle **   <a name="FSx-Type-SnapmirrorRelationship-Lifecycle"></a>
The lifecycle status of the SnapMirror relationship can be one of the following:
+  `CREATED` – The SnapMirror relationship is fully available for use.
+  `CREATING` – Amazon FSx is creating the SnapMirror relationship.
+  `DELETING` – Amazon FSx is deleting the SnapMirror relationship.
+  `FAILED` – Amazon FSx was unable to create the SnapMirror relationship.
Type: String
Valid Values: `CREATING | CREATED | DELETING | FAILED`
Required: No

 ** LifecycleTransitionReason **   <a name="FSx-Type-SnapmirrorRelationship-LifecycleTransitionReason"></a>
The reason why the SnapMirror relationship lifecycle status changed.
Type: [LifecycleTransitionReason](API_LifecycleTransitionReason.md) object
Required: No

 ** ResourceARN **   <a name="FSx-Type-SnapmirrorRelationship-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 512.
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`
Required: No

 ** SnapmirrorPolicy **   <a name="FSx-Type-SnapmirrorRelationship-SnapmirrorPolicy"></a>
The SnapMirror policy that the SnapMirror relationship uses.
Type: [SnapmirrorRelationshipPolicy](API_SnapmirrorRelationshipPolicy.md) object
Required: No

 ** SnapmirrorRelationshipId **   <a name="FSx-Type-SnapmirrorRelationship-SnapmirrorRelationshipId"></a>
The system-generated, unique ID of the SnapMirror relationship.
Type: String
Pattern: `^(snapmirror-[0-9a-f]{17})$`
Required: No

 ** Source **   <a name="FSx-Type-SnapmirrorRelationship-Source"></a>
The source endpoint of the SnapMirror relationship.
Type: [SnapmirrorSource](API_SnapmirrorSource.md) object
Required: No

 ** State **   <a name="FSx-Type-SnapmirrorRelationship-State"></a>
The state of the SnapMirror relationship in ONTAP can be one of the following:
+  `UNINITIALIZED` – SnapMirror hasn't transferred the baseline copy of the source volume to the destination volume.
+  `TRANSFERRING` – SnapMirror is transferring data to the destination volume.
+  `SNAPMIRRORED` – SnapMirror transferred the baseline copy, and the destination volume receives updates from the source volume.
+  `PAUSED` – SnapMirror transfers for the relationship are paused.
+  `BROKEN_OFF` – The relationship is broken off, and the destination volume is writable. SnapMirror doesn't transfer data to the destination volume.
Type: String
Valid Values: `UNINITIALIZED | TRANSFERRING | SNAPMIRRORED | PAUSED | BROKEN_OFF`
Required: No

 ** Tags **   <a name="FSx-Type-SnapmirrorRelationship-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** ThrottleInKbps **   <a name="FSx-Type-SnapmirrorRelationship-ThrottleInKbps"></a>
The maximum bandwidth, in kilobytes per second (KBps), that SnapMirror uses to transfer data for the relationship. A value of `0` means that the bandwidth is unlimited. This value overrides the throttle of the SnapMirror policy.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** TransferSchedule **   <a name="FSx-Type-SnapmirrorRelationship-TransferSchedule"></a>
The name of the ONTAP schedule that determines when SnapMirror transfers data for the relationship. This schedule overrides the transfer schedule of the SnapMirror policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_:.-]{0,256}$`
Required: No

 ** TransferState **   <a name="FSx-Type-SnapmirrorRelationship-TransferState"></a>
The latest SnapMirror transfer for the relationship. If a transfer is in progress, this is the in-progress transfer. Otherwise, it's the most recently completed transfer.
Type: [SnapmirrorTransferState](API_SnapmirrorTransferState.md) object
Required: No

 ** UnhealthyReason **   <a name="FSx-Type-SnapmirrorRelationship-UnhealthyReason"></a>
The reason that ONTAP reports for why the SnapMirror relationship is unhealthy, if `Healthy` is `false`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** UUID **   <a name="FSx-Type-SnapmirrorRelationship-UUID"></a>
The SnapMirror relationship's universally unique identifier (UUID).
Type: String
Length Constraints: Maximum length of 36.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,36}$`
Required: No

## See Also
<a name="API_SnapmirrorRelationship_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapmirrorRelationship)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapmirrorRelationship)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapmirrorRelationship)
