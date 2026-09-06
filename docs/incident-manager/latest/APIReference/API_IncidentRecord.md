---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_IncidentRecord.html
---

# IncidentRecord
<a name="API_IncidentRecord"></a>

The record of the incident that's created when an incident occurs.

## Contents
<a name="API_IncidentRecord_Contents"></a>

 ** arn **   <a name="IncidentManager-Type-IncidentRecord-arn"></a>
The Amazon Resource Name (ARN) of the incident record.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** creationTime **   <a name="IncidentManager-Type-IncidentRecord-creationTime"></a>
The timestamp for when Incident Manager created the incident record.
Type: Timestamp
Required: Yes

 ** dedupeString **   <a name="IncidentManager-Type-IncidentRecord-dedupeString"></a>
The string Incident Manager uses to prevent duplicate incidents from being created by the same incident in the same account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** impact **   <a name="IncidentManager-Type-IncidentRecord-impact"></a>
The impact of the incident on customers and applications.

**Supported impact codes**
+  `1` - Critical
+  `2` - High
+  `3` - Medium
+  `4` - Low
+  `5` - No Impact
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: Yes

 ** incidentRecordSource **   <a name="IncidentManager-Type-IncidentRecord-incidentRecordSource"></a>
Details about the action that started the incident.
Type: [IncidentRecordSource](API_IncidentRecordSource.md) object
Required: Yes

 ** lastModifiedBy **   <a name="IncidentManager-Type-IncidentRecord-lastModifiedBy"></a>
Who modified the incident most recently.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** lastModifiedTime **   <a name="IncidentManager-Type-IncidentRecord-lastModifiedTime"></a>
The timestamp for when the incident was most recently modified.
Type: Timestamp
Required: Yes

 ** status **   <a name="IncidentManager-Type-IncidentRecord-status"></a>
The current status of the incident.
Type: String
Valid Values: `OPEN | RESOLVED`
Required: Yes

 ** title **   <a name="IncidentManager-Type-IncidentRecord-title"></a>
The title of the incident.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** automationExecutions **   <a name="IncidentManager-Type-IncidentRecord-automationExecutions"></a>
The runbook, or automation document, that's run at the beginning of the incident.
Type: Array of [AutomationExecution](API_AutomationExecution.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** chatChannel **   <a name="IncidentManager-Type-IncidentRecord-chatChannel"></a>
The chat channel used for collaboration during an incident.
Type: [ChatChannel](API_ChatChannel.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** notificationTargets **   <a name="IncidentManager-Type-IncidentRecord-notificationTargets"></a>
The Amazon SNS targets that are notified when updates are made to an incident.
Type: Array of [NotificationTargetItem](API_NotificationTargetItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** resolvedTime **   <a name="IncidentManager-Type-IncidentRecord-resolvedTime"></a>
The timestamp for when the incident was resolved. This appears as a timeline event.
Type: Timestamp
Required: No

 ** summary **   <a name="IncidentManager-Type-IncidentRecord-summary"></a>
The summary of the incident. The summary is a brief synopsis of what occurred, what's currently happening, and context of the incident.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Required: No

## See Also
<a name="API_IncidentRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/IncidentRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/IncidentRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/IncidentRecord)
