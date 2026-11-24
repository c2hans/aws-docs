---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapshotPolicy.html
---

# SnapshotPolicy

Describes an Amazon FSx for NetApp ONTAP snapshot policy.

## Contents
<a name="API_SnapshotPolicy_Contents"></a>

 ** Enabled **   <a name="FSx-Type-SnapshotPolicy-Enabled"></a>
Specifies whether the snapshot policy is enabled. This value defaults to `true`.
Type: Boolean
Required: No

 ** FileSystemId **   <a name="FSx-Type-SnapshotPolicy-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `^(fs-[0-9a-f]{8,})$`
Required: No

 ** Lifecycle **   <a name="FSx-Type-SnapshotPolicy-Lifecycle"></a>
The lifecycle status of the snapshot policy can be one of the following:
+  `CREATED` – The snapshot policy is fully available for use.
+  `CREATING` – Amazon FSx is creating the snapshot policy.
+  `DELETING` – Amazon FSx is deleting the snapshot policy.
+  `FAILED` – Amazon FSx was unable to create the snapshot policy.
Type: String
Valid Values: `CREATING | CREATED | DELETING | FAILED`
Required: No

 ** LifecycleTransitionReason **   <a name="FSx-Type-SnapshotPolicy-LifecycleTransitionReason"></a>
The reason why the snapshot policy lifecycle status changed.
Type: [LifecycleTransitionReason](API_LifecycleTransitionReason.md) object
Required: No

 ** Name **   <a name="FSx-Type-SnapshotPolicy-Name"></a>
The name of the snapshot policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ResourceARN **   <a name="FSx-Type-SnapshotPolicy-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 512.
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`
Required: No

 ** Schedules **   <a name="FSx-Type-SnapshotPolicy-Schedules"></a>
The schedules on which ONTAP creates snapshots for the snapshot policy.
Type: Array of [SnapshotPolicySchedule](API_SnapshotPolicySchedule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** Scope **   <a name="FSx-Type-SnapshotPolicy-Scope"></a>
The scope of the snapshot policy can be one of the following:
+  `FILESYSTEM` – The snapshot policy was created on the file system.
+  `SVM` – The snapshot policy was created on an SVM.
Type: String
Valid Values: `FILESYSTEM | SVM`
Required: No

 ** SnapshotPolicyId **   <a name="FSx-Type-SnapshotPolicy-SnapshotPolicyId"></a>
The system-generated, unique ID of the snapshot policy.
Type: String
Length Constraints: Fixed length of 29.
Pattern: `^snapshotpol-[0-9a-f]{17}$`
Required: No

 ** StorageVirtualMachineId **   <a name="FSx-Type-SnapshotPolicy-StorageVirtualMachineId"></a>
The ID of the snapshot policy's storage virtual machine, if you created the snapshot policy on a storage virtual machine.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^(svm-[0-9a-f]{17,})$`
Required: No

 ** Tags **   <a name="FSx-Type-SnapshotPolicy-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** UUID **   <a name="FSx-Type-SnapshotPolicy-UUID"></a>
The snapshot policy's universally unique identifier (UUID).
Type: String
Length Constraints: Maximum length of 36.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,36}$`
Required: No

## See Also
<a name="API_SnapshotPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapshotPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapshotPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapshotPolicy)
