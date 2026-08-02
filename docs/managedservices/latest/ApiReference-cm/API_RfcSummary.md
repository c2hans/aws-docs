---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcSummary.html
---

# RfcSummary
<a name="API_RfcSummary"></a>

Summary information about a request for change.

## Contents
<a name="API_RfcSummary_Contents"></a>

 ** ActionState **   <a name="amscm-Type-RfcSummary-ActionState"></a>
The action state of the RFC.
Type: [RfcActionState](API_RfcActionState.md) object
Required: No

 ** ActualExecutionTimeRange **   <a name="amscm-Type-RfcSummary-ActualExecutionTimeRange"></a>
The starting and ending dates and times during which the change was executed.
Type: [TimeRange](API_TimeRange.md) object
Required: No

 ** ApprovalState **   <a name="amscm-Type-RfcSummary-ApprovalState"></a>
The status of the approvals for the RFC.
Type: [RfcApprovalState](API_RfcApprovalState.md) object
Required: No

 ** AutomationStatus **   <a name="amscm-Type-RfcSummary-AutomationStatus"></a>
Whether the change type is automated or manual.
Type: [AutomationStatus](API_AutomationStatus.md) object
Required: No

 ** ChangeTypeId **   <a name="amscm-Type-RfcSummary-ChangeTypeId"></a>
The unique ID of the change type, in the form ct-2ty5seo8rxfsc.
Type: String
Required: No

 ** ChangeTypeVersion **   <a name="amscm-Type-RfcSummary-ChangeTypeVersion"></a>
The version number of the change type version associated with the RFC.
Type: String
Required: No

 ** CreatedBy **   <a name="amscm-Type-RfcSummary-CreatedBy"></a>
The date and time when the RFC was created.
Type: String
Required: No

 ** CreatedTime **   <a name="amscm-Type-RfcSummary-CreatedTime"></a>
The date and time that the RFC was created.
Type: String
Required: No

 ** LastCorrespondenceTime **   <a name="amscm-Type-RfcSummary-LastCorrespondenceTime"></a>
The date and time when the last correspondence was added.
Type: String
Required: No

 ** LastModifiedTime **   <a name="amscm-Type-RfcSummary-LastModifiedTime"></a>
The time that the RFC was most recently modified, expressed in ISO 8601 format. By default, AWS MS uses the basic format (YYYYMMDDThhmmssZ).
Type: String
Required: No

 ** LastSubmittedTime **   <a name="amscm-Type-RfcSummary-LastSubmittedTime"></a>
The date and time when the RFC was last submitted.
Type: String
Required: No

 ** RequestedExecutionTimeRange **   <a name="amscm-Type-RfcSummary-RequestedExecutionTimeRange"></a>
The starting and ending dates and times during which the change should be executed. Null if the RFC was ASAP.
Type: [TimeRange](API_TimeRange.md) object
Required: No

 ** RfcId **   <a name="amscm-Type-RfcSummary-RfcId"></a>
The unique ID (UUID) of the RFC.
Type: String
Required: No

 ** Status **   <a name="amscm-Type-RfcSummary-Status"></a>
The status of the RFC. Possible values: `Editing` \| `PendingApproval` \| `Scheduled` \| `Canceled` \| `Rejected` \| `InProgress` \| `Success` \| `Failure`
Type: [RfcStatus](API_RfcStatus.md) object
Required: No

 ** Title **   <a name="amscm-Type-RfcSummary-Title"></a>
The identifying title of the RFC.
Type: String
Required: No

## See Also
<a name="API_RfcSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/RfcSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/RfcSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/RfcSummary)
