---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_SystemEvent.html
---

# SystemEvent
<a name="API_SystemEvent"></a>

Represents an event in the system event log.

## Contents
<a name="API_SystemEvent_Contents"></a>

 ** actor **   <a name="ngresiliencehub-Type-SystemEvent-actor"></a>
The actor that triggered the event.
Type: [EventActor](API_EventActor.md) object
Required: Yes

 ** eventDetails **   <a name="ngresiliencehub-Type-SystemEvent-eventDetails"></a>
The details of the event.
Type: [SystemEventDetails](API_SystemEventDetails.md) object
Required: Yes

 ** eventId **   <a name="ngresiliencehub-Type-SystemEvent-eventId"></a>
The unique identifier of the event.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: Yes

 ** eventType **   <a name="ngresiliencehub-Type-SystemEvent-eventType"></a>
The type of the event.
Type: String
Valid Values: `SYSTEM_CREATED | SYSTEM_DELETED | SYSTEM_USER_JOURNEY_CREATED | SYSTEM_USER_JOURNEY_UPDATED | SYSTEM_USER_JOURNEY_DELETED | SYSTEM_SERVICE_ASSOCIATED | SYSTEM_SERVICE_DISASSOCIATED | SYSTEM_POLICY_ASSOCIATED | SYSTEM_POLICY_DISASSOCIATED`
Required: Yes

 ** systemArn **   <a name="ngresiliencehub-Type-SystemEvent-systemArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** timestamp **   <a name="ngresiliencehub-Type-SystemEvent-timestamp"></a>
The timestamp of the event.
Type: Timestamp
Required: Yes

## See Also
<a name="API_SystemEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/SystemEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/SystemEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/SystemEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
