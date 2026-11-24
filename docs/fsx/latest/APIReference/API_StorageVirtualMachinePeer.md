---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_StorageVirtualMachinePeer.html
---

# StorageVirtualMachinePeer

Describes an Amazon FSx for NetApp ONTAP storage virtual machine (SVM) peer relationship.

## Contents
<a name="API_StorageVirtualMachinePeer_Contents"></a>

 ** Applications **   <a name="FSx-Type-StorageVirtualMachinePeer-Applications"></a>
The applications that the SVM peer relationship authorizes. The applications can be one or more of the following:
+  `SNAPMIRROR` – SnapMirror replication.
+  `FILE_COPY` – File copy.
+  `LUN_COPY` – LUN copy.
+  `FLEXCACHE` – FlexCache.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SNAPMIRROR | FILE_COPY | LUN_COPY | FLEXCACHE`
Required: No

 ** FileSystemId **   <a name="FSx-Type-StorageVirtualMachinePeer-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `^(fs-[0-9a-f]{8,})$`
Required: No

 ** Lifecycle **   <a name="FSx-Type-StorageVirtualMachinePeer-Lifecycle"></a>
The lifecycle status of the SVM peer can be one of the following:
+  `CREATED` – The SVM peer is fully available for use.
+  `CREATING` – Amazon FSx is creating the SVM peer.
+  `DELETING` – Amazon FSx is deleting the SVM peer.
+  `FAILED` – Amazon FSx was unable to create the SVM peer.
Type: String
Valid Values: `CREATING | CREATED | DELETING | FAILED`
Required: No

 ** LifecycleTransitionReason **   <a name="FSx-Type-StorageVirtualMachinePeer-LifecycleTransitionReason"></a>
The reason why the SVM peer lifecycle status changed.
Type: [LifecycleTransitionReason](API_LifecycleTransitionReason.md) object
Required: No

 ** PeerClusterName **   <a name="FSx-Type-StorageVirtualMachinePeer-PeerClusterName"></a>
The name of the peer cluster that the peer SVM is on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 44.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,44}$`
Required: No

 ** PeerSvmAlias **   <a name="FSx-Type-StorageVirtualMachinePeer-PeerSvmAlias"></a>
The name that the local cluster uses to identify the peer SVM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 41.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,41}$`
Required: No

 ** PeerSvmName **   <a name="FSx-Type-StorageVirtualMachinePeer-PeerSvmName"></a>
The name of the SVM on the peer cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,47}$`
Required: No

 ** ResourceARN **   <a name="FSx-Type-StorageVirtualMachinePeer-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 512.
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`
Required: No

 ** State **   <a name="FSx-Type-StorageVirtualMachinePeer-State"></a>
The state of the SVM peer relationship in ONTAP can be one of the following:
+  `PEERED` – The SVM peer relationship is established.
+  `INITIATED` – The local cluster sent a peering request to the peer SVM.
+  `PENDING` – A peering request from the peer SVM is waiting for acceptance.
+  `INITIALIZING` – ONTAP is setting up the SVM peer relationship.
+  `SUSPENDED` – The SVM peer relationship is suspended.
+  `REJECTED` – The peering request was rejected.
Type: String
Valid Values: `PEERED | REJECTED | SUSPENDED | INITIATED | PENDING | INITIALIZING`
Required: No

 ** StorageVirtualMachineId **   <a name="FSx-Type-StorageVirtualMachinePeer-StorageVirtualMachineId"></a>
The ID of the SVM on the file system that the SVM peer relationship belongs to.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^(svm-[0-9a-f]{17,})$`
Required: No

 ** StorageVirtualMachinePeerId **   <a name="FSx-Type-StorageVirtualMachinePeer-StorageVirtualMachinePeerId"></a>
The system-generated, unique ID of the SVM peer.
Type: String
Pattern: `^(svmpeer-[0-9a-f]{17})$`
Required: No

 ** Tags **   <a name="FSx-Type-StorageVirtualMachinePeer-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** UUID **   <a name="FSx-Type-StorageVirtualMachinePeer-UUID"></a>
The SVM peer's universally unique identifier (UUID).
Type: String
Length Constraints: Maximum length of 36.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,36}$`
Required: No

## See Also
<a name="API_StorageVirtualMachinePeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/StorageVirtualMachinePeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/StorageVirtualMachinePeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/StorageVirtualMachinePeer)
