---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_PendingMaintenanceAction.html
---

# PendingMaintenanceAction
<a name="API_PendingMaintenanceAction"></a>

Provides information about a pending maintenance action for a resource.

## Contents
<a name="API_PendingMaintenanceAction_Contents"></a>

 ** Action **
The type of pending maintenance action that is available for the resource.
Type: String
Required: No

 ** AutoAppliedAfterDate **
The date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any `next-maintenance` opt-in requests are ignored.
Type: Timestamp
Required: No

 ** CurrentApplyDate **
The effective date when the pending maintenance action is applied to the resource. This date takes into account opt-in requests received from the [ApplyPendingMaintenanceAction](API_ApplyPendingMaintenanceAction.md) API, the `AutoAppliedAfterDate`, and the `ForcedApplyDate`. This value is blank if an opt-in request has not been received and nothing has been specified as `AutoAppliedAfterDate` or `ForcedApplyDate`.
Type: Timestamp
Required: No

 ** Description **
A description providing more detail about the maintenance action.
Type: String
Required: No

 ** ForcedApplyDate **
The date when the maintenance action is automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any `immediate` opt-in requests are ignored.
Type: Timestamp
Required: No

 ** OptInStatus **
Indicates the type of opt-in request that has been received for the resource.
Type: String
Required: No

## See Also
<a name="API_PendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/PendingMaintenanceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/PendingMaintenanceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/PendingMaintenanceAction)
