---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_EventSummary.html
---

# EventSummary
<a name="API_EventSummary"></a>

Details about a timeline event during an incident.

## Contents
<a name="API_EventSummary_Contents"></a>

 ** eventId **   <a name="IncidentManager-Type-EventSummary-eventId"></a>
The timeline event ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: Yes

 ** eventTime **   <a name="IncidentManager-Type-EventSummary-eventTime"></a>
The timestamp for when the event occurred.
Type: Timestamp
Required: Yes

 ** eventType **   <a name="IncidentManager-Type-EventSummary-eventType"></a>
The type of event. The timeline event must be `Custom Event` or `Note`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: Yes

 ** eventUpdatedTime **   <a name="IncidentManager-Type-EventSummary-eventUpdatedTime"></a>
The timestamp for when the timeline event was last updated.
Type: Timestamp
Required: Yes

 ** incidentRecordArn **   <a name="IncidentManager-Type-EventSummary-incidentRecordArn"></a>
The Amazon Resource Name (ARN) of the incident that the event happened during.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** eventReferences **   <a name="IncidentManager-Type-EventSummary-eventReferences"></a>
A list of references in a `TimelineEvent`.
Type: Array of [EventReference](API_EventReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_EventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/EventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/EventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/EventSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
