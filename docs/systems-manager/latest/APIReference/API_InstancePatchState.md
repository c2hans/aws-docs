---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstancePatchState.html
---

# InstancePatchState
<a name="API_InstancePatchState"></a>

Defines the high-level patch compliance state for a managed node, providing information about the number of installed, missing, not applicable, and failed patches along with metadata about the operation when this information was gathered for the managed node.

## Contents
<a name="API_InstancePatchState_Contents"></a>

 ** BaselineId **   <a name="systemsmanager-Type-InstancePatchState-BaselineId"></a>
The ID of the patch baseline used to patch the managed node.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`
Required: Yes

 ** InstanceId **   <a name="systemsmanager-Type-InstancePatchState-InstanceId"></a>
The ID of the managed node the high-level patch compliance information was collected for.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** Operation **   <a name="systemsmanager-Type-InstancePatchState-Operation"></a>
The type of patching operation that was performed: or
+  `SCAN` assesses the patch compliance state.
+  `INSTALL` installs missing patches.
Type: String
Valid Values: `Scan | Install`
Required: Yes

 ** OperationEndTime **   <a name="systemsmanager-Type-InstancePatchState-OperationEndTime"></a>
The time the most recent patching operation completed on the managed node.
Type: Timestamp
Required: Yes

 ** OperationStartTime **   <a name="systemsmanager-Type-InstancePatchState-OperationStartTime"></a>
The time the most recent patching operation was started on the managed node.
Type: Timestamp
Required: Yes

 ** PatchGroup **   <a name="systemsmanager-Type-InstancePatchState-PatchGroup"></a>
The name of the patch group the managed node belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** AvailableSecurityUpdateCount **   <a name="systemsmanager-Type-InstancePatchState-AvailableSecurityUpdateCount"></a>
The number of security-related patches that are available but not approved because they didn't meet the patch baseline requirements. For example, an updated version of a patch might have been released before the specified auto-approval period was over.
Applies to Windows Server managed nodes only.
Type: Integer
Required: No

 ** CriticalNonCompliantCount **   <a name="systemsmanager-Type-InstancePatchState-CriticalNonCompliantCount"></a>
The number of patches per node that are specified as `Critical` for compliance reporting in the patch baseline aren't installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is `NON_COMPLIANT`.
Type: Integer
Required: No

 ** FailedCount **   <a name="systemsmanager-Type-InstancePatchState-FailedCount"></a>
The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.
Type: Integer
Required: No

 ** InstalledCount **   <a name="systemsmanager-Type-InstancePatchState-InstalledCount"></a>
The number of patches from the patch baseline that are installed on the managed node.
Type: Integer
Required: No

 ** InstalledOtherCount **   <a name="systemsmanager-Type-InstancePatchState-InstalledOtherCount"></a>
The number of patches not specified in the patch baseline that are installed on the managed node.
Type: Integer
Required: No

 ** InstalledPendingRebootCount **   <a name="systemsmanager-Type-InstancePatchState-InstalledPendingRebootCount"></a>
The number of patches installed by Patch Manager since the last time the managed node was rebooted.
Type: Integer
Required: No

 ** InstalledRejectedCount **   <a name="systemsmanager-Type-InstancePatchState-InstalledRejectedCount"></a>
The number of patches installed on a managed node that are specified in a `RejectedPatches` list. Patches with a status of `InstalledRejected` were typically installed before they were added to a `RejectedPatches` list.
If `ALLOW_AS_DEPENDENCY` is the specified option for `RejectedPatchesAction`, the value of `InstalledRejectedCount` will always be `0` (zero).
Type: Integer
Required: No

 ** InstallOverrideList **   <a name="systemsmanager-Type-InstancePatchState-InstallOverrideList"></a>
An https URL or an Amazon Simple Storage Service (Amazon S3) path-style URL to a list of patches to be installed. This patch installation list, which you maintain in an S3 bucket in YAML format and specify in the SSM document `AWS-RunPatchBaseline`, overrides the patches specified by the default patch baseline.
For more information about the `InstallOverrideList` parameter, see [SSM Command document for patching: `AWS-RunPatchBaseline`](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html) in the * AWS Systems Manager User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^https://.+$|^s3://([^/]+)/(.*?([^/]+))$`
Required: No

 ** LastNoRebootInstallOperationTime **   <a name="systemsmanager-Type-InstancePatchState-LastNoRebootInstallOperationTime"></a>
The time of the last attempt to patch the managed node with `NoReboot` specified as the reboot option.
Type: Timestamp
Required: No

 ** MissingCount **   <a name="systemsmanager-Type-InstancePatchState-MissingCount"></a>
The number of patches from the patch baseline that are applicable for the managed node but aren't currently installed.
Type: Integer
Required: No

 ** NotApplicableCount **   <a name="systemsmanager-Type-InstancePatchState-NotApplicableCount"></a>
The number of patches from the patch baseline that aren't applicable for the managed node and therefore aren't installed on the node. This number may be truncated if the list of patch names is very large. The number of patches beyond this limit are reported in `UnreportedNotApplicableCount`.
Type: Integer
Required: No

 ** OtherNonCompliantCount **   <a name="systemsmanager-Type-InstancePatchState-OtherNonCompliantCount"></a>
The number of patches per node that are specified as other than `Critical` or `Security` but aren't compliant with the patch baseline. The status of these managed nodes is `NON_COMPLIANT`.
Type: Integer
Required: No

 ** OwnerInformation **   <a name="systemsmanager-Type-InstancePatchState-OwnerInformation"></a>
Placeholder information. This field will always be empty in the current release of the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** RebootOption **   <a name="systemsmanager-Type-InstancePatchState-RebootOption"></a>
Indicates the reboot option specified in the patch baseline.
Reboot options apply to `Install` operations only. Reboots aren't attempted for Patch Manager `Scan` operations.
+  `RebootIfNeeded`: Patch Manager tries to reboot the managed node if it installed any patches, or if any patches are detected with a status of `InstalledPendingReboot`.
+  `NoReboot`: Patch Manager attempts to install missing packages without trying to reboot the system. Patches installed with this option are assigned a status of `InstalledPendingReboot`. These patches might not be in effect until a reboot is performed.
Type: String
Valid Values: `RebootIfNeeded | NoReboot`
Required: No

 ** SecurityNonCompliantCount **   <a name="systemsmanager-Type-InstancePatchState-SecurityNonCompliantCount"></a>
The number of patches per node that are specified as `Security` in a patch advisory aren't installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is `NON_COMPLIANT`.
Type: Integer
Required: No

 ** SnapshotId **   <a name="systemsmanager-Type-InstancePatchState-SnapshotId"></a>
The ID of the patch baseline snapshot used during the patching operation when this compliance data was collected.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

 ** UnreportedNotApplicableCount **   <a name="systemsmanager-Type-InstancePatchState-UnreportedNotApplicableCount"></a>
The number of patches beyond the supported limit of `NotApplicableCount` that aren't reported by name to Inventory. Inventory is a tool in AWS Systems Manager.
Type: Integer
Required: No

## See Also
<a name="API_InstancePatchState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstancePatchState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstancePatchState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstancePatchState)
