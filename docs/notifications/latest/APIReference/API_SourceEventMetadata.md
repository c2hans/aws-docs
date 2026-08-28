---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_SourceEventMetadata.html
---

# SourceEventMetadata
<a name="API_SourceEventMetadata"></a>

Describes the metadata for a source event.

For more information, see [Event structure reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html) in the *Amazon EventBridge User Guide*.

## Contents
<a name="API_SourceEventMetadata_Contents"></a>

 ** eventOccurrenceTime **   <a name="Notifications-Type-SourceEventMetadata-eventOccurrenceTime"></a>
The date and time the source event occurred. This is based on the Source Event.
Type: Timestamp
Required: Yes

 ** eventType **   <a name="Notifications-Type-SourceEventMetadata-eventType"></a>
The type of event. For example, an Amazon CloudWatch state change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** eventTypeVersion **   <a name="Notifications-Type-SourceEventMetadata-eventTypeVersion"></a>
The version of the type of event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.
Pattern: `[0-9.]+`
Required: Yes

 ** relatedAccount **   <a name="Notifications-Type-SourceEventMetadata-relatedAccount"></a>
The primary AWS account of `SourceEvent`.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** relatedResources **   <a name="Notifications-Type-SourceEventMetadata-relatedResources"></a>
A list of resources related to this `NotificationEvent`.
Type: Array of [Resource](API_Resource.md) objects
Required: Yes

 ** source **   <a name="Notifications-Type-SourceEventMetadata-source"></a>
The AWS service the event originates from. For example `aws.cloudwatch`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `aws.([a-z0-9\-])+`
Required: Yes

 ** sourceEventId **   <a name="Notifications-Type-SourceEventMetadata-sourceEventId"></a>
The source event id.
Type: String
Required: Yes

 ** eventOriginRegion **   <a name="Notifications-Type-SourceEventMetadata-eventOriginRegion"></a>
The Region the event originated from.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: No

## See Also
<a name="API_SourceEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/SourceEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/SourceEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/SourceEventMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
