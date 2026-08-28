---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_SourceEventMetadataSummary.html
---

# SourceEventMetadataSummary
<a name="API_SourceEventMetadataSummary"></a>

Contains metadata about the event that caused the `NotificationEvent`. For other specific values, see `sourceEventMetadata`.

## Contents
<a name="API_SourceEventMetadataSummary_Contents"></a>

 ** eventType **   <a name="Notifications-Type-SourceEventMetadataSummary-eventType"></a>
The event type to match.
Must match one of the valid Amazon EventBridge event types. For example, EC2 Instance State-change Notification and Amazon CloudWatch Alarm State Change. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** source **   <a name="Notifications-Type-SourceEventMetadataSummary-source"></a>
The matched event source.
Must match one of the valid EventBridge sources. Only AWS service sourced events are supported. For example, `aws.ec2` and `aws.cloudwatch`. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide*.
Type: String
Required: Yes

 ** eventOriginRegion **   <a name="Notifications-Type-SourceEventMetadataSummary-eventOriginRegion"></a>
The Region where the notification originated.
Unavailable for aggregated notifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

## See Also
<a name="API_SourceEventMetadataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/SourceEventMetadataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/SourceEventMetadataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/SourceEventMetadataSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
