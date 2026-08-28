---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsItemSummary.html
---

# OpsItemSummary
<a name="API_OpsItemSummary"></a>

A count of OpsItems.

## Contents
<a name="API_OpsItemSummary_Contents"></a>

 ** ActualEndTime **   <a name="systemsmanager-Type-OpsItemSummary-ActualEndTime"></a>
The time a runbook workflow ended. Currently reported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** ActualStartTime **   <a name="systemsmanager-Type-OpsItemSummary-ActualStartTime"></a>
The time a runbook workflow started. Currently reported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** Category **   <a name="systemsmanager-Type-OpsItemSummary-Category"></a>
A list of OpsItems by category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!\s*$).+`
Required: No

 ** CreatedBy **   <a name="systemsmanager-Type-OpsItemSummary-CreatedBy"></a>
The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem.
Type: String
Required: No

 ** CreatedTime **   <a name="systemsmanager-Type-OpsItemSummary-CreatedTime"></a>
The date and time the OpsItem was created.
Type: Timestamp
Required: No

 ** LastModifiedBy **   <a name="systemsmanager-Type-OpsItemSummary-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem.
Type: String
Required: No

 ** LastModifiedTime **   <a name="systemsmanager-Type-OpsItemSummary-LastModifiedTime"></a>
The date and time the OpsItem was last updated.
Type: Timestamp
Required: No

 ** OperationalData **   <a name="systemsmanager-Type-OpsItemSummary-OperationalData"></a>
Operational data is custom data that provides useful reference details about the OpsItem.
Type: String to [OpsItemDataValue](API_OpsItemDataValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!\s*$).+`
Required: No

 ** OpsItemId **   <a name="systemsmanager-Type-OpsItemSummary-OpsItemId"></a>
The ID of the OpsItem.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: No

 ** OpsItemType **   <a name="systemsmanager-Type-OpsItemSummary-OpsItemType"></a>
The type of OpsItem. Systems Manager supports the following types of OpsItems:
+  `/aws/issue`

  This type of OpsItem is used for default OpsItems created by OpsCenter.
+  `/aws/changerequest`

  This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests.
+  `/aws/insight`

  This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems.
Type: String
Required: No

 ** PlannedEndTime **   <a name="systemsmanager-Type-OpsItemSummary-PlannedEndTime"></a>
The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** PlannedStartTime **   <a name="systemsmanager-Type-OpsItemSummary-PlannedStartTime"></a>
The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** Priority **   <a name="systemsmanager-Type-OpsItemSummary-Priority"></a>
The importance of this OpsItem in relation to other OpsItems in the system.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** Severity **   <a name="systemsmanager-Type-OpsItemSummary-Severity"></a>
A list of OpsItems by severity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!\s*$).+`
Required: No

 ** Source **   <a name="systemsmanager-Type-OpsItemSummary-Source"></a>
The impacted AWS resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!\s*$).+`
Required: No

 ** Status **   <a name="systemsmanager-Type-OpsItemSummary-Status"></a>
The OpsItem status.
Type: String
Valid Values: `Open | InProgress | Resolved | Pending | TimedOut | Cancelling | Cancelled | Failed | CompletedWithSuccess | CompletedWithFailure | Scheduled | RunbookInProgress | PendingChangeCalendarOverride | ChangeCalendarOverrideApproved | ChangeCalendarOverrideRejected | PendingApproval | Approved | Revoked | Rejected | Closed`
Required: No

 ** Title **   <a name="systemsmanager-Type-OpsItemSummary-Title"></a>
A short heading that describes the nature of the OpsItem and the impacted resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`
Required: No

## See Also
<a name="API_OpsItemSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsItemSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsItemSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsItemSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
