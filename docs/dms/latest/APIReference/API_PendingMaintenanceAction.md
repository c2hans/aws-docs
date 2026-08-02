---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_PendingMaintenanceAction.html
---

# PendingMaintenanceAction
<a name="API_PendingMaintenanceAction"></a>

Describes a maintenance action pending for an AWS DMS resource, including when and how it will be applied. This data type is a response element to the `DescribePendingMaintenanceActions` operation.

## Contents
<a name="API_PendingMaintenanceAction_Contents"></a>

 ** Action **   <a name="DMS-Type-PendingMaintenanceAction-Action"></a>
The type of pending maintenance action that is available for the resource.
Type: String
Required: No

 ** AutoAppliedAfterDate **   <a name="DMS-Type-PendingMaintenanceAction-AutoAppliedAfterDate"></a>
The date of the maintenance window when the action is to be applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any `next-maintenance` opt-in requests are ignored.
Type: Timestamp
Required: No

 ** CurrentApplyDate **   <a name="DMS-Type-PendingMaintenanceAction-CurrentApplyDate"></a>
The effective date when the pending maintenance action will be applied to the resource. This date takes into account opt-in requests received from the `ApplyPendingMaintenanceAction` API operation, and also the `AutoAppliedAfterDate` and `ForcedApplyDate` parameter values. This value is blank if an opt-in request has not been received and nothing has been specified for `AutoAppliedAfterDate` or `ForcedApplyDate`.
Type: Timestamp
Required: No

 ** Description **   <a name="DMS-Type-PendingMaintenanceAction-Description"></a>
A description providing more detail about the maintenance action.
Type: String
Required: No

 ** ForcedApplyDate **   <a name="DMS-Type-PendingMaintenanceAction-ForcedApplyDate"></a>
The date when the maintenance action will be automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any `immediate` opt-in requests are ignored.
Type: Timestamp
Required: No

 ** OptInStatus **   <a name="DMS-Type-PendingMaintenanceAction-OptInStatus"></a>
The type of opt-in request that has been received for the resource.
Type: String
Required: No

## See Also
<a name="API_PendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/PendingMaintenanceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/PendingMaintenanceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/PendingMaintenanceAction)
