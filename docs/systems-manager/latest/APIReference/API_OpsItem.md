---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsItem.html
---

# OpsItem
<a name="API_OpsItem"></a>

Operations engineers and IT professionals use AWS Systems Manager OpsCenter to view, investigate, and remediate operational work items (OpsItems) impacting the performance and health of their AWS resources. OpsCenter is integrated with Amazon EventBridge and Amazon CloudWatch. This means you can configure these services to automatically create an OpsItem in OpsCenter when a CloudWatch alarm enters the ALARM state or when EventBridge processes an event from any AWS service that publishes events. Configuring Amazon CloudWatch alarms and EventBridge events to automatically create OpsItems allows you to quickly diagnose and remediate issues with AWS resources from a single console.

To help you diagnose issues, each OpsItem includes contextually relevant information such as the name and ID of the AWS resource that generated the OpsItem, alarm or event details, alarm history, and an alarm timeline graph. For the AWS resource, OpsCenter aggregates information from AWS Config, AWS CloudTrail logs, and EventBridge, so you don't have to navigate across multiple console pages during your investigation. For more information, see [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) in the * AWS Systems Manager User Guide*.

## Contents
<a name="API_OpsItem_Contents"></a>

 ** ActualEndTime **   <a name="systemsmanager-Type-OpsItem-ActualEndTime"></a>
The time a runbook workflow ended. Currently reported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** ActualStartTime **   <a name="systemsmanager-Type-OpsItem-ActualStartTime"></a>
The time a runbook workflow started. Currently reported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** Category **   <a name="systemsmanager-Type-OpsItem-Category"></a>
An OpsItem category. Category options include: Availability, Cost, Performance, Recovery, Security.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!\s*$).+`
Required: No

 ** CreatedBy **   <a name="systemsmanager-Type-OpsItem-CreatedBy"></a>
The ARN of the AWS account that created the OpsItem.
Type: String
Required: No

 ** CreatedTime **   <a name="systemsmanager-Type-OpsItem-CreatedTime"></a>
The date and time the OpsItem was created.
Type: Timestamp
Required: No

 ** Description **   <a name="systemsmanager-Type-OpsItem-Description"></a>
The OpsItem description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** LastModifiedBy **   <a name="systemsmanager-Type-OpsItem-LastModifiedBy"></a>
The ARN of the AWS account that last updated the OpsItem.
Type: String
Required: No

 ** LastModifiedTime **   <a name="systemsmanager-Type-OpsItem-LastModifiedTime"></a>
The date and time the OpsItem was last updated.
Type: Timestamp
Required: No

 ** Notifications **   <a name="systemsmanager-Type-OpsItem-Notifications"></a>
The Amazon Resource Name (ARN) of an Amazon Simple Notification Service (Amazon SNS) topic where notifications are sent when this OpsItem is edited or changed.
Type: Array of [OpsItemNotification](API_OpsItemNotification.md) objects
Required: No

 ** OperationalData **   <a name="systemsmanager-Type-OpsItem-OperationalData"></a>
Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.
Operational data keys *can't* begin with the following: `amazon`, `aws`, `amzn`, `ssm`, `/amazon`, `/aws`, `/amzn`, `/ssm`.
You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the [DescribeOpsItems](API_DescribeOpsItems.md) API operation) can view and search on the specified data. Operational data that isn't searchable is only viewable by users who have access to the OpsItem (as provided by the [GetOpsItem](API_GetOpsItem.md) API operation).
Use the `/aws/resources` key in OperationalData to specify a related resource in the request. Use the `/aws/automations` key in OperationalData to associate an Automation runbook with the OpsItem. To view AWS CLI example commands that use these keys, see [Creating OpsItems manually](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html) in the * AWS Systems Manager User Guide*.
Type: String to [OpsItemDataValue](API_OpsItemDataValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!\s*$).+`
Required: No

 ** OpsItemArn **   <a name="systemsmanager-Type-OpsItem-OpsItemArn"></a>
The OpsItem Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[0-9]{12}:opsitem.*`
Required: No

 ** OpsItemId **   <a name="systemsmanager-Type-OpsItem-OpsItemId"></a>
The ID of the OpsItem.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: No

 ** OpsItemType **   <a name="systemsmanager-Type-OpsItem-OpsItemType"></a>
The type of OpsItem. Systems Manager supports the following types of OpsItems:
+  `/aws/issue`

  This type of OpsItem is used for default OpsItems created by OpsCenter.
+  `/aws/changerequest`

  This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests.
+  `/aws/insight`

  This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems.
Type: String
Required: No

 ** PlannedEndTime **   <a name="systemsmanager-Type-OpsItem-PlannedEndTime"></a>
The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** PlannedStartTime **   <a name="systemsmanager-Type-OpsItem-PlannedStartTime"></a>
The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type `/aws/changerequest`.
Type: Timestamp
Required: No

 ** Priority **   <a name="systemsmanager-Type-OpsItem-Priority"></a>
The importance of this OpsItem in relation to other OpsItems in the system.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** RelatedOpsItems **   <a name="systemsmanager-Type-OpsItem-RelatedOpsItems"></a>
One or more OpsItems that share something in common with the current OpsItem. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.
Type: Array of [RelatedOpsItem](API_RelatedOpsItem.md) objects
Required: No

 ** Severity **   <a name="systemsmanager-Type-OpsItem-Severity"></a>
The severity of the OpsItem. Severity options range from 1 to 4.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!\s*$).+`
Required: No

 ** Source **   <a name="systemsmanager-Type-OpsItem-Source"></a>
The origin of the OpsItem, such as Amazon EC2 or Systems Manager. The impacted resource is a subset of source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!\s*$).+`
Required: No

 ** Status **   <a name="systemsmanager-Type-OpsItem-Status"></a>
The OpsItem status. For more information, see [Editing OpsItem details](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-editing-details.html) in the * AWS Systems Manager User Guide*.
Type: String
Valid Values: `Open | InProgress | Resolved | Pending | TimedOut | Cancelling | Cancelled | Failed | CompletedWithSuccess | CompletedWithFailure | Scheduled | RunbookInProgress | PendingChangeCalendarOverride | ChangeCalendarOverrideApproved | ChangeCalendarOverrideRejected | PendingApproval | Approved | Revoked | Rejected | Closed`
Required: No

 ** Title **   <a name="systemsmanager-Type-OpsItem-Title"></a>
A short heading that describes the nature of the OpsItem and the impacted resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`
Required: No

 ** Version **   <a name="systemsmanager-Type-OpsItem-Version"></a>
The version of this OpsItem. Each time the OpsItem is edited the version number increments by one.
Type: String
Required: No

## See Also
<a name="API_OpsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsItem)
