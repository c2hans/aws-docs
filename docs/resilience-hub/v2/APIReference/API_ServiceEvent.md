---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceEvent.html
---

# ServiceEvent
<a name="API_ServiceEvent"></a>

Represents an event in the service event log.

## Contents
<a name="API_ServiceEvent_Contents"></a>

 ** actor **   <a name="ngresiliencehub-Type-ServiceEvent-actor"></a>
The actor that triggered the event.
Type: [EventActor](API_EventActor.md) object
Required: Yes

 ** eventDetails **   <a name="ngresiliencehub-Type-ServiceEvent-eventDetails"></a>
The details of the event.
Type: [ServiceEventDetails](API_ServiceEventDetails.md) object
Required: Yes

 ** eventId **   <a name="ngresiliencehub-Type-ServiceEvent-eventId"></a>
The unique identifier of the event.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: Yes

 ** eventType **   <a name="ngresiliencehub-Type-ServiceEvent-eventType"></a>
The type of the event.
Type: String
Valid Values: `SERVICE_CREATED | SERVICE_DELETED | SERVICE_SYSTEM_ASSOCIATED | SERVICE_SYSTEM_DISASSOCIATED | SERVICE_RESOURCES_ASSOCIATED | SERVICE_RESOURCES_DISASSOCIATED | SERVICE_WORKFLOW_UPDATED | SERVICE_INPUT_SOURCES_UPDATED | SERVICE_POLICY_ASSOCIATED | SERVICE_POLICY_DISASSOCIATED | SERVICE_FUNCTION_CREATED | SERVICE_FUNCTION_UPDATED | SERVICE_FUNCTION_DELETED | SERVICE_FUNCTION_RESOURCES_ADDED | SERVICE_FUNCTION_RESOURCES_REMOVED | SERVICE_ACHIEVABILITY_UPDATED | ASSERTION_CREATED | ASSERTION_UPDATED | ASSERTION_DELETED`
Required: Yes

 ** serviceArn **   <a name="ngresiliencehub-Type-ServiceEvent-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** timestamp **   <a name="ngresiliencehub-Type-ServiceEvent-timestamp"></a>
The timestamp of the event.
Type: Timestamp
Required: Yes

## See Also
<a name="API_ServiceEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceEvent)
