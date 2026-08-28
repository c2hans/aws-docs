---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_Rfc.html
---

# Rfc
<a name="API_Rfc"></a>

A request for change. For more information, see [CreateRfc](API_CreateRfc.md).

## Contents
<a name="API_Rfc_Contents"></a>

 ** ActionState **   <a name="amscm-Type-Rfc-ActionState"></a>
The action state of the RFC.
Type: [RfcActionState](API_RfcActionState.md) object
Required: No

 ** ActualExecutionTimeRange **   <a name="amscm-Type-Rfc-ActualExecutionTimeRange"></a>
The starting and ending dates and times during which the change was executed.
Type: [TimeRange](API_TimeRange.md) object
Required: No

 ** ApprovalState **   <a name="amscm-Type-Rfc-ApprovalState"></a>
The approval statuses of the RFC.
Type: [RfcApprovalState](API_RfcApprovalState.md) object
Required: No

 ** AutomationStatus **   <a name="amscm-Type-Rfc-AutomationStatus"></a>
Whether the change type is automated or manual.
Type: [AutomationStatus](API_AutomationStatus.md) object
Required: No

 ** ChangeTypeId **   <a name="amscm-Type-Rfc-ChangeTypeId"></a>
The unique ID of the change type, in the form ct-2ty5seo8rxfsc.
Type: String
Required: No

 ** ChangeTypeVersion **   <a name="amscm-Type-Rfc-ChangeTypeVersion"></a>
The version number of the change type version associated with the RFC.
Type: String
Required: No

 ** CreatedBy **   <a name="amscm-Type-Rfc-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the RFC.
Type: String
Required: No

 ** CreatedTime **   <a name="amscm-Type-Rfc-CreatedTime"></a>
The date and time that the RFC was created.
Type: String
Required: No

 ** Description **   <a name="amscm-Type-Rfc-Description"></a>
A text description of the RFC.
Type: String
Required: No

 ** ExecutionOutput **   <a name="amscm-Type-Rfc-ExecutionOutput"></a>
The output from the execution of the change.
Type: String
Required: No

 ** ExecutionParameters **   <a name="amscm-Type-Rfc-ExecutionParameters"></a>
The parameters to use in the execution of the request, in JSON format. To get the JSON schema for the parameters, use the [GetChangeTypeVersion](API_GetChangeTypeVersion.md) operation.
Type: String
Required: No

 ** ExpectedOutcome **   <a name="amscm-Type-Rfc-ExpectedOutcome"></a>
A description of the effects of the change.
Type: String
Required: No

 ** ImplementationPlan **   <a name="amscm-Type-Rfc-ImplementationPlan"></a>
The actions or steps required to implement the change.
Type: String
Required: No

 ** LastCorrespondenceTime **   <a name="amscm-Type-Rfc-LastCorrespondenceTime"></a>
The date and time when the most recent correspondence was created.
Type: String
Required: No

 ** LastModifiedBy **   <a name="amscm-Type-Rfc-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who made the most recent change to the RFC.
Type: String
Required: No

 ** LastModifiedTime **   <a name="amscm-Type-Rfc-LastModifiedTime"></a>
The time that the RFC was most recently modified, expressed in ISO 8601 format. By default, AMS uses the basic format (YYYYMMDDThhmmssZ).
Type: String
Required: No

 ** LastSubmittedTime **   <a name="amscm-Type-Rfc-LastSubmittedTime"></a>
The time that the RFC was most recently submitted, expressed in ISO 8601 format. By default, AMS uses the basic format (YYYYMMDDThhmmssZ).
Type: String
Required: No

 ** Notification **   <a name="amscm-Type-Rfc-Notification"></a>
The RFC notification structure.
Type: [RfcNotification](API_RfcNotification.md) object
Required: No

 ** RequestedExecutionTimeRange **   <a name="amscm-Type-Rfc-RequestedExecutionTimeRange"></a>
The starting and ending dates and times during which the change should be executed. Null if the RFC was ASAP.
Type: [TimeRange](API_TimeRange.md) object
Required: No

 ** RestrictedExecutionTimesOverride **   <a name="amscm-Type-Rfc-RestrictedExecutionTimesOverride"></a>
An indication of whether the change should observe the preset restricted execution times. Possible values: `NoOverrides` \| `OverrideRestrictedTimeRanges`.
Type: [RfcRestrictedExecutionTimesOverride](API_RfcRestrictedExecutionTimesOverride.md) object
Required: No

 ** RfcId **   <a name="amscm-Type-Rfc-RfcId"></a>
The unique ID (UUID) of the RFC.
Type: String
Required: No

 ** RollbackPlan **   <a name="amscm-Type-Rfc-RollbackPlan"></a>
The actions or steps required to undo the change.
Type: String
Required: No

 ** Status **   <a name="amscm-Type-Rfc-Status"></a>
The status of the RFC. Possible values: `Editing` \| `PendingApproval` \| `Scheduled` \| `Canceled` \| `Rejected` \| `InProgress` \| `Success` \| `Failure`
Type: [RfcStatus](API_RfcStatus.md) object
Required: No

 ** StatusReason **   <a name="amscm-Type-Rfc-StatusReason"></a>
The reason provided for RFC status; for example, why it was rejected.
Type: String
Required: No

 ** Title **   <a name="amscm-Type-Rfc-Title"></a>
The identifying title of the RFC.
Type: String
Required: No

 ** WorstCaseScenario **   <a name="amscm-Type-Rfc-WorstCaseScenario"></a>
A description of the most unfavorable outcome of the change.
Type: String
Required: No

## See Also
<a name="API_Rfc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/Rfc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/Rfc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/Rfc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
