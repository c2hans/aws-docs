---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_IncidentTemplate.html
---

# IncidentTemplate
<a name="API_IncidentTemplate"></a>

Basic details used in creating a response plan. The response plan is then used to create an incident record.

## Contents
<a name="API_IncidentTemplate_Contents"></a>

 ** impact **   <a name="IncidentManager-Type-IncidentTemplate-impact"></a>
The impact of the incident on your customers and applications.

**Supported impact codes**
+  `1` - Critical
+  `2` - High
+  `3` - Medium
+  `4` - Low
+  `5` - No Impact
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: Yes

 ** title **   <a name="IncidentManager-Type-IncidentTemplate-title"></a>
The title of the incident.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** dedupeString **   <a name="IncidentManager-Type-IncidentTemplate-dedupeString"></a>
The string Incident Manager uses to prevent the same root cause from creating multiple incidents in the same account.
A deduplication string is a term or phrase the system uses to check for duplicate incidents. If you specify a deduplication string, Incident Manager searches for open incidents that contain the same string in the `dedupeString` field when it creates the incident. If a duplicate is detected, Incident Manager deduplicates the newer incident into the existing incident.
By default, Incident Manager automatically deduplicates multiple incidents created by the same Amazon CloudWatch alarm or Amazon EventBridge event. You don't have to enter your own deduplication string to prevent duplication for these resource types.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** incidentTags **   <a name="IncidentManager-Type-IncidentTemplate-incidentTags"></a>
Tags to assign to the template. When the `StartIncident` API action is called, Incident Manager assigns the tags specified in the template to the incident.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[A-Za-z0-9 _=@:.+-/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 _=@:.+-/]*`
Required: No

 ** notificationTargets **   <a name="IncidentManager-Type-IncidentTemplate-notificationTargets"></a>
The Amazon SNS targets that are notified when updates are made to an incident.
Type: Array of [NotificationTargetItem](API_NotificationTargetItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** summary **   <a name="IncidentManager-Type-IncidentTemplate-summary"></a>
The summary of the incident. The summary is a brief synopsis of what occurred, what's currently happening, and context.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Required: No

## See Also
<a name="API_IncidentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/IncidentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/IncidentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/IncidentTemplate)
