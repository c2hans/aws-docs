---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapmirrorPolicy.html
---

# SnapmirrorPolicy

Describes an Amazon FSx for NetApp ONTAP SnapMirror policy.

## Contents
<a name="API_SnapmirrorPolicy_Contents"></a>

 ** FileSystemId **   <a name="FSx-Type-SnapmirrorPolicy-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `^(fs-[0-9a-f]{8,})$`
Required: No

 ** Lifecycle **   <a name="FSx-Type-SnapmirrorPolicy-Lifecycle"></a>
The lifecycle status of the SnapMirror policy can be one of the following:
+  `CREATED` – The SnapMirror policy is fully available for use.
+  `CREATING` – Amazon FSx is creating the SnapMirror policy.
+  `DELETING` – Amazon FSx is deleting the SnapMirror policy.
+  `FAILED` – Amazon FSx was unable to create the SnapMirror policy.
Type: String
Valid Values: `CREATING | CREATED | DELETING | FAILED`
Required: No

 ** LifecycleTransitionReason **   <a name="FSx-Type-SnapmirrorPolicy-LifecycleTransitionReason"></a>
The reason why the SnapMirror policy lifecycle status changed.
Type: [LifecycleTransitionReason](API_LifecycleTransitionReason.md) object
Required: No

 ** Name **   <a name="FSx-Type-SnapmirrorPolicy-Name"></a>
The name of the SnapMirror policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** NetworkCompressionEnabled **   <a name="FSx-Type-SnapmirrorPolicy-NetworkCompressionEnabled"></a>
Specifies whether SnapMirror compresses data when it transfers the data over the network. This value defaults to `false`.
Type: Boolean
Required: No

 ** ResourceARN **   <a name="FSx-Type-SnapmirrorPolicy-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 512.
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`
Required: No

 ** RetentionRules **   <a name="FSx-Type-SnapmirrorPolicy-RetentionRules"></a>
The rules that determine which snapshots SnapMirror retains on the destination volume.
Type: Array of [SnapmirrorPolicyRetentionRule](API_SnapmirrorPolicyRetentionRule.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** Scope **   <a name="FSx-Type-SnapmirrorPolicy-Scope"></a>
The scope of the SnapMirror policy can be one of the following:
+  `FILESYSTEM` – The SnapMirror policy was created on the file system.
+  `SVM` – The SnapMirror policy was created on an SVM.
Type: String
Valid Values: `FILESYSTEM | SVM`
Required: No

 ** SnapmirrorPolicyId **   <a name="FSx-Type-SnapmirrorPolicy-SnapmirrorPolicyId"></a>
The system-generated, unique ID of the SnapMirror policy.
Type: String
Pattern: `^(snapmirrorpol-[0-9a-f]{17})$`
Required: No

 ** SnapshotCopyMode **   <a name="FSx-Type-SnapmirrorPolicy-SnapshotCopyMode"></a>
The snapshot copy mode of the SnapMirror policy, which determines which snapshots SnapMirror transfers to the destination volume.
Type: String
Valid Values: `COPY_ALL_SOURCE_SNAPSHOTS | COPY_LATEST_SOURCE_SNAPSHOT | NO_CREATE_SNAPSHOT_ON_SOURCE`
Required: No

 ** StorageVirtualMachineId **   <a name="FSx-Type-SnapmirrorPolicy-StorageVirtualMachineId"></a>
The ID of the SnapMirror policy's storage virtual machine, if you created the SnapMirror policy on a storage virtual machine.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^(svm-[0-9a-f]{17,})$`
Required: No

 ** Tags **   <a name="FSx-Type-SnapmirrorPolicy-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** ThrottleInKbps **   <a name="FSx-Type-SnapmirrorPolicy-ThrottleInKbps"></a>
The maximum bandwidth, in kilobytes per second (KBps), that SnapMirror uses to transfer data. A value of `0` means that the bandwidth is unlimited.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** TransferSchedule **   <a name="FSx-Type-SnapmirrorPolicy-TransferSchedule"></a>
The name of the ONTAP schedule that determines when SnapMirror transfers data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_:.-]{0,256}$`
Required: No

 ** UUID **   <a name="FSx-Type-SnapmirrorPolicy-UUID"></a>
The SnapMirror policy's universally unique identifier (UUID).
Type: String
Length Constraints: Maximum length of 36.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,36}$`
Required: No

## See Also
<a name="API_SnapmirrorPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapmirrorPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapmirrorPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapmirrorPolicy)
